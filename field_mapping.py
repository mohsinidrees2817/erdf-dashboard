field_mapping = {
    # --- Overview ---
    ("Overview", "Project name"): None,  # Not collected in wizard
    ("Overview", "Project start date*"): None,
    ("Overview", "Project end date*"): None,
    (
        "Overview",
        "In which municipality or municipalities will the efforts be implemented?",
    ): ("3 - Programme & geography", "regions"),
    ("Overview", "Are you looking for funding for a feasibility study?"): None,
    ("Overview", "Are you looking for financing for a framework project?"): None,
    ("Overview", "Describe the support scheme for the framework project"): None,
    (
        "Overview",
        "Has the project carried out the sustainability analysis described in the EU Handbook?",
    ): None,
    ("Overview", "Are you applying for financing to invest in infrastructure?"): None,
    (
        "Overview",
        "I certify that the investment has a lifespan of at least 5 years after the project is completed",
    ): None,
    (
        "Overview",
        "I certify that the project has implemented climate proofing of infrastructure investments that have a expected lifespan of at least 5 years",
    ): None,
    ("Overview", "Summarize the project"): None,
    # --- Project Owner ---
    ("Project Owner", "Organization number"): (
        "1 - Organisation & contact",
        "registration_number",
    ),
    ("Project Owner", "Organization name"): (
        "1 - Organisation & contact",
        "organisation_name",
    ),
    ("Project Owner", "Legal code / Form"): None,
    ("Project Owner", "Industry code/name"): None,
    ("Project Owner", "Country"): None,
    ("Project Owner", "VAT registration number (optional)"): None,
    (
        "Project Owner",
        "Is the organization covered by the Public Procurement Act or other procurement legislation?",
    ): ("1 - Organisation & contact", "subject_to_lou"),
    ("Project Owner", "Organization website"): None,
    (
        "Project Owner",
        "Have you included VAT as a cost when calculating your budget?",
    ): None,
    ("Project Owner", "Select payment method"): None,
    ("Project Owner", "Bank/Plusgiro account number"): None,
    ("Project Owner", "Application for advance payment"): None,
    # --- Project Partner ---
    ("Project Partner", "Organization number"): None,
    ("Project Partner", "Name"): None,
    ("Project Partner", "post code"): None,
    ("Project Partner", "visiting adress"): None,
    ("Project Partner", "city"): None,
    ("Project Partner", "industry code"): None,
    ("Project Partner", "VAT registration number (optional)"): None,
    (
        "Project Partner",
        "Is the organization covered by the Public Procurement Act or other procurement legislation?",
    ): None,
    ("Project Partner", "State who is the organization's authorized signatory"): None,
    (
        "Project Partner",
        "Have you included VAT as a cost when calculating your budget?",
    ): None,
    # --- Challenges and Needs ---
    (
        "Challenges and Needs",
        "Briefly describe your project goal. The project goal should describe the state that has been achieved at the end of the project. It should have a clear connection to the specific objective in the call.",
    ): ("2 - Project idea", "smart_project_goal"),
    (
        "Challenges and Needs",
        "Which challenge in the call for proposals will the project contribute to solving?",
    ): ("2 - Project idea", "current_situation_challenges"),
    (
        "Challenges and Needs",
        "Describe the current situation that the project will contribute to changing.",
    ): ("2 - Project idea", "current_situation_challenges"),
    (
        "Challenges and Needs",
        "Which of the global goals in Agenda 2030 is the project expected to contribute to in the region in the long term?",
    ): ("5 - Agenda 2030 & risk", "sdg_goals"),
    ("Challenges and Needs", "Justify the choice of Agenda 2030 goals."): None,
    # --- Target Group ---
    (
        "Target Group",
        "Select a primary target group for the project's activities during the project period?",
    ): None,
    (
        "Target Group",
        "Optionally, select one or more secondary target groups for the project's activities during the project period",
    ): None,
    ("Target Group", "Describe the project's target group and their needs"): (
        "4 - Target group",
        "target_group_need",
    ),
    ("Target Group", "What is your previous experience with the target group?"): (
        "4 - Target group",
        "target_group_experience",
    ),
    (
        "Target Group",
        "How have you worked to include the target group in the preparations for the project?",
    ): ("4 - Target group", "involvement_preparation"),
    (
        "Target Group",
        "Which main industry do you expect the project's activities to contribute to?",
    ): None,
    (
        "Target Group",
        "How will you work to include the target group in the implementation of the project?",
    ): ("4 - Target group", "involvement_implementation"),
    (
        "Target Group",
        "In what way will your work packages impact the global goals? What risks of goal conflicts have you identified? And if so, how will you manage the identified goal conflicts?",
    ): None,
    ("Target Group", "Where will the results arise?"): None,
    (
        "Target Group",
        "Capacity – what will the target group or target object gain access to?",
    ): None,
    (
        "Target Group",
        "What changed behaviors are the strengthened capabilities expected to lead to in the target group or target object?",
    ): None,
    # --- Activities (work packages) ---
    ("Activities", "Name of work package"): (
        "6 - Work-package generator",
        "work_packages",
    ),
    (
        "Activities",
        "Description how the work package contributes to the project goal",
    ): ("6 - Work-package generator", "work_packages"),
    ("Activities", "Start date"): None,
    ("Activities", "End date"): None,
    ("Activities", "Name of activity"): None,
    ("Activities", "cost"): None,
    ("Activities", "Description of activity"): None,
    ("Activities", "how will your work packages impact to global goals"): None,
    # --- Expected Results ---
    ("Expected Results", "Where will the results arise?"): None,
    (
        "Expected Results",
        "Capacity/Ability - what will the target group or target object gain access to",
    ): None,
    (
        "Expected Results",
        "What changed behaviors are the strengthened capabilities expected to lead to in the target group or target object?",
    ): None,
    ("Expected Results", "Target Value"): None,
    ("Expected Results", "remarks"): None,
    # --- Organization ---
    (
        "Organization",
        "How will the project's organization be structured to implement the project?",
    ): None,
    (
        "Organization",
        "What other similar projects or activities are you aware of?",
    ): None,
    (
        "Organization",
        "How will you internally in the project organization work for an inclusive culture for equal opportunities to influence the project's direction and results?",
    ): None,
    (
        "Organization",
        "Describe what sustainability expertise exists within the project organization, or is intended to be recruited for the project?",
    ): None,
    (
        "Organization",
        "Will you, in the implementation of your project, work with other actors than those who are part of your project organization?",
    ): None,
    (
        "Organization",
        "Describe what kind of work will be carried out and with which actors, and how it will contribute to the project's implementation.",
    ): None,
    (
        "Organization",
        "Are you seeking support for activities that contribute to the implementation of the Baltic Sea Strategy?",
    ): None,
    (
        "Organization",
        "How does the collaboration contribute to the goals of the Baltic Sea Strategy?",
    ): None,
    # --- Working Method ---
    (
        "Working Method",
        "How have you ensured in the project planning that you have the ability to report and account for costs and activities in the project?",
    ): None,
    ("Working Method", "How are you going to work with communication?"): None,
    (
        "Working Method",
        "Do you have a documented routine for the collection and reporting of gender-disaggregated statistics?",
    ): None,
    (
        "Working Method",
        "Will you follow up and report on the gender distribution of participants to the Swedish Agency for Economic and Regional Development?",
    ): None,
    ("Working Method", "How will you work with procurement in the project?"): None,
    (
        "Working Method",
        "How have you ensured the project's co-financing and management of the project's liquidity?",
    ): None,
    (
        "Working Method",
        "What risks have you identified in the project and what measures do you propose?",
    ): ("5 - Agenda 2030 & risk", "risks"),
    (
        "Working Method",
        "Describe, based on your current guidelines, how you will take these into account in your project?",
    ): None,
    (
        "Working Method",
        "Describe how you will work to document, disseminate, and utilize results during the project period? Also describe how you will ensure that the results are utilized during the project period?",
    ): None,
    # --- Budget, Contacts, Attachments ---
    ("Budget", "Budget and financing for the project."): None,
    ("Contacts", "Project contact persons."): None,
    ("Attachments", "Upload attachments"): None,
}


