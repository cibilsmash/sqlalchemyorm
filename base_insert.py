
from base import  Base, Session, engine, Employee, Department, \
    Dep_Emp, Dep_Man, Salary, Title

    

session = Session()

emp2 = Employee(
    first_name="cibil",
    last_name="smash",
    birth_date='2008-11-11',
    gender='M',
    hire_date='2020-04-04'
     )

emp3 = Employee(
    first_name="varun",
    last_name="vignrsh",
    birth_date='2008-11-11',
    gender='M',
    hire_date='2020-04-04'
     )

emp4 = Employee(
    first_name="angel",
    last_name="will",
    birth_date='2008-11-11',
    gender='F',
    hire_date='2020-04-04'
     )

emp5 = Employee(
    first_name="kuty",
    last_name="john",
    birth_date='2008-11-11',
    gender='M',
    hire_date='2020-04-04'
     )
emp6 = Employee(
    first_name="jose",
    last_name="jones",
    birth_date='2008-11-11',
    gender='M',
    hire_date='2020-04-04'
     )



session.add_all([emp2, emp3, emp4, emp5, emp6]) 



dep2 = Department(dep_name="CSE")


dep3 = Department(dep_name="MECH")


dep4 = Department(dep_name="EEE")


dep5 = Department(dep_name="ECE")


dep6 = Department(dep_name="CIVIL")


session.add_all([dep2, dep3, dep4, dep5, dep6])


dep_emp2 = Dep_Emp(
    employee=emp2,
    department=dep2,
    from_date='2020-04-04',
    to_date='2023-04-04'
    )

session.add(dep_emp2)

dep_man2 = Dep_Man(
    employee=emp2,
    department=dep2,
    from_date='2020-04-04',
    to_date='2023-04-04'
    )

session.add(dep_man2)

sal2 = Salary(
    employee=emp2,
    salary = 2000,
    from_date='2020-04-04',
    to_date='2023-04-04'
    )


session.add(sal2)

tit2 = Title(
    employee=emp2,
    title="Operating System",
    from_date='2020-04-04',
    to_date='2023-04-04')

tit3 = Title(
    employee=emp2,
    title="Databases",
    from_date='2020-04-04',
    to_date='2023-04-04')

session.add_all([tit2, tit3])


session.commit()





