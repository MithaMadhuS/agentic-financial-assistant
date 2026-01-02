from llms.openai_clients import client

def evaluate_feasibility(user, fire_result, target_years):
    prompt = f"""
You are a financial advisor evaluating FIRE feasibility.

User details:
- Age: {user['age']}
- Current corpus: {user['current_corpus']}
- Monthly income: {user['monthly_salary']}
- Monthly expense: {user['monthly_expense']}

Computed FIRE data:
- Required FIRE corpus: {fire_result['fire_corpus']}
- Estimated corpus in {target_years} years: {fire_result['projected_corpus']}

Task:
1. Decide if FIRE is achievable within {target_years} years
2. Explain reasoning
3. Suggest what needs to change if not achievable

Respond ONLY in JSON:
{{
  "achievable": true | false,
  "reasoning": "short explanation",
  "suggestions": ["list", "of", "actions"]
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0
    )

    return response.choices[0].message.content
