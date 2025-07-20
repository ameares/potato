# Potato Growth Simulator

A Python program that generates animated ASCII art of potatoes growing through various stages from seed to harvest.

## Features

- **7 Growth Stages**: Seed, Germination, Sprouting, Vegetative Growth, Flowering, Tuber Formation, and Maturity
- **Multiple Potato Varieties**: Russet, Yukon Gold, Red, and Fingerling potatoes with unique ASCII patterns
- **Configurable Animation**: Adjustable growth speed, canvas size, and timing
- **Flexible Output**: Terminal display, file export, or both
- **CLI Interface**: Easy-to-use command line interface with extensive options
- **Configuration Support**: JSON configuration files for preset configurations

## Installation

No external dependencies required - uses only Python standard library.

```bash
git clone <repository>
cd potato
python3 potato.py --help
```

## Usage

### Basic Usage

```bash
# Run with default settings (russet potato, terminal display)
python3 potato.py

# Run with different variety and speed
python3 potato.py --variety yukon_gold --speed 1.0

# Export to file
python3 potato.py --output file --file my_potato.txt

# Use custom canvas size
python3 potato.py --width 60 --height 30
```

### Command Line Options

```
usage: potato.py [-h] [--config CONFIG] [--speed SPEED] [--variety VARIETY]
                 [--width WIDTH] [--height HEIGHT]
                 [--output {terminal,file,both}] [--file FILE] [--no-colors]

options:
  --config, -c          Configuration file path
  --speed, -s           Growth speed (seconds between stages)
  --variety, -v         Potato variety (russet, yukon_gold, red, fingerling)
  --width, -w           Canvas width
  --height              Canvas height
  --output, -o          Output format (terminal, file, both)
  --file, -f            Output file name
  --no-colors           Disable color output
```

### Configuration File

Create a `config.json` file:

```json
{
    "growth_speed": 1.5,
    "canvas_width": 50,
    "canvas_height": 25,
    "variety": "yukon_gold",
    "show_colors": true,
    "output_format": "both",
    "output_file": "potato_animation.txt"
}
```

Then run with:
```bash
python3 potato.py --config config.json
```

## Potato Varieties

Each variety has unique ASCII art patterns:

- **Russet**: Classic potato with standard box-drawing characters
- **Yukon Gold**: Golden variety with double-line characters
- **Red**: Red-skinned potato with bold line characters
- **Fingerling**: Small variety with curved characters

## Growth Stages

1. **Seed**: A small dot representing the planted seed
2. **Germination**: Root system begins to develop
3. **Sprouting**: Green shoot emerges from soil
4. **Vegetative Growth**: Stem and leaves develop
5. **Flowering**: Optional flower stage appears
6. **Tuber Formation**: Underground potatoes begin forming
7. **Maturity**: Full-grown plant with visible potato harvest

## Architecture

The program follows a modular design:

- `potato.py`: Main program with core classes and CLI
- `potato_varieties.py`: Plugin system for different potato varieties
- `config.json`: Configuration management
- `test_potato.py`: Comprehensive test suite

### Core Classes

- `PotatoConfig`: Configuration management
- `GrowthStage`: Enumeration of growth phases
- `PotatoArt`: ASCII art pattern management
- `AnimationEngine`: Rendering and animation logic
- `PotatoGrowthSimulator`: Main orchestration class

## Testing

Run the test suite:

```bash
python3 test_potato.py
```

## Examples

### Quick Animation
```bash
python3 potato.py --speed 0.5
```

### Export All Varieties
```bash
for variety in russet yukon_gold red fingerling; do
    python3 potato.py --variety $variety --output file --file "${variety}_growth.txt" --speed 0.1
done
```

### Large Canvas Animation
```bash
python3 potato.py --width 80 --height 40 --speed 1.0
```

## Technical Details

- **Python Version**: 3.8+
- **Platform**: Linux terminal (optimized for ANSI terminals)
- **Character Encoding**: UTF-8 for special Unicode characters
- **Performance**: Efficient memory usage for long animations
- **File Format**: Plain text with Unicode characters

## Contributing

1. Add new varieties by creating subclasses of `PotatoVariety`
2. Extend growth stages by modifying the `GrowthStage` enum
3. Enhance ASCII patterns in variety classes
4. Add tests for new functionality

## License

Open source - feel free to modify and distribute.