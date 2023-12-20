from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# Pre-shared secret key (Replace this with your actual secret key)
pre_shared_key = "my_secret_key"

@app.route('/authorize', methods=['POST'])
def authorize():
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({'message': 'Authorization header missing'}), 401

    received_key = auth_header.split()[-1]

    if received_key != pre_shared_key:
        return jsonify({'message': 'Unauthorized'}), 401

    return jsonify({'message': 'Authorized'}), 200

if __name__ == '__main__':
    app.run(debug=True)
