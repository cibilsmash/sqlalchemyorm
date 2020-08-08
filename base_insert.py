
from base import  Base, Session, engine, Employees, Departments, Dep_emp, Dep_man, Salaries, Titles


def seed():

    print("Enter 1 to create tables: ")

    print("Enter 2 to delete tables: ")

    num = int(input("Choose your option: "))

    if num == 1:
        Base.metadata.create_all(engine)

    elif num == 2:
        Base.metadata.drop_all(engine)

    else:
        print("Enter the number between this options")

seed()



session = Session()


emp2 = Employees(first_name = "cibil",  last_name = "smash")

dep2 = Departments(dep_name = "cse")


dep_emp2 = Dep_emp(employee = emp2,  department = dep2)


dep_man2 = Dep_man(employee = emp2,  department = dep2)


sal2 = Salaries(employee = emp2,  salary = 2000)


tit2 = Titles(employee = emp2, title = "Operating System")

tit3 = Titles(employee = emp2,title = "Databases")




session.add(emp2)

session.add(dep2)

session.add(dep_emp2)

session.add(dep_man2)



session.commit()




