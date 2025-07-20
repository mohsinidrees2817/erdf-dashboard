from pydantic import BaseModel
from typing import List, Optional, Dict
from enum import Enum

class OrganisationContact(BaseModel):
    organisation_name: str
    registration_number: str
    contact_name: str
    email: str
    phone: str
    subject_to_lou: bool  # Yes/No
    
    # AI-filled fields
    applicant_legal_name: Optional[str] = None
    applicant_address: Optional[str] = None
    applicant_website: Optional[str] = None

# Step 2: Project Idea
class ProjectIdea(BaseModel):
    project_summary: str  # ≤ 1000 chars
    challenge_needs: Optional[str] = None  # AI-filled
    current_state: Optional[str] = None  # AI-filled
    smart_objective: Optional[str] = None  # AI-filled

# Step 3: Programme & Geography
class ProgrammeGeography(BaseModel):
    programme_area: str  # from dropdown
    regions: List[str]  # multi-select
    
    # AI-filled fields
    regional_strategy_citations: Optional[str] = None

# Step 4: Target Group
class TargetGroup(BaseModel):
    target_group_description: str  # ≤ 500 chars
    
    # AI-filled fields
    target_group_needs: Optional[str] = None  # incl. gender/diversity
    previous_experience: Optional[str] = None
    inclusion_in_preparation: Optional[str] = None
    inclusion_during_execution: Optional[str] = None

# Step 5: Agenda 2030 & Risk
class RiskType(str, Enum):
    LOW_PARTICIPATION = "Low participation"
    BUDGET_OVERRUN = "Budget overrun"
    TECH_DELAYS = "Tech delays"
    STAFF_TURNOVER = "Staff turnover"

class SDGGoal(str, Enum):
    GOAL_7 = "Goal 7"
    GOAL_9 = "Goal 9"
    GOAL_11 = "Goal 11"

class Agenda2030Risk(BaseModel):
    sdg_goals: List[SDGGoal]  # 1-2 goals
    risks: List[RiskType]  # up to 3 risks
    
    # AI-filled fields
    sdg_motivation: Optional[str] = None
    risk_analysis: Optional[str] = None
    risk_mitigation: Optional[str] = None
    investment_attestations: Optional[str] = None

# Step 6: Work Package
class WorkPackage(BaseModel):
    name: str
    purpose: Optional[str] = None  # AI-filled
    activities: Optional[str] = None  # AI-filled
    deliverables: Optional[str] = None  # AI-filled
    timeline: Optional[str] = None  # AI-filled
    budget_share: Optional[str] = None  # AI-filled
    kpi: Optional[str] = None  # optional, AI-filled

class WorkPackageGenerator(BaseModel):
    work_packages: List[WorkPackage]

# Step 7: Policies & Sign-off (updated to remove subject LOU)
class PolicyType(str, Enum):
    PROCUREMENT = "Procurement"
    REPORTING = "Reporting"
    OTHER = "Other"

class PoliciesSignOff(BaseModel):
    procurement_according_lou: bool  # Yes/No
    uploaded_policies: Optional[List[str]] = None  # list of filenames
    
    # AI-filled fields
    policy_section: Optional[str] = None
    reporting_routines: Optional[str] = None
    procurement_routines: Optional[str] = None

# Complete Application Structure
class ERDFApplication(BaseModel):
    organisation_contact: OrganisationContact
    project_idea: ProjectIdea
    programme_geography: ProgrammeGeography
    target_group: TargetGroup
    agenda_2030_risk: Agenda2030Risk
    work_packages: WorkPackageGenerator
    policies_sign_off: PoliciesSignOff