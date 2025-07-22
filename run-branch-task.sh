#!/bin/bash

# Function to show help
show_help() {
    echo "Usage: $0 [branch-name] [prompt]"
    echo "No arguments - Interactive mode"
}

# Check if no arguments provided - enter interactive mode
if [ $# -eq 0 ]; then
    show_help
    echo ""
    
    # Get list of existing worktrees
    worktrees=$(git worktree list | grep -v "bare" | awk '{print $3}' | sed 's/\[//; s/\]//')
    
    # Create options array with "New worktree" as first option
    options=("New worktree")
    
    # Add existing worktrees to options
    while IFS= read -r worktree; do
        if [[ -n "$worktree" ]]; then
            options+=("$worktree")
        fi
    done <<< "$worktrees"
    
    # Use gum to present the choice
    choice=$(printf '%s\n' "${options[@]}" | gum choose --selected="New worktree")
    
    # Handle the selection
    if [[ "$choice" == "New worktree" ]]; then
        # Ask for new worktree name
        BRANCH_NAME=$(gum input --placeholder "Enter worktree name")
        
        if [[ -z "$BRANCH_NAME" ]]; then
            echo "No name provided. Exiting."
            exit 1
        fi
    else
        BRANCH_NAME="$choice"
    fi
    
    # Get task description
    PROMPT=$(gum write --placeholder "Enter task description..." --header "Task Description")
    
    if [[ -z "$PROMPT" ]]; then
        echo "No task description provided. Exiting."
        exit 1
    fi
    
    # Ask if user wants Interactive Claude mode
    if gum confirm "Use Interactive Claude? (removes -p flag for both tasks)"; then
        INTERACTIVE_MODE=true
    else
        INTERACTIVE_MODE=false
    fi
    
    # Ask if user wants to run Preparing PR task (only if not main branch)
    if [[ "$BRANCH_NAME" != "main" ]]; then
        if gum confirm "Run Preparing PR task?"; then
            RUN_PR_TASK=true
        else
            RUN_PR_TASK=false
        fi
    else
        RUN_PR_TASK=false
        echo "Note: Preparing PR task disabled for main branch"
    fi
    
elif [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <branch-name> <prompt>"
    exit 1
else
    BRANCH_NAME="$1"
    PROMPT="$2"
    # Set defaults for non-interactive mode
    INTERACTIVE_MODE=false
    RUN_PR_TASK=true
fi

# Echo the arguments and ask if they are correct
echo "Branch Name: $BRANCH_NAME"
echo "Prompt: $PROMPT"
gum confirm "Are these correct?" || exit 1

# Handle worktree creation/switching for interactive mode
if [[ "$choice" == "New worktree" ]] || [[ $# -gt 0 ]]; then
    # Check if both branch and directory already exist
    if git show-ref --verify --quiet refs/heads/"$BRANCH_NAME" && [ -d "../$BRANCH_NAME" ]; then
        echo "Branch '$BRANCH_NAME' and directory '../$BRANCH_NAME' already exist. Skipping worktree creation."
        cd "../$BRANCH_NAME"
    else
        # Check if branch already exists without directory
        if git show-ref --verify --quiet refs/heads/"$BRANCH_NAME"; then
            echo "Error: Branch '$BRANCH_NAME' already exists but directory '../$BRANCH_NAME' does not exist"
            exit 1
        fi

        # Check if worktree directory exists without branch
        if [ -d "../$BRANCH_NAME" ]; then
            echo "Error: Directory '../$BRANCH_NAME' already exists but branch '$BRANCH_NAME' does not exist"
            exit 1
        fi

        echo "Creating new worktree for branch '$BRANCH_NAME' in directory '../$BRANCH_NAME'"
        git worktree add -b "$BRANCH_NAME" "../$BRANCH_NAME"
        cd "../$BRANCH_NAME"
    fi
else
    # Switch to selected existing worktree
    worktree_path=$(git worktree list | grep "\[$BRANCH_NAME\]" | awk '{print $1}')
    if [[ -n "$worktree_path" ]]; then
        echo "Switching to worktree: $BRANCH_NAME"
        echo "Path: $worktree_path"
        cd "$worktree_path"
    else
        echo "Could not find path for worktree: $BRANCH_NAME"
        exit 1
    fi
fi

# Build the claude command based on interactive mode setting
if [[ "$INTERACTIVE_MODE" == true ]]; then
    CLAUDE_CMD="claude \"/gtask $PROMPT\""
    CLAUDE_PR_CMD="claude \"/ghpr\""
else
    CLAUDE_CMD="claude -p \"/gtask $PROMPT\""
    CLAUDE_PR_CMD="claude -p \"/ghpr\""
fi

gum spin --title "Running Task" --show-output \
-- $CLAUDE_CMD --allowedTools "Edit Write MultiEdit" --model sonnet

# Only run Preparing PR if requested
if [[ "$RUN_PR_TASK" == true ]]; then
    gum spin --title "Preparing PR" --show-output \
    -- $CLAUDE_PR_CMD --model sonnet --allowedTools "Edit Write MultiEdit Bash(git stash:*) Bash(git push:*) Bash(gh pr create:*) Bash(gh pr view:*)"
fi

