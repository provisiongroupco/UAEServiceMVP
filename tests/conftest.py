"""
Pytest configuration and fixtures for Halton KSA Service Reports tests
"""

import pytest
import sys
import os
from unittest.mock import MagicMock, patch

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import test fixtures
from tests.fixtures import (
    BASIC_REPORT_DATA,
    COMPLETE_REPORT_DATA,
    TEST_EQUIPMENT_KVF,
    TEST_EQUIPMENT_UVF,
    create_test_signature,
    create_test_photo
)


@pytest.fixture
def basic_report_data():
    """Fixture providing basic report data"""
    return BASIC_REPORT_DATA.copy()


@pytest.fixture
def complete_report_data():
    """Fixture providing complete report data with equipment inspection"""
    return COMPLETE_REPORT_DATA.copy()


@pytest.fixture
def test_equipment_kvf():
    """Fixture providing test KVF equipment data"""
    return TEST_EQUIPMENT_KVF.copy()


@pytest.fixture
def test_equipment_uvf():
    """Fixture providing test UVF equipment data"""
    return TEST_EQUIPMENT_UVF.copy()


@pytest.fixture
def test_signature():
    """Fixture providing test signature"""
    return create_test_signature()


@pytest.fixture
def test_photo():
    """Fixture providing test photo"""
    return create_test_photo()


@pytest.fixture
def mock_streamlit():
    """Fixture providing mock Streamlit"""
    with patch('streamlit') as mock_st:
        # Setup common streamlit mocks
        mock_st.session_state = {}
        mock_st.selectbox = MagicMock(return_value='Yes')
        mock_st.text_input = MagicMock(return_value='Test input')
        mock_st.text_area = MagicMock(return_value='Test area')
        mock_st.number_input = MagicMock(return_value=1)
        mock_st.file_uploader = MagicMock(return_value=None)
        mock_st.checkbox = MagicMock(return_value=False)
        mock_st.multiselect = MagicMock(return_value=[])
        mock_st.columns = MagicMock(return_value=[MagicMock(), MagicMock()])
        mock_st.container = MagicMock()
        mock_st.markdown = MagicMock()
        mock_st.success = MagicMock()
        mock_st.warning = MagicMock()
        mock_st.error = MagicMock()
        mock_st.info = MagicMock()
        mock_st.expander = MagicMock()
        mock_st.tabs = MagicMock()
        mock_st.button = MagicMock(return_value=False)
        mock_st.form = MagicMock()
        mock_st.form_submit_button = MagicMock(return_value=False)
        mock_st.date_input = MagicMock(return_value=None)
        mock_st.rerun = MagicMock()
        mock_st.stop = MagicMock()
        
        yield mock_st


@pytest.fixture
def mock_document():
    """Fixture providing mock Document"""
    with patch('app.Document') as mock_doc_class:
        mock_doc = MagicMock()
        mock_doc_class.return_value = mock_doc
        
        # Setup document structure
        mock_doc.sections = [MagicMock()]
        mock_doc.add_paragraph.return_value = MagicMock()
        mock_doc.add_heading.return_value = MagicMock()
        mock_doc.add_table.return_value = MagicMock()
        mock_doc.add_page_break.return_value = MagicMock()
        mock_doc.save = MagicMock()
        
        yield mock_doc


@pytest.fixture
def mock_session_state():
    """Fixture providing mock session state"""
    return {
        'kitchen_list': [],
        'equipment_list': [],
        'current_equipment_index': 0,
        'inspection_data': {},
        'report_data': {},
        'report_generated': False,
        'technician_signature': None,
        'form_data': {}
    }


@pytest.fixture
def sample_kitchen_list():
    """Fixture providing sample kitchen list"""
    return [
        {
            'name': 'Main Kitchen',
            'equipment_list': [
                {
                    'type': 'KVF',
                    'location': 'Station 1',
                    'with_marvel': False,
                    'inspection_data': {
                        'lights_operational': {'answer': 'Yes', 'comment': 'Working'},
                        'capture_jet_fan': {'answer': 'No', 'comment': 'Needs repair'}
                    },
                    'photos': {
                        'photo_lights_operational': 'test_photo.jpg'
                    }
                }
            ]
        }
    ]


@pytest.fixture
def equipment_types():
    """Fixture providing equipment types"""
    from equipment_config import EQUIPMENT_TYPES
    return EQUIPMENT_TYPES


@pytest.fixture
def temp_directory(tmp_path):
    """Fixture providing temporary directory"""
    return tmp_path


@pytest.fixture
def mock_file_operations():
    """Fixture providing mock file operations"""
    with patch('builtins.open', create=True) as mock_open, \
         patch('os.path.exists') as mock_exists, \
         patch('os.makedirs') as mock_makedirs:
        
        mock_exists.return_value = True
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        
        yield {
            'open': mock_open,
            'exists': mock_exists,
            'makedirs': mock_makedirs,
            'file': mock_file
        }


# Test configuration
def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line("markers", "slow: marks tests as slow")
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "unit: marks tests as unit tests")


def pytest_collection_modifyitems(config, items):
    """Modify test collection"""
    # Add markers to tests based on file location
    for item in items:
        if "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        
        # Mark large dataset tests as slow
        if "large" in item.name or "performance" in item.name:
            item.add_marker(pytest.mark.slow)


# Helper functions for tests
def create_mock_equipment(equipment_type='KVF', with_data=True):
    """Helper function to create mock equipment"""
    equipment = {
        'id': f'test_{equipment_type.lower()}',
        'type': equipment_type,
        'serial_number': f'{equipment_type}-TEST-001',
        'location': 'Test Location',
        'inspection_data': {},
        'photos': {}
    }
    
    if with_data:
        equipment['inspection_data'] = {
            'test_item': {'answer': 'Yes', 'comment': 'Test comment'}
        }
        equipment['photos'] = {
            'photo_test': create_test_photo()
        }
    
    return equipment


def create_mock_kitchen(name='Test Kitchen', equipment_count=1):
    """Helper function to create mock kitchen"""
    equipment_list = []
    for i in range(equipment_count):
        equipment_list.append(create_mock_equipment())
    
    return {
        'name': name,
        'equipment_list': equipment_list
    }


# Add helper functions to pytest namespace
pytest.create_mock_equipment = create_mock_equipment
pytest.create_mock_kitchen = create_mock_kitchen