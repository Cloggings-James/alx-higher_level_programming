#!/usr/bin/python3
"""Script to filter states by name starting with 'N' using SQLAlchemy"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3])

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Define the State model
Base = declarative_base()


class State(Base):
    """State model"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(256), nullable=False)

# Filter and print states starting with 'N'
if __name__ == "__main__":
    try:
        # Query for states starting with 'N'
        states = session.query(State).filter(State.name.like('N%')).order_by(State.id).all()

        # Display the results
        for state in states:
            print("({}, '{}')".format(state.id, state.name))

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)
        sys.exit(1)

