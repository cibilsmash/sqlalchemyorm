from sqlalchemy import create_engine, MetaData, Table, Integer, String, Enum, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, sessionmaker, Session

from datetime import datetime


engine = create_engine(
    "mysql+mysqldb://root:Mariaselvam@96@localhost/sqlalchemyorm")

Base = declarative_base()


Session = sessionmaker(bind=engine)


class Employee(Base):

    __tablename__ = 'employees'

    emp_no = Column(Integer(), primary_key=True)
    birth_date = Column(DateTime(), default=datetime.date)
    first_name = Column(String(14), nullable=False)

    last_name = Column(String(16), nullable=False)

    gender = Column(Enum('M', 'F'))

    hire_date = Column(DateTime(), default=datetime.now)

    dep_emp_map = relationship("DepartmentEmployee", backref='employee')

    dep_man_map = relationship("DepartmentManager", backref='employee')

    salary = relationship("Salary", backref='employee')

    title = relationship("Title", backref='employee')


class Department(Base):

    __tablename__ = 'departments'

    dep_no = Column(Integer(), primary_key=True)

    dep_name = Column(String(40))

    dep_emp_map = relationship("DepartmentEmployee", backref='department')

    dep_man_map = relationship("DepartmentManager", backref='department')


class DepartmentEmployee(Base):

    __tablename__ = 'departmentemployees'

    id = Column(Integer(), primary_key=True)

    emp_no = Column(Integer(), ForeignKey(Employee.emp_no))

    dep_no = Column(Integer(), ForeignKey(Department.dep_no))

    from_date = Column(DateTime(), default=datetime.now)

    to_date = Column(DateTime(), default=datetime.now)


class DepartmentManager(Base):

    __tablename__ = 'departmentmanagers'

    id = Column(Integer(), primary_key=True)

    dep_no = Column(Integer(), ForeignKey(Department.dep_no))

    emp_no = Column(Integer(), ForeignKey(Employee.emp_no))

    from_date = Column(DateTime(), default=datetime.now)

    to_date = Column(DateTime(), default=datetime.now)


class Salary(Base):

    __tablename__ = 'salaries'

    id = Column(Integer(), primary_key=True)

    emp_no = Column(Integer(), ForeignKey(Employee.emp_no))

    salary = Column(Integer())

    from_date = Column(DateTime(), default=datetime.now)

    to_date = Column(DateTime(), default=datetime.now)


class Title(Base):

    __tablename__ = 'titles'

    id = Column(Integer(), primary_key=True)

    emp_no = Column(Integer(), ForeignKey(Employee.emp_no))

    title = Column(String(40), nullable=False)

    from_date = Column(DateTime(), default=datetime.now)

    to_date = Column(DateTime(), default=datetime.now)

def seed():
    

    print("Enter 1 to create tables: ")

    print("Enter 2 to delete tables: ")

    print("Enter 3 to Insert Dummy values to all tables")

    num = int(input("Choose your option: "))

    if num == 1:
        Base.metadata.create_all(engine)

    elif num == 2:
        Base.metadata.drop_all(engine)

    elif num == 3:

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

        dep_emp2 = DepartmentEmployee(
            employee=emp2,
            department=dep2,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )

        dep_emp3 = DepartmentEmployee(
            employee=emp3,
            department=dep3,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )

        dep_emp4 = DepartmentEmployee(
            employee=emp4,
            department=dep4,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )
        dep_emp5 = DepartmentEmployee(
            employee=emp5,
            department=dep5,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )
        dep_emp6 = DepartmentEmployee(
            employee=emp6,
            department=dep6,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )

        session.add_all([dep_emp2, dep_emp3, dep_emp4, dep_emp5, dep_emp6])

        dep_man2 = DepartmentManager(
            employee=emp2,
            department=dep2,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )

        dep_man3 = DepartmentManager(
            employee=emp3,
            department=dep3,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )

        session.add_all([dep_man2, dep_man3])

        sal2 = Salary(
            employee=emp2,
            salary=200000,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )
        sal3 = Salary(
            employee=emp3,
            salary=20000,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )
        sal4 = Salary(
            employee=emp4,
            salary=40000,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )
        sal5 = Salary(
            employee=emp5,
            salary=300000,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )
        sal6 = Salary(
            employee=emp6,
            salary=30000,
            from_date='2020-04-04',
            to_date='2023-04-04'
        )

        session.add_all([sal2, sal3, sal4, sal5, sal6])

        tit2 = Title(
            employee=emp2,
            title="Operating System",
            from_date='2020-04-04',
            to_date='2023-04-04')

        tit3 = Title(
            employee=emp3,
            title="Machine Learning",
            from_date='2020-04-04',
            to_date='2023-04-04')

        tit4 = Title(
            employee=emp4,
            title="Circuits Systems and Signal Processing",
            from_date='2020-04-04',
            to_date='2023-04-04')
        tit5 = Title(
            employee=emp5,
            title="Electrical Basics",
            from_date='2020-04-04',
            to_date='2023-04-04')
        tit6 = Title(
            employee=emp6,
            title="Surveying",
            from_date='2020-04-04',
            to_date='2023-04-04')

        session.add_all([tit2, tit3, tit4, tit5, tit6])

        session.commit()

    else:
        print("You are Out of Options")
    


seed()
