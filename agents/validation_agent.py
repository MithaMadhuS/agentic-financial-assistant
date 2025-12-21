class ValidationAgent:
    REQUIRED_FIELDS = ["age", "monthly_income", "monthly_expense"]

    def run(self, user_data: dict):
        missing = [
            field for field in self.REQUIRED_FIELDS
            if user_data.get(field) is None
        ]

        if missing:
            return {
                "valid": False,
                "missing_fields": missing
            }

        return {
            "valid": True
        }
