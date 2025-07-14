import streamlit as st
from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import io
from PIL import Image
import base64
from streamlit_drawable_canvas import st_canvas
import numpy as np
from utils import (add_header_with_logo, add_footer, style_heading, 
                  create_info_table, add_logo_to_doc, set_cell_margins)

# Page configuration
st.set_page_config(
    page_title="Halton KSA Service Reports",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f4788;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #2c5aa0;
        font-weight: bold;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .stButton > button {
        background-color: #1f4788;
        color: white;
        font-weight: bold;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        border: none;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #2c5aa0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'report_data' not in st.session_state:
    st.session_state.report_data = {}
if 'report_generated' not in st.session_state:
    st.session_state.report_generated = False
if 'technician_signature' not in st.session_state:
    st.session_state.technician_signature = None

def process_uploaded_signature(uploaded_file):
    """Process an uploaded signature image and return image bytes"""
    if uploaded_file is not None:
        # Read the uploaded image
        img = Image.open(uploaded_file)
        
        # Convert to RGB if necessary
        if img.mode != 'RGB':
            rgb_img = Image.new('RGB', img.size, 'white')
            if img.mode == 'RGBA':
                rgb_img.paste(img, mask=img.split()[3])
            else:
                rgb_img.paste(img)
        else:
            rgb_img = img
        
        # Resize to reasonable signature size (maintain aspect ratio)
        max_width = 200
        max_height = 80
        rgb_img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        
        # Save to bytes
        img_bytes = io.BytesIO()
        rgb_img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        return img_bytes
    return None

def create_technical_report(data):
    """Generate a Professional Technical Report Word document"""
    doc = Document()
    
    # Set document margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        section.header_distance = Inches(0.5)
        section.footer_distance = Inches(0.5)
    
    # Check for logo and add professional header
    logo_path = add_logo_to_doc(doc)
    add_header_with_logo(doc, logo_path)
    
    # Add footer
    add_footer(doc)
    
    # Add some space after header
    doc.add_paragraph()
    
    # Add title with styling
    title = doc.add_heading('TECHNICAL REPORT', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    style_heading(title, level=0)
    
    # Add report reference and date
    ref_para = doc.add_paragraph()
    ref_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ref_run = ref_para.add_run(f"Report Date: {data.get('date', datetime.now().strftime('%B %d, %Y'))}")
    ref_run.font.size = Pt(11)
    ref_run.font.color.rgb = RGBColor(100, 100, 100)
    
    # Add a subtle line separator
    doc.add_paragraph('_' * 85)
    
    # GENERAL INFORMATION SECTION
    general_heading = doc.add_heading('1. GENERAL INFORMATION', level=1)
    style_heading(general_heading, level=1)
    
    # Create professional info table
    general_info = [
        ("Customer Name", data.get('customer_name', '')),
        ("Project Name", data.get('project_name', '')),
        ("Contact Person", data.get('contact_person', '')),
        ("Location", data.get('outlet_location', '')),
        ("Contact Number", data.get('contact_number', '')),
        ("Visit Type", data.get('visit_type', '')),
        ("Visit Classification", data.get('visit_class', ''))
    ]
    
    create_info_table(doc, general_info)
    doc.add_paragraph()  # Add spacing
    
    # EQUIPMENT DETAILS SECTION
    equipment_heading = doc.add_heading('2. EQUIPMENT DETAILS', level=1)
    style_heading(equipment_heading, level=1)
    
    equipment_para = doc.add_paragraph()
    equipment_text = equipment_para.add_run(data.get('equipment_details', ''))
    equipment_text.font.size = Pt(11)
    equipment_para.paragraph_format.line_spacing = 1.5
    equipment_para.paragraph_format.space_after = Pt(12)
    
    # WORK PERFORMED SECTION
    work_heading = doc.add_heading('3. WORK PERFORMED', level=1)
    style_heading(work_heading, level=1)
    
    work_para = doc.add_paragraph()
    work_text = work_para.add_run(data.get('work_performed', ''))
    work_text.font.size = Pt(11)
    work_para.paragraph_format.line_spacing = 1.5
    work_para.paragraph_format.space_after = Pt(12)
    
    # FINDINGS AND OBSERVATIONS SECTION
    findings_heading = doc.add_heading('4. FINDINGS AND OBSERVATIONS', level=1)
    style_heading(findings_heading, level=1)
    
    findings_para = doc.add_paragraph()
    findings_text = findings_para.add_run(data.get('findings', ''))
    findings_text.font.size = Pt(11)
    findings_para.paragraph_format.line_spacing = 1.5
    findings_para.paragraph_format.space_after = Pt(12)
    
    # RECOMMENDATIONS SECTION
    if data.get('recommendations'):
        rec_heading = doc.add_heading('5. RECOMMENDATIONS', level=1)
        style_heading(rec_heading, level=1)
        
        rec_para = doc.add_paragraph()
        rec_text = rec_para.add_run(data.get('recommendations', ''))
        rec_text.font.size = Pt(11)
        rec_para.paragraph_format.line_spacing = 1.5
        rec_para.paragraph_format.space_after = Pt(12)
    
    # SERVICE INFORMATION SECTION
    service_heading = doc.add_heading('6. SERVICE INFORMATION', level=1)
    style_heading(service_heading, level=1)
    
    service_info = [
        ("Technician Name", data.get('technician_name', '')),
        ("Technician ID", data.get('technician_id', '')),
        ("Service Date", data.get('service_date', datetime.now().strftime('%B %d, %Y')))
    ]
    
    create_info_table(doc, service_info, col_widths=[2.5, 4])
    
    # Add page break before signatures
    doc.add_page_break()
    
    # SIGNATURE SECTION
    sig_heading = doc.add_heading('ACKNOWLEDGMENT AND SIGNATURES', level=1)
    style_heading(sig_heading, level=1)
    
    # Add acknowledgment text
    ack_para = doc.add_paragraph()
    ack_text = ack_para.add_run(
        "The undersigned acknowledge that the service described in this report has been "
        "completed satisfactorily and in accordance with the agreed specifications."
    )
    ack_text.font.size = Pt(10)
    ack_text.font.italic = True
    ack_para.paragraph_format.space_after = Pt(24)
    
    # Create signature table
    sig_table = doc.add_table(rows=4, cols=2)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Configure signature columns
    for col in sig_table.columns:
        for cell in col.cells:
            cell.width = Inches(3)
    
    # Technician signature
    sig_table.cell(0, 0).text = "Service Technician:"
    
    # Add signature image if available
    if data.get('technician_signature'):
        sig_cell = sig_table.cell(1, 0)
        sig_para = sig_cell.paragraphs[0]
        sig_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = sig_para.add_run()
        run.add_picture(data.get('technician_signature'), width=Inches(1.5))
    else:
        sig_table.cell(1, 0).text = "_" * 35
    
    sig_table.cell(2, 0).text = data.get('technician_name', '')
    sig_table.cell(3, 0).text = f"Date: {datetime.now().strftime('%B %d, %Y')}"
    
    # Customer signature
    sig_table.cell(0, 1).text = "Customer Representative:"
    sig_table.cell(1, 1).text = "_" * 35
    sig_table.cell(2, 1).text = "Name: _________________________"
    sig_table.cell(3, 1).text = "Date: _________________________"
    
    # Style signature table
    for row in sig_table.rows:
        for cell in row.cells:
            cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in cell.paragraphs[0].runs:
                run.font.size = Pt(11)
            set_cell_margins(cell, top=0.1, bottom=0.1)
    
    # Make labels bold
    sig_table.cell(0, 0).paragraphs[0].runs[0].font.bold = True
    sig_table.cell(0, 1).paragraphs[0].runs[0].font.bold = True
    
    # Add final note
    doc.add_paragraph()
    note_para = doc.add_paragraph()
    note_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    note_text = note_para.add_run(
        "This report is confidential and proprietary to Halton Foodservice KSA.\n"
        "For service inquiries, please contact our Service Department."
    )
    note_text.font.size = Pt(9)
    note_text.font.color.rgb = RGBColor(128, 128, 128)
    
    # Save to bytes
    doc_bytes = io.BytesIO()
    doc.save(doc_bytes)
    doc_bytes.seek(0)
    
    return doc_bytes

def main():
    # Header
    st.markdown('<h1 class="main-header">Halton KSA Service Reports</h1>', unsafe_allow_html=True)
    
    # Sidebar for report type selection
    with st.sidebar:
        st.markdown("### Report Type Selection")
        report_type = st.selectbox(
            "Select Report Type",
            ["Technical Report", "Testing and Commissioning Report (Coming Soon)", "General Service Report (Coming Soon)"],
            index=0
        )
        
        if report_type != "Technical Report":
            st.info("This report type will be available in future versions.")
            st.stop()
    
    # Main form for Technical Report
    st.markdown('<h2 class="section-header">Technical Report Form</h2>', unsafe_allow_html=True)
    
    with st.form("technical_report_form"):
        # General Information Section
        st.markdown("### General Information")
        col1, col2 = st.columns(2)
        
        with col1:
            customer_name = st.text_input("Customer's Name*", placeholder="e.g., SELA Company")
            project_name = st.text_input("Project Name*", placeholder="e.g., Stella kitchen hoods")
            contact_person = st.text_input("Contact Person*", placeholder="e.g., Sultan Alofi")
            outlet_location = st.text_input("Outlet/Location*", placeholder="e.g., Via - Riyadh")
        
        with col2:
            contact_number = st.text_input("Contact #*", placeholder="e.g., +966 55 558 5449")
            visit_type = st.text_input("Visit Type*", placeholder="e.g., Servicing/Preventive Maintenance")
            visit_class = st.selectbox(
                "Visit Class*",
                ["To be invoiced (Chargeable)", "Warranty", "Complaint", "Scheduled Maintenance", "Emergency Service"]
            )
            date = st.date_input("Report Date", value=datetime.now())
        
        # Equipment Details Section
        st.markdown("### Equipment Details")
        equipment_details = st.text_area(
            "Equipment Details and Description*",
            placeholder="Enter equipment model, serial number, and any relevant details...",
            height=100
        )
        
        # Work Performed Section
        st.markdown("### Work Performed")
        work_performed = st.text_area(
            "Describe Work Performed*",
            placeholder="Detail all maintenance, repairs, or services completed...",
            height=150
        )
        
        # Findings Section
        st.markdown("### Findings and Observations")
        findings = st.text_area(
            "Findings and Observations*",
            placeholder="Document any issues found, equipment condition, etc...",
            height=150
        )
        
        # Recommendations Section
        st.markdown("### Recommendations")
        recommendations = st.text_area(
            "Recommendations",
            placeholder="Suggest any follow-up actions, parts needed, or future maintenance...",
            height=100
        )
        
        # Technician Information Section
        st.markdown("### Technician Information")
        col3, col4 = st.columns(2)
        
        with col3:
            technician_name = st.text_input("Technician Name*", placeholder="Enter your full name")
            technician_id = st.text_input("Technician ID*", placeholder="Enter your employee ID")
        
        with col4:
            service_date = st.date_input("Service Date", value=datetime.now())
        
        # Signature Section
        st.markdown("### Technician Signature")
        
        # Initialize signature variables
        signature_file = None
        signature_img = None
        
        # Create tabs for signature options
        sig_tab1, sig_tab2 = st.tabs(["Draw Signature", "Upload Signature"])
        
        with sig_tab1:
            st.markdown("Draw your signature below:")
            
            # Create columns for canvas and controls
            canvas_col, control_col = st.columns([3, 1])
            
            with control_col:
                # Clear button outside the form
                if 'clear_canvas' not in st.session_state:
                    st.session_state.clear_canvas = False
                    
                clear_clicked = st.button("Clear", key="clear_btn")
                if clear_clicked:
                    st.session_state.clear_canvas = not st.session_state.clear_canvas
            
            with canvas_col:
                # Create the signature canvas
                canvas_result = st_canvas(
                    fill_color="rgba(255, 255, 255, 0)",
                    stroke_width=3,
                    stroke_color="#000000",
                    background_color="#FFFFFF",
                    height=150,
                    width=400,
                    drawing_mode="freedraw",
                    key=f"sig_canvas_{st.session_state.get('clear_canvas', False)}",
                )
                
                # Store canvas data in session state
                if canvas_result.image_data is not None:
                    st.session_state.signature_canvas = canvas_result.image_data
                    # Check if canvas has any drawing
                    if np.any(canvas_result.image_data[:,:,3] > 0):
                        st.success("✅ Signature captured")
        
        with sig_tab2:
            st.markdown("Upload a signature image file")
            signature_file = st.file_uploader(
                "Choose signature image",
                type=['png', 'jpg', 'jpeg'],
                help="Upload a signature image created on your device",
                key="sig_upload"
            )
            
            if signature_file:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(signature_file, width=200, caption="Your signature")
                with col2:
                    st.info("✅ Signature uploaded successfully")
        
        # Submit button
        submitted = st.form_submit_button("Generate Report", type="primary")
        
        if submitted:
            # Validation
            required_fields = {
                "Customer's Name": customer_name,
                "Project Name": project_name,
                "Contact Person": contact_person,
                "Outlet/Location": outlet_location,
                "Contact Number": contact_number,
                "Visit Type": visit_type,
                "Equipment Details": equipment_details,
                "Work Performed": work_performed,
                "Findings": findings,
                "Technician Name": technician_name,
                "Technician ID": technician_id
            }
            
            missing_fields = [field for field, value in required_fields.items() if not value]
            
            if missing_fields:
                st.error(f"Please fill in the following required fields: {', '.join(missing_fields)}")
            else:
                # Process signature
                signature_img = None
                
                # Check for drawn signature first
                if hasattr(st.session_state, 'signature_canvas') and np.any(st.session_state.signature_canvas[:,:,3] > 0):
                    # Convert canvas data to PIL Image
                    canvas_img = Image.fromarray(st.session_state.signature_canvas.astype('uint8'), 'RGBA')
                    # Convert to RGB (remove alpha channel)
                    rgb_img = Image.new('RGB', canvas_img.size, (255, 255, 255))
                    rgb_img.paste(canvas_img, mask=canvas_img.split()[3])
                    # Convert to bytes
                    img_byte_arr = io.BytesIO()
                    rgb_img.save(img_byte_arr, format='PNG')
                    signature_img = img_byte_arr.getvalue()
                # Otherwise check for uploaded signature
                elif signature_file is not None:
                    signature_img = process_uploaded_signature(signature_file)
                
                # Collect all data
                report_data = {
                    'customer_name': customer_name,
                    'project_name': project_name,
                    'contact_person': contact_person,
                    'outlet_location': outlet_location,
                    'contact_number': contact_number,
                    'visit_type': visit_type,
                    'visit_class': visit_class,
                    'date': date.strftime('%Y-%m-%d'),
                    'equipment_details': equipment_details,
                    'work_performed': work_performed,
                    'findings': findings,
                    'recommendations': recommendations,
                    'technician_name': technician_name,
                    'technician_id': technician_id,
                    'service_date': service_date.strftime('%Y-%m-%d'),
                    'technician_signature': signature_img
                }
                
                # Store data in session state for download outside form
                st.session_state.report_data = report_data
                st.session_state.report_generated = True
                st.session_state.customer_name = customer_name
                st.session_state.report_date = date
    
    # Handle report download outside of form
    if st.session_state.get('report_generated', False):
        try:
            # Generate the report
            doc_bytes = create_technical_report(st.session_state.report_data)
            
            # Create filename
            customer_name = st.session_state.customer_name
            date = st.session_state.report_date
            filename = f"Technical_Report_{customer_name.replace(' ', '_')}_{date.strftime('%Y%m%d')}.docx"
            
            # Success message
            st.success("✅ Report generated successfully!")
            
            # Download button (outside form)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.download_button(
                    label="📥 Download Report",
                    data=doc_bytes,
                    file_name=filename,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )
            
            # Option to generate another report
            if st.button("Generate Another Report", type="secondary"):
                st.session_state.report_generated = False
                st.rerun()
                
        except Exception as e:
            st.error(f"❌ Error generating report: {str(e)}")
            if st.button("Try Again"):
                st.session_state.report_generated = False
                st.rerun()

if __name__ == "__main__":
    main()