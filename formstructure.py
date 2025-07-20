form_structure = {
    "Overview": [
        {
            "section_info": "General information about the project.",
        },
        {
            "question": "Project name",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Project start date*",
            "type": "date",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Project end date*",
            "type": "date",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "In which municipality or municipalities will the efforts be implemented?",
            "type": "multiselect",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [
                "Kronoberg",
                "Kalmar",
                "Alvesta",
                "Ljungby",
                "Lessebo",
                "Markaryd",
                "Älmhult",
                "Tingsryd",
                "Växjö",
                "Uppvidinge",
                "Borgholm",
                "Västervik",
            ],
        },
        {
            "question": "Are you looking for funding for a feasibility study?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "Are you looking for financing for a framework project?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "Describe the support scheme for the framework project",
            "type": "textarea",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Has the project carried out the sustainability analysis described in the EU Handbook?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "Are you applying for financing to invest in infrastructure?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "I certify that the investment has a lifespan of at least 5 years after the project is completed",
            "type": "checkbox",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "I certify that the project has implemented climate proofing of infrastructure investments that have a expected lifespan of at least 5 years",
            "type": "checkbox",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Summarize the project",
            "type": "textarea",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
    ],
    "Project Owner": [
        {
            "section_info": "Information about the main project owner organization.",
        },
        # Main org fields
        {
            "question": "Organization number",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Organization name",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Legal code / Form",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Industry code/name",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Country",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        # Workplaces table will be handled specially in UI (see below)
        # {
        #     "question": "Workplaces",
        #     "type": "workplace_table",
        #     "info": "Select the workplace most affected by the project.",
        #     "max_length": None,
        #     "has_info": True,
        #     "options": [],  # Each row: workplace_no, name, visiting address, postal code, postort, industry code
        # },
        {
            "question": "VAT registration number (optional)",
            "type": "text",
            "info": "Only to be filled in by foreign operators participating in the project.",
            "max_length": None,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Is the organization covered by the Public Procurement Act or other procurement legislation?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "Organization website",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Have you included VAT as a cost when calculating your budget?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "Select payment method",
            "type": "selectbox",
            "info": "We can only make payments to Plus or Bankgiro. If you do not have this type of account, you will need to obtain one before applying for support.",
            "max_length": None,
            "has_info": True,
            "options": ["Bankgiro", "Plusgiro"],
        },
        {
            "question": "Bank/Plusgiro account number",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Application for advance payment",
            "type": "radio",
            "info": "Recipients with weak liquidity can apply for an advance of up to half the support but a maximum of SEK 400,000 in total for the project during the project period.",
            "max_length": None,
            "has_info": True,
            "options": ["Yes", "No"],
        },
    ],
    "Project Partner": [
        {
            "section_info": "Details for each partner organization involved in the project.",
        },
        # {
        #     "question": "Add project partner",
        #     "type": "button",
        #     "info": "",
        #     "max_length": None,
        #     "has_info": False,
        #     "options": [],
        # },
        {
            "question": "Organization number",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Name",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "post code",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "visiting adress",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "city",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "industry code",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "VAT registration number (optional)",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Is the organization covered by the Public Procurement Act or other procurement legislation?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "State who is the organization's authorized signatory",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Have you included VAT as a cost when calculating your budget?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
    ],
    "Challenges and Needs": [
        {
            "section_info": (
                "This section helps define your project's purpose, the challenges it addresses, "
                "the current situation it aims to improve, and its relevance to global sustainability goals."
            ),
        },
        {
            "question": "Briefly describe your project goal. The project goal should describe the state that has been achieved at the end of the project. It should have a clear connection to the specific objective in the call.",
            "type": "textarea",
            "info": (
                "The project goal must meet the SMART criteria:\n"
                "- **Specific**: What exactly should be achieved?\n"
                "- **Measurable**: How will you know it’s achieved?\n"
                "- **Accepted**: Why is it important to achieve?\n"
                "- **Realistic**: Is the goal reasonable?\n"
                "- **Time-bound**: It should be reached by project end."
            ),
            "max_length": 1000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Which challenge in the call for proposals will the project contribute to solving?",
            "type": "textarea",
            "info": "Refer to the challenge(s) stated in the call. The project should clearly address one or more of these challenges.",
            "max_length": 1000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Describe the current situation that the project will contribute to changing.",
            "type": "textarea",
            "info": "Base your answer on facts and analysis. Clarify who needs the project and why.",
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Which of the global goals in Agenda 2030 is the project expected to contribute to in the region in the long term?",
            "type": "selectbox",
            "info": "Refer to the guidance in the call. The project's impact should support societal changes aligned with these global goals.",
            "max_length": None,
            "has_info": True,
            "options": [
                "Industry, Innovation and Infrastructure",
                "Decent Work and Economic Growth",
                "Climate Action",
                "Other",
            ],
        },
        {
            "question": "Justify the choice of Agenda 2030 goals.",
            "type": "textarea",
            "info": "Explain how the chosen goal(s) are relevant to your project and the regional context.",
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
    ],
    "Target Group": [
        {
            "section_info": "Define and describe your primary and secondary target groups for the project.",
        },
        {
            "question": "Select a primary target group for the project's activities during the project period?",
            "type": "selectbox",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [
                "Micro enterprises",
                "Small enterprises",
                "Medium enterprises",
                "Large companies",
                "Startups",
                "Academia",
                "Public sector",
            ],
        },
        {
            "question": "Optionally, select one or more secondary target groups for the project's activities during the project period",
            "type": "multiselect",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [
                "Micro enterprises",
                "Small enterprises",
                "Medium enterprises",
                "Large companies",
                "Startups",
                "Academia",
                "Public sector",
            ],
        },
        {
            "question": "Describe the project's target group and their needs",
            "type": "textarea",
            "info": (
                "To answer this question, consider:\n"
                "- What does the project's target group look like in terms of diversity and gender equality?\n"
                "- What is the composition in the industry the project targets, and why?\n"
                "- How is the distribution by gender, age, background, disability, geography, etc.?\n"
                "- What needs does the target group have regarding the project?\n\n"
                "Use relevant gender-disaggregated statistics where possible. This question encourages you to map and broaden the representation of the project's target group by identifying any structural imbalances. These insights should guide you during project implementation, especially when engaging and collaborating with the target group in activities."
            ),
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "What is your previous experience with the target group?",
            "type": "textarea",
            "info": (
                "Describe your experience with the target group. You can give examples of previous activities and projects involving this group. "
                "Other relevant experience or knowledge that supports your project application can also be included, such as studies, reports, or other background."
            ),
            "max_length": 2000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "How have you worked to include the target group in the preparations for the project?",
            "type": "textarea",
            "info": (
                "Describe how the target group has been included in the project preparations. "
                "For example, has the target group been involved in developing the application, and if so, how?"
            ),
            "max_length": 2000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Which main industry do you expect the project's activities to contribute to?",
            "type": "selectbox",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [
                "Manufacturing",
                "Information and Communication",
                "Financial and Insurance",
                "Real Estate",
                "Professional, Scientific and Technical",
                "Public Administration",
                "Education",
                "Health and Social Work",
                "Other",
            ],
        },
        {
            "question": "How will you work to include the target group in the implementation of the project?",
            "type": "textarea",
            "info": (
                "Describe how you will ensure the project's activities reach the target group. "
                "How will you work, implement, and follow up to ensure that the right target group is engaged during the project period?"
            ),
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "In what way will your work packages impact the global goals? What risks of goal conflicts have you identified? And if so, how will you manage the identified goal conflicts?",
            "type": "textarea",
            "info": (
                "Assess and justify the impact of the work package based on the following factors:\n"
                "- No impact\n"
                "- Risk of negative impact\n"
                "- Positive impact\n"
                "- More knowledge needed\n\n"
                "Understanding goal conflicts provides opportunities for improvement. Making goal conflicts visible creates opportunities to address them and can clarify who has the mandate to handle them. "
                "Progress towards one agenda goal or sub-goal may sometimes hinder progress towards others, both within and between goals.\n\n"
                "Example: Implementation and scaling up of new technology can be very energy-intensive. It is therefore important to assess whether efforts might increase energy consumption in the short term, negatively affecting sub-goal 7.2 (Increase the share of renewable energy in the world).\n\n"
                "Being able to consider and prepare for potential conflicts related to the global goals is part of the assessment criteria. You can read more about the assessment criteria in the handbook."
            ),
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Where will the results arise?",
            "type": "selectbox",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [
                "In the project organization",
                "In the target group",
                "In the broader community",
                "Other",
            ],
        },
        {
            "question": "Capacity – what will the target group or target object gain access to?",
            "type": "selectbox",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [
                "New knowledge",
                "New technology",
                "Networks/Contacts",
                "Funding or resources",
                "Other",
            ],
        },
        {
            "question": "What changed behaviors are the strengthened capabilities expected to lead to in the target group or target object?",
            "type": "selectbox",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [
                "Increased collaboration",
                "Adoption of new methods",
                "Greater inclusion/diversity",
                "Improved sustainability",
                "Other",
            ],
        },
    ],
    "Activities": [
        {
            "section_info": "Detailed information about the project activities and work packages.",
        },
        {
            "question": "Name of work package",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Description how the work package contributes to the project goal",
            "type": "textarea",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Start date",
            "type": "date",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "End date",
            "type": "date",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Name of activity",
            "type": "text",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "cost",
            "type": "number",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Description of activity",
            "type": "textarea",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "how will your work packages impact to global goals",
            "type": "textarea",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
    ],
    "Expected Results": [
        {
            "section_info": "What results are expected and how will they be measured?",
        },
        {
            "question": "Where will the results arise?",
            "type": "textarea",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Capacity/Ability - what will the target group or target object gain access to",
            "type": "textarea",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "What changed behaviors are the strengthened capabilities expected to lead to in the target group or target object?",
            "type": "textarea",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "Target Value",
            "type": "number",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
        {
            "question": "remarks",
            "type": "textarea",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
    ],
    "Organization": [
        {
            "section_info": "Describe the organization and project management.",
        },
        {
            "question": "How will the project's organization be structured to implement the project?",
            "type": "textarea",
            "info": (
                "Consider these aspects:\n"
                "- What roles, functions, and skills are needed to carry out the project's activities?\n"
                "- How will you ensure that these roles, functions, and skills are available when needed? In projects with several partners, clearly state each partner's contribution.\n"
                "- What does your ownership look like? Active ownership means that a function or person at management level in your organization is involved in the project, e.g., as chairperson of the steering group or otherwise actively participating.\n"
                "- Will the project have a steering group or similar function? If so, describe the intended members and their mandates for managing project results.\n"
                "If your project includes activities aimed at companies, briefly describe your previous experience of working with and reporting on activities that constitute support to companies under de minimis aid and state aid rules."
            ),
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "What other similar projects or activities are you aware of?",
            "type": "textarea",
            "info": (
                "Applied support cannot fund activities that are part of your ordinary operations. Please describe:\n"
                "- Whether similar activities are ongoing in your organization, in Sweden or internationally, and how your project relates to them.\n"
                "- If similar activities are ongoing, describe how your project complements what already exists and how you will interact with those involved.\n"
                "- How you intend to benefit from results and experiences from similar activities conducted by you or others previously."
            ),
            "max_length": 2000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "How will you internally in the project organization work for an inclusive culture for equal opportunities to influence the project's direction and results?",
            "type": "textarea",
            "info": (
                "Describe how you will strive for the most gender-balanced internal organization possible and how your decision-making processes will enable an inclusive culture where different voices are heard."
            ),
            "max_length": 2000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Describe what sustainability expertise exists within the project organization, or is intended to be recruited for the project?",
            "type": "textarea",
            "info": "Describe what sustainability expertise is present or will be recruited for the project.",
            "max_length": 2000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Will you, in the implementation of your project, work with other actors than those who are part of your project organization?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "Describe what kind of work will be carried out and with which actors, and how it will contribute to the project's implementation.",
            "type": "textarea",
            "info": (
                "Describe the kind of work to be conducted, with which actors, and how it will contribute to project implementation. State which actors you will cooperate with, in which activities, and how. Clarify how this cooperation will contribute to project delivery. Indicate if any partners are outside the program area. If your project is a Baltic Sea Strategy project, answer the relevant questions below."
            ),
            "max_length": 2000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Are you seeking support for activities that contribute to the implementation of the Baltic Sea Strategy?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "How does the collaboration contribute to the goals of the Baltic Sea Strategy?",
            "type": "textarea",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
    ],
    "Working Method": [
        {
            "section_info": "How will the work be organized and results reported?",
        },
        {
            "question": "How have you ensured in the project planning that you have the ability to report and account for costs and activities in the project?",
            "type": "textarea",
            "info": (
                "Describe how your administrative capacity and routines will enable you to carry out and report on the project.\n\n"
                "- How will you ensure that the reporting of activities and costs is in accordance with Tillväxtverket’s general conditions and funding decisions?\n"
                "- How will you ensure that costs not covered by flat rates are reported in a way that allows for a detailed ledger showing actual costs and revenues?\n"
                "- Describe your routine to ensure such costs are eligible, paid, and in accordance with the decision.\n"
                "- Describe your routine for handling staff time reporting."
            ),
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "How are you going to work with communication?",
            "type": "textarea",
            "info": (
                "EU requires supported projects to inform and share knowledge about the project and its EU funding. Briefly describe your communication plan and how you will disseminate results:\n\n"
                "- **Target group:** Who will you communicate with?\n"
                "- **Communication goals:** What do you want the target group to know, think, or do?\n"
                "- **Message:** What do you want to convey that is useful for the target group?\n"
                "- **Channels:** Which channels will you use?\n"
                "- **Inclusion:** How will you ensure inclusive communication and adapt external communications/marketing to reach a diverse target group (background, gender, age, geography)?\n\n"
                "You must also use the EU logo correctly and provide a brief project description and funding information on your website and social channels."
            ),
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
        # {
        #     "question": "As project owners, we have understood that we must collect gender-disaggregated statistics for the participants who receive support through the project.\n\nAll projects are required to follow up on the gender distribution of participants who receive support, which will be reported to the Swedish Agency for Economic and Regional Development when reporting on the situation.",
        #     "type": "radio",
        #     "info": "",
        #     "max_length": None,
        #     "has_info": False,
        #     "options": ["Yes", "No"],
        # },
        {
            "question": "Do you have a documented routine for the collection and reporting of gender-disaggregated statistics?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "Will you follow up and report on the gender distribution of participants to the Swedish Agency for Economic and Regional Development?",
            "type": "radio",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": ["Yes", "No"],
        },
        {
            "question": "How will you work with procurement in the project?",
            "type": "textarea",
            "info": (
                "If your organization is subject to public procurement, you are responsible for ensuring all project purchases follow current procurement legislation:\n\n"
                "- Public Procurement Act (2016:1145)\n"
                "- Procurement in the Utilities Sectors Act (2016:1146)\n"
                "- Concessions Procurement Act (2016:1147)\n\n"
                "If you are not subject to procurement law, follow the principles in Chapter 4, Section 1 of the Public Procurement Act and Tillväxtverket’s special procurement guidelines. Describe how you will ensure the correct procedures are used for project purchases. If there are multiple partners, describe how you ensure procurement is carried out according to the rules.\n\n"
                "You must attach a procurement and purchasing plan to the application."
            ),
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "How have you ensured the project's co-financing and management of the project's liquidity?",
            "type": "textarea",
            "info": (
                "You claim support after incurring and paying costs. This means you must pre-finance costs while waiting for approval and payment from Tillväxtverket.\n\n"
                "Describe:\n"
                "- How you have secured ongoing financing from other co-financiers beyond Tillväxtverket.\n"
                "- If you have ensured liquidity even if a cost is disallowed.\n"
                "- If you can complete the project before the final payment is received."
            ),
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "What risks have you identified in the project and what measures do you propose?",
            "type": "textarea",
            "info": (
                "Base your description on a completed risk analysis.\n\n"
                "- Implementing a project involves various risks. Develop a plan for handling foreseeable risks. A risk is not an existing fact, but something that could happen in the future. For example, a tight schedule is not a risk if you already know it will occur.\n"
                "- Involve different competencies in your analysis for better preparedness.\n"
                "- Use the EU Project Handbook's risk analysis template as support (not required for submission).\n"
                "- Describe risks with medium/high risk value and proposed mitigation measures."
            ),
            "max_length": 2000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Describe, based on your current guidelines, how you will take these into account in your project?",
            "type": "textarea",
            "info": (
                "Tillväxtverket requires your project to comply with the project owner's guidelines and/or policies, such as your environmental policy, meeting/travel policy, and gender equality plan.\n\n"
                "Reflect on, for example, how your travel policy will affect project travel and how your gender equality plan will be integrated in the project's implementation."
            ),
            "max_length": 2000,
            "has_info": True,
            "options": [],
        },
        {
            "question": "Describe how you will work to document, disseminate, and utilize results during the project period? Also describe how you will ensure that the results are utilized during the project period?",
            "type": "textarea",
            "info": (
                "To demonstrate and report your project's results to Tillväxtverket, you need to collect information showing what has been done and measure the indicators relevant to your project. This also involves learning from experience and acting on that knowledge."
            ),
            "max_length": 4000,
            "has_info": True,
            "options": [],
        },
    ],
    "Budget": [
        {
            "section_info": "Budget and financing for the project.",
        },
    ],
    "Contacts": [
        {
            "section_info": "Project contact persons.",
        },
    ],
    "Attachments": [
        {
            "section_info": "Upload all necessary attachments.",
        },
        {
            "question": "Upload attachments",
            "type": "file_uploader",
            "info": "",
            "max_length": None,
            "has_info": False,
            "options": [],
        },
    ],
}
