import os
from dotenv import load_dotenv
from openai import OpenAI

# ✅ LOAD .env FILE
load_dotenv()

# ✅ VERIFY KEY IS LOADED
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found. Check .env loading.")

client = OpenAI(api_key=api_key)
 

def extract_fire_inputs(query: str):
    prompt = f"""
You are a JSON extraction engine.
You are a JSON extraction engine.

Extract the following fields from the text.
If a field is missing, set it to null.

Fields
- age (integer)
- monthly_expense (integer, INR)
- monthly_salary (integer, INR)

Rules:
- Return ONLY valid JSON
- Do NOT add explanations
- Do NOT use markdown
- Do NOT add text before or after JSON

Text:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )


    print("🔍 RAW LLM OUTPUT:\n", response.choices[0].message.content)   
    return response.choices[0].message.content
