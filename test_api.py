import json
from exercise3 import app, db, User

# Flask test client
client = app.test_client()

# Setup and teardown for tests
def setup_module(module):
    # Set up a test database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db.db'
    with app.app_context():
        db.create_all()

def teardown_module(module):
    # Clean up the test database
    with app.app_context():
        db.drop_all()

# Tests for CRUD operations
def test_create_user():
    # Test creating a user
    data = {'name': 'Test User', 'email': 'test@example.com'}
    response = client.post('/save', json=data)
    assert response.status_code == 201

def test_get_users():
    # Test getting all users
    response = client.get('/get')
    assert response.status_code == 200
    users = json.loads(response.data)
    assert len(users) == 1  # Assuming one user was created

def test_get_user():
    # Test getting a specific user
    response = client.get('/get/1')
    assert response.status_code == 200
    user = json.loads(response.data)
    assert user['id'] == 1

def test_update_user():
    # Test updating a user
    data = {'name': 'Updated User', 'email': 'updated@example.com'}
    response = client.put('/save/1', json=data)
    assert response.status_code == 200

def test_delete_user():
    # Test deleting a user
    response = client.delete('/delete/1')
    assert response.status_code == 200
