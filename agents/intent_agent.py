from llms.openai_clients import client

def classify_intent(query: str):
    prompt = f"""
Classify the user's intent.

Possible intents:
- fire_estimation
- fire_feasibility
- fire_advisory
- missing_info
- general_question

User query:
{query}

Respond ONLY in JSON:
{{ "intent": "<one_of_the_above>" }}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0
    )

    return response.choices[0].message.content