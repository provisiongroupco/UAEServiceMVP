"""
Equipment inspection component for Service Reports
Handles dynamic equipment forms and inspection workflows
"""

import streamlit as st
from datetime import datetime
import io
from PIL import Image
from equipment_config import (
    EQUIPMENT_TYPES, UVF_MODULE_CHECKLIST, PPM_CHECKLIST, 
    UV_PPM_ITEMS, WATER_WASH_PPM_ITEMS, ECOLOGY_PPM_ITEMS
)


class EquipmentInspection:
    def __init__(self):
        # Initialize session state for kitchen-based equipment structure
        # Handle both attribute access and dictionary access for testing compatibility
        self._init_session_state_item('kitchen_list', [])
        self._init_session_state_item('equipment_list', [])
        self._init_session_state_item('current_equipment_index', 0)
        self._init_session_state_item('inspection_data', {})
    
    def _init_session_state_item(self, key, default_value):
        """Initialize a session state item safely for both dict and attribute access"""
        if hasattr(st.session_state, key):
            # Already exists
            return
        elif key not in st.session_state:
            # Initialize using dict access (works for both dict and attribute access)
            st.session_state[key] = default_value
    
    def render_equipment_section(self):
        """Render the main equipment inspection section"""
        st.markdown("### Equipment Inspection")
        
        # Equipment management buttons
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            equipment_type = st.selectbox(
                "Select Equipment Type",
                options=list(EQUIPMENT_TYPES.keys()),
                format_func=lambda x: EQUIPMENT_TYPES[x]["name"],
                key="new_equipment_type"
            )
        
        with col2:
            if st.button("➕ Add Equipment", type="secondary"):
                self.add_equipment(equipment_type)
        
        with col3:
            if st.session_state.get('equipment_list', []) and st.button("🗑️ Remove Last", type="secondary"):
                self.remove_last_equipment()
        
        # Display equipment list
        if st.session_state.get('equipment_list', []):
            st.markdown("#### Equipment Added:")
            for idx, equip in enumerate(st.session_state.get('equipment_list', [])):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.text(f"{idx + 1}. {EQUIPMENT_TYPES[equip['type']]['name']} - {equip['serial_number']}")
                with col2:
                    if st.button(f"Edit", key=f"edit_equip_{idx}"):
                        st.session_state['current_equipment_index'] = idx
            
            # Render current equipment inspection form
            if st.session_state.get('current_equipment_index', 0) < len(st.session_state.get('equipment_list', [])):
                self.render_equipment_form(st.session_state.get('current_equipment_index', 0))
        else:
            st.info("No equipment added yet. Click 'Add Equipment' to start.")
    
    def add_equipment(self, equipment_type):
        """Add a new equipment to the inspection list"""
        equipment_id = f"{equipment_type}_{len(st.session_state.get('equipment_list', []))}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        new_equipment = {
            'id': equipment_id,
            'type': equipment_type,
            'serial_number': '',
            'location': '',
            'inspection_data': {},
            'photos': {}
        }
        
        if 'equipment_list' not in st.session_state:
            st.session_state['equipment_list'] = []
        st.session_state['equipment_list'].append(new_equipment)
        st.session_state['current_equipment_index'] = len(st.session_state.get('equipment_list', [])) - 1
        st.success(f"Added {EQUIPMENT_TYPES[equipment_type]['name']} to inspection list")
    
    def remove_last_equipment(self):
        """Remove the last equipment from the list"""
        if st.session_state.get('equipment_list', []):
            removed = st.session_state['equipment_list'].pop()
            st.success(f"Removed {EQUIPMENT_TYPES[removed['type']]['name']}")
            if st.session_state.get('current_equipment_index', 0) >= len(st.session_state.get('equipment_list', [])):
                st.session_state['current_equipment_index'] = max(0, len(st.session_state.get('equipment_list', [])) - 1)
    
    def render_equipment_form(self, index):
        """Render the inspection form for a specific equipment"""
        equipment = st.session_state.get('equipment_list', [])[index]
        equipment_type = equipment['type']
        equipment_config = EQUIPMENT_TYPES[equipment_type]
        
        st.markdown(f"#### Inspecting: {equipment_config['name']} #{index + 1}")
        
        # Basic equipment information
        col1, col2 = st.columns(2)
        with col1:
            equipment['serial_number'] = st.text_input(
                "Serial Number/ID*",
                value=equipment.get('serial_number', ''),
                key=f"serial_{equipment['id']}"
            )
        with col2:
            equipment['location'] = st.text_input(
                "Location*",
                value=equipment.get('location', ''),
                key=f"location_{equipment['id']}"
            )
        
        # For UVF, check if modules need to be handled
        if equipment_type == "UVF":
            self.handle_uvf_modules(equipment)
        
        # Render checklist
        st.markdown("##### Inspection Checklist")
        self.render_checklist(equipment, equipment_config['checklist'])
        
        # If this is an AMC visit, show PPM checklist
        if st.session_state.get('visit_type') == 'AMC (Contract)':
            st.markdown("##### Preventive Maintenance Checklist")
            self.render_ppm_checklist(equipment)
    
    def handle_uvf_modules(self, equipment):
        """Handle UVF module-specific inspections"""
        # Check if module count has been answered
        module_count_data = equipment['inspection_data'].get('module_count')
        if module_count_data and isinstance(module_count_data.get('answer'), int):
            module_count = module_count_data['answer']
            
            st.markdown(f"##### Module Inspections ({module_count} modules)")
            
            # Create tabs for each module
            if module_count > 0:
                module_tabs = st.tabs([f"Module {i+1}" for i in range(module_count)])
                
                for i, tab in enumerate(module_tabs):
                    with tab:
                        module_key = f"module_{i}"
                        if module_key not in equipment['inspection_data']:
                            equipment['inspection_data'][module_key] = {}
                        
                        self.render_checklist(
                            equipment, 
                            UVF_MODULE_CHECKLIST, 
                            prefix=f"module_{i}_"
                        )
    
    def render_checklist(self, equipment, checklist, prefix=""):
        """Render a checklist with conditional logic"""
        for item in checklist:
            item_key = prefix + item['id']
            
            # Check if this item should be shown based on parent conditions
            if not self.should_show_item(equipment, item, prefix):
                continue
            
            # Get or create item data
            if item_key not in equipment['inspection_data']:
                equipment['inspection_data'][item_key] = {}
            
            item_data = equipment['inspection_data'][item_key]
            
            # Render the question based on type
            self.render_question(equipment, item, item_key, item_data)
            
            # Handle follow-up questions if answer exists
            answer = item_data.get('answer')
            if answer and 'conditions' in item:
                condition = item['conditions'].get(str(answer).lower())
                if condition:
                    # Handle photo requirement
                    if condition.get('photo'):
                        self.render_photo_upload(equipment, item_key, item['question'])
                    
                    # Handle comment requirement
                    if condition.get('comment'):
                        item_data['comment'] = st.text_area(
                            f"Comments for: {item['question']}",
                            value=item_data.get('comment', ''),
                            key=f"comment_{item_key}_{equipment['id']}"
                        )
                    
                    # Handle action instruction
                    if condition.get('action'):
                        st.warning(condition['action'])
                    
                    # Handle follow-up questions
                    if condition.get('follow_up'):
                        self.render_checklist(equipment, condition['follow_up'], prefix)
    
    def should_show_item(self, equipment, item, prefix):
        """Check if an item should be shown based on conditions"""
        # Always show top-level items
        return True
    
    def render_question(self, equipment, item, item_key, item_data):
        """Render a single question based on its type"""
        question = item['question']
        question_type = item['type']
        
        if question_type == 'yes_no':
            options = ['', 'Yes', 'No']
            current_answer = item_data.get('answer', '')
            
            item_data['answer'] = st.selectbox(
                question,
                options=options,
                index=options.index(current_answer) if current_answer in options else 0,
                key=f"q_{item_key}_{equipment['id']}"
            )
        
        elif question_type == 'yes_no_na':
            options = ['', 'Yes', 'No', 'N/A']
            current_answer = item_data.get('answer', '')
            
            item_data['answer'] = st.selectbox(
                question,
                options=options,
                index=options.index(current_answer) if current_answer in options else 0,
                key=f"q_{item_key}_{equipment['id']}"
            )
        
        elif question_type == 'text':
            item_data['answer'] = st.text_input(
                question,
                value=item_data.get('answer', ''),
                key=f"q_{item_key}_{equipment['id']}"
            )
        
        elif question_type == 'number':
            item_data['answer'] = st.number_input(
                question,
                min_value=0,
                value=item_data.get('answer', 0),
                step=1,
                key=f"q_{item_key}_{equipment['id']}"
            )
        
        elif question_type == 'select':
            options = [''] + item.get('options', [])
            current_answer = item_data.get('answer', '')
            
            item_data['answer'] = st.selectbox(
                question,
                options=options,
                index=options.index(current_answer) if current_answer in options else 0,
                key=f"q_{item_key}_{equipment['id']}"
            )
        
        elif question_type == 'multi_select':
            item_data['answer'] = st.multiselect(
                question,
                options=item.get('options', []),
                default=item_data.get('answer', []),
                key=f"q_{item_key}_{equipment['id']}"
            )
            
            # Handle follow-up questions per selected option
            if 'follow_up_per_option' in item and item_data['answer']:
                for selected_option in item_data['answer']:
                    if selected_option in item['follow_up_per_option']:
                        st.markdown(f"**{selected_option}:**")
                        follow_up_prefix = f"{item_key}_{selected_option.replace(' ', '_')}_"
                        self.render_checklist(
                            equipment,
                            item['follow_up_per_option'][selected_option],
                            follow_up_prefix
                        )
        
        elif question_type == 'photo':
            self.render_photo_upload(equipment, item_key, question)
    
    def render_photo_upload(self, equipment, item_key, label):
        """Render photo upload widget"""
        photo_key = f"photo_{item_key}"
        
        uploaded_file = st.file_uploader(
            f"📷 {label}",
            type=['png', 'jpg', 'jpeg'],
            key=f"photo_{item_key}_{equipment['id']}"
        )
        
        if uploaded_file:
            # Store the photo
            if 'photos' not in equipment:
                equipment['photos'] = {}
            
            equipment['photos'][photo_key] = uploaded_file
            
            # Display thumbnail
            col1, col2 = st.columns([1, 3])
            with col1:
                image = Image.open(uploaded_file)
                st.image(image, width=100)
            with col2:
                st.success(f"Photo uploaded for: {label}")
    
    def render_ppm_checklist(self, equipment):
        """Render PPM checklist for AMC visits"""
        equipment_type = equipment['type']
        
        # Basic PPM items
        ppm_checklist = PPM_CHECKLIST.copy()
        
        # Add equipment-specific PPM items
        if equipment_type in ['UVF'] and equipment['inspection_data'].get('module_count', {}).get('answer', 0) > 0:
            ppm_checklist = UV_PPM_ITEMS + ppm_checklist
        
        if equipment_type == 'CMW' and equipment['inspection_data'].get('cold_mist_system', {}).get('answer') == 'Yes':
            ppm_checklist = WATER_WASH_PPM_ITEMS + ppm_checklist
        
        if equipment_type == 'ECOLOGY':
            ppm_checklist = ppm_checklist + ECOLOGY_PPM_ITEMS
        
        # Render the PPM checklist
        self.render_checklist(equipment, ppm_checklist, prefix="ppm_")
        
        # Handle before/after photos
        photo_count = equipment['inspection_data'].get('ppm_before_after_photos_count', {}).get('answer', 0)
        if photo_count > 0:
            st.markdown("##### Before and After Photos")
            for i in range(int(photo_count)):
                col1, col2 = st.columns(2)
                with col1:
                    self.render_photo_upload(equipment, f"before_photo_{i}", f"Before Photo {i+1}")
                with col2:
                    self.render_photo_upload(equipment, f"after_photo_{i}", f"After Photo {i+1}")
                
                # Description for this photo pair
                equipment['inspection_data'][f'photo_pair_{i}_description'] = st.text_area(
                    f"Description for Photo Pair {i+1}",
                    value=equipment['inspection_data'].get(f'photo_pair_{i}_description', ''),
                    key=f"photo_desc_{i}_{equipment['id']}"
                )
    
    def get_inspection_summary(self):
        """Get a summary of all equipment inspections"""
        summary = []
        
        for equipment in st.session_state.get('equipment_list', []):
            equip_summary = {
                'type': equipment['type'],
                'type_name': EQUIPMENT_TYPES[equipment['type']]['name'],
                'serial_number': equipment.get('serial_number', ''),
                'location': equipment.get('location', ''),
                'issues_found': [],
                'photos_count': len(equipment.get('photos', {})),
                'inspection_data': equipment['inspection_data']
            }
            
            # Check for issues (any "No" answers or comments indicating problems)
            for key, data in equipment['inspection_data'].items():
                if isinstance(data, dict):
                    answer = data.get('answer', '')
                    if answer == 'No' or (answer and data.get('comment')):
                        equip_summary['issues_found'].append({
                            'item': key,
                            'answer': answer,
                            'comment': data.get('comment', '')
                        })
            
            summary.append(equip_summary)
        
        return summary
    
    def validate_equipment_data(self):
        """Validate that all required equipment data is filled"""
        errors = []
        
        for idx, equipment in enumerate(st.session_state.get('equipment_list', [])):
            equip_name = f"{EQUIPMENT_TYPES[equipment['type']]['name']} #{idx + 1}"
            
            if not equipment.get('serial_number'):
                errors.append(f"{equip_name}: Serial number is required")
            
            if not equipment.get('location'):
                errors.append(f"{equip_name}: Location is required")
            
            # Check for unanswered required questions
            checklist = EQUIPMENT_TYPES[equipment['type']]['checklist']
            for item in checklist:
                if item.get('required') and not equipment['inspection_data'].get(item['id'], {}).get('answer'):
                    errors.append(f"{equip_name}: '{item['question']}' is required")
        
        return errors


# Export the class
equipment_inspector = EquipmentInspection()