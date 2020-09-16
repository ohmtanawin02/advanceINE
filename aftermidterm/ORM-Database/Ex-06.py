from models import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

#Create engine
db_uri = 'sqlite:///Ex2.db'
engine = create_engine('sqlite:///user.db', echo=False)

# Create All tables
# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = Member(
    name='toddy',
    description='im testing this',
    vip=True,
    join_date=datetime.date.today(),
    number=45.0
)

session.add(user)
session.commit()
print(user)