from flask import Flask

app = Flask(__name__)

#Api for server responding
@app.route('/ping')
def ping():
    return 'Pong!'

if __name__ == '__main__':
    app.run(debug=True)