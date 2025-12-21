class AdvisorAgent:
    def run(self, result):
        if result.get("error"):
            return f"""
⚠️ Missing Information

{result['message']}
Missing fields: {result['missing_fields']}
"""

        return f"""
📊 FIRE ESTIMATION

• FIRE Corpus Needed: ₹{result['fire_corpus']}
• Years to FIRE: {result['years_to_fire']}
• Estimated Retirement Age: {result['retire_age']}

Assumptions:
- 12% returns
- 4% withdrawal rule
"""
