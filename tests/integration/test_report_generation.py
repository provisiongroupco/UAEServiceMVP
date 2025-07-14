"""
Integration tests for report generation
"""

import unittest
import sys
import os
from unittest.mock import MagicMock, patch, Mock
from datetime import datetime
from io import BytesIO
import tempfile

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import create_technical_report, get_kitchen_summary
from sample_report_generator import sample_data
from equipment_config import EQUIPMENT_TYPES


class TestReportGenerationIntegration(unittest.TestCase):
    """Integration tests for the complete report generation process"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_data = {
            'customer_name': 'Test Customer',
            'project_name': 'Test Project',
            'contact_person': 'Test Contact',
            'outlet_location': 'Test Location',
            'contact_number': '+966123456789',
            'visit_type': 'Service Call',
            'visit_class': 'To Be Invoiced',
            'date': '2024-01-01',
            'equipment_inspection': [],
            'work_performed': 'Test work performed',
            'recommendations': 'Test recommendations',
            'technician_name': 'Test Technician',
            'technician_id': 'TEST001',
            'service_date': '2024-01-01'
        }
    
    @patch('app.Document')
    @patch('app.os.path.exists')
    def test_complete_report_generation_no_template(self, mock_exists, mock_document):
        """Test complete report generation without template"""
        # Setup mocks
        mock_exists.return_value = False
        mock_doc = MagicMock()
        mock_document.return_value = mock_doc
        
        # Setup document structure
        self._setup_mock_document(mock_doc)
        
        # Generate report
        result = create_technical_report(self.test_data)
        
        # Verify result
        self.assertIsInstance(result, BytesIO)
        mock_document.assert_called_once()
        mock_doc.save.assert_called_once()
    
    @patch('app.Document')
    @patch('app.os.path.exists')
    def test_complete_report_generation_with_template(self, mock_exists, mock_document):
        """Test complete report generation with template"""
        # Setup mocks
        mock_exists.return_value = True
        mock_doc = MagicMock()
        mock_document.return_value = mock_doc
        
        # Setup document structure
        self._setup_mock_document(mock_doc)
        
        # Generate report
        result = create_technical_report(self.test_data)
        
        # Verify result
        self.assertIsInstance(result, BytesIO)
        mock_document.assert_called_once()
        mock_doc.save.assert_called_once()
    
    def _setup_mock_document(self, mock_doc):
        """Helper method to setup mock document"""
        mock_doc.sections = [MagicMock()]
        mock_doc.add_paragraph.return_value = MagicMock()
        mock_doc.add_heading.return_value = MagicMock()
        mock_doc.add_table.return_value = MagicMock()
        mock_doc.add_page_break.return_value = MagicMock()
        mock_doc.save = MagicMock()
        
        # Setup paragraph and run structure
        mock_para = MagicMock()
        mock_run = MagicMock()
        mock_para.add_run.return_value = mock_run
        mock_doc.add_paragraph.return_value = mock_para
        
        # Setup heading structure
        mock_heading = MagicMock()
        mock_heading.style = MagicMock()
        mock_heading.style.font = MagicMock()
        mock_heading.style.font.color = MagicMock()
        mock_doc.add_heading.return_value = mock_heading
        
        # Setup table structure
        mock_table = MagicMock()
        mock_table.alignment = MagicMock()
        mock_table.columns = [MagicMock(), MagicMock()]
        mock_table.columns[0].cells = [MagicMock()]
        mock_table.columns[1].cells = [MagicMock()]
        mock_table.rows = [MagicMock()]
        mock_table.rows[0].cells = [MagicMock(), MagicMock()]
        
        # Setup cell structure
        for col in mock_table.columns:
            for cell in col.cells:
                cell.width = MagicMock()
                cell.text = ""
                cell.paragraphs = [MagicMock()]
                cell.paragraphs[0].runs = [MagicMock()]
                cell.paragraphs[0].alignment = MagicMock()
                cell._tc = MagicMock()
                cell._tc.get_or_add_tcPr.return_value = MagicMock()
        
        # Setup table cell function
        def mock_cell_func(row, col):
            return mock_table.rows[row].cells[col]
        
        mock_table.cell = mock_cell_func
        mock_doc.add_table.return_value = mock_table
    
    @patch('app.Document')
    @patch('app.os.path.exists')
    def test_report_with_equipment_inspection(self, mock_exists, mock_document):
        """Test report generation with equipment inspection data"""
        # Setup mocks
        mock_exists.return_value = False
        mock_doc = MagicMock()
        mock_document.return_value = mock_doc
        self._setup_mock_document(mock_doc)
        
        # Add equipment inspection data
        self.test_data['equipment_inspection'] = [
            {
                'name': 'Test Kitchen',
                'equipment': [
                    {
                        'type': 'KVF',
                        'type_name': 'KVF Hood',
                        'location': 'Main Kitchen',
                        'with_marvel': False,
                        'yes_responses': [
                            {
                                'item': 'lights_operational',
                                'question': 'Are the hood lights operational?',
                                'answer': 'Yes',
                                'comment': 'Working fine'
                            }
                        ],
                        'no_responses': [
                            {
                                'item': 'capture_jet_fan',
                                'question': 'Is the capture jet fan working?',
                                'answer': 'No',
                                'comment': 'Needs repair'
                            }
                        ],
                        'photos_count': 2,
                        'yes_photos': {},
                        'no_photos': {}
                    }
                ]
            }
        ]
        
        # Generate report
        result = create_technical_report(self.test_data)
        
        # Verify result
        self.assertIsInstance(result, BytesIO)
        mock_document.assert_called_once()
        mock_doc.save.assert_called_once()
    
    @patch('app.Document')
    @patch('app.os.path.exists')
    def test_report_with_photos(self, mock_exists, mock_document):
        """Test report generation with photos"""
        # Setup mocks
        mock_exists.return_value = False
        mock_doc = MagicMock()
        mock_document.return_value = mock_doc
        self._setup_mock_document(mock_doc)
        
        # Create mock photo
        mock_photo = MagicMock()
        mock_photo.seek = MagicMock()
        
        # Add equipment inspection data with photos
        self.test_data['equipment_inspection'] = [
            {
                'name': 'Test Kitchen',
                'equipment': [
                    {
                        'type': 'KVF',
                        'type_name': 'KVF Hood',
                        'location': 'Main Kitchen',
                        'with_marvel': False,
                        'yes_responses': [],
                        'no_responses': [],
                        'photos_count': 1,
                        'yes_photos': {'photo_test': mock_photo},
                        'no_photos': {}
                    }
                ]
            }
        ]
        
        # Generate report
        result = create_technical_report(self.test_data)
        
        # Verify result
        self.assertIsInstance(result, BytesIO)
        mock_document.assert_called_once()
        mock_doc.save.assert_called_once()
    
    @patch('app.Document')
    @patch('app.os.path.exists')
    def test_report_with_signatures(self, mock_exists, mock_document):
        """Test report generation with signatures"""
        # Setup mocks
        mock_exists.return_value = False
        mock_doc = MagicMock()
        mock_document.return_value = mock_doc
        self._setup_mock_document(mock_doc)
        
        # Create mock signature
        mock_signature = MagicMock()
        mock_signature.seek = MagicMock()
        
        # Add signatures to test data
        self.test_data['technician_signature'] = mock_signature
        self.test_data['customer_signature'] = mock_signature
        self.test_data['customer_signatory'] = 'Test Customer Rep'
        
        # Generate report
        result = create_technical_report(self.test_data)
        
        # Verify result
        self.assertIsInstance(result, BytesIO)
        mock_document.assert_called_once()
        mock_doc.save.assert_called_once()
    
    @patch('app.st.session_state')
    def test_kitchen_summary_integration(self, mock_session_state):
        """Test kitchen summary integration"""
        # Setup mock session state with realistic data
        mock_session_state.kitchen_list = [
            {
                'name': 'Main Kitchen',
                'equipment_list': [
                    {
                        'type': 'KVF',
                        'location': 'Main Area',
                        'with_marvel': False,
                        'inspection_data': {
                            'lights_operational': {
                                'answer': 'Yes',
                                'comment': 'Working fine'
                            },
                            'capture_jet_fan': {
                                'answer': 'No',
                                'comment': 'Needs repair'
                            }
                        },
                        'photos': {
                            'photo_lights_operational': 'mock_photo1.jpg',
                            'photo_capture_jet_fan': 'mock_photo2.jpg'
                        }
                    }
                ]
            }
        ]
        
        # Get kitchen summary
        summary = get_kitchen_summary()
        
        # Verify summary structure
        self.assertIsInstance(summary, list)
        self.assertEqual(len(summary), 1)
        
        kitchen = summary[0]
        self.assertEqual(kitchen['name'], 'Main Kitchen')
        self.assertEqual(len(kitchen['equipment']), 1)
        
        equipment = kitchen['equipment'][0]
        self.assertEqual(equipment['type'], 'KVF')
        self.assertEqual(equipment['location'], 'Main Area')
        self.assertEqual(equipment['photos_count'], 2)
        self.assertGreater(len(equipment['yes_responses']), 0)
        self.assertGreater(len(equipment['no_responses']), 0)
    
    def test_sample_data_report_integration(self):
        """Test that sample data can generate a report"""
        # This test uses the actual sample data
        with patch('app.Document') as mock_document, \
             patch('app.os.path.exists') as mock_exists:
            
            # Setup mocks
            mock_exists.return_value = False
            mock_doc = MagicMock()
            mock_document.return_value = mock_doc
            self._setup_mock_document(mock_doc)
            
            # Generate report with sample data
            result = create_technical_report(sample_data)
            
            # Verify result
            self.assertIsInstance(result, BytesIO)
            mock_document.assert_called_once()
            mock_doc.save.assert_called_once()
    
    def test_all_equipment_types_integration(self):
        """Test that all equipment types can be processed"""
        for equip_type, config in EQUIPMENT_TYPES.items():
            with self.subTest(equipment_type=equip_type):
                # Create mock equipment for this type
                mock_equipment = {
                    'type': equip_type,
                    'type_name': config['name'],
                    'location': 'Test Location',
                    'with_marvel': False,
                    'yes_responses': [],
                    'no_responses': [],
                    'photos_count': 0,
                    'yes_photos': {},
                    'no_photos': {}
                }
                
                # Create test data with this equipment
                test_data = self.test_data.copy()
                test_data['equipment_inspection'] = [
                    {
                        'name': 'Test Kitchen',
                        'equipment': [mock_equipment]
                    }
                ]
                
                # Generate report
                with patch('app.Document') as mock_document, \
                     patch('app.os.path.exists') as mock_exists:
                    
                    mock_exists.return_value = False
                    mock_doc = MagicMock()
                    mock_document.return_value = mock_doc
                    self._setup_mock_document(mock_doc)
                    
                    result = create_technical_report(test_data)
                    
                    # Verify result
                    self.assertIsInstance(result, BytesIO)
                    mock_document.assert_called_once()
                    mock_doc.save.assert_called_once()


class TestReportGenerationEdgeCases(unittest.TestCase):
    """Test edge cases in report generation"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.minimal_data = {
            'customer_name': '',
            'project_name': '',
            'contact_person': '',
            'outlet_location': '',
            'contact_number': '',
            'visit_type': '',
            'visit_class': 'To Be Invoiced',
            'date': '2024-01-01',
            'equipment_inspection': [],
            'work_performed': '',
            'recommendations': '',
            'technician_name': '',
            'technician_id': '',
            'service_date': '2024-01-01'
        }
    
    @patch('app.Document')
    @patch('app.os.path.exists')
    def test_empty_data_report(self, mock_exists, mock_document):
        """Test report generation with empty data"""
        # Setup mocks
        mock_exists.return_value = False
        mock_doc = MagicMock()
        mock_document.return_value = mock_doc
        
        # Setup minimal document structure
        mock_doc.sections = [MagicMock()]
        mock_doc.add_paragraph.return_value = MagicMock()
        mock_doc.add_heading.return_value = MagicMock()
        mock_doc.add_table.return_value = MagicMock()
        mock_doc.add_page_break.return_value = MagicMock()
        mock_doc.save = MagicMock()
        
        # Generate report with minimal data
        result = create_technical_report(self.minimal_data)
        
        # Should still generate a report
        self.assertIsInstance(result, BytesIO)
        mock_document.assert_called_once()
        mock_doc.save.assert_called_once()
    
    @patch('app.Document')
    @patch('app.os.path.exists')
    def test_missing_recommendations(self, mock_exists, mock_document):
        """Test report generation without recommendations"""
        # Setup mocks
        mock_exists.return_value = False
        mock_doc = MagicMock()
        mock_document.return_value = mock_doc
        
        # Setup minimal document structure
        mock_doc.sections = [MagicMock()]
        mock_doc.add_paragraph.return_value = MagicMock()
        mock_doc.add_heading.return_value = MagicMock()
        mock_doc.add_table.return_value = MagicMock()
        mock_doc.add_page_break.return_value = MagicMock()
        mock_doc.save = MagicMock()
        
        # Remove recommendations
        test_data = self.minimal_data.copy()
        test_data['recommendations'] = None
        
        # Generate report
        result = create_technical_report(test_data)
        
        # Should still generate a report
        self.assertIsInstance(result, BytesIO)
        mock_document.assert_called_once()
        mock_doc.save.assert_called_once()
    
    @patch('app.st.session_state')
    def test_empty_kitchen_list(self, mock_session_state):
        """Test kitchen summary with empty kitchen list"""
        mock_session_state.kitchen_list = []
        
        summary = get_kitchen_summary()
        
        self.assertEqual(summary, [])
    
    @patch('app.st.session_state')
    def test_kitchen_without_equipment(self, mock_session_state):
        """Test kitchen summary with kitchen but no equipment"""
        mock_session_state.kitchen_list = [
            {
                'name': 'Empty Kitchen',
                'equipment_list': []
            }
        ]
        
        summary = get_kitchen_summary()
        
        # Should return empty list since no equipment
        self.assertEqual(summary, [])


if __name__ == '__main__':
    unittest.main()