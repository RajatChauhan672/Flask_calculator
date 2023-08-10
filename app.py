from flask import Flask,render_template,redirect,url_for,request,jsonify
import json

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

@app.route('/Calculator',methods=['GET'])
def math_operation():
    
    operation=request.json['operation']
    number1=request.json['number1']
    number2=request.json['number2']
    
    if operation=="add":
        result=int(number1)+int(number2)
    
    elif operation=="subtraction":
        result=int(number1)-int(number2)
    
    elif operation=="multiply":
        result=int(number1)*int(number2)
    
    elif operation=="division":
        result=int(number1)/int(number2) 
        
    return jsonify(result)    
    

if(__name__=="__main__"):
    app.run(debug=True)

