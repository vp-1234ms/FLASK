#Jinja2 Template engine
"""
{%  %} this is used for if statement , for loops    
{{  }} expression to printing output
{#  #} this is for comments
"""
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route("/")
def welcome():
    return render_template("index3.html")

"""
#If statement in HTML
@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method=="POST":
        science=int(request.form["science"])
        math=int(request.form["math"])
        java=int(request.form["java"])
        name=(request.form["name"])
        if(((science>=0) and (science<=100) ) and ((math>=0) and (math<=100) ) and ((java>=0) and (java<=100))):
            percentage=round((science+math+java)/3,2)
            return (render_template("index4.html",percent=percentage))
        else:
            return "Invalid Input"
    return "Server Busy"


RESPECTIVE HTML IF STATEMENT
If statement
         {% if percent>=50  %}
        <h1>You Pass</h1>
        {% else %}
        <h1>You Fail</h1>
        {% endif %} 
        
"""
#for loop statement in HTML
@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method=="POST":
        science=int(request.form["science"])
        math=int(request.form["math"])
        java=int(request.form["java"])
        name=(request.form["name"])
        if(((science>=0) and (science<=100) ) and ((math>=0) and (math<=100) ) and ((java>=0) and (java<=100))):
            percentage=round((science+math+java)/3,2)
            d={"Name":name,"Science":science,"Math":math,"Java":java,"Percentage":percentage}
            return (render_template("index4.html",dt=d))
        else:
            return "Invalid Input"
    return "Server Busy"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
