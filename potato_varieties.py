"""
Potato variety definitions and ASCII art patterns.
This module provides different potato varieties with unique visual characteristics.
"""

from typing import Dict, List


class PotatoVariety:
    """Base class for potato varieties"""
    
    def __init__(self, name: str):
        self.name = name
        self.patterns = self._define_patterns()
    
    def _define_patterns(self) -> Dict[str, List[str]]:
        """Define ASCII patterns for each growth stage"""
        raise NotImplementedError("Subclasses must implement _define_patterns")
    
    def get_pattern(self, stage) -> List[str]:
        """Get ASCII pattern for a specific growth stage"""
        # Handle both enum and string stage inputs
        stage_key = stage.value if hasattr(stage, 'value') else stage
        return self.patterns.get(stage_key, ["?"])


class RussetPotato(PotatoVariety):
    """Classic russet potato variety"""
    
    def __init__(self):
        super().__init__("russet")
    
    def _define_patterns(self) -> Dict[str, List[str]]:
        return {
            "seed": [
                "·"
            ],
            "germination": [
                "·",
                "┴"
            ],
            "sprouting": [
                " │",
                "·┴"
            ],
            "vegetative": [
                " ┌┐",
                " ││",
                "·┴┴"
            ],
            "flowering": [
                " ❀❀",
                " ┌┐",
                " ││",
                "·┴┴"
            ],
            "tuber_formation": [
                " ❀❀",
                " ┌┐",
                " ││",
                "○┴┴○"
            ],
            "maturity": [
                " ❀❀❀",
                " ┌─┐",
                " │ │",
                "●┴─┴●"
            ]
        }


class YukonGoldPotato(PotatoVariety):
    """Yukon Gold potato variety with yellow characteristics"""
    
    def __init__(self):
        super().__init__("yukon_gold")
    
    def _define_patterns(self) -> Dict[str, List[str]]:
        return {
            "seed": [
                "°"
            ],
            "germination": [
                "°",
                "┬"
            ],
            "sprouting": [
                " ║",
                "°┬"
            ],
            "vegetative": [
                " ╔╗",
                " ║║",
                "°┬┬"
            ],
            "flowering": [
                " ✿✿",
                " ╔╗",
                " ║║",
                "°┬┬"
            ],
            "tuber_formation": [
                " ✿✿",
                " ╔╗",
                " ║║",
                "◐┬┬◑"
            ],
            "maturity": [
                " ✿✿✿",
                " ╔═╗",
                " ║ ║",
                "◉┬═┬◉"
            ]
        }


class RedPotato(PotatoVariety):
    """Red potato variety with distinctive red skin"""
    
    def __init__(self):
        super().__init__("red")
    
    def _define_patterns(self) -> Dict[str, List[str]]:
        return {
            "seed": [
                "•"
            ],
            "germination": [
                "•",
                "┼"
            ],
            "sprouting": [
                " ┃",
                "•┼"
            ],
            "vegetative": [
                " ┏┓",
                " ┃┃",
                "•┼┼"
            ],
            "flowering": [
                " ❋❋",
                " ┏┓",
                " ┃┃",
                "•┼┼"
            ],
            "tuber_formation": [
                " ❋❋",
                " ┏┓",
                " ┃┃",
                "◈┼┼◈"
            ],
            "maturity": [
                " ❋❋❋",
                " ┏━┓",
                " ┃ ┃",
                "◆┼━┼◆"
            ]
        }


class FingerlingPotato(PotatoVariety):
    """Small fingerling potato variety"""
    
    def __init__(self):
        super().__init__("fingerling")
    
    def _define_patterns(self) -> Dict[str, List[str]]:
        return {
            "seed": [
                "⋅"
            ],
            "germination": [
                "⋅",
                "╷"
            ],
            "sprouting": [
                " │",
                "⋅╷"
            ],
            "vegetative": [
                " ╭╮",
                " ││",
                "⋅╷╷"
            ],
            "flowering": [
                " ✾✾",
                " ╭╮",
                " ││",
                "⋅╷╷"
            ],
            "tuber_formation": [
                " ✾✾",
                " ╭╮",
                " ││",
                "○╷╷○"
            ],
            "maturity": [
                " ✾✾✾",
                " ╭─╮",
                " │ │",
                "◇╷─╷◇"
            ]
        }


# Variety registry
POTATO_VARIETIES = {
    "russet": RussetPotato,
    "yukon_gold": YukonGoldPotato,
    "red": RedPotato,
    "fingerling": FingerlingPotato
}


def get_variety(name: str) -> PotatoVariety:
    """Get a potato variety by name"""
    variety_class = POTATO_VARIETIES.get(name.lower(), RussetPotato)
    return variety_class()


def list_varieties() -> List[str]:
    """List all available potato varieties"""
    return list(POTATO_VARIETIES.keys())