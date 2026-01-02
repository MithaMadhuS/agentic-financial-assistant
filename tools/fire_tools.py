def fire_estimate(
    age,
    monthly_salary,
    monthly_expense,
    current_corpus=0,
    projection_years=None,
    inflation=0.06,
    nominal_return=0.12,
    withdrawal_rate=0.04
):
    # 🔹 Convert to annual
    annual_expense_today = monthly_expense * 12
    annual_investment = max(monthly_salary - monthly_expense, 0) * 12

    # 🔹 Real return (economic reality)
    real_return = (1 + nominal_return) / (1 + inflation) - 1

    # 🔹 FIRE corpus in TODAY’s rupees (real terms)
    fire_corpus_real = annual_expense_today / withdrawal_rate

    # 🔹 Time to FIRE (real terms)
    corpus = current_corpus
    years = 0
    while corpus < fire_corpus_real:
        corpus = corpus * (1 + real_return) + annual_investment
        years += 1

    result = {
        "fire_corpus_real": round(fire_corpus_real),
        "years_to_fire": years,
        "retire_age": age + years,
        "real_return": round(real_return * 100, 2)
    }

    # 🔹 Projection if timeline provided
    if projection_years is not None:
        projected_corpus = current_corpus
        for _ in range(projection_years):
            projected_corpus = projected_corpus * (1 + real_return) + annual_investment

        result["projected_corpus_real"] = round(projected_corpus)
        result["projection_years"] = projection_years

    return result