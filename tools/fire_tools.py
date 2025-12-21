def fire_estimate(age, monthly_expense, monthly_salary):
    annual_expense = monthly_expense * 12
    fire_corpus = annual_expense / 0.04

    annual_investment = (monthly_salary - monthly_expense) * 12

    corpus = 0
    years = 0
    while corpus < fire_corpus:
        corpus = corpus * 1.12 + annual_investment
        years += 1

    return {
        "fire_corpus": round(fire_corpus),
        "years_to_fire": years,
        "retire_age": age + years
    }
