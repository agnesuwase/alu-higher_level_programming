# Python - Object-relational mapping

This project connects Python scripts to a MySQL database,
first with MySQLdb and then with SQLAlchemy (ORM).

## Concepts
- Connecting to a MySQL database from a Python script
- SELECT and INSERT rows in a MySQL table from Python
- What ORM means
- Mapping a Python class to a MySQL table

## Files
- 0-select_states.py: lists all states from the database hbtn_0e_0_usa,
  sorted by states.id
- 1-filter_states.py: lists all states with a name starting with N
- 2-my_filter_states.py: displays states where name matches the argument
- 3-my_safe_filter_states.py: same as 2, but safe from MySQL injection
- 4-cities_by_state.py: lists all cities with their state name
- 5-filter_cities.py: lists all cities of a given state
- model_state.py: State class and Base for SQLAlchemy (table states)

## Usage
    ./0-select_states.py <mysql username> <mysql password> <database name>

Agnes Uwase
