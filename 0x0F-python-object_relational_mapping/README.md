## 0x0F. Python - Object-relational mapping

This repository contains Python scripts for working with object-relational mapping (ORM) using SQLAlchemy and MySQL. Below is a summary of the key scripts in this repository:

### 0-select_states.py

- Lists all states from the database hbtn_0e_0_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module MySQLdb.
- Connects to a MySQL server on localhost at port 3306.
- Sorts results in ascending order by states.id.

### 1-filter_states.py

- Lists all states with names starting with 'N' (uppercase N) from the database hbtn_0e_0_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module MySQLdb.
- Connects to a MySQL server on localhost at port 3306.
- Sorts results in ascending order by states.id.

### 2-my_filter_states.py

- Displays all values in the states table of hbtn_0e_0_usa where the name matches the argument.
- Takes 4 arguments: MySQL username, MySQL password, database name, and state name searched.
- Uses the module MySQLdb.
- Connects to a MySQL server on localhost at port 3306.
- Uses format to create the SQL query with user input.
- Sorts results in ascending order by states.id.

### 3-my_safe_filter_states.py

- Similar to 2-my_filter_states.py but safe from MySQL injections.
- Takes 4 arguments: MySQL username, MySQL password, database name, and state name searched (safe from MySQL injection).
- Uses the module MySQLdb.
- Connects to a MySQL server on localhost at port 3306.
- Sorts results in ascending order by states.id.

### 4-cities_by_state.py

- Lists all cities from the database hbtn_0e_4_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module MySQLdb.
- Connects to a MySQL server on localhost at port 3306.
- Uses execute() once.
- Sorts results in ascending order by cities.id.

### 5-filter_cities.py

- Lists all cities of a given state from the database hbtn_0e_4_usa.
- Takes 4 arguments: MySQL username, MySQL password, database name, and state name (SQL injection free).
- Uses the module MySQLdb.
- Connects to a MySQL server on localhost at port 3306.
- Uses execute() once.
- Sorts results in ascending order by cities.id.

### model_state.py

- Contains the class definition of a State with SQLAlchemy.
- Represents a State with an id and name.
- Class attribute cities represents a relationship with the City class.

### 7-model_state_fetch_all.py

- Lists all State objects from the database hbtn_0e_6_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module SQLAlchemy.
- Connects to a MySQL server on localhost at port 3306.
- Sorts results in ascending order by states.id.

### 8-model_state_fetch_first.py

- Prints the first State object from the database hbtn_0e_6_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module SQLAlchemy.
- Connects to a MySQL server on localhost at port 3306.
- Displays the state with the lowest states.id.

### 9-model_state_filter_a.py

- Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module SQLAlchemy.
- Connects to a MySQL server on localhost at port 3306.
- Sorts results in ascending order by states.id.

### 10-model_state_my_get.py

- Prints the State object with the specified name from the database hbtn_0e_6_usa.
- Takes 4 arguments: MySQL username, MySQL password, database name, and state name to search (SQL injection free).
- Uses the module SQLAlchemy.
- Connects to a MySQL server on localhost at port 3306.
- Displays the state's id or "Not found" if no state matches the name.

### 11-model_state_insert.py

- Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module SQLAlchemy.
- Connects to a MySQL server on localhost at port 3306.
- Prints the new state's id after creation.

### 12-model_state_update_id_2.py

- Changes the name of a State object with id 2 to "New Mexico" in the database hbtn_0e_6_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module SQLAlchemy.
- Connects to a MySQL server on localhost at port 3306.

### 13-model_state_delete_a.py

- Deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module SQLAlchemy.
- Connects to a MySQL server on localhost at port 3306.

### model_city.py and 14-model_city_fetch_by_state.py

- Contains the class definition of a City that inherits from Base.
- Represents a City with an id, name, and state_id.
- Defines a relationship with the State class.

### relationship_city.py, relationship_state.py, 100-relationship_states_cities.py

- Enhanced versions of model_city.py and model_state.py.
- Introduces relationships between State and City classes.
- Ensures that when a State is deleted, linked City objects are also deleted.
- 100-relationship_states_cities.py script creates the State "California" with the City "San Francisco" in the database hbtn_0e_100_usa.

### 101-relationship_states_cities_list.py

- Lists all State objects along with their corresponding City objects from the database hbtn_0e_101_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module SQLAlchemy.
- Connects to a MySQL server on localhost at port 3306.
- Sorts results in ascending order by states.id and cities.id.

### 102-relationship_cities_states_list.py

- Lists all City objects along with their linked State objects from the database hbtn_0e_101_usa.
- Takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the module SQLAlchemy.
- Connects to a MySQL server on localhost at port 3306.
- Sorts results in ascending order by cities.id.

These scripts help you interact with a MySQL database using SQLAlchemy, demonstrating various ORM concepts and database operations.
