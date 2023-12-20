step 1: First Create a Virtual Environment.
       python -m venv demo_api
-To activate the virtual Environment:
        source demo_api/bin/activate

step 2: pip install -r req.txt (install in virtual env)

step 3:nano exercise1.py
    ![image](https://github.com/anmolk3797/flask-test-task/assets/74237250/3050c381-6946-4645-b2ea-49d46869fd22)



step 4:nano exercise2.py 
     ![Screenshot from 2023-12-20 16-18-09](https://github.com/anmolk3797/flask-test-task/assets/74237250/7f9128a9-b4ff-4d4d-bf2f-0aca5c37c733)


step 5:nano exercise3.py 
    - export FLASK_APP=app
    - export FLASK_ENV=development
    - flask run
    ![image](https://github.com/anmolk3797/flask-test-task/assets/74237250/327086bf-2b77-464a-ac6d-b681cab797f0)
    ![image](https://github.com/anmolk3797/flask-test-task/assets/74237250/57289613-53f1-4b59-9429-320312d93c88)
       
    create migration:
       flask db init  # This initializes the migrations directory (do this only once)
       flask db migrate -m "initial migration"  # Create a migration
       flask db upgrade  # Apply the migration to the database

step 6: nano pytest
      ![image](https://github.com/anmolk3797/flask-test-task/assets/74237250/614e0c56-04ac-44ed-9929-04923cdd5d61)

