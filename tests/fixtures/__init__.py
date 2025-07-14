"""
Test fixtures for Halton KSA Service Reports application
"""

from .test_data import (
    BASIC_REPORT_DATA,
    COMPLETE_REPORT_DATA,
    TEST_EQUIPMENT_KVF,
    TEST_EQUIPMENT_UVF,
    TEST_EQUIPMENT_MARVEL,
    TEST_KITCHEN_SINGLE,
    TEST_KITCHEN_MULTIPLE,
    TEST_KITCHEN_WITH_MARVEL,
    SERVICE_CALL_DATA,
    AMC_VISIT_DATA,
    EMERGENCY_SERVICE_DATA,
    MINIMAL_DATA,
    UNICODE_DATA,
    ALL_EQUIPMENT_TYPES,
    create_test_signature,
    create_test_photo,
    create_large_test_data
)

__all__ = [
    'BASIC_REPORT_DATA',
    'COMPLETE_REPORT_DATA',
    'TEST_EQUIPMENT_KVF',
    'TEST_EQUIPMENT_UVF',
    'TEST_EQUIPMENT_MARVEL',
    'TEST_KITCHEN_SINGLE',
    'TEST_KITCHEN_MULTIPLE',
    'TEST_KITCHEN_WITH_MARVEL',
    'SERVICE_CALL_DATA',
    'AMC_VISIT_DATA',
    'EMERGENCY_SERVICE_DATA',
    'MINIMAL_DATA',
    'UNICODE_DATA',
    'ALL_EQUIPMENT_TYPES',
    'create_test_signature',
    'create_test_photo',
    'create_large_test_data'
]