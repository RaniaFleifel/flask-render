from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
#def hello_world():
#    return 'Hello, World!'
def home():
    return render_template('index_new_v2.html')
