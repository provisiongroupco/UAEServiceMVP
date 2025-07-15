# Halton KSA Service Reports - User Guide

## 📋 Table of Contents
1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [Step-by-Step Usage Guide](#step-by-step-usage-guide)
4. [Equipment Inspection Workflows](#equipment-inspection-workflows)
5. [Special Features](#special-features)
6. [Tips and Best Practices](#tips-and-best-practices)
7. [Troubleshooting](#troubleshooting)

---

## Overview

### What is the Service Reports System?

The Halton KSA Service Reports System is a web-based application designed for field service technicians to:
- Document equipment inspections and maintenance visits
- Create professional technical reports for customers
- Capture digital signatures from both technicians and customers
- Generate branded Word documents with inspection details and photos

### Key Benefits
- **Streamlined Process**: Complete inspections digitally without paper forms
- **Professional Output**: Generate consistent, branded reports automatically
- **Photo Documentation**: Attach photos directly to specific inspection items
- **Smart Forms**: Questions adapt based on your answers, showing only relevant fields
- **Share Progress**: Save and share partially completed forms with colleagues

### Access the System
- **Production URL**: https://ksaservicemvp.streamlit.app
- **Supported Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **Device Compatibility**: Desktop, laptop, tablet (mobile supported but desktop recommended)

---

## Getting Started

### Before You Begin
Ensure you have:
- [ ] Customer information (name, contact, location)
- [ ] Equipment details for inspection
- [ ] Camera/phone ready for photos
- [ ] Internet connection

### System Overview
The application is organized into these main sections:
1. **General Information** - Customer and visit details
2. **Kitchen & Equipment Inspection** - Equipment-specific checklists
3. **Work Documentation** - Work performed and recommendations
4. **Signatures** - Digital signature capture
5. **Report Generation** - Create and download final document

---

## Step-by-Step Usage Guide

### Step 1: Enter General Information

#### Required Fields (marked with *)
| Field | Description | Example |
|-------|-------------|---------|
| Customer Name* | Company/organization name | "Al Faisaliah Hotel" |
| Project Name* | Project or site identifier | "Main Kitchen Renovation" |
| Contact Person* | Your primary contact | "Ahmed Al-Rashid" |
| Outlet/Location* | Specific location/address | "Riyadh - Olaya District" |
| Contact Number* | Phone number | "+966 50 123 4567" |
| Visit Type* | Type of service visit | Select from dropdown |
| Visit Class* | Billing category | Select from dropdown |
| Report Date | Date of report creation | Click calendar icon |

#### Visit Types Explained
- **Service Call**: Standard maintenance or repair visit
- **AMC (Contract)**: Annual maintenance contract visit (includes PPM checklist)
- **Emergency Service**: Urgent response visit
- **Installation**: New equipment installation
- **Commissioning**: Initial setup and testing

### Step 2: Configure Kitchens

1. **Specify Number of Kitchens** (unlimited)
   - Enter the total number of kitchens to inspect
   - Form automatically creates sections for each kitchen
   - No upper limit on number of kitchens

2. **Name Each Kitchen**
   - Provide descriptive names (e.g., "Main Kitchen", "Pastry Kitchen", "Cold Kitchen")
   - This helps organize the final report

3. **Add Equipment to Each Kitchen**
   - Enter number of equipment pieces (0-20 per kitchen)
   - Click "➕ Add Equipment" for each piece

### Step 3: Equipment Inspection

#### Adding Equipment
1. **Select Equipment Type** from dropdown
2. **Enter Location** within the kitchen (e.g., "North wall", "Center island")
3. **Check "With Marvel"** if Marvel control system is included
4. **Complete Inspection Checklist** - questions appear based on equipment type

#### Understanding the Checklist
- **Yes/No/N/A Options**: Select the most appropriate answer
- **Red Asterisk (*)**: Required fields
- **Camera Icon 📷**: Photo required for this answer
- **Comment Box**: Appears when explanation needed
- **Follow-up Questions**: Additional questions may appear based on your answers

### Step 4: Document Work Performed

1. **Work Performed Section**
   - Describe all maintenance, repairs, or inspections completed
   - Be specific and thorough
   - Example: "Cleaned KSA filters, replaced UV lamps in modules 2 and 4, adjusted capture jet fan speed"

2. **Spare Parts Required Section**
   - Click "➕ Add Spare Part" to add parts
   - For each part, specify:
     - **Part Name**: e.g., "KSA Filter", "UV Lamp", "Solenoid Valve"
     - **Quantity**: Number needed
   - Remove parts with 🗑️ button if added by mistake
   - If no parts needed, leave empty - report will show "No spare parts required"

3. **Recommendations Section** (Optional)
   - Suggest future maintenance or repairs
   - Note any concerns for follow-up
   - Example: "Recommend replacing worn door seals within 30 days"

### Step 5: Capture Signatures

#### Technician Signature
1. **Enter Your Details**
   - Technician Name*
   - Technician ID*
   - Service Date*
2. **Draw Signature** on the canvas
3. **Clear** if you need to redo

#### Customer Signature
1. **Customer Representative Name** - Who is signing
2. **Customer draws signature** on the canvas
3. **Clear** if they need to redo

### Step 6: Generate Report

1. **Review All Information** - Ensure completeness
2. **Click "Generate Technical Report"** button
3. **Download** the generated Word document
4. **Share Form** (optional) - Generate URL to share progress

---

## Equipment Inspection Workflows

### 🔧 KVF Hood Inspection

The KVF Hood inspection covers ventilation hoods with capture jet fans. Here's the complete workflow:

| Question | Response Options | Actions Required |
|----------|-----------------|------------------|
| **Are the hood lights operational?** | Yes / No / N/A | • Yes: Upload photo<br>• No: Upload photo + explain issue<br>• N/A: Explain why not applicable |
| **Is there a ballast for the Hood lights?** | Yes / No / N/A | • Yes: Upload photo + triggers follow-up question<br>• No: No action<br>• N/A: Add comment |
| **→ Is there an issue with the hood light ballast?** | Yes / No / N/A | • Yes: Upload photo + explain issue<br>• No: Upload photo of working ballast<br>• N/A: Add comment |
| **Is the capture jet fan working and in good condition?** | Yes / No / N/A | • Yes: Upload photo<br>• No: Upload photo + describe problem<br>• N/A: Add comment |
| **Is there an issue in the hood extract airflow?** | Yes / No / N/A | • Yes: Add comment + follow-up questions<br>• N/A: Add comment |
| **→ Is the extract airflow achieving the design airflow?** | Yes / No / N/A | • No: Upload photo + comment + more follow-ups |
| **→ → Is the manual damper fully opened?** | Yes / No / N/A | • No: Upload photo + "Please open the damper" |
| **Is there an issue in the hood supply airflow?** | Yes / No / N/A | • Yes: Similar flow to extract airflow |
| **Are the KSA filters in good condition?** | Yes / No / N/A | • Yes: Upload photo<br>• No: Upload photo + describe condition<br>• N/A: Add comment |
| **Are the KSA filters all in place?** | Yes / No / N/A | • Yes: Upload photo<br>• No: Upload photo + note missing filters<br>• N/A: Add comment |
| **Are the Personal supply air nozzles in place and in good condition?** | Yes / No / N/A | • Yes: Upload photo<br>• No: Upload photo + describe issue<br>• N/A: Add comment |
| **Any comments about hood condition?** | Yes / No / N/A | • Yes: Add detailed comments<br>• Optional: Include photos |

### 🔧 KVI Hood Inspection

KVI Hood (induction type) follows a similar pattern to KVF but with some differences:
- No supply airflow questions (induction system)
- Includes blank nozzles instead of personal supply nozzles
- Simplified airflow troubleshooting

### 🔧 UVF System Inspection

The UVF system has a unique workflow with module-specific inspections:

1. **Initial Setup**
   - Enter monitoring console type (text)
   - Specify number of modules (creates individual tabs)
   - Check for system alarms

2. **Per-Module Inspection** (for each module):
   - UV cassette photos showing tube count
   - KSA filter magnet photos
   - Filter dimensions
   - UV door sensor and magnet photos
   - Controller photos (MU1 & VV1)
   - Pressure tube connections
   - UV ballast and PCB board photos
   - Power cable connections
   - Module-specific alarms

3. **System-Wide Checks**
   - UV power cables condition
   - Filter placement
   - Standard hood components (lights, fans, airflow)

### 🔧 CMW Hood (Cold Mist) Inspection

The CMW system includes extensive water system checks:

#### Basic Inspection
- Standard hood components (lights, fans, filters)
- Cold mist nozzle operation
- Solenoid valve functionality
- Pressure switches and settings
- Water supply and connections
- Leakage inspection

#### Special Feature: Cold Mist with Hot Water Wash
If system includes hot water wash, additional checks appear:
- Power supply for control panel
- Hot water availability
- Hot water solenoid valves
- Nozzle quantities and condition
- Detergent system operation
- Chemical tank levels (photos required)
- Pressure switch calibration (75PA)

### 🔧 ECOLOGY Unit Inspection

ECOLOGY units focus on air treatment components:

1. **Control System**
   - Control panel presence
   - Touch screen operation and alarms

2. **ESP Section** (if available)
   - ESP functionality
   - HVPS (High Voltage Power Supply) status
   - Autowash system checks
   - Water supply for autowash
   - Detergent availability

3. **Filter Configuration**
   Multi-select filter types:
   - **Pre-filters (Washable/Disposable)**: Size, quantity, dimensions
   - **Bag Filters**: Type (ELF/Normal), photos required
   - **HEPA Filters**: Type (V-Type/Normal), photos required
   - **Carbon Filters**: Type selection

### 🔧 MOBICHEF Inspection

MOBICHEF is a self-contained mobile extraction system with simpler checklist:
- Hood lights functionality
- KSA filter condition and placement
- Mesh filters status
- Pre-filter inspection
- ESP operation
- Carbon filter check
- Capture jet fan operation
- Touch screen status

---

## Special Features

### 🎮 MARVEL System Integration

When "With Marvel" is checked for any equipment, additional inspection items appear:

| Marvel Component | Check Required | Actions Required |
|-----------------|----------------|------------------|
| Power supply availability | Yes/No/N/A | • Yes: Upload photo<br>• No: Upload photo + comment |
| Touch screen operation | Yes/No/N/A | • Yes: Upload photo<br>• No: Upload photo + comment |
| Internal components | Yes/No/N/A | • Yes: Upload photo<br>• No: Add comment |
| 0-10V signal communication | Yes/No/N/A | • Yes: Upload photo<br>• No: Add comment |
| NTC sensors | Yes/No/N/A | • Yes: Upload photo<br>• No: Upload photo + comment |
| IR sensors | Yes/No/N/A | • Yes: Upload photo<br>• No: Upload photo + comment |
| ABD dampers | Yes/No/N/A | • Yes: Upload photo<br>• No: Upload photo + comment |
| ABD actuators | Yes/No/N/A | • Yes: Upload photo<br>• No: Upload photo + comment |

### 📅 PPM Checklist (AMC Visits Only)

When Visit Type is "AMC (Contract)", additional Preventive Maintenance items appear:

#### Standard PPM Items
1. Hood light cleaning
2. Capture jet fan cleaning
3. Hood plenum cleaning
4. Before/After photo documentation
   - Specify number of photo pairs
   - Upload before and after images
   - Add descriptions for each

#### Equipment-Specific PPM
- **UVF Systems**: UV cassette, lamps, and door cleaning
- **CMW Systems**: Cold and hot water nozzle cleaning
- **ECOLOGY Units**: Complete unit maintenance including:
  - Filter cleaning/replacement
  - VFD panel maintenance
  - Fan and motor service
  - All items require photos

### 🔗 Form Sharing Feature

Share partially completed forms with colleagues:

1. **Generate Share Link**
   - Click "Generate Shareable Link"
   - Copy the generated URL
   - Send to colleague via email/message

2. **What's Included**
   - All form fields and answers
   - Comments and text entries
   - Equipment configurations

3. **What's NOT Included**
   - Photos (too large for URL)
   - Signatures
   - These must be re-added

4. **Using a Shared Link**
   - Open the URL in browser
   - Form auto-populates with shared data
   - Continue where colleague left off

---

## Tips and Best Practices

### 📸 Photo Guidelines

1. **Quality Matters**
   - Ensure good lighting
   - Focus on the specific issue/component
   - Include surrounding context when helpful

2. **Required Photos**
   - **NEW**: "Yes" answers now require photos (except for airflow issue questions)
   - "No" answers require photos + comments
   - Show equipment condition clearly
   - Multiple angles if needed for complex issues

3. **File Management**
   - Use descriptive filenames
   - Keep file sizes reasonable
   - JPG/PNG formats only

### ✍️ Writing Effective Comments

1. **Be Specific**
   - "Fan bearing worn, excessive noise at high speed" ✓
   - "Fan broken" ✗

2. **Include Measurements**
   - "Airflow reading: 850 CFM (design: 1200 CFM)"
   - "UV lamp output: 60% of rated capacity"

3. **Note Part Numbers**
   - Helps with ordering replacements
   - Include model numbers when visible

### 🚀 Efficiency Tips

1. **Prepare Before Starting**
   - Gather all customer information
   - Have equipment list ready
   - Take all photos before starting form

2. **Use Browser Features**
   - Keep form open in one tab
   - Reference manuals in another
   - Use browser spell-check

3. **Save Progress**
   - Generate share link periodically
   - Acts as a backup
   - Can resume if connection lost

### ⚠️ Common Mistakes to Avoid

1. **Incomplete Information**
   - Always fill required fields (*)
   - Don't skip photo requirements
   - Add comments when prompted

2. **Generic Descriptions**
   - Avoid "OK" or "Good"
   - Provide specific conditions
   - Quantify when possible

3. **Signature Issues**
   - Ensure signatures are clear
   - Get correct representative name
   - Don't use initials only

---

## Troubleshooting

### Common Issues and Solutions

| Problem | Solution |
|---------|----------|
| **Form won't submit** | Check all required fields (*) are filled |
| **Photos won't upload** | Ensure JPG/PNG format and reasonable size |
| **Share link too long** | Normal - use URL shortener if needed |
| **Signature canvas not working** | Try different browser or clear cache |
| **Report generation fails** | Check internet connection, try again |
| **Lost progress** | Use share link feature regularly as backup |

### Getting Help

1. **Technical Support**
   - Contact your system administrator
   - Include error messages in support request
   - Note browser and device used

2. **Training Resources**
   - Request additional training if needed
   - Practice with test customer data
   - Review completed reports for examples

---

## Quick Reference Card

### Essential Shortcuts
- **Required Field**: Red asterisk (*)
- **Photo Required**: Camera icon 📷 appears
- **Comment Needed**: Text box appears automatically
- **Follow-up Questions**: Appear based on your answers

### Report Sections Order
1. General Information
2. Equipment by Kitchen
3. Positive Findings (with photos)
4. Issues Reported (with photos)
5. Work Performed
6. Spare Parts Required
7. Recommendations
8. Signatures

### Photo Categories
- **Positive Findings**: "Yes" responses with photos
- **Issues Reported**: "No" responses with photos
- **PPM Documentation**: Before/after pairs

---

*This guide is designed to help field technicians effectively use the Halton KSA Service Reports System. For additional support or feature requests, please contact your supervisor.*

*Version 1.1 - 2024*

### Change Log
**Version 1.1**
- Added photo requirements for "Yes" answers to better document working equipment
- Added Spare Parts section for tracking required replacements
- Removed kitchen limit - now supports unlimited kitchens
- Updated Marvel system documentation with photo requirements