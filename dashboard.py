import streamlit as st
from datetime import date
import pandas as pd
from formstructure import form_structure
from field_mapping import field_mapping
from llm_dummy_data import llm_dummy_data

import hashlib
from datetime import datetime


def unique_field_key(section, question, widget_type):
    q_hash = hashlib.md5(str(question).encode("utf-8")).hexdigest()[:8]
    return f"{section}_{q_hash}_{widget_type}"


def parse_date_safe(s):
    if not s:
        return date.today()
    if isinstance(s, date):
        return s
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except Exception:
        return date.today()


def get_prefill_value(section, label):
    mapping = field_mapping.get((section, label))
    if mapping:
        wizard_step, wizard_key = mapping
        # Handles nested user_data like st.session_state.user_data[wizard_step][wizard_key]
        if wizard_step in st.session_state.user_data:
            value = st.session_state.user_data[wizard_step].get(wizard_key, "")
            return value
    return ""


def safe_prefill(prefill_val, options, multiselect=False):
    """
    Ensures prefill values match available options for select/multiselect/radio.
    - For selectbox/radio: returns first matching value or fallback to first option.
    - For multiselect: returns list of values present in options.
    """
    if multiselect:
        # Accept both comma-separated string and list
        if isinstance(prefill_val, str):
            vals = [x.strip() for x in prefill_val.split(",") if x.strip()]
        elif isinstance(prefill_val, list):
            vals = prefill_val
        else:
            vals = []
        # Only keep those in options
        return [v for v in vals if v in options]
    else:
        if isinstance(prefill_val, list):
            # Pick the first one that's in options
            for v in prefill_val:
                if v in options:
                    return v
            return options[0]
        if prefill_val in options:
            return prefill_val
        return options[0] if options else ""


GOAL_CODE_TO_LABEL = {
    "Goal 7": "Affordable and Clean Energy",  # update if your actual label differs
    "Goal 9": "Industry, Innovation and Infrastructure",
    "Goal 11": "Sustainable Cities and Communities",  # update if your actual label differs
    # Add more as needed...
}


def map_goal_codes(vals):
    if isinstance(vals, str):
        vals = [vals]
    return [GOAL_CODE_TO_LABEL.get(v, v) for v in vals]


# st.set_page_config(page_title="Project Application Dashboard", layout="wide")


