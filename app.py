from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index (): 
    exp=''
    return render_template('index.html',exp=exp)