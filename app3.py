from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route("/")
def welcome():
    return render_template("index3.html")

@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method=="POST":
        science=int(request.form["science"])
        math=int(request.form["math"])
        java=int(request.form["java"])
        name=(request.form["name"])
        if(((science>=0) and (science<=100) ) and ((math>=0) and (math<=100) ) and ((java>=0) and (java<=100))):
            percentage=round((science+math+java)/3,2)
            if(percentage<35):
                return (f"{name} you failed better luck next time!!!")
            elif(percentage<50):
                return (f"Congrats {name} you got C grade and {percentage}% percentage!!!")
            elif(percentage<70):
                return (f"Congrats {name} you got B grade and {percentage}% percentage!!!")
            elif(percentage<90):
                return (f"Congrats {name} you got A grade and {percentage}% percentage!!!")
            elif(percentage<=100):
                return (f"Congrats {name} you got S grade and {percentage}% percentage!!!")
        else:
            return "Invalid Input"
    return "Server Busy"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
