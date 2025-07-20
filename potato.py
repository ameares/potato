#!/usr/bin/env python3
"""
Potato Growth Animation Program

A Python program that generates animated ASCII art of potatoes growing 
through various stages from seed to harvest.
"""

import time
import os
import sys
import argparse
import json
import logging
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum


class GrowthStage(Enum):
    """Potato growth stages"""
    SEED = "seed"
    GERMINATION = "germination" 
    SPROUTING = "sprouting"
    VEGETATIVE = "vegetative"
    FLOWERING = "flowering"
    TUBER_FORMATION = "tuber_formation"
    MATURITY = "maturity"


@dataclass
class PotatoConfig:
    """Configuration for potato growth animation"""
    growth_speed: float = 2.0  # seconds between stages
    canvas_width: int = 40
    canvas_height: int = 20
    variety: str = "russet"
    show_colors: bool = True
    output_format: str = "terminal"  # terminal, file, both
    output_file: Optional[str] = None


class PotatoArt:
    """ASCII art patterns for different growth stages"""
    
    def __init__(self, variety: str = "russet"):
        self.variety = variety
        try:
            from potato_varieties import get_variety
            self.variety_obj = get_variety(variety)
            self.patterns = None  # Use variety_obj patterns
        except ImportError:
            self.variety_obj = None
            self.patterns = self._load_default_patterns()
    
    def _load_default_patterns(self) -> Dict[GrowthStage, List[str]]:
        """Load default ASCII patterns for each growth stage"""
        patterns = {
            GrowthStage.SEED: [
                "·"
            ],
            GrowthStage.GERMINATION: [
                "·",
                "┴"
            ],
            GrowthStage.SPROUTING: [
                " │",
                "·┴"
            ],
            GrowthStage.VEGETATIVE: [
                " ┌┐",
                " ││",
                "·┴┴"
            ],
            GrowthStage.FLOWERING: [
                " ❀❀",
                " ┌┐",
                " ││",
                "·┴┴"
            ],
            GrowthStage.TUBER_FORMATION: [
                " ❀❀",
                " ┌┐",
                " ││",
                "○┴┴○"
            ],
            GrowthStage.MATURITY: [
                " ❀❀❀",
                " ┌─┐",
                " │ │",
                "●┴─┴●"
            ]
        }
        return patterns
    
    def get_pattern(self, stage: GrowthStage) -> List[str]:
        """Get ASCII pattern for a specific growth stage"""
        if self.variety_obj:
            return self.variety_obj.get_pattern(stage)
        elif self.patterns:
            return self.patterns.get(stage, ["?"])
        else:
            # Load default patterns if not loaded
            self.patterns = self._load_default_patterns()
            return self.patterns.get(stage, ["?"])


class AnimationEngine:
    """Handles the animation logic and rendering"""
    
    def __init__(self, config: PotatoConfig):
        self.config = config
        self.potato_art = PotatoArt(config.variety)
        self.current_stage = 0
        self.stages = list(GrowthStage)
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def render_frame(self, stage: GrowthStage) -> str:
        """Render a single frame of the animation"""
        pattern = self.potato_art.get_pattern(stage)
        canvas = []
        
        # Create soil line
        soil_line = self.config.canvas_height - 5
        
        # Build canvas
        for row in range(self.config.canvas_height):
            line = ""
            for col in range(self.config.canvas_width):
                if row == soil_line:
                    line += "~" if col % 2 == 0 else "-"
                elif row > soil_line:
                    line += "█" if col % 3 == 0 else "▓"
                else:
                    line += " "
            canvas.append(line)
        
        # Place potato pattern
        if pattern and len(pattern) > 0:
            start_col = self.config.canvas_width // 2 - len(pattern[0]) // 2 if pattern[0] else self.config.canvas_width // 2
            start_row = soil_line - len(pattern) + 1
            
            for i, pattern_line in enumerate(pattern):
                if start_row + i >= 0 and start_row + i < len(canvas):
                    row = start_row + i
                    canvas_line = list(canvas[row])
                    for j, char in enumerate(pattern_line):
                        if start_col + j >= 0 and start_col + j < len(canvas_line):
                            canvas_line[start_col + j] = char
                    canvas[row] = ''.join(canvas_line)
        
        return '\n'.join(canvas)
    
    def animate(self):
        """Run the complete growth animation"""
        if self.config.output_format in ["terminal", "both"]:
            for stage in self.stages:
                self.clear_screen()
                frame = self.render_frame(stage)
                print(f"Growth Stage: {stage.value.title()}")
                print("=" * self.config.canvas_width)
                print(frame)
                print("=" * self.config.canvas_width)
                
                if stage != self.stages[-1]:  # Don't wait after final stage
                    time.sleep(self.config.growth_speed)
        
        if self.config.output_format in ["file", "both"]:
            self.save_to_file()
    
    def save_to_file(self):
        """Save animation frames to a file"""
        filename = self.config.output_file or "potato_growth.txt"
        with open(filename, 'w') as f:
            f.write("Potato Growth Animation\n")
            f.write("=" * 50 + "\n\n")
            
            for stage in self.stages:
                f.write(f"Stage: {stage.value.title()}\n")
                f.write("-" * 30 + "\n")
                frame = self.render_frame(stage)
                f.write(frame)
                f.write("\n\n")


class PotatoGrowthSimulator:
    """Main class that orchestrates the potato growth simulation"""
    
    def __init__(self, config: PotatoConfig):
        self.config = config
        self.animation_engine = AnimationEngine(config)
        self._setup_logging()
    
    def _setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def run(self):
        """Start the potato growth simulation"""
        self.logger.info(f"Starting potato growth simulation - variety: {self.config.variety}")
        self.animation_engine.animate()
        self.logger.info("Potato growth simulation completed")


def load_config(config_file: Optional[str] = None) -> PotatoConfig:
    """Load configuration from JSON file or use defaults"""
    config = PotatoConfig()
    
    if config_file and os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config_data = json.load(f)
            for key, value in config_data.items():
                if hasattr(config, key):
                    setattr(config, key, value)
    
    return config


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Potato Growth Animation Simulator")
    parser.add_argument("--config", "-c", help="Configuration file path")
    parser.add_argument("--speed", "-s", type=float, default=2.0, 
                       help="Growth speed (seconds between stages)")
    parser.add_argument("--variety", "-v", default="russet",
                       help="Potato variety")
    parser.add_argument("--width", "-w", type=int, default=40,
                       help="Canvas width")
    parser.add_argument("--height", type=int, default=20,
                       help="Canvas height")
    parser.add_argument("--output", "-o", choices=["terminal", "file", "both"],
                       default="terminal", help="Output format")
    parser.add_argument("--file", "-f", help="Output file name")
    parser.add_argument("--no-colors", action="store_true",
                       help="Disable color output")
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Override with command line arguments
    if args.speed != 2.0:
        config.growth_speed = args.speed
    if args.variety != "russet":
        config.variety = args.variety
    if args.width != 40:
        config.canvas_width = args.width
    if args.height != 20:
        config.canvas_height = args.height
    if args.output != "terminal":
        config.output_format = args.output
    if args.file:
        config.output_file = args.file
    if args.no_colors:
        config.show_colors = False
    
    # Create and run simulator
    simulator = PotatoGrowthSimulator(config)
    simulator.run()


if __name__ == "__main__":
    main()