step 1:Firstly Create virtual Environment.
       virtualenv --python=python3.10 ~/.env/demo_api

step 2: pip install -r req.txt (intall in virtuall env)

step 3:nano exercise1.py
step 4:nano exercise2.py 
step 5:nano exercise3.py 
    - export FLASK_APP=app
    - export FLASK_ENV=development
    - flask run
 

step 6: create migration:
flask db init  # This initializes the migrations directory (do this only once)
flask db migrate -m "initial migration"  # Create a migration
flask db upgrade  # Apply the migration to the database


