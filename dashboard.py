# Import necessary libraries for the dashboard
import streamlit as st  # Main framework for building the web dashboard
from datetime import date  # For handling date objects
import pandas as pd  # For data manipulation (if needed)
from formstructure import form_structure  # Contains the form structure definitions
from field_mapping import field_mapping  # Maps form fields to wizard data
from llm_dummy_data import llm_dummy_data  # Contains dummy data for testing

import hashlib  # For creating unique hash keys for form fields
from datetime import datetime  # For parsing datetime strings


def unique_field_key(section, question, widget_type):
    """
    Generate a unique key for each form field to avoid conflicts in Streamlit.
    
    Args:
        section (str): The section name the field belongs to
        question (str): The question/label text of the field
        widget_type (str): The type of widget (text, selectbox, etc.)
    
    Returns:
        str: A unique key combining section, hash of question, and widget type
    """
    # Create a short hash from the question text to ensure uniqueness
    q_hash = hashlib.md5(str(question).encode("utf-8")).hexdigest()[:8]
    return f"{section}_{q_hash}_{widget_type}"


def parse_date_safe(s):
    """
    Safely parse a date string, returning today's date if parsing fails.
    
    Args:
        s (str|date|None): Date string, date object, or None
    
    Returns:
        date: Parsed date or today's date as fallback
    """
    # Return today if input is empty or None
    if not s:
        return date.today()
    # Return as-is if already a date object
    if isinstance(s, date):
        return s
    try:
        # Try to parse as YYYY-MM-DD format
        return datetime.strptime(s, "%Y-%m-%d").date()
    except Exception:
        # Fallback to today's date if parsing fails
        return date.today()


def get_prefill_value(section, label):
    """
    Get the prefill value for a form field from the wizard session data.
    
    Args:
        section (str): The current section name
        label (str): The field label to look up
    
    Returns:
        str: The prefill value or empty string if not found
    """
    # Look up the field mapping to find corresponding wizard data
    mapping = field_mapping.get((section, label))
    if mapping:
        wizard_step, wizard_key = mapping
        # Handles nested user_data like st.session_state.user_data[wizard_step][wizard_key]
        # Check if the wizard step exists in session data
        if wizard_step in st.session_state.user_data:
            # Get the specific value from nested dictionary structure
            value = st.session_state.user_data[wizard_step].get(wizard_key, "")
            return value
    # Return empty string if no mapping found
    return ""


def safe_prefill(prefill_val, options, multiselect=False):
    """
    Ensures prefill values match available options for select/multiselect/radio widgets.
    This prevents errors when prefill data doesn't match current form options.
    
    Args:
        prefill_val: The value to prefill (string, list, or other)
        options (list): Available options for the widget
        multiselect (bool): Whether this is for a multiselect widget
    
    Returns:
        For multiselect: list of values present in options
        For single select: first matching value or fallback to first option
    """
    if multiselect:
        # Handle multiselect widgets
        # Accept both comma-separated string and list formats
        if isinstance(prefill_val, str):
            # Split comma-separated values and clean whitespace
            vals = [x.strip() for x in prefill_val.split(",") if x.strip()]
        elif isinstance(prefill_val, list):
            vals = prefill_val
        else:
            vals = []
        # Only keep values that exist in the available options
        return [v for v in vals if v in options]
    else:
        # Handle single-select widgets (selectbox, radio)
        if isinstance(prefill_val, list):
            # If prefill is a list, pick the first one that's in options
            for v in prefill_val:
                if v in options:
                    return v
            # If none match, return first option as fallback
            return options[0]
        # If prefill value exists in options, use it
        if prefill_val in options:
            return prefill_val
        # Otherwise fallback to first option (or empty if no options)
        return options[0] if options else ""


# Mapping dictionary to convert SDG goal codes to readable labels
GOAL_CODE_TO_LABEL = {
    "Goal 7": "Affordable and Clean Energy",  # update if your actual label differs
    "Goal 9": "Industry, Innovation and Infrastructure",
    "Goal 11": "Sustainable Cities and Communities",  # update if your actual label differs
    # Add more as needed...
}


def map_goal_codes(vals):
    """
    Convert SDG goal codes to human-readable labels.
    
    Args:
        vals: Single value or list of goal codes
    
    Returns:
        list: Mapped goal labels
    """
    # Ensure we're working with a list
    if isinstance(vals, str):
        vals = [vals]
    # Map each code to its label, keeping original if no mapping exists
    return [GOAL_CODE_TO_LABEL.get(v, v) for v in vals]


