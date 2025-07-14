# Halton KSA Service Reports MVP

## Overview
This is a Streamlit-based MVP application for Halton KSA's service team to generate standardized service reports. The application allows technicians to fill out dynamic forms and download completed reports as Word documents.

## Features
- **Report Type Selection**: Currently supports Technical Reports (with more types coming soon)
- **Dynamic Form Interface**: Adaptive form fields based on report type
- **Digital Signature Capability**: 
  - Upload signature images (PNG, JPG, JPEG)
  - Includes standalone HTML signature pad for creating signatures
  - Signatures are embedded in the final Word document
  - Touch-screen compatible for mobile devices
- **Professional Document Generation**: 
  - Exports reports as professionally formatted Word documents
  - Includes Halton branding and color scheme
  - Professional table layouts with alternating row shading
  - Numbered sections and consistent formatting
  - Signature page with acknowledgment text and actual signature image
  - Header and footer on all pages
- **Input Validation**: Ensures all required fields are completed
- **User-Friendly Interface**: Clean, intuitive design optimized for field use

## Installation

1. **Clone or download this repository**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Navigate to the project directory**:
   ```bash
   cd /path/to/MVP
   ```

2. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

3. **Access the application**:
   - The application will automatically open in your default browser
   - If not, navigate to: `http://localhost:8501`

## Usage

### Generating a Technical Report

1. **Select Report Type**: Choose "Technical Report" from the sidebar (default selection)

2. **Fill in the Form**:
   - **General Information**: Customer details, project name, contact information
   - **Equipment Details**: Description of equipment serviced
   - **Work Performed**: Detailed description of services completed
   - **Findings**: Observations and issues discovered
   - **Recommendations**: Suggested follow-up actions
   - **Technician Information**: Your name and ID
   - **Digital Signature**: Upload a signature image or create one using the provided signature pad

3. **Generate Report**: Click the "Generate Report" button at the bottom of the form

4. **Download**: After successful generation, click "Download Report" to save the Word document

### Required Fields
All fields marked with an asterisk (*) are required and must be filled before generating a report.

## Technical Details

- **Framework**: Streamlit 1.28.2
- **Document Generation**: python-docx 1.1.0
- **Python Version**: 3.8 or higher recommended

## File Structure
```
MVP/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Future Enhancements (Post-MVP)
- Additional report types (Testing & Commissioning, General Service)
- Halton KSA letterhead integration
- Role-based access control
- Manager approval workflows
- Database persistence
- Mobile application

## Support
For issues or questions, please contact the development team.

## Version
MVP Version 1.0 - July 2025