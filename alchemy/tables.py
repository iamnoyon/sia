from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMTEXT, VARCHAR, BOOLEAN, DATETIME, LONGTEXT, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Members(Base):

    __tablename__ = 'member'
    __table_args__ = {'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_bin'}

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    member_id = Column(Integer, ForeignKey("memberoffice.member_id"))
    #internal_id = Column(INTEGER, unique=True, nullable=False)
    url = Column(VARCHAR(350))
    language = Column(VARCHAR(2))
    full_address = Column(VARCHAR(350))
    gender = Column(MEDIUMTEXT)
    name = Column(MEDIUMTEXT)
    education = Column(MEDIUMTEXT)
    address = Column(MEDIUMTEXT)
    city = Column(MEDIUMTEXT)
    zipcode = Column(MEDIUMTEXT)
    email = Column(MEDIUMTEXT)
    tel = Column(MEDIUMTEXT)
    fax = Column(MEDIUMTEXT)
    website = Column(MEDIUMTEXT)
    job = Column(MEDIUMTEXT)
    sector = Column(MEDIUMTEXT)
    group = Column(MEDIUMTEXT)
    section = Column(MEDIUMTEXT)
    #child = relationship("Child", back_populates="parents")

class Offices(Base):

    __tablename__ = 'office'
    __table_args__ = {'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_bin'}

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    office_id = Column(Integer, ForeignKey("memberoffice.officeid"))
    #internal_id = Column(INTEGER, unique=True, nullable=False)
    url = Column(VARCHAR(350))
    language = Column(VARCHAR(2))
    full_address = Column(VARCHAR(350))
    name = Column(MEDIUMTEXT)
    address = Column(MEDIUMTEXT)
    city = Column(MEDIUMTEXT)
    zipcode = Column(MEDIUMTEXT)
    email = Column(MEDIUMTEXT)
    tel = Column(MEDIUMTEXT)
    fax = Column(MEDIUMTEXT)
    website = Column(MEDIUMTEXT)
    sector = Column(MEDIUMTEXT)
    #child = relationship("Child", back_populates="parents")

class MemberOffice(Base):

    __tablename__ = 'memberoffice'
    __table_args__ = {'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_bin'}

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    member_id = Column(INTEGER, unique=True, nullable=True)
    officeid = Column(INTEGER, unique=True, nullable=True)
    created_date = Column(DATETIME)
    #child = relationship("Child", backref="parents")
def create_all(engine):
    print("creating databases")
    Base.metadata.create_all(engine)
