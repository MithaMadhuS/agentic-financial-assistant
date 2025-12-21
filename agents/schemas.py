from pydantic import BaseModel

class FireInput(BaseModel):
    age: int
    monthly_expense: int
    monthly_salary: int
