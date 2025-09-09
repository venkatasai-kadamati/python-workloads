from fastapi import FastAPI, HTTPException
from models_val import Employee
from typing import List

app = FastAPI()

employees_db: List[Employee] = []

# 1. Read all employees
@app.get("/employees", response_model=List[Employee])
def read_employees():
    return employees_db


# 2. Read the specific employee -> path parameter
# HTTPException has 2 parameters: status_code & detail
@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for employee in employees_db:
        if employee.id == emp_id:
            return employee
    raise HTTPException(status_code=404, detail='Employee Not Found')


# 3. Adding an employee
@app.post('/employees')
def add_employee(new_emp: Employee):
    for employee in employees_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail='Employee already exists')
    employees_db.append(new_emp)
    return new_emp


# 4. Update an Employee
@app.put('/update_employee/{emp_id}')
def update_employee(emp_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail='Employee not found')


# 5. Delete an Employee
@app.delete('/delete_employee/{emp_id}')
def delete_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            del employees_db[index]
            return {"message": "Employee Deleted successfully"}
    raise HTTPException(status_code=404, detail='Employee not found')