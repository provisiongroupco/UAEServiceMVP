"""
Test data fixtures for Halton KSA Service Reports application
"""

from datetime import datetime
from io import BytesIO
from PIL import Image, ImageDraw


def create_test_signature(text="Test Signature"):
    """Create a test signature image"""
    # Create a white image
    img = Image.new('RGB', (200, 80), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple signature-like text
    draw.text((10, 30), text, fill='black')
    
    # Save to bytes
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    return img_bytes


def create_test_photo(width=300, height=200, color='blue'):
    """Create a test photo for equipment inspection"""
    # Create a colored image
    img = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(img)
    
    # Add some text to make it identifiable
    draw.text((10, 10), f"Test Photo - {color}", fill='white')
    
    # Save to bytes
    img_bytes = BytesIO()
    img.save(img_bytes, format='JPEG')
    img_bytes.seek(0)
    return img_bytes


# Basic test data for report generation
BASIC_REPORT_DATA = {
    'customer_name': 'Test Customer Corp',
    'project_name': 'Test Kitchen Installation',
    'contact_person': 'John Test',
    'outlet_location': 'Test Mall - Test City',
    'contact_number': '+966 50 123 4567',
    'visit_type': 'Service Call',
    'visit_class': 'To Be Invoiced',
    'date': '2024-01-15',
    'equipment_inspection': [],
    'work_performed': 'Performed comprehensive inspection of kitchen ventilation system.',
    'recommendations': 'Continue with regular maintenance schedule.',
    'technician_name': 'Test Technician',
    'technician_id': 'TEST-001',
    'service_date': '2024-01-15',
    'technician_signature': create_test_signature("Test Technician"),
    'customer_signature': create_test_signature("Customer Rep"),
    'customer_signatory': 'Customer Representative'
}

# Complete test data with equipment inspection
COMPLETE_REPORT_DATA = {
    'customer_name': 'ACME Restaurant Group',
    'project_name': 'Downtown Kitchen Ventilation',
    'contact_person': 'Sarah Johnson',
    'outlet_location': 'Downtown Food Court - Riyadh',
    'contact_number': '+966 55 987 6543',
    'visit_type': 'AMC (Contract)',
    'visit_class': 'To Be Invoiced',
    'date': '2024-01-20',
    'equipment_inspection': [
        {
            'name': 'Main Kitchen',
            'equipment': [
                {
                    'type': 'KVF',
                    'type_name': 'KVF Hood',
                    'location': 'Station 1',
                    'with_marvel': False,
                    'yes_responses': [
                        {
                            'item': 'lights_operational',
                            'question': 'Are the hood lights operational?',
                            'answer': 'Yes',
                            'comment': 'All lights functioning properly'
                        },
                        {
                            'item': 'ksa_filters_condition',
                            'question': 'Are the KSA filters in good condition?',
                            'answer': 'Yes',
                            'comment': 'Recently cleaned'
                        }
                    ],
                    'no_responses': [
                        {
                            'item': 'capture_jet_fan',
                            'question': 'Is the capture jet fan working and in good condition?',
                            'answer': 'No',
                            'comment': 'Fan making unusual noise, needs maintenance'
                        }
                    ],
                    'photos_count': 3,
                    'yes_photos': {
                        'photo_lights_operational': create_test_photo(color='green'),
                        'photo_ksa_filters_condition': create_test_photo(color='blue')
                    },
                    'no_photos': {
                        'photo_capture_jet_fan': create_test_photo(color='red')
                    }
                }
            ]
        },
        {
            'name': 'Prep Kitchen',
            'equipment': [
                {
                    'type': 'UVF',
                    'type_name': 'UVF Hood',
                    'location': 'Station 2',
                    'with_marvel': True,
                    'yes_responses': [
                        {
                            'item': 'monitoring_console_type',
                            'question': 'What is the monitoring console type installed in the hood?',
                            'answer': 'Advanced Console V2',
                            'comment': 'Latest model installed'
                        }
                    ],
                    'no_responses': [
                        {
                            'item': 'alarms_registered',
                            'question': 'Is there an alarm registered in the monitoring console?',
                            'answer': 'Yes',
                            'comment': 'UV lamp replacement needed'
                        }
                    ],
                    'photos_count': 2,
                    'yes_photos': {
                        'photo_monitoring_console': create_test_photo(color='cyan')
                    },
                    'no_photos': {
                        'photo_alarms_registered': create_test_photo(color='orange')
                    }
                }
            ]
        }
    ],
    'work_performed': '''1. Performed comprehensive inspection of all kitchen ventilation systems
2. Cleaned and replaced KSA filters in Station 1
3. Identified fan noise issue in KVF hood
4. Checked UV lamp status in UVF hood
5. Documented all findings with photographic evidence
6. Provided recommendations for maintenance schedule''',
    'recommendations': '''1. Schedule fan maintenance for Station 1 KVF hood within 1 week
2. Replace UV lamp in Station 2 UVF hood within 2 weeks
3. Continue quarterly filter maintenance
4. Consider upgrading to Marvel system for better control''',
    'technician_name': 'Ahmad Al-Rashid',
    'technician_id': 'HLT-TECH-105',
    'service_date': '2024-01-20',
    'technician_signature': create_test_signature("Ahmad Al-Rashid"),
    'customer_signature': create_test_signature("Sarah Johnson"),
    'customer_signatory': 'Sarah Johnson'
}

# Test equipment data
TEST_EQUIPMENT_KVF = {
    'id': 'kvf_test_001',
    'type': 'KVF',
    'serial_number': 'KVF-2024-001',
    'location': 'Main Kitchen Area',
    'inspection_data': {
        'lights_operational': {'answer': 'Yes', 'comment': 'Working fine'},
        'lights_ballast': {'answer': 'Yes', 'comment': ''},
        'capture_jet_fan': {'answer': 'No', 'comment': 'Needs repair'},
        'ksa_filters_condition': {'answer': 'Yes', 'comment': 'Clean'}
    },
    'photos': {
        'photo_lights_operational': create_test_photo(color='green'),
        'photo_capture_jet_fan': create_test_photo(color='red')
    }
}

TEST_EQUIPMENT_UVF = {
    'id': 'uvf_test_001',
    'type': 'UVF',
    'serial_number': 'UVF-2024-001',
    'location': 'Prep Kitchen Area',
    'inspection_data': {
        'monitoring_console_type': {'answer': 'Advanced Console V2'},
        'module_count': {'answer': 3},
        'alarms_registered': {'answer': 'Yes', 'comment': 'UV lamp alarm'},
        'uv_power_cable': {'answer': 'Yes', 'comment': 'Good condition'}
    },
    'photos': {
        'photo_monitoring_console': create_test_photo(color='blue'),
        'photo_alarms_registered': create_test_photo(color='orange')
    }
}

TEST_EQUIPMENT_MARVEL = {
    'id': 'marvel_test_001',
    'type': 'MARVEL',
    'serial_number': 'MARVEL-2024-001',
    'location': 'Control Room',
    'inspection_data': {
        'power_supply': {'answer': 'Yes', 'comment': 'Stable power'},
        'touch_screen_operational': {'answer': 'Yes', 'comment': 'Responsive'},
        'ntc_sensors': {'answer': 'Yes', 'comment': 'All 8 sensors working'},
        'ir_sensors': {'answer': 'No', 'comment': 'Sensor 3 not responding'}
    },
    'photos': {
        'photo_touch_screen': create_test_photo(color='green'),
        'photo_ir_sensors': create_test_photo(color='red')
    }
}

# Test kitchen configurations
TEST_KITCHEN_SINGLE = {
    'name': 'Single Kitchen',
    'equipment_list': [TEST_EQUIPMENT_KVF]
}

TEST_KITCHEN_MULTIPLE = {
    'name': 'Main Kitchen',
    'equipment_list': [TEST_EQUIPMENT_KVF, TEST_EQUIPMENT_UVF]
}

TEST_KITCHEN_WITH_MARVEL = {
    'name': 'Advanced Kitchen',
    'equipment_list': [TEST_EQUIPMENT_KVF, TEST_EQUIPMENT_MARVEL]
}

# Test scenarios for different visit types
SERVICE_CALL_DATA = BASIC_REPORT_DATA.copy()
SERVICE_CALL_DATA.update({
    'visit_type': 'Service Call',
    'visit_class': 'To Be Invoiced',
    'work_performed': 'Responded to service call for hood malfunction. Identified and repaired issue.',
    'recommendations': 'Monitor system for 24 hours. Schedule preventive maintenance.'
})

AMC_VISIT_DATA = BASIC_REPORT_DATA.copy()
AMC_VISIT_DATA.update({
    'visit_type': 'AMC (Contract)',
    'visit_class': 'Free of Charge',
    'work_performed': 'Conducted scheduled preventive maintenance including filter cleaning and system checks.',
    'recommendations': 'All systems operating normally. Next service due in 3 months.'
})

EMERGENCY_SERVICE_DATA = BASIC_REPORT_DATA.copy()
EMERGENCY_SERVICE_DATA.update({
    'visit_type': 'Emergency Service',
    'visit_class': 'To Be Invoiced',
    'work_performed': 'Emergency response to fire suppression system alarm. Reset system after inspection.',
    'recommendations': 'System functioning normally. Recommend training for kitchen staff on alarm procedures.'
})

# Edge case test data
MINIMAL_DATA = {
    'customer_name': '',
    'project_name': '',
    'contact_person': '',
    'outlet_location': '',
    'contact_number': '',
    'visit_type': '',
    'visit_class': 'To Be Invoiced',
    'date': datetime.now().strftime('%Y-%m-%d'),
    'equipment_inspection': [],
    'work_performed': '',
    'recommendations': '',
    'technician_name': '',
    'technician_id': '',
    'service_date': datetime.now().strftime('%Y-%m-%d')
}

UNICODE_DATA = BASIC_REPORT_DATA.copy()
UNICODE_DATA.update({
    'customer_name': 'شركة الاختبار السعودية',
    'contact_person': 'أحمد محمد',
    'outlet_location': 'الرياض - حي الملك فهد',
    'work_performed': 'تم فحص أنظمة التهوية والتأكد من سلامتها',
    'recommendations': 'الاستمرار في الصيانة الدورية'
})

# Test data collections
ALL_EQUIPMENT_TYPES = [
    TEST_EQUIPMENT_KVF,
    TEST_EQUIPMENT_UVF,
    TEST_EQUIPMENT_MARVEL,
    {
        'id': 'kvi_test_001',
        'type': 'KVI',
        'serial_number': 'KVI-2024-001',
        'location': 'Kitchen Station 3',
        'inspection_data': {
            'lights_operational': {'answer': 'Yes'},
            'capture_jet_fan': {'answer': 'Yes'},
            'ksa_filters_condition': {'answer': 'Yes'}
        },
        'photos': {}
    },
    {
        'id': 'cmw_test_001',
        'type': 'CMW',
        'serial_number': 'CMW-2024-001',
        'location': 'Kitchen Station 4',
        'inspection_data': {
            'lights_operational': {'answer': 'Yes'},
            'cold_mist_system': {'answer': 'Yes', 'comment': 'Working properly'}
        },
        'photos': {}
    },
    {
        'id': 'ecology_test_001',
        'type': 'ECOLOGY',
        'serial_number': 'ECO-2024-001',
        'location': 'Exhaust Room',
        'inspection_data': {
            'control_panel': {'answer': 'Yes'},
            'esp_section': {'answer': 'Yes'}
        },
        'photos': {}
    },
    {
        'id': 'mobichef_test_001',
        'type': 'MOBICHEF',
        'serial_number': 'MOBI-2024-001',
        'location': 'Mobile Station',
        'inspection_data': {
            'hood_lights': {'answer': 'Yes'},
            'ksa_filters': {'answer': 'Yes'}
        },
        'photos': {}
    }
]

# Performance test data - large dataset
def create_large_test_data(num_kitchens=10, num_equipment_per_kitchen=5):
    """Create large test dataset for performance testing"""
    import random
    
    equipment_types = ['KVF', 'KVI', 'UVF', 'CMW', 'ECOLOGY', 'MOBICHEF']
    
    kitchens = []
    for kitchen_idx in range(num_kitchens):
        equipment_list = []
        for equip_idx in range(num_equipment_per_kitchen):
            equip_type = random.choice(equipment_types)
            equipment = {
                'id': f'{equip_type.lower()}_perf_{kitchen_idx}_{equip_idx}',
                'type': equip_type,
                'serial_number': f'{equip_type}-PERF-{kitchen_idx:03d}-{equip_idx:03d}',
                'location': f'Kitchen {kitchen_idx} Station {equip_idx}',
                'inspection_data': {
                    'test_item': {
                        'answer': random.choice(['Yes', 'No']),
                        'comment': f'Performance test item {equip_idx}'
                    }
                },
                'photos': {}
            }
            equipment_list.append(equipment)
        
        kitchen = {
            'name': f'Performance Kitchen {kitchen_idx}',
            'equipment_list': equipment_list
        }
        kitchens.append(kitchen)
    
    return {
        'customer_name': 'Performance Test Customer',
        'project_name': 'Performance Test Project',
        'contact_person': 'Performance Tester',
        'outlet_location': 'Performance Test Location',
        'contact_number': '+966 50 000 0000',
        'visit_type': 'Service Call',
        'visit_class': 'To Be Invoiced',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'equipment_inspection': [],  # Will be populated by kitchen summary
        'work_performed': 'Performance test work performed',
        'recommendations': 'Performance test recommendations',
        'technician_name': 'Performance Tester',
        'technician_id': 'PERF-001',
        'service_date': datetime.now().strftime('%Y-%m-%d')
    }


# Export commonly used test data
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