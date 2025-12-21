import json
from llms.openai_clients import extract_fire_inputs
from tools.fire_tools import fire_estimate
from agents.validation_agent import ValidationAgent

class FireAgent:
    def run(self, query: str):
        extracted = extract_fire_inputs(query)
        user = json.loads(extracted)

        validator = ValidationAgent()
        validation_result = validator.run(user)

        if not validation_result["valid"]:
            missing = ", ".join(validation_result["missing_fields"])
            return {
                "error": True,
                "message": (
                    "Required information not present. "
                    "Please provide your age, monthly income, "
                    "and approximate monthly expenditure."
                ),
                "missing_fields": missing
            }

        return fire_estimate(
            age=user["age"],
            monthly_income=user["monthly_income"],
            monthly_expense=user["monthly_expense"]
        )
