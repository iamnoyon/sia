from sqlalchemy import Column
from sqlalchemy.dialects.mysql import MEDIUMTEXT, VARCHAR, BOOLEAN, DATETIME, LONGTEXT, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Members(Base):

    __tablename__ = 'member'
    __table_args__ = {'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_bin'}

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    internal_id = Column(INTEGER, unique=True, nullable=False)
    url = Column(VARCHAR(350))

    publication_time = Column(DATETIME)
    has_video = Column(BOOLEAN)
    category = Column(MEDIUMTEXT)
    subcategory = Column(MEDIUMTEXT)
    title = Column(MEDIUMTEXT)
    subtitle = Column(MEDIUMTEXT)
    text = Column(LONGTEXT)
    main_image_url = Column(MEDIUMTEXT)


def create_all(engine):
    print("creating databases")
    Base.metadata.create_all(engine)
