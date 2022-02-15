from sqlalchemy import Column, Integer, String

from database import Base


class ExampleModel(Base):
    __tablename__ = "example"

    id = Column(Integer, primary_key=True)
    something = Column(String)
