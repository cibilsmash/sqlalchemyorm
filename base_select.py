from base import  Base, Session, Employees, Departments, Dep_emp, Dep_man, Salaries, Titles




session = Session()


q = session.query(Titles)

for c in q:
    print(c.employee.first_name)




k = session.query(Dep_emp)

for t in k:

    print(t.employee.last_name, t.department.dep_name)



