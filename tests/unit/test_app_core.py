"""
Unit tests for core functions in app.py
"""

import unittest
import sys
import os
from unittest.mock import MagicMock, patch, Mock
from datetime import datetime
from io import BytesIO

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import (
    find_question_text,
    get_kitchen_summary,
    create_technical_report,
    render_checklist_item
)
from equipment_config import EQUIPMENT_TYPES


class TestAppCore(unittest.TestCase):
    """Test cases for core app functions"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.sample_equipment = {
            'type': 'KVF',
            'location': 'Main Kitchen',
            'inspection_data': {
                'lights_operational': {'answer': 'Yes', 'comment': 'Working fine'},
                'lights_ballast': {'answer': 'Yes'},
                'capture_jet_fan': {'answer': 'No', 'comment': 'Needs repair'},
                'marvel_power_supply': {'answer': 'Yes'}
            },
            'photos': {
                'photo_lights_operational': 'mock_photo1.jpg',
                'photo_capture_jet_fan': 'mock_photo2.jpg'
            },
            'with_marvel': True
        }
        
        self.sample_kitchen = {
            'name': 'Main Kitchen',
            'equipment_list': [self.sample_equipment]
        }
    
    def test_find_question_text_basic(self):
        """Test finding question text for basic items"""
        # Test with KVF equipment
        result = find_question_text('KVF', 'lights_operational')
        self.assertEqual(result, 'Are the hood lights operational?')
        
        # Test with UVF equipment
        result = find_question_text('UVF', 'module_count')
        self.assertEqual(result, 'How many modules are connected to the monitoring system?')
    
    def test_find_question_text_marvel(self):
        """Test finding question text for Marvel items"""
        # Test with Marvel prefix
        result = find_question_text('KVF', 'marvel_power_supply')
        self.assertEqual(result, 'Power supply is available for marvel control panel?')
    
    def test_find_question_text_fallback(self):
        """Test fallback when question text not found"""
        # Test with non-existent item
        result = find_question_text('KVF', 'non_existent_item')
        self.assertEqual(result, 'Non Existent Item')
    
    @patch('app.st.session_state')
    def test_get_kitchen_summary_basic(self, mock_session_state):
        """Test getting kitchen summary with basic data"""
        # Setup mock session state
        mock_session_state.kitchen_list = [self.sample_kitchen]
        
        result = get_kitchen_summary()
        
        # Verify structure
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        
        kitchen_summary = result[0]
        self.assertEqual(kitchen_summary['name'], 'Main Kitchen')
        self.assertEqual(len(kitchen_summary['equipment']), 1)
        
        equipment_summary = kitchen_summary['equipment'][0]
        self.assertEqual(equipment_summary['type'], 'KVF')
        self.assertEqual(equipment_summary['location'], 'Main Kitchen')
        self.assertTrue(equipment_summary['with_marvel'])
    
    @patch('app.st.session_state')
    def test_get_kitchen_summary_responses(self, mock_session_state):
        """Test kitchen summary response categorization"""
        # Setup mock session state
        mock_session_state.kitchen_list = [self.sample_kitchen]
        
        result = get_kitchen_summary()
        equipment_summary = result[0]['equipment'][0]
        
        # Check yes responses
        yes_responses = equipment_summary['yes_responses']
        self.assertGreater(len(yes_responses), 0)
        
        # Check no responses
        no_responses = equipment_summary['no_responses']
        self.assertGreater(len(no_responses), 0)
        
        # Verify no response has correct structure
        no_response = no_responses[0]
        self.assertIn('item', no_response)
        self.assertIn('question', no_response)
        self.assertIn('answer', no_response)
        self.assertIn('comment', no_response)
        self.assertEqual(no_response['answer'], 'No')
    
    @patch('app.st.session_state')
    def test_get_kitchen_summary_photos(self, mock_session_state):
        """Test kitchen summary photo categorization"""
        # Setup mock session state
        mock_session_state.kitchen_list = [self.sample_kitchen]
        
        result = get_kitchen_summary()
        equipment_summary = result[0]['equipment'][0]
        
        # Check photos count
        self.assertEqual(equipment_summary['photos_count'], 2)
        
        # Check photo categorization
        self.assertIn('yes_photos', equipment_summary)
        self.assertIn('no_photos', equipment_summary)
    
    @patch('app.st.session_state')
    def test_get_kitchen_summary_empty(self, mock_session_state):
        """Test kitchen summary with empty data"""
        # Setup mock session state with empty kitchen list
        mock_session_state.kitchen_list = []
        
        result = get_kitchen_summary()
        
        # Should return empty list
        self.assertEqual(result, [])
    
    @patch('app.st.session_state')
    def test_get_kitchen_summary_no_equipment(self, mock_session_state):
        """Test kitchen summary with kitchen but no equipment"""
        # Setup kitchen with no equipment
        empty_kitchen = {
            'name': 'Empty Kitchen',
            'equipment_list': []
        }
        mock_session_state.kitchen_list = [empty_kitchen]
        
        result = get_kitchen_summary()
        
        # Should return empty list since no equipment
        self.assertEqual(result, [])
    
    @patch('app.Document')
    @patch('app.os.path.exists')
    def test_create_technical_report_basic(self, mock_exists, mock_document):
        """Test creating technical report with basic data"""
        # Setup mocks
        mock_exists.return_value = False
        mock_doc = MagicMock()
        mock_document.return_value = mock_doc
        
        # Setup mock document structure
        mock_doc.sections = [MagicMock()]
        mock_doc.add_paragraph.return_value = MagicMock()
        mock_doc.add_heading.return_value = MagicMock()
        mock_doc.add_table.return_value = MagicMock()
        mock_doc.add_page_break.return_value = MagicMock()
        mock_doc.save = MagicMock()
        
        # Test data
        test_data = {
            'customer_name': 'SELA Company',
            'project_name': 'Test Project',
            'contact_person': 'John Doe',
            'outlet_location': 'Riyadh',
            'contact_number': '+966123456789',
            'visit_type': 'Service Call',
            'visit_class': 'To Be Invoiced',
            'date': '2024-01-01',
            'equipment_inspection': [],
            'work_performed': 'Test work performed',
            'recommendations': 'Test recommendations',
            'technician_name': 'Tech Name',
            'technician_id': 'TECH001',
            'service_date': '2024-01-01'
        }
        
        # Call function
        result = create_technical_report(test_data)
        
        # Verify result is BytesIO
        self.assertIsInstance(result, BytesIO)
        
        # Verify document creation
        mock_document.assert_called_once()
        mock_doc.save.assert_called_once()
    
    @patch('app.Document')
    @patch('app.os.path.exists')
    def test_create_technical_report_with_template(self, mock_exists, mock_document):
        """Test creating technical report with template"""
        # Setup mocks
        mock_exists.return_value = True
        mock_doc = MagicMock()
        mock_document.return_value = mock_doc
        
        # Setup mock document structure
        mock_doc.sections = [MagicMock()]
        mock_doc.add_paragraph.return_value = MagicMock()
        mock_doc.add_heading.return_value = MagicMock()
        mock_doc.add_table.return_value = MagicMock()
        mock_doc.add_page_break.return_value = MagicMock()
        mock_doc.save = MagicMock()
        
        # Test data
        test_data = {
            'customer_name': 'SELA Company',
            'project_name': 'Test Project',
            'contact_person': 'John Doe',
            'outlet_location': 'Riyadh',
            'contact_number': '+966123456789',
            'visit_type': 'Service Call',
            'visit_class': 'To Be Invoiced',
            'date': '2024-01-01',
            'equipment_inspection': [],
            'work_performed': 'Test work performed',
            'recommendations': 'Test recommendations',
            'technician_name': 'Tech Name',
            'technician_id': 'TECH001',
            'service_date': '2024-01-01'
        }
        
        # Call function
        result = create_technical_report(test_data)
        
        # Verify template path was used
        expected_template_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Templates', 'Report Letter Head.docx')
        mock_document.assert_called_once()
    
    @patch('app.st')
    def test_render_checklist_item_yes_no(self, mock_st):
        """Test rendering yes/no checklist item"""
        # Setup mock streamlit
        mock_st.selectbox.return_value = 'Yes'
        mock_st.session_state = {}
        
        # Setup test data
        equipment = {
            'inspection_data': {}
        }
        
        item = {
            'id': 'test_item',
            'question': 'Test question?',
            'type': 'yes_no',
            'conditions': {
                'yes': {'photo': True, 'comment': False},
                'no': {'photo': True, 'comment': True}
            }
        }
        
        # Call function
        render_checklist_item(equipment, item, 'test_prefix')
        
        # Verify item was added to inspection data
        self.assertIn('test_item', equipment['inspection_data'])
        
        # Verify selectbox was called
        mock_st.selectbox.assert_called()
    
    @patch('app.st')
    def test_render_checklist_item_text(self, mock_st):
        """Test rendering text checklist item"""
        # Setup mock streamlit
        mock_st.text_input.return_value = 'Test answer'
        mock_st.session_state = {}
        
        # Setup test data
        equipment = {
            'inspection_data': {}
        }
        
        item = {
            'id': 'test_text_item',
            'question': 'Enter text:',
            'type': 'text'
        }
        
        # Call function
        render_checklist_item(equipment, item, 'test_prefix')
        
        # Verify item was added to inspection data
        self.assertIn('test_text_item', equipment['inspection_data'])
        
        # Verify text input was called
        mock_st.text_input.assert_called()
    
    @patch('app.st')
    def test_render_checklist_item_number(self, mock_st):
        """Test rendering number checklist item"""
        # Setup mock streamlit
        mock_st.number_input.return_value = 5
        mock_st.session_state = {}
        
        # Setup test data
        equipment = {
            'inspection_data': {}
        }
        
        item = {
            'id': 'test_number_item',
            'question': 'Enter number:',
            'type': 'number'
        }
        
        # Call function
        render_checklist_item(equipment, item, 'test_prefix')
        
        # Verify item was added to inspection data
        self.assertIn('test_number_item', equipment['inspection_data'])
        
        # Verify number input was called
        mock_st.number_input.assert_called()
    
    @patch('app.st')
    def test_render_checklist_item_with_conditions(self, mock_st):
        """Test rendering checklist item with conditions"""
        # Setup mock streamlit
        mock_st.selectbox.return_value = 'No'
        mock_st.session_state = {}
        mock_st.file_uploader.return_value = None
        mock_st.text_area.return_value = 'Test comment'
        mock_st.warning = MagicMock()
        mock_st.markdown = MagicMock()
        mock_st.success = MagicMock()
        mock_st.container.return_value.__enter__ = MagicMock(return_value=MagicMock())
        mock_st.container.return_value.__exit__ = MagicMock(return_value=None)
        mock_st.columns.return_value = [MagicMock(), MagicMock()]
        
        # Setup test data
        equipment = {
            'inspection_data': {}
        }
        
        item = {
            'id': 'test_condition_item',
            'question': 'Test question with conditions?',
            'type': 'yes_no',
            'conditions': {
                'no': {
                    'photo': True,
                    'comment': True,
                    'action': 'Please fix this issue'
                }
            }
        }
        
        # Call function
        render_checklist_item(equipment, item, 'test_prefix')
        
        # Verify selectbox was called
        mock_st.selectbox.assert_called()
        
        # Verify warning was shown (action)
        mock_st.warning.assert_called_with('Please fix this issue')
        
        # Verify comment area was shown
        mock_st.text_area.assert_called()


class TestAppHelpers(unittest.TestCase):
    """Test cases for helper functions"""
    
    def test_find_question_text_nested(self):
        """Test finding question text in nested follow-up questions"""
        # This tests the recursive search capability
        result = find_question_text('KVF', 'ballast_issue')
        self.assertEqual(result, 'Is there an issue with the hood light ballast?')
    
    def test_find_question_text_deep_nesting(self):
        """Test finding question text in deeply nested questions"""
        # Test with deeply nested follow-up question
        result = find_question_text('KVF', 'manual_damper')
        self.assertEqual(result, 'Is the manual damper fully opened?')
    
    def test_equipment_type_coverage(self):
        """Test that all equipment types are covered"""
        equipment_types = list(EQUIPMENT_TYPES.keys())
        
        for equip_type in equipment_types:
            # Test at least one question from each equipment type
            checklist = EQUIPMENT_TYPES[equip_type]['checklist']
            if checklist:
                first_item = checklist[0]
                result = find_question_text(equip_type, first_item['id'])
                self.assertEqual(result, first_item['question'])


if __name__ == '__main__':
    unittest.main()