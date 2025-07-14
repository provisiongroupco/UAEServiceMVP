"""
Unit tests for equipment_inspection.py
"""

import unittest
import sys
import os
from unittest.mock import MagicMock, patch, Mock
from datetime import datetime

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from equipment_inspection import EquipmentInspection
from equipment_config import EQUIPMENT_TYPES


class TestEquipmentInspection(unittest.TestCase):
    """Test cases for EquipmentInspection class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.inspection = EquipmentInspection()
        
    @patch('equipment_inspection.st')
    def test_init(self, mock_st):
        """Test EquipmentInspection initialization"""
        # Setup mock session state
        mock_st.session_state = {}
        
        # Create new instance
        inspection = EquipmentInspection()
        
        # Verify session state was initialized
        self.assertIsNotNone(inspection)
    
    @patch('equipment_inspection.st')
    def test_add_equipment(self, mock_st):
        """Test adding equipment to inspection list"""
        # Setup mock session state
        mock_st.session_state = {
            'equipment_list': [],
            'current_equipment_index': 0,
            'inspection_data': {}
        }
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Add equipment
        inspection.add_equipment('KVF')
        
        # Verify equipment was added
        self.assertEqual(len(mock_st.session_state['equipment_list']), 1)
        
        # Verify equipment structure
        equipment = mock_st.session_state['equipment_list'][0]
        self.assertEqual(equipment['type'], 'KVF')
        self.assertIn('id', equipment)
        self.assertIn('serial_number', equipment)
        self.assertIn('location', equipment)
        self.assertIn('inspection_data', equipment)
        self.assertIn('photos', equipment)
    
    @patch('equipment_inspection.st')
    def test_remove_last_equipment(self, mock_st):
        """Test removing last equipment from list"""
        # Setup mock session state with equipment
        mock_equipment = {
            'id': 'test_id',
            'type': 'KVF',
            'serial_number': 'TEST123',
            'location': 'Test Location',
            'inspection_data': {},
            'photos': {}
        }
        
        mock_st.session_state = {
            'equipment_list': [mock_equipment],
            'current_equipment_index': 0,
            'inspection_data': {}
        }
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Remove equipment
        inspection.remove_last_equipment()
        
        # Verify equipment was removed
        self.assertEqual(len(mock_st.session_state['equipment_list']), 0)
    
    @patch('equipment_inspection.st')
    def test_remove_last_equipment_empty_list(self, mock_st):
        """Test removing equipment from empty list"""
        # Setup mock session state with empty list
        mock_st.session_state = {
            'equipment_list': [],
            'current_equipment_index': 0,
            'inspection_data': {}
        }
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Should not raise error when removing from empty list
        inspection.remove_last_equipment()
        
        # List should still be empty
        self.assertEqual(len(mock_st.session_state['equipment_list']), 0)
    
    @patch('equipment_inspection.st')
    def test_render_question_yes_no(self, mock_st):
        """Test rendering yes/no question"""
        # Setup mock streamlit
        mock_st.selectbox.return_value = 'Yes'
        
        # Setup test data
        equipment = {'id': 'test_equipment'}
        item = {
            'id': 'test_item',
            'question': 'Test question?',
            'type': 'yes_no'
        }
        item_data = {}
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        inspection.render_question(equipment, item, 'test_item', item_data)
        
        # Verify selectbox was called
        mock_st.selectbox.assert_called()
        
        # Verify answer was set
        self.assertEqual(item_data['answer'], 'Yes')
    
    @patch('equipment_inspection.st')
    def test_render_question_text(self, mock_st):
        """Test rendering text question"""
        # Setup mock streamlit
        mock_st.text_input.return_value = 'Test answer'
        
        # Setup test data
        equipment = {'id': 'test_equipment'}
        item = {
            'id': 'test_item',
            'question': 'Enter text:',
            'type': 'text'
        }
        item_data = {}
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        inspection.render_question(equipment, item, 'test_item', item_data)
        
        # Verify text input was called
        mock_st.text_input.assert_called()
        
        # Verify answer was set
        self.assertEqual(item_data['answer'], 'Test answer')
    
    @patch('equipment_inspection.st')
    def test_render_question_number(self, mock_st):
        """Test rendering number question"""
        # Setup mock streamlit
        mock_st.number_input.return_value = 5
        
        # Setup test data
        equipment = {'id': 'test_equipment'}
        item = {
            'id': 'test_item',
            'question': 'Enter number:',
            'type': 'number'
        }
        item_data = {}
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        inspection.render_question(equipment, item, 'test_item', item_data)
        
        # Verify number input was called
        mock_st.number_input.assert_called()
        
        # Verify answer was set
        self.assertEqual(item_data['answer'], 5)
    
    @patch('equipment_inspection.st')
    def test_render_question_select(self, mock_st):
        """Test rendering select question"""
        # Setup mock streamlit
        mock_st.selectbox.return_value = 'Option 1'
        
        # Setup test data
        equipment = {'id': 'test_equipment'}
        item = {
            'id': 'test_item',
            'question': 'Select option:',
            'type': 'select',
            'options': ['Option 1', 'Option 2', 'Option 3']
        }
        item_data = {}
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        inspection.render_question(equipment, item, 'test_item', item_data)
        
        # Verify selectbox was called
        mock_st.selectbox.assert_called()
        
        # Verify answer was set
        self.assertEqual(item_data['answer'], 'Option 1')
    
    @patch('equipment_inspection.st')
    def test_render_question_multi_select(self, mock_st):
        """Test rendering multi-select question"""
        # Setup mock streamlit
        mock_st.multiselect.return_value = ['Option 1', 'Option 2']
        
        # Setup test data
        equipment = {'id': 'test_equipment'}
        item = {
            'id': 'test_item',
            'question': 'Select options:',
            'type': 'multi_select',
            'options': ['Option 1', 'Option 2', 'Option 3']
        }
        item_data = {}
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        inspection.render_question(equipment, item, 'test_item', item_data)
        
        # Verify multiselect was called
        mock_st.multiselect.assert_called()
        
        # Verify answer was set
        self.assertEqual(item_data['answer'], ['Option 1', 'Option 2'])
    
    @patch('equipment_inspection.st')
    def test_render_photo_upload(self, mock_st):
        """Test rendering photo upload"""
        # Setup mock streamlit
        mock_uploaded_file = MagicMock()
        mock_st.file_uploader.return_value = mock_uploaded_file
        mock_st.columns.return_value = [MagicMock(), MagicMock()]
        mock_st.success = MagicMock()
        
        # Setup test data
        equipment = {'id': 'test_equipment', 'photos': {}}
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        inspection.render_photo_upload(equipment, 'test_item', 'Test Label')
        
        # Verify file uploader was called
        mock_st.file_uploader.assert_called()
        
        # Verify photo was stored
        self.assertIn('photo_test_item', equipment['photos'])
        self.assertEqual(equipment['photos']['photo_test_item'], mock_uploaded_file)
    
    @patch('equipment_inspection.st')
    def test_render_checklist(self, mock_st):
        """Test rendering checklist"""
        # Setup mock streamlit
        mock_st.selectbox.return_value = 'Yes'
        
        # Setup test data
        equipment = {'inspection_data': {}}
        checklist = [
            {
                'id': 'test_item',
                'question': 'Test question?',
                'type': 'yes_no'
            }
        ]
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        inspection.render_checklist(equipment, checklist)
        
        # Verify item was added to inspection data
        self.assertIn('test_item', equipment['inspection_data'])
        
        # Verify selectbox was called
        mock_st.selectbox.assert_called()
    
    @patch('equipment_inspection.st')
    def test_handle_uvf_modules(self, mock_st):
        """Test handling UVF modules"""
        # Setup mock streamlit
        mock_st.markdown = MagicMock()
        mock_st.tabs.return_value = [MagicMock()]
        
        # Setup test data with module count
        equipment = {
            'inspection_data': {
                'module_count': {'answer': 2}
            }
        }
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        inspection.handle_uvf_modules(equipment)
        
        # Verify markdown was called for module inspections
        mock_st.markdown.assert_called()
        
        # Verify tabs were created
        mock_st.tabs.assert_called()
    
    @patch('equipment_inspection.st')
    def test_get_inspection_summary(self, mock_st):
        """Test getting inspection summary"""
        # Setup mock session state
        mock_equipment = {
            'type': 'KVF',
            'serial_number': 'TEST123',
            'location': 'Test Location',
            'inspection_data': {
                'test_item': {'answer': 'No', 'comment': 'Test comment'}
            },
            'photos': {'photo_test': 'test_photo.jpg'}
        }
        
        mock_st.session_state = {
            'equipment_list': [mock_equipment]
        }
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        result = inspection.get_inspection_summary()
        
        # Verify result structure
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        
        equipment_summary = result[0]
        self.assertEqual(equipment_summary['type'], 'KVF')
        self.assertEqual(equipment_summary['serial_number'], 'TEST123')
        self.assertEqual(equipment_summary['location'], 'Test Location')
        self.assertEqual(equipment_summary['photos_count'], 1)
        self.assertEqual(len(equipment_summary['issues_found']), 1)
    
    @patch('equipment_inspection.st')
    def test_validate_equipment_data(self, mock_st):
        """Test validating equipment data"""
        # Setup mock session state with missing data
        mock_equipment = {
            'type': 'KVF',
            'serial_number': '',  # Missing serial number
            'location': 'Test Location',
            'inspection_data': {}
        }
        
        mock_st.session_state = {
            'equipment_list': [mock_equipment]
        }
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        errors = inspection.validate_equipment_data()
        
        # Verify errors were found
        self.assertGreater(len(errors), 0)
        
        # Verify specific error for missing serial number
        self.assertTrue(any('Serial number is required' in error for error in errors))
    
    @patch('equipment_inspection.st')
    def test_validate_equipment_data_complete(self, mock_st):
        """Test validating complete equipment data"""
        # Setup mock session state with complete data
        mock_equipment = {
            'type': 'KVF',
            'serial_number': 'TEST123',
            'location': 'Test Location',
            'inspection_data': {}
        }
        
        mock_st.session_state = {
            'equipment_list': [mock_equipment]
        }
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Call method
        errors = inspection.validate_equipment_data()
        
        # Verify no errors for complete data
        self.assertEqual(len(errors), 0)
    
    def test_should_show_item(self):
        """Test should_show_item method"""
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Test basic functionality (always returns True for now)
        result = inspection.should_show_item({}, {}, "")
        self.assertTrue(result)
    
    @patch('equipment_inspection.st')
    def test_render_ppm_checklist(self, mock_st):
        """Test rendering PPM checklist"""
        # Setup mock streamlit
        mock_st.session_state = {'visit_type': 'AMC (Contract)'}
        
        # Setup test data
        equipment = {
            'type': 'KVF',
            'inspection_data': {}
        }
        
        # Create inspection instance
        inspection = EquipmentInspection()
        
        # Mock the render_checklist method
        inspection.render_checklist = MagicMock()
        
        # Call method
        inspection.render_ppm_checklist(equipment)
        
        # Verify render_checklist was called
        inspection.render_checklist.assert_called()


class TestEquipmentInspectionIntegration(unittest.TestCase):
    """Integration tests for EquipmentInspection class"""
    
    def test_equipment_types_coverage(self):
        """Test that all equipment types are supported"""
        inspection = EquipmentInspection()
        
        # Verify all equipment types from config are supported
        for equip_type in EQUIPMENT_TYPES.keys():
            # This should not raise an error
            checklist = EQUIPMENT_TYPES[equip_type]['checklist']
            self.assertIsInstance(checklist, list)
    
    def test_question_type_coverage(self):
        """Test that all question types are handled"""
        inspection = EquipmentInspection()
        
        # Get all question types used in config
        question_types = set()
        for equip_type, config in EQUIPMENT_TYPES.items():
            for item in config['checklist']:
                question_types.add(item['type'])
        
        # Verify all types are handled
        handled_types = {
            'yes_no', 'yes_no_na', 'text', 'number', 
            'select', 'multi_select', 'photo'
        }
        
        for q_type in question_types:
            self.assertIn(q_type, handled_types)


if __name__ == '__main__':
    unittest.main()