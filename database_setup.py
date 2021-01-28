import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# создание экземпляра declarative_base
Base = declarative_base()


class ActivateCodes(Base):
    __tablename__ = 'ActivateCodes'

    id = Column(Integer, primary_key=True)
    code = Column(String(250), nullable=False)
    user_id = Column(String(250))

# создает экземпляр create_engine в конце файла
engine = create_engine('sqlite:///ActivateCodes.db')
Base.metadata.create_all(engine)


