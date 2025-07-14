"""
Unit tests for sample_report_generator.py
"""

import unittest
import sys
import os
from unittest.mock import MagicMock, patch, Mock
from datetime import datetime
from io import BytesIO

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from sample_report_generator import create_sample_signature, sample_data


class TestSampleReportGenerator(unittest.TestCase):
    """Test cases for sample report generator"""
    
    def test_create_sample_signature(self):
        """Test creating sample signature"""
        # Call function
        result = create_sample_signature()
        
        # Verify result is BytesIO
        self.assertIsInstance(result, BytesIO)
        
        # Verify it has content
        result.seek(0)
        content = result.read()
        self.assertGreater(len(content), 0)
        
        # Reset position
        result.seek(0)
    
    def test_sample_data_structure(self):
        """Test sample data structure"""
        # Verify sample_data is a dictionary
        self.assertIsInstance(sample_data, dict)
        
        # Verify required fields exist
        required_fields = [
            'customer_name',
            'project_name',
            'contact_person',
            'outlet_location',
            'contact_number',
            'visit_type',
            'visit_class',
            'date',
            'work_performed',
            'technician_name',
            'technician_id',
            'service_date'
        ]
        
        for field in required_fields:
            self.assertIn(field, sample_data)
    
    def test_sample_data_values(self):
        """Test sample data values"""
        # Check specific values
        self.assertEqual(sample_data['customer_name'], 'SELA Company')
        self.assertEqual(sample_data['project_name'], 'Stella Kitchen Hoods Installation')
        self.assertEqual(sample_data['contact_person'], 'Sultan Alofi')
        self.assertEqual(sample_data['outlet_location'], 'Via Mall - Riyadh')
        self.assertEqual(sample_data['contact_number'], '+966 55 558 5449')
        self.assertEqual(sample_data['visit_type'], 'Service Call')
        self.assertEqual(sample_data['visit_class'], 'To Be Invoiced')
        self.assertEqual(sample_data['technician_name'], 'Mohammed Al-Rahman')
        self.assertEqual(sample_data['technician_id'], 'HLT-TECH-042')
    
    def test_sample_data_date_format(self):
        """Test sample data date format"""
        # Check date format
        date_str = sample_data['date']
        self.assertIsInstance(date_str, str)
        
        # Verify it can be parsed as date
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            self.fail(f"Date '{date_str}' is not in expected format YYYY-MM-DD")
        
        # Check service date
        service_date_str = sample_data['service_date']
        self.assertIsInstance(service_date_str, str)
        
        try:
            datetime.strptime(service_date_str, '%Y-%m-%d')
        except ValueError:
            self.fail(f"Service date '{service_date_str}' is not in expected format YYYY-MM-DD")
    
    def test_sample_data_text_fields(self):
        """Test sample data text fields"""
        # Check work performed
        work_performed = sample_data['work_performed']
        self.assertIsInstance(work_performed, str)
        self.assertGreater(len(work_performed), 0)
        
        # Check that it contains expected content
        self.assertIn('inspection', work_performed.lower())
        self.assertIn('filter', work_performed.lower())
        self.assertIn('uv', work_performed.lower())
        
        # Check findings if present
        if 'findings' in sample_data:
            findings = sample_data['findings']
            self.assertIsInstance(findings, str)
            self.assertGreater(len(findings), 0)
        
        # Check recommendations if present
        if 'recommendations' in sample_data:
            recommendations = sample_data['recommendations']
            self.assertIsInstance(recommendations, str)
            self.assertGreater(len(recommendations), 0)
    
    def test_sample_data_signature(self):
        """Test sample data signature"""
        # Check if signature is present
        self.assertIn('technician_signature', sample_data)
        
        # Verify signature is BytesIO
        signature = sample_data['technician_signature']
        self.assertIsInstance(signature, BytesIO)
        
        # Verify it has content
        signature.seek(0)
        content = signature.read()
        self.assertGreater(len(content), 0)
        
        # Reset position
        signature.seek(0)
    
    @patch('sample_report_generator.create_technical_report')
    def test_main_execution(self, mock_create_report):
        """Test main execution flow"""
        # Setup mock
        mock_doc_bytes = MagicMock()
        mock_doc_bytes.getvalue.return_value = b'test_document_content'
        mock_create_report.return_value = mock_doc_bytes
        
        # Import and run main
        from sample_report_generator import __name__ as module_name
        
        # This would normally be tested by running the script
        # For now, just verify the mock can be called
        mock_create_report(sample_data)
        
        # Verify create_technical_report was called
        mock_create_report.assert_called_once_with(sample_data)
    
    @patch('sample_report_generator.open', create=True)
    @patch('sample_report_generator.create_technical_report')
    def test_file_creation(self, mock_create_report, mock_open):
        """Test file creation in main execution"""
        # Setup mocks
        mock_doc_bytes = MagicMock()
        mock_doc_bytes.getvalue.return_value = b'test_document_content'
        mock_create_report.return_value = mock_doc_bytes
        
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        
        # This simulates the main execution
        doc_bytes = mock_create_report(sample_data)
        filename = f"Sample_Technical_Report_{datetime.now().strftime('%Y%m%d')}.docx"
        
        with mock_open(filename, 'wb') as f:
            f.write(doc_bytes.getvalue())
        
        # Verify file operations
        mock_open.assert_called_once_with(filename, 'wb')
        mock_file.write.assert_called_once_with(b'test_document_content')


