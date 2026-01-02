class AdvisorAgent:
    """
    Responsible ONLY for user-facing explanations.
    No calculations, no branching logic.
    """

    def ask_for_missing_fields(self, missing_fields):
        fields = ", ".join(missing_fields)

        return (
            "I need a bit more information to continue.\n"
            f"Please provide your: {fields}."
        )

    def ask_for_target_years(self):
        return """
⏳ Timeline Required

You asked whether FIRE is achievable within a certain time frame,
but I don’t see the target number of years.

Please tell me:
👉 In how many years are you aiming to achieve FIRE?
"""

    def explain_fire(self, fire_result):
        return f"""
📊 FIRE ESTIMATION

• FIRE Corpus (real terms): ₹{fire_result['fire_corpus_real']:,}
• Years to FIRE: {fire_result['years_to_fire']}
• Estimated Retirement Age: {fire_result['retire_age']}

Assumptions:
• Inflation-adjusted returns
• Expenses grow with inflation
• Consistent long-term investing
"""

    def explain_feasibility(self, fire_result, feasibility):
        status = "✅ ACHIEVABLE" if feasibility["achievable"] else "❌ NOT ACHIEVABLE"

        suggestions_text = ""
        if feasibility.get("suggestions"):
            suggestions_text = "\n".join(
                [f"• {s}" for s in feasibility["suggestions"]]
            )

        return f"""
📊 FIRE FEASIBILITY CHECK — {status}

Here’s an honest assessment of your goal:

🧠 Reasoning:
{feasibility['reasoning']}

📌 FIRE Reference:
• Required FIRE Corpus: ₹{fire_result['fire_corpus']:,}
• Estimated Retirement Age (baseline): {fire_result['retire_age']}

💡 What could improve feasibility:
{suggestions_text if suggestions_text else "• Your current plan is broadly aligned with your goal."}

If you want, we can now:
• Adjust assumptions (expenses, returns)
• Explore alternative timelines
• Stress-test this plan under different scenarios
"""
