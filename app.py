
from tkinter.messagebox import RETRY
from flask import Flask, redirect, render_template, request
from re import findall 
from exp import  generate



def create_app(): 
    app = Flask(__name__)
    
    @app.route('/exception')
    def exception(): 
        return render_template('exception.html')
    
    @app.route('/', methods=["GET", "POST",])
    def index (): 
        language=''
        if request.method == "POST":
            exp= request.form.get("expression")
            if len(findall('\(',exp)) !=0  :
                return redirect('/exception') 

            language = generate(exp)       
    
        return render_template('index.html',language=language)
    return app