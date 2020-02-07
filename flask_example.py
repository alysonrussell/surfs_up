from flask import Flask

# Create a new Flask instance called app.
app = Flask(__name__)

# Create our first route.
# Define the starting point.
@app.route('/')
def hello_world():
    return 'Hello world'