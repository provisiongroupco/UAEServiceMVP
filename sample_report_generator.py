"""
Sample report generator to demonstrate the document output
Run this script to generate a sample Technical Report
"""

from app import create_technical_report
from datetime import datetime
from PIL import Image, ImageDraw
import io

# Sample data
sample_data = {
    'customer_name': 'SELA Company',
    'project_name': 'Stella Kitchen Hoods Installation',
    'contact_person': 'Sultan Alofi',
    'outlet_location': 'Via Mall - Riyadh',
    'contact_number': '+966 55 558 5449',
    'visit_type': 'Service Call',
    'visit_class': 'To Be Invoiced',
    'date': datetime.now().strftime('%Y-%m-%d'),
    'equipment_details': '''Hood Model: Halton KVL-3000
Serial Number: HLT-2024-KSA-1234
Installation Date: January 15, 2024
Location: Main Kitchen, Section A

The equipment is a commercial kitchen ventilation hood system with integrated UV-C technology for grease elimination. The system includes variable air volume (VAV) controls and M.A.R.V.E.L. demand-controlled ventilation.''',
    'work_performed': '''1. Performed complete inspection of hood system and exhaust fans
2. Cleaned and replaced all grease filters (6 units)
3. Inspected and tested UV-C lamps - all functioning within specifications
4. Checked and calibrated VAV controls and sensors
5. Cleaned hood surfaces and interior chambers
6. Tested fire suppression system linkage and controls
7. Verified exhaust fan operation and balanced airflow
8. Lubricated fan bearings and checked belt tension
9. Inspected and cleaned make-up air units
10. Updated maintenance log and system documentation''',
    'findings': '''During the inspection, the following observations were made:

1. All UV-C lamps are functioning properly with expected UV output levels
2. Grease filters showed normal accumulation for 3-month service interval
3. VAV controls responding correctly to kitchen demand
4. Minor adjustment needed on exhaust fan belt tension - completed
5. Fire suppression system test successful - all components operational
6. Make-up air balance within design specifications
7. No unusual noise or vibration detected in fan systems
8. Control panel displays all systems normal

Overall system condition: GOOD
The ventilation system is operating within design parameters and manufacturer specifications.''',
    'recommendations': '''Based on today's service visit, we recommend the following:

1. Continue with quarterly preventive maintenance schedule
2. Replace UV-C lamps at next service visit (6-month interval)
3. Consider upgrading to Halton Connect IoT monitoring system for real-time performance tracking
4. Schedule annual fire suppression system certification with authorized provider
5. Maintain current filter replacement schedule (quarterly)

No immediate repairs or replacements are required. The system is performing optimally.''',
    'technician_name': 'Mohammed Al-Rahman',
    'technician_id': 'HLT-TECH-042',
    'service_date': datetime.now().strftime('%Y-%m-%d')
}

def create_sample_signature():
    """Create a sample signature image for demonstration"""
    # Create a white image
    img = Image.new('RGB', (200, 80), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple signature-like curve
    points = [
        (20, 40), (30, 35), (40, 30), (50, 35), (60, 40),
        (70, 45), (80, 40), (90, 30), (100, 25), (110, 30),
        (120, 40), (130, 50), (140, 45), (150, 40), (160, 35)
    ]
    
    # Draw the signature
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill='black', width=2)
    
    # Add a underline
    draw.line([(20, 55), (160, 55)], fill='black', width=1)
    
    # Save to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    return img_bytes

# Add signature to sample data
sample_data['technician_signature'] = create_sample_signature()

if __name__ == "__main__":
    print("Generating sample Technical Report...")
    
    # Generate the report
    doc_bytes = create_technical_report(sample_data)
    
    # Save to file
    filename = f"Sample_Technical_Report_{datetime.now().strftime('%Y%m%d')}.docx"
    with open(filename, 'wb') as f:
        f.write(doc_bytes.getvalue())
    
    print(f"Sample report generated successfully: {filename}")
    print("You can open this file in Microsoft Word to see the professional layout.")