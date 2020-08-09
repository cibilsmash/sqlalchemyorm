
from base import  Base, Session, Employees, Departments, Dep_emp, Dep_man, Salaries, Titles




session = Session()


q = session.query(Titles)

for c in q:
    print(c.employee.first_name)




t = session.query(Dep_emp)

for w in t:

    print(w.employee.last_name, w.department.dep_name)



