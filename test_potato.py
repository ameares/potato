#!/usr/bin/env python3
"""
Basic tests for the potato growth simulator
"""

import unittest
import tempfile
import os
from potato import PotatoConfig, PotatoArt, AnimationEngine, GrowthStage, PotatoGrowthSimulator
from potato_varieties import get_variety, list_varieties, RussetPotato


class TestPotatoConfig(unittest.TestCase):
    def test_default_config(self):
        config = PotatoConfig()
        self.assertEqual(config.growth_speed, 2.0)
        self.assertEqual(config.canvas_width, 40)
        self.assertEqual(config.canvas_height, 20)
        self.assertEqual(config.variety, "russet")
        self.assertTrue(config.show_colors)
        self.assertEqual(config.output_format, "terminal")


class TestPotatoArt(unittest.TestCase):
    def test_default_patterns(self):
        art = PotatoArt()
        pattern = art.get_pattern(GrowthStage.SEED)
        self.assertIsInstance(pattern, list)
        self.assertGreater(len(pattern), 0)
    
    def test_all_growth_stages_have_patterns(self):
        art = PotatoArt()
        for stage in GrowthStage:
            pattern = art.get_pattern(stage)
            self.assertIsInstance(pattern, list)
            self.assertGreater(len(pattern), 0)


class TestPotatoVarieties(unittest.TestCase):
    def test_list_varieties(self):
        varieties = list_varieties()
        self.assertIn('russet', varieties)
        self.assertIn('yukon_gold', varieties)
        self.assertIn('red', varieties)
        self.assertIn('fingerling', varieties)
    
    def test_get_variety(self):
        russet = get_variety('russet')
        self.assertEqual(russet.name, 'russet')
        
        # Test unknown variety falls back to russet
        unknown = get_variety('unknown_variety')
        self.assertIsInstance(unknown, RussetPotato)
    
    def test_variety_patterns(self):
        for variety_name in list_varieties():
            variety = get_variety(variety_name)
            for stage in GrowthStage:
                pattern = variety.get_pattern(stage)
                self.assertIsInstance(pattern, list)
                self.assertGreater(len(pattern), 0)


class TestAnimationEngine(unittest.TestCase):
    def test_render_frame(self):
        config = PotatoConfig()
        engine = AnimationEngine(config)
        frame = engine.render_frame(GrowthStage.SEED)
        
        self.assertIsInstance(frame, str)
        lines = frame.split('\n')
        self.assertEqual(len(lines), config.canvas_height)
        
        # Check that each line has the correct width
        for line in lines:
            self.assertEqual(len(line), config.canvas_width)
    
    def test_different_canvas_sizes(self):
        config = PotatoConfig()
        config.canvas_width = 60
        config.canvas_height = 30
        
        engine = AnimationEngine(config)
        frame = engine.render_frame(GrowthStage.MATURITY)
        
        lines = frame.split('\n')
        self.assertEqual(len(lines), 30)
        for line in lines:
            self.assertEqual(len(line), 60)


class TestFileExport(unittest.TestCase):
    def test_file_export(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
            tmp_path = tmp.name
        
        try:
            config = PotatoConfig()
            config.output_format = "file"
            config.output_file = tmp_path
            config.growth_speed = 0.01  # Very fast for testing
            
            simulator = PotatoGrowthSimulator(config)
            simulator.run()
            
            # Check that file was created and has content
            self.assertTrue(os.path.exists(tmp_path))
            with open(tmp_path, 'r') as f:
                content = f.read()
            
            self.assertIn("Potato Growth Animation", content)
            self.assertIn("Stage: Seed", content)
            self.assertIn("Stage: Maturity", content)
            
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)


class TestGrowthStages(unittest.TestCase):
    def test_all_stages_exist(self):
        expected_stages = [
            GrowthStage.SEED,
            GrowthStage.GERMINATION,
            GrowthStage.SPROUTING,
            GrowthStage.VEGETATIVE,
            GrowthStage.FLOWERING,
            GrowthStage.TUBER_FORMATION,
            GrowthStage.MATURITY
        ]
        
        actual_stages = list(GrowthStage)
        self.assertEqual(len(actual_stages), len(expected_stages))
        
        for stage in expected_stages:
            self.assertIn(stage, actual_stages)


if __name__ == '__main__':
    unittest.main()