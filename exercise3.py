from flask import Flask, request, jsonify,json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache

app = Flask(__name__)

#Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Cache Configuration
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'  # Replace with your Redis server details
cache = Cache(app)

# Create a model (example: a simple User model)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

# Routes for CRUD operations
    
#GET API for fetch all users
@app.route('/get', methods=['GET'])
def get_users():
    cached_value = cache.get("users")
    if cached_value:
        print('cache')
        response = app.response_class(response=json.dumps(cached_value),
                                  status=200,
                                  mimetype='application/json')
        return response
    else:
        # If not in cache, perform the database query
        users = User.query.all()
        user_list = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]

        # Cache the result with a timeout (adjust timeout as needed)
        cache.set("users", user_list, timeout=60)
        response = app.response_class(response=json.dumps(user_list),
                                  status=200,
                                  mimetype='application/json')
        return response
    
#GET API for fetch single user according to ID 
@app.route('/get/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

#POST API for creating user
@app.route('/save', methods=['POST'])
def create_user():
    data = request.json
    try:
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        if new_user:
            cache.clear()
        response = app.response_class(response=json.dumps({'message': 'User created successfully'}),
                                  status=201,
                                  mimetype='application/json')
    except Exception as e:
        response = app.response_class(response=json.dumps({'error': str(e)}),
                                  status=422,
                                  mimetype='application/json')
    return response

#PUT API to update user details according to ID 
@app.route('/save/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    try:
        response = app.response_class(response=json.dumps({'message': 'User updated successfully'}),
                                    status=200,
                                    mimetype='application/json')
    except Exception as e:
        response = app.response_class(response=json.dumps({'error': str(e)}),
                                  status=422,
                                  mimetype='application/json')
    return response

#DELETE API for deleting single user according to ID 
@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
