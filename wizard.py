import streamlit as st
from openai import OpenAI
from streamlit_extras.switch_page_button import switch_page
from generateresponse import generate_from_ai, generate_work_packages_from_ai

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

wizard_steps = [
    "1 - Organisation & contact",
    "2 - Project idea",
    "3 - Programme & geography",
    "4 - Target group",
    "5 - Agenda 2030 & risk",
    "6 - Work-package generator",
    "7 - Policies & sign-off",
]

section_mapping = {
    0: "Project Summary",
    1: "Challenges and Needs",
    2: "Target Group",
    3: "Organisation Structure",
    4: "Risk Analysis",
    5: "Communication Plan",
    6: "Internal Policies",
}


def info_arrow(label, info, show_label=True, arrow_key=None, exp_key=None):
    # exp_key: unique for field/section
    if arrow_key is None:
        arrow_key = f"arrow_{label}"
    if exp_key is None:
        exp_key = f"expanded_{label}"
    exp_state = st.session_state.get(exp_key, False)
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


if "user_data" not in st.session_state:
    st.session_state.user_data = {}


def wizard_ui():
    email = st.session_state.get("user", "guest@example.com")
    username = email.split("@")[0]

    st.markdown(
        f"""
        <div style='background-color: #f5f5f5; padding: 1rem; border-radius: 8px;'>
        <b>🧙‍♂️ ERDF Application Wizard</b> | 👤 <span style='color:gray'>Logged in as: <strong>{username}</strong></span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "step" not in st.session_state:
        st.session_state.step = 0
        st.session_state.user_data = {}
        st.session_state.generated_data = {}
        st.session_state.edited_sections = {}

    step = st.session_state.step
    step_label = wizard_steps[step]
    st.subheader(f"Step {step+1}/{len(wizard_steps)}: {step_label}")
    st.divider()

    user_input_obj = {}

    if step == 0:
        # Step 1 – Organisation & contact
        info_arrow(
            "Enter basic organisation details and main contact.",
            "Provide legal name, Swedish organisation number (XXXXXXXX XXXX), and one primary contact (name, phone, e-mail). Confirm whether your organisation falls under the Swedish Public Procurement Act (LOU).",
            arrow_key="arrow_org",
            exp_key="exp_org",
        )
        col1, col2 = st.columns(2)
        with col1:
            org = st.text_input(
                "Organisation name", key="org_name", placeholder="GreenCity AB"
            )
            reg = st.text_input(
                "Registration number", key="reg_number", placeholder="556677 8899"
            )
        with col2:
            contact = st.text_input(
                "Contact name", key="contact_name", placeholder="Maria Lind"
            )
            email = st.text_input(
                "E-mail", key="email", placeholder="maria@greencity.se"
            )
            phone = st.text_input("Phone", key="phone", placeholder="+46 70 123 45 67")
        lou = st.radio(
            "Subject to LOU (Public Procurement)?", ["Yes", "No"], key=f"lou_{step}"
        )
        user_input_obj = {
            "organisation_name": org,
            "registration_number": reg,
            "contact_name": contact,
            "email": email,
            "phone": phone,
            "subject_to_lou": lou == "Yes",
        }

    elif step == 1:
        # Step 2 – Project idea (max 2 x 2000 chars)
        st.markdown("#### Current situation & challenges")
        info_arrow(
            "Describe the current situation and the specific challenges your project will address.",
            "Summarise the facts and analysis that prove a need exists.\n\n– Use data, reports or stakeholder feedback.\n– Explain who is affected and why the situation must change.\n– List the key barriers or problems the project intends to solve.",
            arrow_key="arrow_proj1",
            exp_key="exp_proj1",
        )
        maxlen_a = 2000
        a_val = st.text_area(
            "Current situation & challenges",
            key="proj_situation",
            max_chars=maxlen_a,
            placeholder="Region X has 7 000 SMEs; 60 % lack climate smart logistics, leading to 1 200 t of extra CO₂ per year …",
        )
        st.caption(f"{len(a_val)}/{maxlen_a} characters")

        st.markdown("#### SMART project goal")
        info_arrow(
            "State your SMART project goal—the future situation that will exist once the project is complete.",
            "Your goal must follow the SMART criteria:\n\nSpecific – exactly what will be achieved?\nMeasurable – how will you verify success?\nAccepted – why is it important and by whom?\nRealistic – can it be achieved with available resources?\nTime bound – the goal should be reached by the project’s end date.",
            arrow_key="arrow_proj2",
            exp_key="exp_proj2",
        )
        maxlen_b = 2000
        b_val = st.text_area(
            "SMART project goal",
            key="proj_smartgoal",
            max_chars=maxlen_b,
            placeholder="By 30 June 2027, 50 SMEs will adopt route optimisation software, reducing CO₂ emissions by 20 % …",
        )
        st.caption(f"{len(b_val)}/{maxlen_b} characters")

        user_input_obj = {
            "current_situation_challenges": a_val,
            "smart_project_goal": b_val,
        }

    elif step == 2:
        # Step 3 – Programme & geography
        info_arrow(
            "Select the ERDF programme area and all regions/municipalities where activities will take place.",
            "Your choices tell the AI which regional development strategy to cite in later sections. If activities span several municipalities, tick them all.",
            arrow_key="arrow_prog",
            exp_key="exp_prog",
        )
        programme = st.selectbox(
            "Programme area", ["Smart Growth", "Green Transition"], key="programme"
        )
        regions = st.multiselect(
            "Region / municipality",
            ["Region North", "Region South", "Region East", "Region West"],
            key="region",
        )
        user_input_obj = {"programme_area": programme, "regions": regions}

    elif step == 3:
        # Step 4 – Target group (expanded)
        st.markdown("#### Target group & need")
        info_arrow(
            "Who is your main target group and what key need do they have?",
            "Mention size, sector, and diversity aspects (gender, age, background, geography, disabilities). State the primary need your project will meet.",
            arrow_key="arrow_tg1",
            exp_key="exp_tg1",
        )
        maxlen_a = 600
        tg_a = st.text_area(
            "Target group & need",
            key="target_group_need",
            max_chars=maxlen_a,
            placeholder="Small rural manufacturers, 30 % women owned, need digital logistics support …",
        )
        st.caption(f"{len(tg_a)}/{maxlen_a} characters")

        st.markdown("#### Previous experience")
        info_arrow(
            "What prior experience do you have with this group?",
            "List earlier projects, studies, or other relevant activities showing you understand the group.",
            arrow_key="arrow_tg2",
            exp_key="exp_tg2",
        )
        maxlen_b = 300
        tg_b = st.text_area(
            "Previous experience",
            key="target_group_exp",
            max_chars=maxlen_b,
            placeholder="Ran ERUF ‘RoboSME’ pilot in 2023; coached 25 firms …",
        )
        st.caption(f"{len(tg_b)}/{maxlen_b} characters")

        st.markdown("#### Involvement in preparation")
        info_arrow(
            "How did you involve the group while preparing this project?",
            "Give concrete actions: surveys, interviews, workshops, advisory meetings, etc.",
            arrow_key="arrow_tg3",
            exp_key="exp_tg3",
        )
        maxlen_c = 300
        tg_c = st.text_area(
            "Involvement in preparation",
            key="target_group_prep",
            max_chars=maxlen_c,
            placeholder="Online survey (58 responses) and focus group workshop, Dec 2024 …",
        )
        st.caption(f"{len(tg_c)}/{maxlen_c} characters")

        st.markdown("#### Involvement during project")
        info_arrow(
            "How will you keep the group involved during implementation?",
            "Describe planned outreach, participation in activities, follow up or monitoring methods.",
            arrow_key="arrow_tg4",
            exp_key="exp_tg4",
        )
        maxlen_d = 300
        tg_d = st.text_area(
            "Involvement during project",
            key="target_group_impl",
            max_chars=maxlen_d,
            placeholder="Quarterly feedback sessions, SME advisory board seats, pilot tests …",
        )
        st.caption(f"{len(tg_d)}/{maxlen_d} characters")

        user_input_obj = {
            "target_group_need": tg_a,
            "target_group_experience": tg_b,
            "involvement_preparation": tg_c,
            "involvement_implementation": tg_d,
        }

    elif step == 4:
        # Step 5 – Agenda 2030 & risk
        info_arrow(
            "Choose up to two SDG goals and up to three main risks.",
            "• SDG goals: Select the goals your project supports (e.g. Goal 7 “Affordable & Clean Energy”).\n• Risks: Select the most likely threats—delays, low SME engagement, procurement issues, staff turnover, etc. The AI will generate the motivation text and a risk analysis with mitigation.",
            arrow_key="arrow_sdg",
            exp_key="exp_sdg",
        )
        sdgs = st.multiselect(
            "Select 1-2 SDG goals", ["Goal 7", "Goal 9", "Goal 11"], key="sdg_goals"
        )
        risks = st.multiselect(
            "Select up to 3 risks",
            ["Low participation", "Budget overrun", "Tech delays", "Staff turnover"],
            key="risks",
        )
        user_input_obj = {"sdg_goals": sdgs, "risks": risks}

    elif step == 5:
        # Step 6 – Work packages (DETAILED)
        info_arrow(
            "Click “Generate work packages”. Review the AI suggestions; drag to reorder, edit titles or descriptions, delete, or add your own.",
            "Work packages structure the project. The AI will propose 3–5 packages with purpose, activities, deliverables and timeline. You can rename, shorten or expand them as needed before saving.",
            arrow_key="arrow_wp",
            exp_key="exp_wp",
        )

        if "work_packages" not in st.session_state:
            st.session_state.work_packages = []

        if st.button("Generate Work Packages "):
            dummy_packages = generate_work_packages_from_ai("test", test_mode=True)
            st.session_state.work_packages = dummy_packages
            st.success("Dummy work packages loaded!")

        st.write("#### Work packages")
        packages = st.session_state.work_packages

        # Editing interface for each package
        for i, pkg in enumerate(packages):
            with st.container():
                col1, col2, col4 = st.columns([4, 6, 1])
                with col1:
                    pkg["name"] = st.text_input(
                        f"Name {i+1}", value=pkg.get("name", ""), key=f"wp_name_{i}"
                    )
                with col2:
                    pkg["description"] = st.text_area(
                        f"Description {i+1}",
                        value=pkg.get("description", ""),
                        key=f"wp_desc_{i}",
                        height=60,
                    )
                # Detect if this is a "custom" (new/blank) work package
                is_custom = not pkg.get("name") and not pkg.get("description")
                # with col3:
                #     if not is_custom:
                #         if st.button("▲", key=f"wp_up_{i}", disabled=i == 0):
                #             packages.insert(i - 1, packages.pop(i))
                #             st.rerun()
                #         if st.button(
                #             "▼", key=f"wp_down_{i}", disabled=i == len(packages) - 1
                #         ):
                #             packages.insert(i + 1, packages.pop(i))
                #             st.rerun()
                #     else:
                #         st.write("")  # Spacer for layout
                #         st.write("")

                with col4:
                    if st.button("❌", key=f"wp_del_{i}"):
                        packages.pop(i)
                        st.rerun()

        # Add new work package (manual)
        if st.button("Add Custom Work Package"):
            packages.append(
                {
                    "name": "",
                    "description": "",
                }
            )
            st.rerun()

        # Save back to session
        st.session_state.work_packages = packages
        user_input_obj = {"work_packages": packages}

    elif step == 6:
        # Step 7 – Policies & sign off
        info_arrow(
            "Upload any internal policies (optional)",
            "Typical policies: environmental plan, travel policy, equality & diversity plan. If you have no files ready, you can skip uploads now and add them later.",
            arrow_key="arrow_pol",
            exp_key="exp_pol",
        )
        uploaded_files = st.file_uploader(
            "Upload PDF/DOC files", type=["pdf", "docx"], accept_multiple_files=True
        )
        file_names = [f.name for f in uploaded_files] if uploaded_files else []
        user_input_obj = {
            "uploaded_policies": file_names,
        }

    # Save current step user input
    st.session_state.user_data[step_label] = user_input_obj

    # Navigation & "Next" blocking logic
    disable_next = False
    if step == 1:
        if (
            len(user_input_obj["current_situation_challenges"]) > 2000
            or len(user_input_obj["smart_project_goal"]) > 2000
        ):
            disable_next = True
    if step == 3:
        if (
            len(user_input_obj["target_group_need"]) > 600
            or len(user_input_obj["target_group_experience"]) > 300
            or len(user_input_obj["involvement_preparation"]) > 300
            or len(user_input_obj["involvement_implementation"]) > 300
        ):
            disable_next = True

    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        if step > 0 and st.button("◀ Previous"):
            st.session_state.step -= 1
            st.rerun()

    with col3:
        if step < len(wizard_steps) - 1 and st.button("Next ▶", disabled=disable_next):
            user_input_obj = st.session_state.user_data[step_label]
            ai_data = generate_from_ai(step_label, user_input_obj)
            st.session_state.generated_data[step_label] = ai_data
            section_name = section_mapping.get(step, step_label)
            st.session_state.edited_sections[section_name] = ai_data

            st.session_state.step += 1
            st.rerun()

        elif step == len(wizard_steps) - 1 and st.button("✅ Submit"):
            with st.spinner("Finalizing all content with AI..."):
                for i, label in enumerate(wizard_steps):
                    if label not in st.session_state.generated_data:
                        user_input_obj = st.session_state.user_data.get(label, {})
                        ai_data = generate_from_ai(label, user_input_obj)
                        st.session_state.generated_data[label] = ai_data
                        section_name = section_mapping.get(i, label)
                        st.session_state.edited_sections[section_name] = ai_data

                st.session_state["wizard_complete"] = True

            st.rerun()
