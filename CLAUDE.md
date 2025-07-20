# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Running the Program
```bash
# Basic usage with default russet potato
python3 potato.py

# Fast animation with different variety
python3 potato.py --speed 0.5 --variety yukon_gold

# Export to file
python3 potato.py --output file --file my_potato.txt

# Use configuration file
python3 potato.py --config config.json
```

### Testing
```bash
# Run all tests
python3 test_potato.py

# Run specific test class
python3 -m unittest test_potato.TestPotatoArt
```

### Available Potato Varieties
- `russet` - Classic potato with standard box-drawing characters
- `yukon_gold` - Golden variety with double-line characters  
- `red` - Red-skinned potato with bold line characters
- `fingerling` - Small variety with curved characters

## Architecture

### Core Components
- **potato.py**: Main program containing core classes and CLI interface
  - `PotatoConfig`: Configuration management via dataclass
  - `GrowthStage`: Enum defining 7 growth phases (seed → maturity)
  - `PotatoArt`: ASCII art pattern management with variety support
  - `AnimationEngine`: Handles rendering frames and animation logic
  - `PotatoGrowthSimulator`: Main orchestration class

- **potato_varieties.py**: Plugin system for different potato varieties
  - `PotatoVariety`: Base class for all varieties
  - Concrete variety classes: `RussetPotato`, `YukonGoldPotato`, `RedPotato`, `FingerlingPotato`
  - Registry system via `POTATO_VARIETIES` dict

- **test_potato.py**: Comprehensive unittest suite covering all components

### Key Design Patterns
- **Plugin Architecture**: Varieties are self-contained classes with their own ASCII patterns
- **Configuration-driven**: JSON config files override defaults, CLI args override config
- **Modular Rendering**: Animation engine separates frame rendering from display logic
- **Stage-based Growth**: Seven distinct growth stages with unique ASCII art per variety

### File Outputs
- Terminal animation with configurable timing
- Text file export with all growth stages
- Both modes can run simultaneously with `--output both`

### Canvas System
- Configurable canvas size (width/height)
- Soil line automatically calculated at `height - 5`
- Pattern placement centered horizontally, aligned with soil line vertically
- Underground area rendered with soil textures (`█`, `▓`)