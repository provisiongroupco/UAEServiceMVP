"""
Unit tests for equipment_config.py
"""

import unittest
import sys
import os

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from equipment_config import (
    EQUIPMENT_TYPES, 
    UVF_MODULE_CHECKLIST, 
    PPM_CHECKLIST,
    UV_PPM_ITEMS,
    WATER_WASH_PPM_ITEMS,
    ECOLOGY_PPM_ITEMS
)


class TestEquipmentConfig(unittest.TestCase):
    """Test cases for equipment configuration"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.expected_equipment_types = [
            "KVF", "KVI", "UVF", "CMW", "MARVEL", "ECOLOGY", "MOBICHEF"
        ]
    
    def test_equipment_types_structure(self):
        """Test that all expected equipment types are present"""
        self.assertIsInstance(EQUIPMENT_TYPES, dict)
        
        # Check that all expected equipment types exist
        for equip_type in self.expected_equipment_types:
            self.assertIn(equip_type, EQUIPMENT_TYPES)
            
        # Check that each equipment type has required fields
        for equip_type, config in EQUIPMENT_TYPES.items():
            self.assertIn('name', config)
            self.assertIn('checklist', config)
            self.assertIsInstance(config['name'], str)
            self.assertIsInstance(config['checklist'], list)
            
    def test_equipment_names(self):
        """Test that equipment names are correctly defined"""
        expected_names = {
            "KVF": "KVF Hood",
            "KVI": "KVI Hood", 
            "UVF": "UVF Hood",
            "CMW": "CMW Hood (Cold Mist Wash)",
            "MARVEL": "MARVEL System",
            "ECOLOGY": "Ecology Unit",
            "MOBICHEF": "Mobichef"
        }
        
        for equip_type, expected_name in expected_names.items():
            self.assertEqual(EQUIPMENT_TYPES[equip_type]['name'], expected_name)
    
    def test_checklist_item_structure(self):
        """Test that checklist items have the correct structure"""
        for equip_type, config in EQUIPMENT_TYPES.items():
            checklist = config['checklist']
            
            for item in checklist:
                # Required fields
                self.assertIn('id', item)
                self.assertIn('question', item)
                self.assertIn('type', item)
                
                # Field types
                self.assertIsInstance(item['id'], str)
                self.assertIsInstance(item['question'], str)
                self.assertIsInstance(item['type'], str)
                
                # Valid question types
                valid_types = ['yes_no', 'yes_no_na', 'text', 'number', 'select', 'multi_select', 'photo']
                self.assertIn(item['type'], valid_types)
    
    def test_conditions_structure(self):
        """Test that conditions have the correct structure"""
        for equip_type, config in EQUIPMENT_TYPES.items():
            checklist = config['checklist']
            
            for item in checklist:
                if 'conditions' in item:
                    conditions = item['conditions']
                    self.assertIsInstance(conditions, dict)
                    
                    for condition_key, condition_value in conditions.items():
                        self.assertIsInstance(condition_value, dict)
                        
                        # Check valid condition fields
                        valid_condition_fields = ['photo', 'comment', 'action', 'follow_up']
                        for field in condition_value:
                            self.assertIn(field, valid_condition_fields)
    
    def test_uvf_module_checklist(self):
        """Test UVF module checklist structure"""
        self.assertIsInstance(UVF_MODULE_CHECKLIST, list)
        
        for item in UVF_MODULE_CHECKLIST:
            self.assertIn('id', item)
            self.assertIn('question', item)
            self.assertIn('type', item)
            
            # Check for required field
            if 'required' in item:
                self.assertIsInstance(item['required'], bool)
    
    def test_ppm_checklist_structure(self):
        """Test PPM checklist structure"""
        ppm_lists = [PPM_CHECKLIST, UV_PPM_ITEMS, WATER_WASH_PPM_ITEMS, ECOLOGY_PPM_ITEMS]
        
        for ppm_list in ppm_lists:
            self.assertIsInstance(ppm_list, list)
            
            for item in ppm_list:
                self.assertIn('id', item)
                self.assertIn('question', item)
                self.assertIn('type', item)
    
    def test_follow_up_questions(self):
        """Test that follow-up questions are properly structured"""
        def check_follow_up(items):
            for item in items:
                if 'conditions' in item:
                    for condition_key, condition_value in item['conditions'].items():
                        if 'follow_up' in condition_value:
                            follow_up = condition_value['follow_up']
                            self.assertIsInstance(follow_up, list)
                            # Recursively check follow-up items
                            check_follow_up(follow_up)
        
        for equip_type, config in EQUIPMENT_TYPES.items():
            check_follow_up(config['checklist'])
    
    def test_kvf_hood_checklist(self):
        """Test KVF hood specific checklist items"""
        kvf_checklist = EQUIPMENT_TYPES['KVF']['checklist']
        
        # Check for essential KVF items
        item_ids = [item['id'] for item in kvf_checklist]
        expected_ids = [
            'lights_operational',
            'lights_ballast',
            'capture_jet_fan',
            'ksa_filters_condition',
            'ksa_filters_in_place'
        ]
        
        for expected_id in expected_ids:
            self.assertIn(expected_id, item_ids)
    
    def test_uvf_hood_checklist(self):
        """Test UVF hood specific checklist items"""
        uvf_checklist = EQUIPMENT_TYPES['UVF']['checklist']
        
        # Check for essential UVF items
        item_ids = [item['id'] for item in uvf_checklist]
        expected_ids = [
            'monitoring_console_type',
            'module_count',
            'alarms_registered',
            'uv_power_cable',
            'filter_magnets'
        ]
        
        for expected_id in expected_ids:
            self.assertIn(expected_id, item_ids)
    
    def test_marvel_system_checklist(self):
        """Test MARVEL system specific checklist items"""
        marvel_checklist = EQUIPMENT_TYPES['MARVEL']['checklist']
        
        # Check for essential MARVEL items
        item_ids = [item['id'] for item in marvel_checklist]
        expected_ids = [
            'power_supply',
            'touch_screen_operational',
            'ntc_sensors',
            'ir_sensors',
            'abd_dampers'
        ]
        
        for expected_id in expected_ids:
            self.assertIn(expected_id, item_ids)
    
    def test_ecology_unit_checklist(self):
        """Test Ecology unit specific checklist items"""
        ecology_checklist = EQUIPMENT_TYPES['ECOLOGY']['checklist']
        
        # Check for essential Ecology items
        item_ids = [item['id'] for item in ecology_checklist]
        expected_ids = [
            'control_panel',
            'touch_screen_operational',
            'esp_section',
            'filter_types'
        ]
        
        for expected_id in expected_ids:
            self.assertIn(expected_id, item_ids)
    
    def test_multi_select_options(self):
        """Test multi-select questions have proper options"""
        for equip_type, config in EQUIPMENT_TYPES.items():
            checklist = config['checklist']
            
            for item in checklist:
                if item['type'] == 'multi_select':
                    self.assertIn('options', item)
                    self.assertIsInstance(item['options'], list)
                    self.assertGreater(len(item['options']), 0)
    
    def test_select_options(self):
        """Test select questions have proper options"""
        for equip_type, config in EQUIPMENT_TYPES.items():
            checklist = config['checklist']
            
            for item in checklist:
                if item['type'] == 'select':
                    self.assertIn('options', item)
                    self.assertIsInstance(item['options'], list)
                    self.assertGreater(len(item['options']), 0)
    
    def test_required_fields(self):
        """Test that required fields are properly marked"""
        for equip_type, config in EQUIPMENT_TYPES.items():
            checklist = config['checklist']
            
            for item in checklist:
                if 'required' in item:
                    self.assertIsInstance(item['required'], bool)
    
    def test_unique_item_ids(self):
        """Test that item IDs are unique within each equipment type"""
        for equip_type, config in EQUIPMENT_TYPES.items():
            checklist = config['checklist']
            
            item_ids = []
            for item in checklist:
                self.assertNotIn(item['id'], item_ids, 
                               f"Duplicate ID '{item['id']}' found in {equip_type}")
                item_ids.append(item['id'])


if __name__ == '__main__':
    unittest.main()