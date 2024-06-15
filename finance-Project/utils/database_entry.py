from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from urllib.parse import quote_plus

def data_entry(password,table_name,data):
    # SQLAlchemy setup
    engine = create_engine("postgresql://postgres:%s@localhost:5432/finance" % quote_plus(password))
    Base = declarative_base()

    class YourTable(Base):
        __tablename__ = table_name
        complaint_id = Column(Integer, primary_key=True)
        date_received = Column(String)
        date_sent_to_company = Column(String)
        product = Column(String)
        consumer_complaint_narrative = Column(String)
        issue = Column(String)
        subissue = Column(String)
        company = Column(String)
        state = Column(String)
        submittedvia = Column(String)
        timelyresponse = Column(String)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create an instance of YourTable and insert data
    new_row = YourTable(complaint_id=data['Complaint ID'], date_received=data['Date received'], date_sent_to_company=data['Date sent to company'],product=data['Product'],issue=data['Issue'],subissue=data['Sub-issue'],company=data['Company'],state=data['State'],submittedvia=data['Submitted via'],timelyresponse=data['Timely response?'],consumer_complaint_narrative=data['Consumer complaint narrative'])
    session.add(new_row)
    session.commit()