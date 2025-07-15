# Technical Report System - Requirements Documentation

## 📋 Table of Contents
1. [System Overview](#system-overview)
2. [Data Model & Schema](#data-model--schema)
3. [User Interface Requirements](#user-interface-requirements)
4. [Equipment Configuration](#equipment-configuration)
5. [Word Document Generation](#word-document-generation)
6. [Advanced Features](#advanced-features)
7. [Technical Implementation](#technical-implementation)
8. [Business Logic & Workflows](#business-logic--workflows)
9. [Integration Requirements](#integration-requirements)

---

## 1. System Overview

### Purpose
The Technical Report System is a comprehensive form-based application for Halton KSA field technicians to document service visits, equipment inspections, and generate professional Word documents for customers.

### Key Features
- **Multi-kitchen Equipment Management**: Support for multiple kitchens with various equipment types
- **Dynamic Inspection Checklists**: Equipment-specific forms with conditional logic
- **Digital Signatures**: Both technician and customer signature capture
- **Professional Document Generation**: Branded Word documents with letterhead
- **Form Data Sharing**: Save and share form progress via encoded URLs
- **Photo Documentation**: Equipment inspection photos with categorization

### Target Users
- **Primary**: Field service technicians
- **Secondary**: Service managers, customers (for signatures)

### Use Cases
- Service call documentation
- AMC (Annual Maintenance Contract) inspections
- Emergency service reports
- Installation and commissioning documentation

---

## 2. Data Model & Schema

### 2.1 Report Data Structure

```python
{
    "basic_info": {
        "customer_name": str,          # Required
        "project_name": str,           # Required
        "contact_person": str,         # Required
        "outlet_location": str,        # Required
        "contact_number": str,         # Required
        "visit_type": str,             # Required: ["Service Call", "AMC (Contract)", "Emergency Service", "Installation", "Commissioning"]
        "visit_class": str,            # Required: ["To Be Invoiced", "Free of Charge", "Warranty"]
        "report_date": date,           # Required
        "work_performed": str,         # Required
        "recommendations": str,        # Optional
        "technician_name": str,        # Required
        "technician_id": str,          # Required
        "service_date": date           # Required
    },
    "kitchen_data": {
        "num_kitchens": int,           # Min: 1, Max: 10
        "kitchen_list": [
            {
                "id": str,             # Auto-generated unique ID
                "name": str,           # Kitchen name/identifier
                "equipment_list": [
                    {
                        "id": str,     # Auto-generated unique ID
                        "type": str,   # Equipment type code (KVF, UVF, etc.)
                        "with_marvel": bool,  # Marvel system included
                        "location": str,      # Equipment location
                        "inspection_data": {
                            "question_id": {
                                "answer": str,    # User response
                                "comment": str    # Optional comment
                            }
                        },
                        "photos": {
                            "photo_key": file_object  # Uploaded images
                        }
                    }
                ]
            }
        ]
    },
    "signatures": {
        "technician_signature": image_bytes,     # PNG format
        "customer_signature": image_bytes,       # PNG format
        "customer_signatory": str                # Customer rep name
    }
}
```

### 2.2 Equipment Types

| Code | Name | Description |
|------|------|-------------|
| KVF | KVF Hood | Kitchen ventilation hood with capture jet fan |
| UVF | UVF System | UV filtration system with modules |
| ECOLOGY | Ecology Unit | Air treatment system |
| CMW | Cold Mist Wash | Water wash system |
| AIRBOX | Air Box | Air handling unit |
| SWHP | SW Heat Pump | Heat pump system |
| ERV | ERV System | Energy recovery ventilation |
| MARVEL | MARVEL System | Control and monitoring system |

### 2.3 Visit Types & Behavior

- **Service Call**: Standard inspection checklist
- **AMC (Contract)**: Includes additional PPM (Preventive Maintenance) checklist
- **Emergency Service**: Standard checklist with priority handling
- **Installation**: Focus on installation verification
- **Commissioning**: Comprehensive testing and validation

---

## 3. User Interface Requirements

### 3.1 Form Structure

#### Page Layout
```
Header: "Halton KSA Service Reports"
├── Sidebar: Report Type Selection
└── Main Content:
    ├── General Information (2-column layout)
    ├── Kitchen & Equipment Inspection
    │   ├── Kitchen Management (expandable sections)
    │   └── Equipment Forms (conditional rendering)
    ├── Work Performed & Recommendations
    ├── Technician Signature (canvas)
    ├── Customer Signature (canvas)
    ├── Form Sharing Section
    └── Report Generation
```

#### General Information Fields
```
Column 1:                    Column 2:
- Customer Name*             - Contact Number*
- Project Name*              - Visit Type* (dropdown)
- Contact Person*            - Visit Class* (dropdown)
- Outlet/Location*           - Report Date (date picker)
```

#### Kitchen Management
- **Number Input**: "Number of Kitchens" (1-10)
- **Dynamic Sections**: Auto-create/remove kitchen sections
- **Kitchen Naming**: Text input for each kitchen name
- **Equipment Count**: Number input per kitchen

### 3.2 Equipment Inspection Flow

#### Equipment Addition
1. **Select Equipment Type** (dropdown)
2. **Click "➕ Add Equipment"**
3. **Fill Basic Info**:
   - Location* (text input)
   - With Marvel checkbox
4. **Complete Inspection Checklist** (dynamic based on equipment type)

#### Conditional Form Logic
- **Answer-based follow-ups**: Yes/No answers trigger additional questions
- **Photo requirements**: Automatic photo upload prompts based on answers
- **Comment requirements**: Mandatory comments for "No" answers
- **Marvel integration**: Additional checklist when "With Marvel" is selected

### 3.3 Validation Rules

#### Required Fields (marked with *)
- All basic information fields except recommendations
- Equipment location for each added equipment
- At least one signature (technician)

#### Field Validation
- **Contact Number**: Phone number format
- **Equipment Count**: Min 0, Max 20 per kitchen
- **Kitchen Count**: Min 1, Max 10
- **File Uploads**: PNG/JPG only, max size limits

#### Form Submission
- **Validation Check**: Display missing required fields
- **Error Handling**: Prevent submission until all required fields completed
- **Success State**: Generate and offer Word document download

---

## 4. Equipment Configuration

### 4.1 Question Types

#### Available Input Types
```python
{
    "yes_no": ["", "Yes", "No"],
    "yes_no_na": ["", "Yes", "No", "N/A"],
    "text": "Free text input",
    "number": "Numeric input with min/max",
    "select": "Single selection dropdown",
    "multi_select": "Multiple selection checkboxes",
    "photo": "File upload widget"
}
```

#### Conditional Logic Structure
```python
{
    "id": "question_identifier",
    "question": "Question text displayed to user",
    "type": "input_type",
    "required": bool,
    "conditions": {
        "yes": {
            "photo": bool,           # Require photo
            "comment": bool,         # Require comment
            "action": str,           # Display warning/instruction
            "follow_up": []          # Additional questions
        },
        "no": {
            "photo": bool,
            "comment": bool,
            "action": str,
            "follow_up": []
        }
    }
}
```

### 4.2 Equipment-Specific Checklists

#### KVF Hood Questions
1. **Hood Lights Operational?** (yes_no_na)
   - Yes: Photo required
   - No: Photo + comment required
2. **Ballast for Hood Lights?** (yes_no)
   - Yes → Follow-up: "Ballast issue?" (yes_no)
3. **Capture Jet Fan Working?** (yes_no)
   - Yes: Photo required
   - No: Photo + comment required
4. **Extract Airflow Issue?** (yes_no)
   - Yes → Complex follow-up chain with damper checks
5. **Supply Airflow Issue?** (yes_no)
   - Similar logic to extract airflow

#### UVF System Questions
1. **Module Count** (number input)
   - Triggers individual module inspection tabs
2. **Per-module questions**:
   - UV lamp operational
   - Module control status
   - Airflow readings

#### Marvel System Integration
When "With Marvel" is selected for any equipment:
- **Additional Questions**: Marvel-specific checklist appended
- **Control Panel Check**: Internal components operational
- **Display Status**: Screen and interface checks
- **Communication**: Network connectivity verification

### 4.3 PPM (Preventive Maintenance) Checklist

Activated when visit_type == "AMC (Contract)":

#### Universal PPM Items
- Filter replacement/cleaning
- Motor inspection
- Electrical connections check
- Before/after photos with descriptions

#### Equipment-Specific PPM
- **UVF**: UV lamp replacement, module cleaning
- **CMW**: Water system maintenance, nozzle cleaning
- **ECOLOGY**: Air treatment component service

---

## 5. Word Document Generation

### 5.1 Document Structure

#### Template Requirements
- **Letterhead**: `Templates/Report Letter Head.docx`
- **Fallback**: Create new document if template missing
- **Margins**: 0.75" all sides
- **Fonts**: Professional corporate styling

#### Document Sections
```
1. TECHNICAL REPORT (Title)
2. GENERAL INFORMATION (Table format)
3. EQUIPMENT INSPECTION DETAILS
   ├── Kitchen: [Kitchen Name]
   │   ├── [Equipment Type] (With Marvel)
   │   │   ├── Location: [Location]
   │   │   ├── Total Photos: [Count]
   │   │   ├── Positive Findings (Table)
   │   │   ├── Photos - Positive Findings
   │   │   ├── Issues Reported (Table)
   │   │   └── Photos - Issues Reported
   │   └── [Next Equipment...]
   └── [Next Kitchen...]
4. WORK PERFORMED
5. RECOMMENDATIONS
6. SIGNATURES
   ├── Technician Signature & Info
   └── Customer Representative Signature
```

### 5.2 Formatting Requirements

#### Tables
- **2-column format**: Question | Answer
- **Halton branding**: Blue headers (#1f4788)
- **Alternating row shading**: Light gray (#F5F5F5)
- **Professional borders**: Subtle lines

#### Photos
- **Side-by-side layout**: 2 photos per row
- **Size**: 2.0" width each
- **Captions**: Descriptive text below each photo
- **Categorization**:
  - Photos for "Yes" answers (positive findings)
  - Photos for "No" answers (issues reported)

#### Text Styling
- **Headings**: Halton blue, bold
- **Body text**: Standard black, 11pt
- **Equipment headers**: Include Marvel status if applicable

### 5.3 Dynamic Content Generation

#### Equipment Processing Logic
```python
for kitchen in kitchen_list:
    # Kitchen header
    add_kitchen_section(kitchen.name)
    
    for equipment in kitchen.equipment_list:
        # Equipment header with Marvel indicator
        title = f"{equipment.type_name}"
        if equipment.with_marvel:
            title += " (With Marvel)"
        
        # Categorize responses
        yes_responses = filter_responses(equipment, "Yes")
        no_responses = filter_responses(equipment, "No")
        
        # Generate tables and photos
        create_findings_table(yes_responses)
        add_photos_section(yes_responses, "Positive Findings")
        create_issues_table(no_responses)
        add_photos_section(no_responses, "Issues Reported")
```

---

## 6. Advanced Features

### 6.1 Form Data Sharing

#### URL Encoding System
```python
# Data Collection
form_data = collect_current_form_state()

# Encoding Process
json_string = json.dumps(form_data)
base64_encoded = base64.urlsafe_b64encode(json_string)
url_encoded = urllib.parse.quote(base64_encoded)

# Share URL Generation
share_url = f"https://ksaservicemvp.streamlit.app?data={url_encoded}"
```

#### Shared Data Limitations
- **Included**: All form fields, inspection answers, comments
- **Excluded**: Photos (too large), signatures (too large)
- **Size Limit**: ~10KB encoded data

#### Restoration Process
1. **URL Parameter Detection**: Check for `?data=` parameter
2. **Decoding**: Reverse the encoding process
3. **Validation**: Verify data structure integrity
4. **State Restoration**: Populate form fields and session state
5. **User Notification**: Success/error message display

### 6.2 Session State Management

#### State Persistence
```python
# Core session variables
st.session_state = {
    "kitchen_list": [],           # Kitchen and equipment data
    "report_data": {},            # Final report data for generation
    "report_generated": bool,     # Generation status flag
    "technician_signature": bytes, # Signature image data
    "customer_signatory": str,    # Customer rep name
    "data_restored": bool,        # URL restoration flag
    "generated_share_url": str    # Current share URL
}
```

#### State Cleanup
- **New Report**: Clear all previous data
- **Widget Keys**: Remove form-specific session keys
- **Selective Clearing**: Preserve user preferences

---

## 7. Technical Implementation

### 7.1 Required Dependencies

```python
# Core Framework
streamlit>=1.28.0

# Document Generation
python-docx>=0.8.11
Pillow>=9.0.0

# Signature Capture
streamlit-drawable-canvas>=0.9.2
numpy>=1.21.0

# Data Handling
datetime
json
base64
urllib.parse
io
os
```

### 7.2 Key Functions

#### Core Application Functions
```python
def main():
    """Main application entry point with URL parameter handling"""

def collect_form_data():
    """Gather all form data for sharing"""

def restore_form_data(form_data):
    """Restore form data from shared link"""

def create_technical_report(data):
    """Generate Word document from form data"""

def get_kitchen_summary():
    """Process equipment data for report generation"""
```

#### Equipment Management
```python
def render_checklist_item(equipment, item, prefix=""):
    """Recursive checklist rendering with conditional logic"""

def find_question_text(equipment_type, question_id):
    """Locate question text in nested checklist structure"""

def should_show_item(equipment, item, prefix):
    """Determine if question should be displayed based on conditions"""
```

#### Document Generation
```python
def style_heading(heading, level=1):
    """Apply Halton branding to document headings"""

def create_info_table(doc, data_rows):
    """Create professionally formatted information tables"""

def format_table_style_enhanced(table):
    """Apply enhanced Halton styling to tables"""
```

### 7.3 File Structure Requirements

```
project_root/
├── app.py                    # Main application
├── equipment_config.py       # Equipment definitions
├── equipment_inspection.py   # Equipment handling logic
├── utils.py                 # Document generation utilities
├── Templates/
│   └── Report Letter Head.docx  # Word template
├── assets/                  # Static resources
├── requirements.txt         # Dependencies
└── tests/                   # Test suite
```

---

## 8. Business Logic & Workflows

### 8.1 Visit Type Workflows

#### Service Call Workflow
1. **Basic Information** → Equipment Selection → Inspection → Report Generation
2. **Standard Checklist**: Regular inspection items only
3. **Photo Requirements**: Based on Yes/No answers

#### AMC (Contract) Workflow
1. **Enhanced Process**: Standard checklist + PPM checklist
2. **Additional Requirements**:
   - Before/after photos for maintenance
   - Photo descriptions
   - Extended documentation
3. **PPM Items**: Equipment-specific maintenance checklist

### 8.2 Equipment Addition Logic

#### Dynamic Equipment Management
```python
# Kitchen Creation
for i in range(num_kitchens):
    kitchen = create_kitchen(f"Kitchen {i+1}")
    
    # Equipment Addition per Kitchen
    for j in range(equipment_count):
        equipment = create_equipment(selected_type)
        
        # Marvel Integration
        if equipment.with_marvel:
            append_marvel_checklist(equipment)
        
        # Visit Type Specific Items
        if visit_type == "AMC (Contract)":
            append_ppm_checklist(equipment)
```

#### Conditional Question Flow
```python
# Question Processing
def process_question(question, answer):
    if answer in question.conditions:
        condition = question.conditions[answer]
        
        # Photo Requirement
        if condition.get("photo"):
            show_photo_upload()
        
        # Comment Requirement  
        if condition.get("comment"):
            show_comment_field()
        
        # Follow-up Questions
        if condition.get("follow_up"):
            render_followup_questions(condition.follow_up)
        
        # Action Instructions
        if condition.get("action"):
            display_warning(condition.action)
```

### 8.3 Validation & Error Handling

#### Field Validation Rules
```python
required_fields = {
    "basic_info": [
        "customer_name", "project_name", "contact_person",
        "outlet_location", "contact_number", "visit_type",
        "work_performed", "technician_name", "technician_id"
    ],
    "equipment_info": [
        "location"  # Required for each equipment
    ]
}
```

#### Error States
- **Missing Required Fields**: Highlight and list missing items
- **Invalid Data**: Format validation messages
- **Equipment Errors**: Location missing, no equipment added
- **Generation Errors**: Document creation failures

---

## 9. Integration Requirements

### 9.1 Service Dashboard Integration

#### Embedding Options
1. **Standalone Route**: `/technical-report` endpoint
2. **Modal Integration**: Popup window within dashboard
3. **Tab Integration**: Additional tab in service management

#### Data Flow Integration
```python
# Dashboard → Technical Report
{
    "customer_id": int,
    "service_request_id": int,
    "technician_id": int,
    "pre_filled_data": {
        "customer_name": str,
        "contact_info": dict,
        "equipment_list": []  # Pre-known equipment
    }
}

# Technical Report → Dashboard
{
    "report_id": str,
    "report_data": dict,
    "document_path": str,
    "completion_status": str,
    "signatures_captured": bool
}
```

### 9.2 Database Requirements

#### Report Storage Schema
```sql
CREATE TABLE technical_reports (
    id UUID PRIMARY KEY,
    service_request_id UUID FOREIGN KEY,
    technician_id UUID FOREIGN KEY,
    customer_id UUID FOREIGN KEY,
    report_data JSON,
    document_path VARCHAR(255),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    status VARCHAR(50)
);

CREATE TABLE report_signatures (
    id UUID PRIMARY KEY,
    report_id UUID FOREIGN KEY,
    signature_type VARCHAR(20), -- 'technician' or 'customer'
    signatory_name VARCHAR(100),
    signature_data BYTEA,
    captured_at TIMESTAMP
);

CREATE TABLE report_photos (
    id UUID PRIMARY KEY,
    report_id UUID FOREIGN KEY,
    equipment_id VARCHAR(100),
    question_id VARCHAR(100),
    photo_data BYTEA,
    photo_type VARCHAR(20), -- 'positive' or 'issue'
    caption TEXT,
    uploaded_at TIMESTAMP
);
```

### 9.3 API Endpoints

#### Required Endpoints
```python
# Report Management
POST /api/technical-reports/          # Create new report
GET  /api/technical-reports/{id}      # Retrieve report
PUT  /api/technical-reports/{id}      # Update report
DELETE /api/technical-reports/{id}    # Delete report

# Document Generation
POST /api/technical-reports/{id}/generate-document
GET  /api/technical-reports/{id}/download-document

# Data Sharing
POST /api/technical-reports/share    # Generate share URL
GET  /api/technical-reports/restore  # Restore from share URL

# Photo Management
POST /api/technical-reports/{id}/photos
GET  /api/technical-reports/{id}/photos/{photo_id}
DELETE /api/technical-reports/{id}/photos/{photo_id}
```

### 9.4 Authentication & Authorization

#### User Roles
- **Technician**: Create/edit own reports, view customer info
- **Supervisor**: View/edit all technician reports
- **Manager**: Full access, analytics, export capabilities
- **Customer**: View completed reports, provide signatures

#### Security Requirements
- **Authentication**: JWT token-based
- **Authorization**: Role-based access control (RBAC)
- **Data Privacy**: Encrypt sensitive customer information
- **Audit Trail**: Log all report modifications

---

## 📊 Summary

This Technical Report system provides a comprehensive solution for field service documentation with:

- **Multi-equipment support** across 8+ equipment types
- **Dynamic conditional logic** for intelligent form flow
- **Professional document generation** with Halton branding
- **Digital signature capture** for technician and customer approval
- **Advanced sharing capabilities** for collaboration
- **Robust validation** and error handling
- **Seamless integration** potential with existing service dashboard

The system is designed to streamline field service operations while maintaining professional documentation standards and ensuring comprehensive equipment inspection coverage.

---

*Generated for Halton KSA Service Dashboard Integration*
*Document Version: 1.0*
*Last Updated: 2024*