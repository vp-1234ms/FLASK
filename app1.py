###Buiiding Url Dynamically 
###Variable rules and URL Building
from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Hi my am unknown"

#Taking input in url  
@app.route("/success/<int:score>") #By default score will be string format 
def success(score):
    percentage=score*100/100
    return f"Person has passed with percentage - {percentage}"

@app.route("/results/<int:score>")
def grade(score):
    if(score<35):
        grade="Your final grade is F"
    elif(score<50):
        grade="Your final grade is C"
    elif(score<70):
        grade="Your final grade is B"
    elif(score<90):
        grade="Your final grade is A"
    else:
        grade="Your final grade is S"
    return grade

@app.route("/fail/<int:score>") #By default score will be string format
def fail(score):
    percentage=score*100/100
    return f"Person has failed with percentage - {percentage}"

#Now building URL dynamically
#That is wantedt to show different page for those who got internship and different for those who got placement
#For this we use redirect and url_for

@app.route("/intern/<int:ye>")
def internship(ye):
    return(f"You are doing internship in {ye} year")

@app.route("/placed/<int:ye>")
def placement(ye):
    return(f"You are doing placement in {ye} year")

@app.route("/list/<int:year>")
def list(year): 
    if(year!=4):
        return redirect(url_for("internship",ye=year))
    else:
        return redirect(url_for("placement",ye=year))



if __name__ == "__main__":
    app.run(host="0.0.0.0")