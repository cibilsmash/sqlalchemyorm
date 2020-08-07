from sqlalchemy import Column, String, Integer, Date

from base import Base


class Actor(Base):
    __tablename__ = 'actor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday