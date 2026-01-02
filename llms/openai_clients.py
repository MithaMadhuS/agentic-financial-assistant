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
You are a deterministic financial data extraction engine.

Your task is to extract user financial information even if phrased differently.

Target Fields:
- age (integer, years)
- monthly_expense (integer, INR)
- monthly_salary (integer, INR)
- target_years (integer, years)
- current_corpus (integer, INR)

Synonym Mapping:
- monthly_expense may be referred to as: expense, expenditure, spending, monthly spend, cost of living
- monthly_salary may be referred to as: income, salary, earnings, pay
- target_years may be referred to as: 
  retire in X years, after X years, within X years, in another X years, X yrs, X years later
- current_corpus may be referred to as : savings, bank balance, current corpus, current savings.

Extraction Rules:
- Actively search for numbers related to expenses even if the word "monthly" appears later.
- If expense frequency is monthly, extract directly.
- If income frequency is yearly/annual/per annum, convert to monthly (divide by 12).
- If a retirement horizon is mentioned as a duration (e.g., "in another 10 years"), extract that number as target_years.
- If retirement is expressed as an age (e.g., "retire at 60"), compute:
  target_years = retirement_age - current age
- 1 lakh = 100000 INR.
- 1 crore = 10000000 INR.
- Return only integers.
- If multiple numbers exist, associate them using semantic meaning, not proximity.
- If a field cannot be confidently extracted, set it to null.
- If current corpus is not provided assume its zero

Output Rules:
- Return ONLY valid JSON
- No markdown
- No explanation
- No extra text

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