# field_mapping_dashboard = {
#     # --- Overview ---
#     ("Overview", "Project name"): "user_filledindashboard",  # Not collected in wizard
#     ("Overview", "Project start date*"): "user_filledindashboard",
#     ("Overview", "Project end date*"): "user_filledindashboard",
#     (
#         "Overview",
#         "In which municipality or municipalities will the efforts be implemented?",
#     ): "wizard_filled",  # ("3 - Programme & geography", "regions"),
#     ("Overview", "Are you looking for funding for a feasibility study?"): "llm",
#     ("Overview", "Are you looking for financing for a framework project?"): "llm",
#     ("Overview", "Describe the support scheme for the framework project"): "llm",
#     (
#         "Overview",
#         "Has the project carried out the sustainability analysis described in the EU Handbook?",
#     ): "llm",
#     ("Overview", "Are you applying for financing to invest in infrastructure?"): "llm",
#     (
#         "Overview",
#         "I certify that the investment has a lifespan of at least 5 years after the project is completed",
#     ): "llm",
#     (
#         "Overview",
#         "I certify that the project has implemented climate proofing of infrastructure investments that have a expected lifespan of at least 5 years",
#     ): "llm",
#     ("Overview", "Summarize the project"): "llm",
#     # --- Project Owner ---
#     (
#         "Project Owner",
#         "Organization number",
#     ): "wizard_filled",  # ("1 - Organisation & contact", "registration_number"),
#     (
#         "Project Owner",
#         "Organization name",
#     ): "wizard_filled",  # ("1 - Organisation & contact", "organisation_name"),
#     ("Project Owner", "Legal code / Form"): "llm",
#     ("Project Owner", "Industry code/name"): "llm",
#     ("Project Owner", "Country"): "llm",
#     ("Project Owner", "VAT registration number (optional)"): "llm",
#     (
#         "Project Owner",
#         "Is the organization covered by the Public Procurement Act or other procurement legislation?",
#     ): "wizard_filled",  # ("1 - Organisation & contact", "subject_to_lou"),
#     ("Project Owner", "Organization website"): "llm",
#     (
#         "Project Owner",
#         "Have you included VAT as a cost when calculating your budget?",
#     ): "llm",
#     ("Project Owner", "Select payment method"): "llm",
#     ("Project Owner", "Bank/Plusgiro account number"): "llm",
#     ("Project Owner", "Application for advance payment"): "llm",
#     # --- Project Partner ---
#     ("Project Partner", "Organization number"): "user_filledindashboard",
#     ("Project Partner", "Name"): "user_filledindashboard",
#     ("Project Partner", "post code"): "user_filledindashboard",
#     ("Project Partner", "visiting adress"): "user_filledindashboard",
#     ("Project Partner", "city"): "user_filledindashboard",
#     ("Project Partner", "industry code"): "llm",
#     ("Project Partner", "VAT registration number (optional)"): "llm",
#     (
#         "Project Partner",
#         "Is the organization covered by the Public Procurement Act or other procurement legislation?",
#     ): "llm",
#     ("Project Partner", "State who is the organization's authorized signatory"): "llm",
#     (
#         "Project Partner",
#         "Have you included VAT as a cost when calculating your budget?",
#     ): "llm",
#     # --- Challenges and Needs ---
#     (
#         "Challenges and Needs",
#         "Briefly describe your project goal. The project goal should describe the state that has been achieved at the end of the project. It should have a clear connection to the specific objective in the call.",
#     ): "wizard_filled",  # ("2 - Project idea", "smart_project_goal"),
#     (
#         "Challenges and Needs",
#         "Which challenge in the call for proposals will the project contribute to solving?",
#     ): "wizard_filled",  # ("2 - Project idea", "current_situation_challenges"),
#     (
#         "Challenges and Needs",
#         "Describe the current situation that the project will contribute to changing.",
#     ): "wizard_filled",  # ("2 - Project idea", "current_situation_challenges"),
#     (
#         "Challenges and Needs",
#         "Which of the global goals in Agenda 2030 is the project expected to contribute to in the region in the long term?",
#     ): "wizard_filled",  # ("5 - Agenda 2030 & risk", "sdg_goals"),
#     ("Challenges and Needs", "Justify the choice of Agenda 2030 goals."): "llm",
#     # --- Target Group ---
#     (
#         "Target Group",
#         "Select a primary target group for the project's activities during the project period?",
#     ): "user_filledindashboard",
#     (
#         "Target Group",
#         "Optionally, select one or more secondary target groups for the project's activities during the project period",
#     ): "user_filledindashboard",
#     (
#         "Target Group",
#         "Describe the project's target group and their needs",
#     ): "wizard_filled",  # ("4 - Target group", "target_group_need"),
#     (
#         "Target Group",
#         "What is your previous experience with the target group?",
#     ): "wizard_filled",  # ("4 - Target group", "target_group_experience"),
#     (
#         "Target Group",
#         "How have you worked to include the target group in the preparations for the project?",
#     ): "wizard_filled",  # ("4 - Target group", "involvement_preparation"),
#     (
#         "Target Group",
#         "Which main industry do you expect the project's activities to contribute to?",
#     ): "user_filledindashboard",
#     (
#         "Target Group",
#         "How will you work to include the target group in the implementation of the project?",
#     ): "wizard_filled",  # ("4 - Target group", "involvement_implementation"),
#     (
#         "Target Group",
#         "In what way will your work packages impact the global goals? What risks of goal conflicts have you identified? And if so, how will you manage the identified goal conflicts?",
#     ): "llm",
#     ("Target Group", "Where will the results arise?"): "llm",
#     (
#         "Target Group",
#         "Capacity – what will the target group or target object gain access to?",
#     ): "llm",
#     (
#         "Target Group",
#         "What changed behaviors are the strengthened capabilities expected to lead to in the target group or target object?",
#     ): "llm",
#     # --- Activities (work packages) ---
#     (
#         "Activities",
#         "Name of work package",
#     ): "wizard_filled",  # ("6 - Work-package generator", "work_packages"),
#     (
#         "Activities",
#         "Description how the work package contributes to the project goal",
#     ): "wizard_filled",  # ("6 - Work-package generator", "work_packages"),
#     ("Activities", "Start date"): "user_filledindashboard",
#     ("Activities", "End date"): "user_filledindashboard",
#     ("Activities", "Name of activity"): "user_filledindashboard",
#     ("Activities", "cost"): "user_filledindashboard",
#     ("Activities", "Description of activity"): "user_filledindashboard",
#     ("Activities", "how will your work packages impact to global goals"): "llm",
#     # --- Expected Results ---
#     ("Expected Results", "Where will the results arise?"): "llm",
#     (
#         "Expected Results",
#         "Capacity/Ability - what will the target group or target object gain access to",
#     ): "llm",
#     (
#         "Expected Results",
#         "What changed behaviors are the strengthened capabilities expected to lead to in the target group or target object?",
#     ): "llm",
#     ("Expected Results", "Target Value"): "user_filledindashboard",
#     ("Expected Results", "remarks"): "llm",
#     # --- Organization ---
#     (
#         "Organization",
#         "How will the project's organization be structured to implement the project?",
#     ): "llm",
#     (
#         "Organization",
#         "What other similar projects or activities are you aware of?",
#     ): "llm",
#     (
#         "Organization",
#         "How will you internally in the project organization work for an inclusive culture for equal opportunities to influence the project's direction and results?",
#     ): "llm",
#     (
#         "Organization",
#         "Describe what sustainability expertise exists within the project organization, or is intended to be recruited for the project?",
#     ): "llm",
#     (
#         "Organization",
#         "Will you, in the implementation of your project, work with other actors than those who are part of your project organization?",
#     ): "llm",
#     (
#         "Organization",
#         "Describe what kind of work will be carried out and with which actors, and how it will contribute to the project's implementation.",
#     ): "llm",
#     (
#         "Organization",
#         "Are you seeking support for activities that contribute to the implementation of the Baltic Sea Strategy?",
#     ): "llm",
#     (
#         "Organization",
#         "How does the collaboration contribute to the goals of the Baltic Sea Strategy?",
#     ): "llm",
#     # --- Working Method ---
#     (
#         "Working Method",
#         "How have you ensured in the project planning that you have the ability to report and account for costs and activities in the project?",
#     ): "llm",
#     ("Working Method", "How are you going to work with communication?"): "llm",
#     (
#         "Working Method",
#         "Do you have a documented routine for the collection and reporting of gender-disaggregated statistics?",
#     ): "llm",
#     (
#         "Working Method",
#         "Will you follow up and report on the gender distribution of participants to the Swedish Agency for Economic and Regional Development?",
#     ): "llm",
#     ("Working Method", "How will you work with procurement in the project?"): "llm",
#     (
#         "Working Method",
#         "How have you ensured the project's co-financing and management of the project's liquidity?",
#     ): "llm",
#     (
#         "Working Method",
#         "What risks have you identified in the project and what measures do you propose?",
#     ): "wizard_filled",  # ("5 - Agenda 2030 & risk", "risks"),
#     (
#         "Working Method",
#         "Describe, based on your current guidelines, how you will take these into account in your project?",
#     ): "llm",
#     (
#         "Working Method",
#         "Describe how you will work to document, disseminate, and utilize results during the project period? Also describe how you will ensure that the results are utilized during the project period?",
#     ): "llm",
#     # --- Budget, Contacts, Attachments ---
#     ("Budget", "Budget and financing for the project."): "user_filledindashboard",
#     ("Contacts", "Project contact persons."): "user_filledindashboard",
#     ("Attachments", "Upload attachments"): "user_filledindashboard",
# }
