from models2 import Base, Member
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

#Create engine
db_uri = 'sqlite:///Ex2.db'
engine = create_engine(db_uri, echo=False)

# Create All tables
# Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = Member(
    name='kookki',
    description='im huh',
    vip=True,
    join_date=datetime.date.today(),
    number=40
)

#obj=session.query(Member).filter(Member.id==3).first()
#session.delete(obj)
#session.add(user)
session.query(Member)\
    .filter(Member.id== 2)\
    .update({Member.name:"Jonsan"})
session.commit()
print(user)