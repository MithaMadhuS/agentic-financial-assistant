from tools.fire_tools import fire_estimate

class FireAgent:
    def run(self, user):
        return fire_estimate(
            age=user["age"],
            monthly_salary=user["monthly_salary"],
            monthly_expense=user["monthly_expense"],
            current_corpus=user.get("current_corpus", 0),
            projection_years=user.get("target_years")
        )