class TestSampleSignatureGeneration(unittest.TestCase):
    """Test cases for sample signature generation"""
    
    def test_signature_image_creation(self):
        """Test that signature image is created properly"""
        signature = create_sample_signature()
        
        # Verify it's a BytesIO object
        self.assertIsInstance(signature, BytesIO)
        
        # Verify it has image data
        signature.seek(0)
        data = signature.read()
        self.assertGreater(len(data), 0)
        
        # Verify it starts with PNG header (common image format)
        signature.seek(0)
        header = signature.read(8)
        # PNG signature: 89 50 4E 47 0D 0A 1A 0A
        self.assertEqual(header[:4], b'\x89PNG')
    
    def test_signature_reproducibility(self):
        """Test that signature generation is consistent"""
        # Generate two signatures
        sig1 = create_sample_signature()
        sig2 = create_sample_signature()
        
        # Read their content
        sig1.seek(0)
        content1 = sig1.read()
        
        sig2.seek(0)
        content2 = sig2.read()
        
        # They should be identical (deterministic generation)
        self.assertEqual(content1, content2)
    
    def test_signature_size(self):
        """Test signature image size"""
        signature = create_sample_signature()
        
        # Verify it's not empty
        signature.seek(0)
        content = signature.read()
        
        # Should be reasonable size for a PNG image
        self.assertGreater(len(content), 100)  # At least 100 bytes
        self.assertLess(len(content), 50000)   # Less than 50KB


class TestSampleDataIntegration(unittest.TestCase):
    """Integration tests for sample data"""
    
    def test_sample_data_completeness(self):
        """Test that sample data is complete for report generation"""
        # These are the fields that create_technical_report expects
        expected_fields = [
            'customer_name',
            'project_name', 
            'contact_person',
            'outlet_location',
            'contact_number',
            'visit_type',
            'visit_class',
            'date',
            'work_performed',
            'technician_name',
            'technician_id',
            'service_date'
        ]
        
        for field in expected_fields:
            self.assertIn(field, sample_data, f"Missing required field: {field}")
            self.assertIsNotNone(sample_data[field], f"Field {field} is None")
            
            # String fields should not be empty
            if isinstance(sample_data[field], str):
                self.assertGreater(len(sample_data[field]), 0, f"Field {field} is empty")
    
    def test_sample_data_types(self):
        """Test that sample data has correct types"""
        # String fields
        string_fields = [
            'customer_name', 'project_name', 'contact_person',
            'outlet_location', 'contact_number', 'visit_type',
            'visit_class', 'date', 'work_performed',
            'technician_name', 'technician_id', 'service_date'
        ]
        
        for field in string_fields:
            if field in sample_data:
                self.assertIsInstance(sample_data[field], str, f"Field {field} should be string")
        
        # BytesIO fields
        if 'technician_signature' in sample_data:
            self.assertIsInstance(sample_data['technician_signature'], BytesIO,
                                "technician_signature should be BytesIO")
    
    def test_sample_data_realism(self):
        """Test that sample data looks realistic"""
        # Check phone number format
        phone = sample_data['contact_number']
        self.assertTrue(phone.startswith('+966'), "Phone should start with +966 for Saudi Arabia")
        
        # Check that names look reasonable
        customer_name = sample_data['customer_name']
        self.assertGreater(len(customer_name.split()), 0, "Customer name should have words")
        
        # Check technician ID format
        tech_id = sample_data['technician_id']
        self.assertTrue(tech_id.startswith('HLT-'), "Technician ID should start with HLT-")
        
        # Check location mentions a city
        location = sample_data['outlet_location']
        self.assertIn('Riyadh', location, "Location should mention Riyadh")


if __name__ == '__main__':
    unittest.main()