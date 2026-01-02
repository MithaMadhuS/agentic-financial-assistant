import json
from llms.openai_clients import extract_fire_inputs
from agents.intent_agent import classify_intent
from agents.validation_agent import ValidationAgent
from agents.fire_agent import FireAgent
from agents.fire_feasibility import evaluate_feasibility
from agents.advisor_agent import AdvisorAgent


def run_fire(query: str,state):
    advisor = AdvisorAgent()
    validator = ValidationAgent()
    fire_agent = FireAgent()

    # 1️⃣ Extract structured data from query (LLM)
    extracted = extract_fire_inputs(query)
    new_data = json.loads(extracted)
    for k, v in new_data.items():
        if v is not None:
            state.user_data[k] = v

    # 2️⃣ Validate minimum required info
    validation = validator.run(state.user_data)
    if not validation["valid"]:
        state.missing_fields = validation["missing_fields"]
       # return advisor.ask_for_missing_info(validation)
        return {
            "status": "NEED_INPUT",
            "message": advisor.ask_for_missing_fields(
                validation["missing_fields"]
            )
        }

    # 3️⃣ Classify user intent (LLM)
    intent_result = json.loads(classify_intent(query))
    intent = intent_result["intent"]

    # 4️⃣ Run deterministic FIRE calculations
    fire_result = fire_agent.run(state.user_data)

    # 5️⃣ Branch based on intent
    if intent == "fire_feasibility":
        target_years = state.user_data.get("target_years")

        if not target_years:
            return advisor.ask_for_target_years()

        feasibility = json.loads(
            evaluate_feasibility(
                user=user,
                fire_result=fire_result,
                target_years=target_years
            )
        )

        state.completed =True

        return advisor.explain_feasibility(
            fire_result=fire_result,
            feasibility=feasibility
        )

    # 6️⃣ Default: normal FIRE estimation
    return {
        "status" : "DONE",
        "message" : advisor.explain_fire(fire_result)
    }
