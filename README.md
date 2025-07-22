# 🥔 Potato Growth Simulator 

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-linux-lightgrey.svg)

**Watch your potatoes grow in beautiful ASCII art! 🌱➡️🥔**

*A mesmerizing Python program that simulates potato growth through animated ASCII art*

</div>

---

## 🎥 What This Does

Ever wondered what it looks like when a potato grows? Wonder no more! This program creates stunning ASCII animations showing the complete lifecycle of a potato from a tiny seed to a fully grown, harvest-ready tuber. 

**Choose your potato destiny:**
- 🤎 **Russet** - The classic American potato  
- 🟡 **Yukon Gold** - Creamy and delicious
- 🔴 **Red** - Beautiful red-skinned variety
- 🥖 **Fingerling** - Cute little finger-shaped potatoes

## ✨ Features

🎬 **12 Growth Stages** - From seed to harvest ready, watch every moment  
🎨 **4 Unique Varieties** - Each with custom ASCII art patterns  
⚡ **Configurable Speed** - Control the pace of growth  
📐 **Custom Canvas** - Set your own animation dimensions  
💾 **Multiple Outputs** - Terminal display, file export, or both  
🎛️ **CLI Interface** - Professional command-line interface  
⚙️ **JSON Config** - Save your favorite settings  

## 🚀 Quick Start

**Zero dependencies needed!** Just Python 3.8+ and your terminal.

```bash
# Clone and run immediately
git clone <your-repo-url>
cd potato-growth-simulator
python3 potato.py
```

*Sit back and watch your potato grow! 🍿*

## 🎮 Usage Examples

### 🏃‍♂️ Quick & Easy
```bash
# Default magic - russet potato in terminal
python3 potato.py

# Speed run! ⚡
python3 potato.py --speed 0.5 --variety yukon_gold

# Save your masterpiece 💾
python3 potato.py --output file --file my_epic_potato.txt

# Go big or go home! 📏
python3 potato.py --width 80 --height 40
```

### 🎛️ All Command Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--config` | `-c` | 📄 Configuration file | `--config settings.json` |
| `--speed` | `-s` | ⏱️ Seconds between stages | `--speed 1.5` |
| `--variety` | `-v` | 🥔 Potato type | `--variety red` |
| `--width` | `-w` | ↔️ Canvas width | `--width 60` |
| `--height` | | ↕️ Canvas height | `--height 30` |
| `--output` | `-o` | 📺 Where to show | `--output both` |
| `--file` | `-f` | 💾 Output filename | `--file potato.txt` |
| `--no-colors` | | 🎨 Disable colors | `--no-colors` |

### ⚙️ Configuration File

Create your ultimate potato-growing setup! Save this as `config.json`:

```json
{
    "growth_speed": 1.5,
    "canvas_width": 50,
    "canvas_height": 25,
    "variety": "yukon_gold",
    "show_colors": true,
    "output_format": "both",
    "output_file": "my_amazing_potato.txt"
}
```

Then activate your settings:
```bash
python3 potato.py --config config.json
```

## 🥔 Meet the Potato Family

Each variety is a unique ASCII masterpiece with its own personality:

| Variety | Emoji | Description | ASCII Style |
|---------|-------|-------------|-------------|
| **Russet** | 🤎 | The dependable classic | Standard box-drawing |
| **Yukon Gold** | 🟡 | Smooth and buttery | Double-line elegance |
| **Red** | 🔴 | Bold and beautiful | Thick line characters |
| **Fingerling** | 🥖 | Cute and compact | Curved artistic flair |

*Each potato tells its own growth story through carefully crafted ASCII art!*

## 🌱 The Journey of Growth

Watch your potato transform through **12 epic stages**:

| Stage | Description | Visual |
|-------|-------------|--------|
| 🌰 **Seed** | The humble beginning | A tiny dot in the soil |
| 🌱 **Germination** | Life awakens | Roots start spreading |
| 🌿 **Sprouting** | Breaking ground | Green shoot emerges |
| 🌱 **Early Vegetative** | Getting stronger | Small leaves appear |
| 🍃 **Vegetative** | Growing up | Stem and leaves develop |
| 🌳 **Root Development** | Underground expansion | Root system grows |
| 🌸 **Flowering** | Beauty blooms | Flowers appear (optional) |
| 🥔 **Early Tuber** | Magic begins | First potatoes form |
| 🥔 **Tuber Formation** | Getting serious | More potatoes develop |
| 🥔 **Tuber Bulking** | Size matters | Potatoes grow bigger |
| 🌿 **Maturity** | Almost ready | Full-grown plant |
| 🥔 **Harvest Ready** | The grand finale | Time to dig up your treasure! |

## 🏗️ Architecture

**Clean, modular, and extensible design:**

```
🏛️ potato.py              - Main program + CLI magic
🔌 potato_varieties.py     - Plugin system for varieties  
⚙️ config.json            - Your personal settings
🧪 test_potato.py          - Bulletproof test suite
```

### 🧩 Core Components

| Class | Purpose | Superpower |
|-------|---------|------------|
| `PotatoConfig` | 📋 Configuration | Manages all your settings |
| `GrowthStage` | 📊 Stage tracking | Knows every growth phase |
| `PotatoArt` | 🎨 ASCII artistry | Creates beautiful patterns |
| `AnimationEngine` | 🎬 Rendering | Brings potatoes to life |
| `PotatoGrowthSimulator` | 🎭 The director | Orchestrates the whole show |

## 🧪 Testing

Ensure everything works perfectly:

```bash
python3 test_potato.py
```

*All tests pass? Your potatoes are ready to grow! ✅*

## 🎪 Epic Examples

### ⚡ Speed Demon
```bash
# Watch a potato grow in hyperspeed!
python3 potato.py --speed 0.5
```

### 🏭 Potato Factory (All Varieties)
```bash
# Create a complete potato collection
for variety in russet yukon_gold red fingerling; do
    python3 potato.py --variety $variety --output file --file "${variety}_masterpiece.txt" --speed 0.1
done
```

### 🎬 IMAX Experience  
```bash
# Go big screen with your potato!
python3 potato.py --width 80 --height 40 --speed 1.0
```

### 🎨 The Artist's Setup
```bash
# Perfect for potato connoisseurs
python3 potato.py --variety fingerling --speed 2.0 --output both --file gallery_piece.txt
```

## 🔧 Technical Specs

| Requirement | Details |
|-------------|---------|
| 🐍 **Python** | 3.8+ (no external deps!) |
| 💻 **Platform** | Linux terminal (ANSI optimized) |
| 🔤 **Encoding** | UTF-8 for beautiful Unicode |
| ⚡ **Performance** | Memory efficient for marathon sessions |
| 📄 **Output** | Plain text with Unicode magic |

## 🤝 Contributing

Want to grow the potato empire? Here's how:

1. 🥔 **New Varieties**: Create subclasses of `PotatoVariety`
2. 🌱 **Growth Stages**: Extend the `GrowthStage` enum
3. 🎨 **ASCII Art**: Enhance patterns in variety classes  
4. 🧪 **Tests**: Add tests for new functionality

*Every contribution makes the potato world more beautiful!*

## 📜 License

**MIT Licensed** - Grow potatoes freely! 

See [LICENSE.md](LICENSE.md) for the legal potato growing terms.

---

<div align="center">

**Made with 🥔 and ❤️**

*Happy potato growing! May your ASCII art be ever beautiful and your growth stages smooth!* 

🌱➡️🥔

</div>