# Streamlit page configuration (commented out to avoid conflicts)
# st.set_page_config(page_title="Project Application Dashboard", layout="wide")


# Custom CSS styles for the dashboard interface
st.markdown(
    """
    <style>
        /* Sidebar navigation button styles */
        .sidebar-buttons button {
            width: 100%;
            padding: 10px;
            margin-bottom: 5px;
            font-size: 16px;
            background-color: #f0f2f6;
            border: none;
            border-left: 5px solid transparent;
            text-align: left;
            transition: all 0.2s ease-in-out;
        }
        /* Selected button highlighting */
        .sidebar-buttons button.selected {
            background-color: #dce6f9;
            border-left: 5px solid #1f77b4;
            font-weight: bold;
        }
        /* Copy icon styling for field copying functionality */
        .copy-icon {
            cursor: pointer;
            color: gray;
            float: right;
        }
        .copy-icon:hover {
            color: black;
        }
        
        


    </style>
""",
    unsafe_allow_html=True,
)


def dashboard_ui():
    """
    Main function that renders the dashboard UI with navigation and form sections.
    """
    # Create sidebar title for navigation
    st.sidebar.title("Sections")

    # Initialize session state for tracking selected section
    # This persists the user's current section across interactions
    if "selected_section" not in st.session_state:
        # Default to the first section in form_structure
        st.session_state.selected_section = list(form_structure.keys())[0]

    # Create navigation buttons in sidebar for each form section
    for section in form_structure.keys():
        # Each button updates the selected section when clicked
        if st.sidebar.button(section, key=section):
            st.session_state.selected_section = section

    # Display the main page title based on selected section
    st.title(f"{st.session_state.selected_section}")

    # Function to add copy icon next to field labels
    def with_copy_button(field_label, field_id):
        """
        Add a copy button next to field labels for easy copying of field values.
        
        Args:
            field_label (str): The label text to display
            field_id (str): The HTML ID of the field for copying functionality
        """
        # JavaScript-based copy functionality using clipboard API
        copy_button_html = f"""
            <span class="copy-icon" onclick="navigator.clipboard.writeText(document.getElementById('{field_id}').value || document.getElementById('{field_id}').innerText)">📋</span>
        """
        st.markdown(
            f"<label for='{field_id}'>{field_label} {copy_button_html}</label>",
            unsafe_allow_html=True,
        )

    # Main form rendering loop - iterate through all fields in current section
    for idx, field in enumerate(form_structure[st.session_state.selected_section]):
        # Handle section information display (informational content, not form fields)
        if "section_info" in field:
            st.info(field["section_info"])
            continue

        # Extract field properties from form structure
        label = field.get("question", "")  # Field label/question text
        input_type = field.get("type", "")  # Widget type (text, selectbox, etc.)
        info = field.get("info", "")  # Additional info/help text
        max_length = field.get("max_length", None)  # Character limit for text fields
        has_info = field.get("has_info", False)  # Whether field has expandable info
        options = field.get("options", [])  # Options for select/radio widgets
        section = st.session_state.selected_section  # Current section name

        # Generate unique keys for this field's widgets
        widget_key = unique_field_key(section, label, input_type)  # Main widget key
        exp_key = unique_field_key(section, label, "expand")  # Expandable info key

        # Fetch prefill value from wizard data if available
        prefill_val = get_prefill_value(section, label)

        # --- Info arrow logic: shows expandable info if available ---
        arrow_key = f"arrow_{exp_key}"  # Key for the expand/collapse arrow button
        exp_state = st.session_state.get(exp_key, False)  # Current expand state
        show_arrow = has_info and info  # Only show arrow if info exists

        # Determine if label should be shown above widget
        # Some widgets (radio, selectbox) handle their own labels
        show_label = input_type not in [
            "radio",
            "checkbox", 
            "selectbox",
            "multiselect",
            "fileuploader",
        ]

        # Render info arrow and label section
        if show_arrow:
            # Create two columns: label and arrow button
            col1, col2 = st.columns([20, 1])
            with col1:
                # Show label if appropriate
                if show_label and label:
                    st.markdown(f"**{label}**")
            with col2:
                # Toggle arrow direction based on expand state
                arrow = "▼" if not exp_state else "▲"
                # Arrow button toggles the expand state
                if st.button(arrow, key=arrow_key):
                    st.session_state[exp_key] = not exp_state
                    st.rerun()  # Refresh to show/hide info
            # Show info content if expanded
            if st.session_state.get(exp_key, False):
                st.info(info)
        elif show_label and label:
            # Show label without arrow if no expandable info
            st.markdown(f"**{label}**")

        # ------------- Render different widget types with prefill values ---------------
        
        if input_type == "text":
            # Text input field with character limit support
            value = st.text_input(
                "",  # Empty label since we handle it above
                key=widget_key,
                value=prefill_val if prefill_val else "",  # Use prefill or empty string
                label_visibility="collapsed",  # Hide default label
                max_chars=max_length if max_length else None,  # Apply character limit
            )
            # Show character count if limit is set
            if max_length:
                st.caption(f"Characters: {len(value)}/{max_length}")
                # Show error if limit exceeded
                if len(value) > max_length:
                    st.error("Character limit exceeded!")
                    
        elif input_type == "textarea":
            # Multi-line text area with character limit support
            value = st.text_area(
                "",  # Empty label since we handle it above
                key=widget_key,
                value=prefill_val if prefill_val else "",  # Use prefill or empty string
                label_visibility="collapsed",  # Hide default label
                max_chars=max_length if max_length else None,  # Apply character limit
            )
            # Show character count if limit is set
            if max_length:
                st.caption(f"Characters: {len(value)}/{max_length}")
                # Show error if limit exceeded
                if len(value) > max_length:
                    st.error("Character limit exceeded!")
                    
        elif input_type == "number":
            # Number input with safe parsing of prefill value
            try:
                # Try to convert prefill to integer
                default_num = int(prefill_val) if prefill_val else 0
            except Exception:
                # Fallback to 0 if conversion fails
                default_num = 0
            value = st.number_input(
                label if show_label else "",  # Show label for number inputs
                min_value=0,  # Minimum value constraint
                key=widget_key,
                value=default_num,  # Use parsed prefill value
            )
            
        elif input_type == "date":
            # Date picker with safe date parsing
            value = st.date_input(
                label if show_label else "",  # Show label for date inputs
                value=parse_date_safe(prefill_val),  # Use safe date parser
                key=widget_key,
            )
            
        elif input_type == "checkbox":
            # Checkbox with flexible boolean value handling
            # Accept both bool and "yes"/"no" string formats
            if isinstance(prefill_val, bool):
                checked = prefill_val
            elif isinstance(prefill_val, str):
                # Convert various string representations to boolean
                checked = prefill_val.lower() in ("yes", "true", "1")
            else:
                checked = False  # Default to unchecked
            value = st.checkbox(label, key=widget_key, value=checked)
            
        elif input_type == "selectbox":
            # Single-select dropdown with prefill support
            prefill_val = prefill_val or ""  # Ensure not None
            
            # Special handling for SDG goals mapping
            if (
                label
                == "Which of the global goals in Agenda 2030 is the project expected to contribute to in the region in the long term?"
            ):
                # Convert goal codes to readable labels
                prefill_val = map_goal_codes(prefill_val)
                
            # Ensure prefill value matches available options
            default_option = safe_prefill(prefill_val, options)
            value = st.selectbox(
                label, 
                options, 
                key=widget_key, 
                index=options.index(default_option)  # Set default selection
            )
            
        elif input_type == "multiselect":
            # Multi-select widget with list prefill support
            default_vals = safe_prefill(prefill_val, options, multiselect=True)
            value = st.multiselect(label, options, default=default_vals, key=widget_key)
            
        elif input_type == "radio":
            # Radio button group with prefill support
            default_option = safe_prefill(prefill_val, options)
            value = st.radio(
                label, 
                options, 
                key=widget_key, 
                index=options.index(default_option)  # Set default selection
            )
            
        elif input_type == "file_uploader":
            # File upload widget
            value = st.file_uploader(label, key=widget_key)
            
        elif input_type == "button":
            # Simple button widget
            st.button(label, key=widget_key)
            
        elif input_type == "info":
            # Information display (not an input)
            st.info(label)

    # Initialize contacts table in session state if not exists
    # This persists contact data across page interactions
    if "contacts_table" not in st.session_state:
        # Default sample contact data
        st.session_state.contacts_table = [
            {
                "Name": "Anna Andersson",
                "Role": "Project Manager",
                "Organization": "Tech AB",
                "Phone number": "012-3456789",
                "Mobile number": "070-1234567",
                "Email address": "anna@techab.se",
                "project bank": "SE12 3456 7890 1234 5678 9012",
            }
        ]

    # Special handling for "Project Owner" section
    if st.session_state.selected_section == "Project Owner":
        # Define sample workplace data (could be fetched from database)
        workplaces = [
            {
                "workplace_no": "19064104",
                "name": "Linnaeus University Växjö",
                "visiting_address": "University Square 1",
                "postal_code": "35252",
                "city": "Växjö",
                "industry_code": "85420",
            },
            {
                "workplace_no": "43699958",
                "name": "Linnaeus University Kalmar",
                "visiting_address": "University Square 1",
                "postal_code": "39231",
                "city": "Kalmar",
                "industry_code": "85420",
            },
        ]

        # Initialize selected workplace index if not set
        # This ensures we always have a valid selection
        if "selected_workplace_idx" not in st.session_state:
            st.session_state.selected_workplace_idx = 0

        # Workplace selection interface
        st.markdown("#### Workplaces")
        st.caption("Select the workplace most affected")

        # Radio button selection for workplaces
        # format_func creates readable labels for each option
        selected_idx = st.radio(
            "",
            options=list(range(len(workplaces))),  # Use indices as values
            format_func=lambda i: f"{workplaces[i]['workplace_no']} — {workplaces[i]['name']}",
            key="selected_workplace_idx",
        )

        # Display information about selected workplace
        # Note: Fix the potential None issue by ensuring selected_idx is valid
        if selected_idx is not None and selected_idx < len(workplaces):
            st.info(f"Selected: {workplaces[selected_idx]['name']}")
        else:
            st.warning("No workplace selected")

    # Special handling for "Project Partner" section
    if st.session_state.selected_section == "Project Partner":
        # Initialize partners list in session state if not exists
        if "partners" not in st.session_state:
            st.session_state.partners = []

        # Button to add new project partners
        if st.button("+ Add project partner"):
            # Add empty partner dictionary to the list
            st.session_state.partners.append({})

        # Render form fields for each partner
        for i, partner in enumerate(st.session_state.partners):
            st.markdown(f"### Projektpartner {i+1}")

            # Partner company information fields
            st.text_input("Company name", key=f"partner_{i}_company")
            st.text_input("Organization number", key=f"partner_{i}_orgnum")
            st.text_input("Address", key=f"partner_{i}_address")
            st.text_input("Momsregistreringsnummer (valfritt)", key=f"partner_{i}_vat")
            
            # Radio button for procurement law compliance
            st.radio(
                "Omfattas organisationen av lagen om offentlig upphandling eller annan upphandlingslagsstiftning?",
                ["Ja", "Nej"],
                key=f"partner_{i}_upphandling",
            )
            
            # Signatory information
            st.text_input(
                "Ange vem som är organisationens firmatecknare?",
                key=f"partner_{i}_firmatecknare",
            )
            
            # VAT budget question
            st.radio(
                "Har ni tagit upp moms som en kostnad när ni beräkna er budget?",
                ["Ja", "Nej"],
                key=f"partner_{i}_momsbudget",
            )
            
            # Visual separator between partners
            st.markdown("---")

    # Special handling for "Activities" section
    if st.session_state.selected_section == "Activities":
        # Retrieve work packages from wizard data if available
        work_packages = []
        mapping = field_mapping.get(("Activities", "Name of work package"))
        if mapping:
            wizard_step, wizard_key = mapping
            # Extract work packages from nested session data
            work_packages = st.session_state.user_data.get(wizard_step, {}).get(
                wizard_key, []
            )

        # Initialize activities in session state if not exists
        if "activities" not in st.session_state:
            st.session_state.activities = []
            # Prefill activities from work packages data (only on first load)
            for wp in work_packages:
                st.session_state.activities.append(
                    {
                        # Map work package data to activity structure
                        "work_package": wp.get("name", ""),
                        "description_goal": wp.get("description", ""),
                        "start": parse_date_safe(wp.get("start_date", "")),  # Safe date parsing
                        "end": parse_date_safe(wp.get("end_date", "")),  # Safe date parsing
                        "name": wp.get("activity_name", ""),
                        "cost": wp.get("cost", 0),
                        "desc": wp.get("activity_description", ""),
                        "impact": wp.get("impact_to_global_goals", ""),
                    }
                )

        # Render activity forms with prefilled data
        for i, activity in enumerate(st.session_state.activities):
            st.markdown(f"### Activity {i+1}")
            
            # Work package name field
            st.text_input(
                "Name of work package",
                key=f"activity_{i}_work_package",
                value=activity["work_package"],  # Prefill from activity data
            )
            
            # Work package description field
            st.text_area(
                "Description how the work package contributes to the project goal",
                key=f"activity_{i}_description_goal",
                value=activity["description_goal"],  # Prefill from activity data
            )
            
            # Activity date range fields
            st.date_input(
                "Start date", 
                value=activity["start"],  # Prefill parsed date
                key=f"activity_{i}_start"
            )
            st.date_input(
                "End date", 
                value=activity["end"],  # Prefill parsed date
                key=f"activity_{i}_end"
            )
            
            # Activity details fields
            st.text_input(
                "Name of activity", 
                key=f"activity_{i}_name", 
                value=activity["name"]  # Prefill from activity data
            )
            st.number_input(
                "cost", 
                min_value=0, 
                key=f"activity_{i}_cost", 
                value=activity["cost"]  # Prefill numeric value
            )
            st.text_area(
                "Description of activity",
                key=f"activity_{i}_desc",
                value=activity["desc"],  # Prefill from activity data
            )
            st.text_area(
                "how will your work packages impact to global goals",
                key=f"activity_{i}_impact",
                value=activity["impact"],  # Prefill from activity data
            )
            
            # Visual separator between activities
            st.markdown("---")

    # Special handling for "Contacts" section
    if st.session_state.selected_section == "Contacts":

        st.markdown("### Contact List")

        # Define table headers for contact display
        headers = [
            "Name",
            "Role", 
            "Organization",
            "Phone number",
            "Mobile number",
            "Email address",
            "project bank",
            "",  # Edit button column
            "",  # Delete button column
        ]
        
        # Create empty line for spacing
        st.columns(len(headers))

        # Render table header row with bold formatting
        cols = st.columns([2, 2, 2, 2, 2, 3, 2, 1, 1])
        for col, header in zip(cols, headers):
            col.markdown(f"**{header}**")

        # Render each contact as a table row
        for idx, contact in enumerate(st.session_state.contacts_table):
            cols = st.columns([2, 2, 2, 2, 2, 3, 2, 1, 1])
            
            # Display contact information in columns
            cols[0].write(contact["Name"])
            cols[1].write(contact["Role"])
            cols[2].write(contact["Organization"])
            cols[3].write(contact["Phone number"])
            cols[4].write(contact["Mobile number"])
            cols[5].write(contact["Email address"])
            cols[6].write(contact["project bank"])
            
            # Edit button (functionality not implemented yet)
            if cols[7].button("✏️", key=f"edit_contact_{idx}"):
                st.warning(f"Edit mode not implemented for {contact['Name']}")
                
            # Delete button with immediate removal and page refresh
            if cols[8].button("🗑️", key=f"delete_contact_{idx}"):
                st.session_state.contacts_table.pop(idx)  # Remove contact from list
                st.rerun()  # Refresh page to show updated list

        # Add new contact form section
        st.markdown("### Add New Contact")
        st.markdown("---")  # Visual separator
        
        # Form for adding new contacts
        with st.form("add_contact_form", clear_on_submit=True):
            # Create three columns for organized input layout
            col1, col2, col3 = st.columns(3)
            
            # First column: basic info
            with col1:
                name = st.text_input("Name")
                role = st.text_input("Role")
                org = st.text_input("Organization")
                
            # Second column: contact info
            with col2:
                phone = st.text_input("Phone number")
                mobile = st.text_input("Mobile number")
                email = st.text_input("Email address")
                
            # Third column: banking info
            with col3:
                bank = st.text_input("project bank")

            # Form submit button
            submitted = st.form_submit_button("➕ Add Contact")

            # Handle form submission
            if submitted:
                # Add new contact to session state
                st.session_state.contacts_table.append(
                    {
                        "Name": name,
                        "Role": role,
                        "Organization": org,
                        "Phone number": phone,
                        "Mobile number": mobile,
                        "Email address": email,
                        "project bank": bank,
                    }
                )
                st.success("Contact added successfully!")
                st.rerun()  # Refresh to show new contact in list

    # JavaScript injection for copy functionality styling
    # This ensures copy icons are properly sized in the rendered HTML
    st.markdown(
        """
        <script>
            // Find all copy icons in the document and set their font size
            const icons = window.parent.document.querySelectorAll(".copy-icon");
            icons.forEach(el => el.style.fontSize = "16px");
        </script>
    """,
        unsafe_allow_html=True,
    )


