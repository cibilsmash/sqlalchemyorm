from base import  Base, Session, Employee, Department, Dep_Emp, Dep_Man, Salary, Title




session = Session()


q = session.query(Employee)

for c in q:

    print(c.emp_no, c.first_name)

one = session.query(Employee).first()

print(one.first_name)

get_one = session.query(Employee).get(4)

print(get_one.first_name)

filter_query = session.query(Employee).filter(Employee.emp_no <= 5).all()

for c in filter_query:
    print(c.last_name)

emp4 = session.query(Employee).filter(Employee.emp_no == 4).first()

dep4 = session.query(Department).filter(Department.dep_no == 4).first()


dep_man4 = Dep_Man(department=dep4, employee=emp4)


between = session.query(Salary).filter(Salary.salary.between(20000, 40000)).all()

for sal in between:

    print(sal.employee.first_name)

for_like = session.query(Employee).filter(Employee.first_name.like("%j")).all()

for like in for_like:
    print(like.first_name)

first_name = "bevin"

last_name = "wilson"

birth_date = '1996-12-07'

gender = 'M'

hire_date = '2019-09-12'

new_emp = Employee(
    birth_date=birth_date,
    first_name=first_name,
    last_name=last_name,
    gender=gender,
    hire_date=hire_date

)




def Add_Department():
    dep_name = input("Enter Department Name: ")

    new_dep = Department(
        dep_name=dep_name
    )
    session = Session()

    session.add(new_dep)

    session.commit()


emp_limit = session.query(Employee).limit(2).all()

for el in emp_limit:
    print("_____________")
    print(el.last_name)


for_join = session.query(Employee,Salary).join(Salary).all()

for fj in for_join:

    print(fj.Employee.first_name, fj.Salary.salary)

