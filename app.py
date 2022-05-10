from re import M
from flask import Flask, render_template, request

app = Flask(__name__)
symbols=('*','+','(',')','^')

def generate(exp): 
    exp_symbols:str
    for i in symbols:
        if i in exp: 
            exp_symbols=exp 
        



@app.route('/', methods=['GET', 'POST'])
def index (): 

    
    exp= request.form.get("Expression")
    cadeias =['aaaaa','bbbbb','cccccc']
    
    
    
    return render_template('index.html',cadeias=cadeias)