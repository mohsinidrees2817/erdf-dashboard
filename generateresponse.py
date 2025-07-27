import streamlit as st

from openai import OpenAI

from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
import json
from pydantic import BaseModel
from typing import List, Optional

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# Step 1 - Organisation & contact
class AIOrganisationContact(BaseModel):
    applicant_legal_name: str
    applicant_address: str
    applicant_website: str


# Step 2 - Project idea
class AIProjectIdea(BaseModel):
    challenge_needs: str
    current_state: str
    smart_objective: str


# Step 3 - Programme & geography
class AIProgrammeGeography(BaseModel):
    regional_strategy_citations: str


# Step 4 - Target group
class AITargetGroup(BaseModel):
    target_group_needs: str
    previous_experience: str
    inclusion_in_preparation: str
    inclusion_during_execution: str


# Step 5 - Agenda 2030 & risk
class AIAgenda2030Risk(BaseModel):
    sdg_motivation: str
    risk_analysis: str
    risk_mitigation: str
    investment_attestations: str


# Step 6 - Work-package generator & Policies (Merged)
class AIWorkPackage(BaseModel):
    name: str
    purpose: str
    activities: str
    deliverables: str
    timeline: str
    budget_share: str
    kpi: Optional[str] = None


class AIWorkPackageGeneratorAndPolicies(BaseModel):
    work_packages: List[AIWorkPackage]
    policy_section: str
    reporting_routines: str
    procurement_routines: str


def generate_from_ai(step_name: str, user_input: dict, context: str = ""):
    """
    Generate AI response for wizard step with optional RAG context.
    
    Args:
        step_name: Name of the wizard step
        user_input: User's input data for the step (dictionary)
        context: Optional context retrieved from classification documents
    
    Returns:
        Structured AI response based on step requirements
    """
    step_model_map = {
        "1 - Organisation & contact": AIOrganisationContact,
        "2 - Project idea": AIProjectIdea,
        "3 - Programme & geography": AIProgrammeGeography,
        "4 - Target group": AITargetGroup,
        "5 - Agenda 2030 & risk": AIAgenda2030Risk,
        "6 - Work-package generator & Policies": AIWorkPackageGeneratorAndPolicies,  # Updated for merged step
    }

    model_class = step_model_map.get(step_name)
    if model_class is None:
        return f"❌ Error: Unknown step '{step_name}'"

    try:
        # Prepare the prompt with context if available
        user_prompt = f"User input for step '{step_name}':\n{str(user_input)}"
        
        if context and context.strip():
            user_prompt += f"\n\nRelevant context from classification documents:\n{context}"
            user_prompt += "\n\nPlease use the provided context to inform your response and ensure consistency with the document requirements."
        
        response = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant writing structured ERDF application sections. Use any provided context from classification documents to ensure your response aligns with the required format and standards.",
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            response_format=model_class,
            temperature=0.6,
            max_tokens=1000,
        )
        
        return response.choices[0].message.parsed  # returns a structured Pydantic object
    except Exception as e:
        return f"❌ Error during AI generation: {e}"


# def generate_work_packages_from_ai(user_input, client, max_tokens=1200):
#     """
#     Calls OpenAI Chat to generate 3–5 structured work packages as a list of dicts.
#     Returns: list of dicts (or empty list if failure)
#     """
#     system_prompt = (
#         "You are an ERDF funding assistant. Based on the user's project information, "
#         "generate 3–5 structured work packages.\n"
#         "Each package must include:\n"
#         "- name (short title)\n"
#         "- description (1–2 sentences summary)\n"
#         "- purpose\n"
#         "- activities (comma-separated or bullet points)\n"
#         "- deliverables\n"
#         "- timeline (e.g. Q1 2025, Month 2-6)\n"
#         "- budget_share (approximate % of total)\n"
#         "- kpi (optional, if relevant)\n\n"
#         "Respond only as a JSON list, like:\n"
#         "[\n"
#         "  {\n"
#         '    "name": "...",\n'
#         '    "description": "...",\n'
#         '    "purpose": "...",\n'
#         '    "activities": "...",\n'
#         '    "deliverables": "...",\n'
#         '    "timeline": "...",\n'
#         '    "budget_share": "...",\n'
#         '    "kpi": "..."\n'
#         "  },\n"
#         "  ...\n"
#         "]\n"
#         "If a field is not known, leave it as an empty string. DO NOT use markdown or any extra text."
#     )
#     user_prompt = f"User input for work packages:\n{user_input}"

#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-2024-08-06",
#             messages=[
#                 {"role": "system", "content": system_prompt},
#                 {"role": "user", "content": user_prompt},
#             ],
#             temperature=0.6,
#             max_tokens=max_tokens,
#             response_format={"type": "json_object"},
#         )
#         # The response will have .choices[0].message.content as a JSON string
#         json_text = response.choices[0].message.content
#         return json.loads(json_text)
#     except Exception as e:
#         print(f"AI generation error: {e}")
#         return []


def generate_work_packages_from_ai(
    user_input="", client=None, max_tokens=1200, test_mode=True
):
    import json

    if test_mode or client is None:
        # Return a realistic dummy response
        return [
            {
                "name": "Digital Needs Analysis",
                "description": "Assess SME digital maturity and readiness for digital transformation.",
                "purpose": "Understand digital gaps in target SMEs",
                "activities": "Survey, interviews, tech audit",
                "deliverables": "Digital maturity report",
                "timeline": "Q1 2025",
                "budget_share": "20%",
                "kpi": "Readiness score",
            },
            {
                "name": "Pilot Lab",
                "description": "Test innovative logistics solutions in a real-world environment.",
                "purpose": "Evaluate effectiveness of new technology",
                "activities": "Pilot setup, user training, data collection",
                "deliverables": "Pilot evaluation report",
                "timeline": "Q2 2025",
                "budget_share": "30%",
                "kpi": "Implementation success rate",
            },
            {
                "name": "SME Coaching",
                "description": "Provide tailored coaching sessions for SMEs to adopt digital tools.",
                "purpose": "Boost adoption of digital solutions",
                "activities": "Workshops, mentoring, troubleshooting",
                "deliverables": "Training attendance list, feedback forms",
                "timeline": "Q3 2025",
                "budget_share": "25%",
                "kpi": "Adoption rate",
            },
        ]

    # # ...the rest of your AI call code (unchanged) below...
    # system_prompt = (
    #     # (Same as before)
    # )
    # user_prompt = f"User input for work packages:\n{user_input}"

    # try:
    #     response = client.chat.completions.create(
    #         model="gpt-4o-2024-08-06",
    #         messages=[
    #             {"role": "system", "content": system_prompt},
    #             {"role": "user", "content": user_prompt},
    #         ],
    #         temperature=0.6,
    #         max_tokens=max_tokens,
    #         response_format={"type": "json_object"},
    #     )
    #     json_text = response.choices[0].message.content
    #     if json_text.strip().startswith("```"):
    #         json_text = json_text.strip().strip("`").strip("json").strip()
    #     data = json.loads(json_text)
    #     if isinstance(data, list):
    #         return data
    #     elif isinstance(data, dict):
    #         for key in ["work_packages", "packages", "WorkPackages", "data"]:
    #             if key in data and isinstance(data[key], list):
    #                 return data[key]
    #     return []
    # except Exception as e:
    #     print(f"AI generation error: {e}")
    #     return []
