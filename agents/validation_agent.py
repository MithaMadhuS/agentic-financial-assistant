class ValidationAgent:
    REQUIRED_FIELDS = ["age", "monthly_salary", "monthly_expense"]

    def run(self, user_data: dict):

        #print("user_date", user_data)
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