st.markdown(
    """
    <style>
        /* Sidebar buttons as nav */
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
        .sidebar-buttons button.selected {
            background-color: #dce6f9;
            border-left: 5px solid #1f77b4;
            font-weight: bold;
        }
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
    st.sidebar.title("Sections")

    # Session state for navigation
    if "selected_section" not in st.session_state:
        st.session_state.selected_section = list(form_structure.keys())[0]

    for section in form_structure.keys():
        if st.sidebar.button(section, key=section):
            st.session_state.selected_section = section

    # Page content
    st.title(f"{st.session_state.selected_section}")

    # Function to add copy icon
    def with_copy_button(field_label, field_id):
        copy_button_html = f"""
            <span class="copy-icon" onclick="navigator.clipboard.writeText(document.getElementById('{field_id}').value || document.getElementById('{field_id}').innerText)">📋</span>
        """
        st.markdown(
            f"<label for='{field_id}'>{field_label} {copy_button_html}</label>",
            unsafe_allow_html=True,
        )

    for idx, field in enumerate(form_structure[st.session_state.selected_section]):
        # Section info display
        if "section_info" in field:
            st.info(field["section_info"])
            continue

        label = field.get("question", "")
        input_type = field.get("type", "")
        info = field.get("info", "")
        max_length = field.get("max_length", None)
        has_info = field.get("has_info", False)
        options = field.get("options", [])
        section = st.session_state.selected_section

        widget_key = unique_field_key(section, label, input_type)
        exp_key = unique_field_key(section, label, "expand")

        # Prefill value fetch!
        prefill_val = get_prefill_value(section, label)

        # --- Info arrow logic always shows if info is present ---
        arrow_key = f"arrow_{exp_key}"
        exp_state = st.session_state.get(exp_key, False)
        show_arrow = has_info and info

        # Decide if label is shown above (hide for radio/checkbox/selectbox)
        show_label = input_type not in [
            "radio",
            "checkbox",
            "selectbox",
            "multiselect",
            "fileuploader",
        ]

        # Info arrow and label handling
        if show_arrow:
            col1, col2 = st.columns([20, 1])
            with col1:
                if show_label and label:
                    st.markdown(f"**{label}**")
            with col2:
                arrow = "▼" if not exp_state else "▲"
                if st.button(arrow, key=arrow_key):
                    st.session_state[exp_key] = not exp_state
                    st.rerun()
            if st.session_state.get(exp_key, False):
                st.info(info)
        elif show_label and label:
            st.markdown(f"**{label}**")

        # ------------- Render widget with prefill where possible ---------------
        if input_type == "text":
            value = st.text_input(
                "",
                key=widget_key,
                value=prefill_val if prefill_val else "",
                label_visibility="collapsed",
                max_chars=max_length if max_length else None,
            )
            if max_length:
                st.caption(f"Characters: {len(value)}/{max_length}")
                if len(value) > max_length:
                    st.error("Character limit exceeded!")
        elif input_type == "textarea":
            value = st.text_area(
                "",
                key=widget_key,
                value=prefill_val if prefill_val else "",
                label_visibility="collapsed",
                max_chars=max_length if max_length else None,
            )
            if max_length:
                st.caption(f"Characters: {len(value)}/{max_length}")
                if len(value) > max_length:
                    st.error("Character limit exceeded!")
        elif input_type == "number":
            try:
                default_num = int(prefill_val) if prefill_val else 0
            except Exception:
                default_num = 0
            value = st.number_input(
                label if show_label else "",
                min_value=0,
                key=widget_key,
                value=default_num,
            )
        elif input_type == "date":
            value = st.date_input(
                label if show_label else "",
                value=parse_date_safe(prefill_val),
                key=widget_key,
            )
        elif input_type == "checkbox":
            # Accept both bool and "yes"/"no"
            if isinstance(prefill_val, bool):
                checked = prefill_val
            elif isinstance(prefill_val, str):
                checked = prefill_val.lower() in ("yes", "true", "1")
            else:
                checked = False
            value = st.checkbox(label, key=widget_key, value=checked)
        elif input_type == "selectbox":
            prefill_val = prefill_val or ""  # fallback to blank
            # Special mapping for SDGs, if needed
            if (
                label
                == "Which of the global goals in Agenda 2030 is the project expected to contribute to in the region in the long term?"
            ):
                prefill_val = map_goal_codes(prefill_val)
            default_option = safe_prefill(prefill_val, options)
            value = st.selectbox(
                label, options, key=widget_key, index=options.index(default_option)
            )
        elif input_type == "multiselect":
            default_vals = safe_prefill(prefill_val, options, multiselect=True)
            value = st.multiselect(label, options, default=default_vals, key=widget_key)
        elif input_type == "radio":
            default_option = safe_prefill(prefill_val, options)
            value = st.radio(
                label, options, key=widget_key, index=options.index(default_option)
            )
        elif input_type == "file_uploader":
            value = st.file_uploader(label, key=widget_key)
        elif input_type == "button":
            st.button(label, key=widget_key)
        elif input_type == "info":
            st.info(label)

    if "contacts_table" not in st.session_state:
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

    if st.session_state.selected_section == "Project Owner":
        # Example workplaces; can fetch from DB/backend
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

        # Only set default BEFORE rendering the widget
        if "selected_workplace_idx" not in st.session_state:
            st.session_state.selected_workplace_idx = 0

        st.markdown("#### Workplaces")
        st.caption("Select the workplace most affected")

        # Show as a radio list
        selected_idx = st.radio(
            "",
            options=list(range(len(workplaces))),
            format_func=lambda i: f"{workplaces[i]['workplace_no']} — {workplaces[i]['name']}",
            key="selected_workplace_idx",
        )

        # Render table header
        header_cols = st.columns([1, 2, 3, 2, 2, 2])
        headers = [
            "",
            "Workplace no",
            "Name",
            "Visiting address",
            "Postal code",
            "City",
            "Industry code",
        ]
        # for c, h in zip(header_cols, headers):
        #     c.markdown(f"**{h}**")

        # # Render table rows, highlight selected
        # for i, w in enumerate(workplaces):
        #     row_cols = st.columns([1, 2, 3, 2, 2, 2])
        #     indicator = "🔘" if selected_idx == i else "⚪"
        #     row_style = "background-color: #f0f2f6;" if selected_idx == i else ""
        #     with row_cols[0]:
        #         st.markdown(
        #             f"<span style='{row_style}'>{indicator}</span>", unsafe_allow_html=True
        #         )
        #     row_cols[1].markdown(
        #         f"<span style='{row_style}'>{w['workplace_no']}</span>",
        #         unsafe_allow_html=True,
        #     )
        #     row_cols[2].markdown(
        #         f"<span style='{row_style}'>{w['name']}</span>", unsafe_allow_html=True
        #     )
        #     row_cols[3].markdown(
        #         f"<span style='{row_style}'>{w['visiting_address']}</span>",
        #         unsafe_allow_html=True,
        #     )
        #     row_cols[4].markdown(
        #         f"<span style='{row_style}'>{w['postal_code']}</span>",
        #         unsafe_allow_html=True,
        #     )
        #     row_cols[5].markdown(
        #         f"<span style='{row_style}'>{w['city']}</span>", unsafe_allow_html=True
        #     )
        #     row_cols[5].markdown(
        #         f"<span style='{row_style}'>{w['industry_code']}</span>",
        #         unsafe_allow_html=True,
        #     )

        # Now selected_idx is the user's chosen workplace index
        st.info(f"Selected: {workplaces[selected_idx]['name']}")

    if st.session_state.selected_section == "Project Partner":
        if "partners" not in st.session_state:
            st.session_state.partners = []

        if st.button("+ Add project partner"):
            st.session_state.partners.append({})  # Add new partner entry

        for i, partner in enumerate(st.session_state.partners):
            st.markdown(f"### Projektpartner {i+1}")

            st.text_input("Company name", key=f"partner_{i}_company")
            st.text_input("Organization number", key=f"partner_{i}_orgnum")
            st.text_input("Address", key=f"partner_{i}_address")
            st.text_input("Momsregistreringsnummer (valfritt)", key=f"partner_{i}_vat")
            st.radio(
                "Omfattas organisationen av lagen om offentlig upphandling eller annan upphandlingslagsstiftning?",
                ["Ja", "Nej"],
                key=f"partner_{i}_upphandling",
            )
            st.text_input(
                "Ange vem som är organisationens firmatecknare?",
                key=f"partner_{i}_firmatecknare",
            )
            st.radio(
                "Har ni tagit upp moms som en kostnad när ni beräknar er budget?",
                ["Ja", "Nej"],
                key=f"partner_{i}_momsbudget",
            )
            st.markdown("---")

    if st.session_state.selected_section == "Activities":
        work_packages = []
        mapping = field_mapping.get(("Activities", "Name of work package"))
        if mapping:
            wizard_step, wizard_key = mapping
            work_packages = st.session_state.user_data.get(wizard_step, {}).get(
                wizard_key, []
            )

        if "activities" not in st.session_state:
            st.session_state.activities = []
            # Only prefill if no prior activities in state
            for wp in work_packages:
                st.session_state.activities.append(
                    {
                        "work_package": wp.get("name", ""),
                        "description_goal": wp.get("description", ""),
                        "start": parse_date_safe(wp.get("start_date", "")),
                        "end": parse_date_safe(wp.get("end_date", "")),
                        "name": wp.get("activity_name", ""),
                        "cost": wp.get("cost", 0),
                        "desc": wp.get("activity_description", ""),
                        "impact": wp.get("impact_to_global_goals", ""),
                    }
                )

        # You can now render the activities as usual, prefilling from st.session_state.activities
        for i, activity in enumerate(st.session_state.activities):
            st.markdown(f"### Activity {i+1}")
            st.text_input(
                "Name of work package",
                key=f"activity_{i}_work_package",
                value=activity["work_package"],
            )
            st.text_area(
                "Description how the work package contributes to the project goal",
                key=f"activity_{i}_description_goal",
                value=activity["description_goal"],
            )
            st.date_input(
                "Start date", value=activity["start"], key=f"activity_{i}_start"
            )
            st.date_input("End date", value=activity["end"], key=f"activity_{i}_end")
            st.text_input(
                "Name of activity", key=f"activity_{i}_name", value=activity["name"]
            )
            st.number_input(
                "cost", min_value=0, key=f"activity_{i}_cost", value=activity["cost"]
            )
            st.text_area(
                "Description of activity",
                key=f"activity_{i}_desc",
                value=activity["desc"],
            )
            st.text_area(
                "how will your work packages impact to global goals",
                key=f"activity_{i}_impact",
                value=activity["impact"],
            )
            st.markdown("---")

    if st.session_state.selected_section == "Contacts":

        st.markdown("### Contact List")

        headers = [
            "Name",
            "Role",
            "Organization",
            "Phone number",
            "Mobile number",
            "Email address",
            "project bank",
            "",
            "",
        ]
        st.columns(len(headers))  # draw empty line for spacing

        # Header row
        cols = st.columns([2, 2, 2, 2, 2, 3, 2, 1, 1])
        for col, header in zip(cols, headers):
            col.markdown(f"**{header}**")

        # Render contact rows
        for idx, contact in enumerate(st.session_state.contacts_table):
            cols = st.columns([2, 2, 2, 2, 2, 3, 2, 1, 1])
            cols[0].write(contact["Name"])
            cols[1].write(contact["Role"])
            cols[2].write(contact["Organization"])
            cols[3].write(contact["Phone number"])
            cols[4].write(contact["Mobile number"])
            cols[5].write(contact["Email address"])
            cols[6].write(contact["project bank"])
            if cols[7].button("✏️", key=f"edit_contact_{idx}"):
                st.warning(f"Edit mode not implemented for {contact['Name']}")
            if cols[8].button("🗑️", key=f"delete_contact_{idx}"):
                st.session_state.contacts_table.pop(idx)
                st.rerun()

        st.markdown("### Add New Contact")
        st.markdown("---")
        with st.form("add_contact_form", clear_on_submit=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                name = st.text_input("Name")
                role = st.text_input("Role")
                org = st.text_input("Organization")
            with col2:
                phone = st.text_input("Phone number")
                mobile = st.text_input("Mobile number")
                email = st.text_input("Email address")
            with col3:
                bank = st.text_input("project bank")

            submitted = st.form_submit_button("➕ Add Contact")

            if submitted:
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
                st.rerun()

    st.markdown(
        """
        <script>
            const icons = window.parent.document.querySelectorAll(".copy-icon");
            icons.forEach(el => el.style.fontSize = "16px");
        </script>
    """,
        unsafe_allow_html=True,
    )


