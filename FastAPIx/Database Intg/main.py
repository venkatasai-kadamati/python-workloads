from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List
import schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


# dependency with the db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# endpoints
# 1. create an employee
@app.post('/employees', response_model=schemas.EmployeeOut)
def create_emp(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)


# 2. get all employees
@app.get('/employees', response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


# 3. get a specific employee
@app.get('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee_specific(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_specific_emp(db, emp_id)
    if employee is None:
        raise HTTPException(400, 'Employee Not Found')
    return employee


# 4. updating an employee
@app.put('/employees/{emp_id}', response_model=schemas.EmployeeUpdate)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(404, 'Employee Not Found')
    return db_employee


# 5. deleting an employee
@app.delete('/employee/{emp_id}', response_model=dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    output = crud.delete_employee(db, emp_id)
    if output is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return {'detail': 'employee deleted'}
