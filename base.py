from sqlalchemy import create_engine, MetaData, Table, Integer, String,Enum, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, sessionmaker, Session

from datetime import datetime




engine = create_engine("mysql+mysqldb://root:Mariaselvam@96@localhost/sqlalchemyorm")

Base = declarative_base()


Session = sessionmaker(bind=engine)



class Employee(Base):

    __tablename__ = 'employees'

    emp_no = Column(Integer(), primary_key=True)

    birth_date = Column(DateTime(), default = datetime.date)

    first_name = Column(String(14), nullable=False)

    last_name = Column(String(16), nullable=False)

    gender = Column(Enum('M','F'))

    hire_date = Column(DateTime(), default=datetime.now)

    dep_emp_map = relationship("Dep_Emp", backref='employee')

    dep_man_map = relationship("Dep_Man", backref='employee')

    salary = relationship("Salary", backref='employee')

    title = relationship("Title", backref= 'employee')



class Department(Base):

    __tablename__ = 'departments'

    dep_no = Column(Integer(), primary_key=True)

    dep_name = Column(String(40))

    dep_emp_map = relationship("Dep_Emp", backref='department')

    dep_man_map = relationship("Dep_Man", backref='department')

    

class Dep_Emp(Base):

    __tablename__ = 'dep_emp'

    id = Column(Integer(), primary_key=True)

    emp_no = Column(Integer(), ForeignKey(Employee.emp_no))

    dep_no = Column(Integer(), ForeignKey(Department.dep_no))

    from_date = Column(DateTime(), default=datetime.now)

    to_date = Column(DateTime(), default=datetime.now)

    
class Dep_Man(Base):

    __tablename__ = 'dep_man'

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




Base.metadata.create_all(engine)















