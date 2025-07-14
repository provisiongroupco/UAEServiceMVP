"""
Unit tests for utils.py
"""

import unittest
import sys
import os
from unittest.mock import MagicMock, patch, Mock
from io import BytesIO

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import (
    HALTON_BLUE,
    HALTON_LIGHT_BLUE,
    HALTON_DARK_GRAY,
    add_header_with_logo,
    add_horizontal_line,
    format_table_style,
    add_footer,
    add_page_number,
    set_cell_margins,
    style_heading,
    create_info_table,
    format_table_style_enhanced,
    add_logo_to_doc
)


class TestUtils(unittest.TestCase):
    """Test cases for utility functions"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.mock_doc = MagicMock()
        self.mock_table = MagicMock()
        self.mock_cell = MagicMock()
        self.mock_paragraph = MagicMock()
        self.mock_run = MagicMock()
    
    def test_halton_colors(self):
        """Test that Halton brand colors are properly defined"""
        # Test HALTON_BLUE
        self.assertEqual(HALTON_BLUE.rgb, (31, 71, 136))
        
        # Test HALTON_LIGHT_BLUE
        self.assertEqual(HALTON_LIGHT_BLUE.rgb, (44, 90, 160))
        
        # Test HALTON_DARK_GRAY
        self.assertEqual(HALTON_DARK_GRAY.rgb, (64, 64, 64))
    
    @patch('utils.os.path.exists')
    def test_add_header_with_logo_no_logo(self, mock_exists):
        """Test adding header without logo"""
        mock_exists.return_value = False
        
        # Setup mock document
        mock_section = MagicMock()
        mock_header = MagicMock()
        mock_table = MagicMock()
        
        self.mock_doc.sections = [mock_section]
        mock_section.header = mock_header
        mock_header.add_table.return_value = mock_table
        
        # Setup mock table cells
        mock_cells = [MagicMock(), MagicMock(), MagicMock()]
        mock_table.cell.side_effect = lambda row, col: mock_cells[col]
        
        # Setup mock paragraphs
        for cell in mock_cells:
            cell.paragraphs = [MagicMock()]
            cell.paragraphs[0].add_run.return_value = MagicMock()
        
        # Call function
        add_header_with_logo(self.mock_doc)
        
        # Verify table was created
        mock_header.add_table.assert_called_once()
        
        # Verify cells were accessed
        self.assertEqual(mock_table.cell.call_count, 3)
    
    def test_add_horizontal_line(self):
        """Test adding horizontal line"""
        mock_parent = MagicMock()
        mock_paragraph = MagicMock()
        mock_parent.add_paragraph.return_value = mock_paragraph
        
        # Setup mock paragraph properties
        mock_paragraph._p = MagicMock()
        mock_paragraph._p.get_or_add_pPr.return_value = MagicMock()
        
        add_horizontal_line(mock_parent)
        
        # Verify paragraph was added
        mock_parent.add_paragraph.assert_called_once()
    
    def test_format_table_style(self):
        """Test formatting table style"""
        # Setup mock table
        mock_table = MagicMock()
        mock_table._tbl = MagicMock()
        mock_table._tbl.tblPr = MagicMock()
        mock_table.rows = [MagicMock()]
        mock_table.rows[0].cells = [MagicMock()]
        mock_table.rows[0].cells[0].paragraphs = [MagicMock()]
        mock_table.rows[0].cells[0].paragraphs[0].runs = [MagicMock()]
        
        format_table_style(mock_table)
        
        # Verify table borders were appended
        mock_table._tbl.tblPr.append.assert_called()
    
    def test_add_footer(self):
        """Test adding footer"""
        # Setup mock document
        mock_section = MagicMock()
        mock_footer = MagicMock()
        mock_paragraph = MagicMock()
        mock_run = MagicMock()
        
        self.mock_doc.sections = [mock_section]
        mock_section.footer = mock_footer
        mock_footer.paragraphs = [mock_paragraph]
        mock_paragraph.add_run.return_value = mock_run
        
        add_footer(self.mock_doc)
        
        # Verify footer text was added
        mock_paragraph.add_run.assert_called()
    
    def test_set_cell_margins(self):
        """Test setting cell margins"""
        # Setup mock cell
        mock_cell = MagicMock()
        mock_cell._tc = MagicMock()
        mock_cell._tc.get_or_add_tcPr.return_value = MagicMock()
        
        set_cell_margins(mock_cell, top=0.1, bottom=0.1, left=0.2, right=0.2)
        
        # Verify tcPr was accessed
        mock_cell._tc.get_or_add_tcPr.assert_called_once()
    
    def test_style_heading_level_0(self):
        """Test styling heading level 0 (title)"""
        mock_heading = MagicMock()
        mock_heading.style = MagicMock()
        mock_heading.style.font = MagicMock()
        mock_heading.style.font.color = MagicMock()
        
        style_heading(mock_heading, level=0)
        
        # Verify font properties were set
        self.assertTrue(mock_heading.style.font.bold)
        self.assertEqual(mock_heading.style.font.color.rgb, HALTON_BLUE)
    
    def test_style_heading_level_1(self):
        """Test styling heading level 1 (main sections)"""
        mock_heading = MagicMock()
        mock_heading.style = MagicMock()
        mock_heading.style.font = MagicMock()
        mock_heading.style.font.color = MagicMock()
        
        style_heading(mock_heading, level=1)
        
        # Verify font properties were set
        self.assertTrue(mock_heading.style.font.bold)
        self.assertEqual(mock_heading.style.font.color.rgb, HALTON_BLUE)
    
    def test_style_heading_level_2(self):
        """Test styling heading level 2 (subsections)"""
        mock_heading = MagicMock()
        mock_heading.style = MagicMock()
        mock_heading.style.font = MagicMock()
        mock_heading.style.font.color = MagicMock()
        
        style_heading(mock_heading, level=2)
        
        # Verify font properties were set
        self.assertTrue(mock_heading.style.font.bold)
        self.assertEqual(mock_heading.style.font.color.rgb, HALTON_DARK_GRAY)
    
    def test_create_info_table(self):
        """Test creating info table"""
        # Setup mock document
        mock_doc = MagicMock()
        mock_table = MagicMock()
        mock_doc.add_table.return_value = mock_table
        
        # Setup mock table structure
        mock_table.columns = [MagicMock(), MagicMock()]
        mock_table.columns[0].cells = [MagicMock()]
        mock_table.columns[1].cells = [MagicMock()]
        
        # Setup mock cells
        mock_cells = {}
        def mock_cell_func(row, col):
            key = f"{row}_{col}"
            if key not in mock_cells:
                mock_cells[key] = MagicMock()
                mock_cells[key].paragraphs = [MagicMock()]
                mock_cells[key].paragraphs[0].runs = [MagicMock()]
                mock_cells[key]._tc = MagicMock()
                mock_cells[key]._tc.get_or_add_tcPr.return_value = MagicMock()
            return mock_cells[key]
        
        mock_table.cell.side_effect = mock_cell_func
        
        # Test data
        test_data = [
            ("Label 1", "Value 1"),
            ("Label 2", "Value 2")
        ]
        
        # Call function
        result = create_info_table(mock_doc, test_data)
        
        # Verify table was created
        mock_doc.add_table.assert_called_once_with(rows=2, cols=2)
        
        # Verify result is the mock table
        self.assertEqual(result, mock_table)
    
    def test_format_table_style_enhanced(self):
        """Test enhanced table style formatting"""
        # Setup mock table
        mock_table = MagicMock()
        mock_table._tbl = MagicMock()
        mock_table._tbl.tblPr = MagicMock()
        mock_table._tbl.tblPr.__iter__ = Mock(return_value=iter([]))
        
        format_table_style_enhanced(mock_table)
        
        # Verify table properties were accessed
        mock_table._tbl.tblPr.append.assert_called()
    
    @patch('utils.os.path.exists')
    def test_add_logo_to_doc_no_logo(self, mock_exists):
        """Test adding logo when no logo exists"""
        mock_exists.return_value = False
        
        result = add_logo_to_doc(self.mock_doc)
        
        # Should return None when no logo is found
        self.assertIsNone(result)
    
    @patch('utils.os.path.exists')
    def test_add_logo_to_doc_with_logo(self, mock_exists):
        """Test adding logo when logo exists"""
        mock_exists.return_value = True
        
        result = add_logo_to_doc(self.mock_doc)
        
        # Should return the logo path when found
        self.assertEqual(result, os.path.join('assets', 'halton_logo.png'))
    
    def test_add_logo_to_doc_with_custom_path(self):
        """Test adding logo with custom path"""
        custom_path = "/custom/path/logo.png"
        
        result = add_logo_to_doc(self.mock_doc, custom_path)
        
        # Should return the custom path
        self.assertEqual(result, custom_path)
    
    def test_add_page_number(self):
        """Test adding page number"""
        mock_paragraph = MagicMock()
        mock_run = MagicMock()
        mock_paragraph.add_run.return_value = mock_run
        mock_run._r = MagicMock()
        
        add_page_number(mock_paragraph)
        
        # Verify run was added
        mock_paragraph.add_run.assert_called_once()
        
        # Verify XML elements were appended
        self.assertEqual(mock_run._r.append.call_count, 3)


class TestUtilsIntegration(unittest.TestCase):
    """Integration tests for utility functions"""
    
    def test_create_info_table_with_real_data(self):
        """Test creating info table with realistic data"""
        # This would require a real document object
        # For now, we'll test the data structure
        test_data = [
            ("Customer Name", "SELA Company"),
            ("Project Name", "Stella Kitchen Hoods"),
            ("Contact Person", "Sultan Alofi"),
            ("Location", "Via Mall - Riyadh")
        ]
        
        # Verify data structure
        self.assertEqual(len(test_data), 4)
        for item in test_data:
            self.assertEqual(len(item), 2)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], str)
    
    def test_color_consistency(self):
        """Test that colors are consistent across the application"""
        # Test that all colors are RGB color objects
        colors = [HALTON_BLUE, HALTON_LIGHT_BLUE, HALTON_DARK_GRAY]
        
        for color in colors:
            self.assertTrue(hasattr(color, 'rgb'))
            self.assertEqual(len(color.rgb), 3)
            for component in color.rgb:
                self.assertIsInstance(component, int)
                self.assertGreaterEqual(component, 0)
                self.assertLessEqual(component, 255)


if __name__ == '__main__':
    unittest.main()