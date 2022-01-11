from flask import Flask
# from flask module, import Flask class.

app = Flask(__name__)
# It's standard way to create flask application.

@app.route('/') # "@app.route('/')" = decorator, from here, we can tell our Flask application which endpoint to listen to for connections. This time, we want to listen to the homepage route =(root route '/').
def index(): # index is a standard name for the route handler that listens for connections to the root route and figures out what to do next.
    return f'Hello, World!'

