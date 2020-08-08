from sqlalchemy import create_engine, MetaData, Table, Integer, String,Enum, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, sessionmaker, Session

from datetime import datetime




engine = create_engine("mysql+mysqldb://root:Mariaselvam@96@localhost/sqlalchemyorm")

Base = declarative_base()


Session = sessionmaker(bind=engine)



class Employees(Base):

    __tablename__ = 'employees'

    emp_no = Column(Integer(), primary_key=True)

    birth_date = Column(DateTime(), default = datetime.now)

    first_name = Column(String(14), nullable=False)

    last_name = Column(String(16), nullable=False)

    hire_date = Column(DateTime(), default=datetime.now)

    dep_emp_map = relationship("Dep_emp", backref='employee')

    dep_man_map = relationship("Dep_man", backref='employee')

    salary = relationship("Salaries", backref='employee')

    title = relationship("Titles", backref= 'employee')

    



    


class Departments(Base):

    __tablename__ = 'departments'

   

    dep_no = Column(Integer(), primary_key=True)

    dep_name = Column(String(40))

    dep_emp_map = relationship("Dep_emp", backref='department')

    dep_man_map = relationship("Dep_man", backref='department')


class Dep_emp(Base):

    __tablename__ = 'dep_emp'

    id = Column(Integer(), primary_key=True)

    emp_no = Column(Integer(), ForeignKey(Employees.emp_no))

    dep_no = Column(Integer(), ForeignKey(Departments.dep_no))


class Dep_man(Base):

    __tablename__ = 'dep_man'

    id = Column(Integer(), primary_key=True)

    emp_no = Column(Integer(), ForeignKey(Employees.emp_no))

    dep_no = Column(Integer(), ForeignKey(Departments.dep_no))


class Salaries(Base):

    __tablename__ = 'salaries'

    id = Column(Integer(), primary_key=True)

    emp_no = Column(Integer(), ForeignKey(Employees.emp_no))

    salary = Column(Integer())


class Titles(Base):

    __tablename__ = 'titles'

    id = Column(Integer(), primary_key=True)

    emp_no = Column(Integer(), ForeignKey(Employees.emp_no))

    title = Column(String(40), nullable=False)




Base.metadata.drop_all(engine)













