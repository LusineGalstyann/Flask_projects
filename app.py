from flask import Flask, render_template

app=Flask(__name__) #APP օբեյեկըի ստեղծեւմը Flask  դասից,  փոխանցում ենք հիմնական ֆայլի անունը

@app.route("/")#դեկերատոր ,որը հետևում է URL-ում նշված էջը այս դեպքում՝ գլխավորը
@app.route('/home')#նաև էս էջի համար կկանչի ինդեքս ֆունկիցան
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/user/<string:name>/<int:age>")
def user(name,age):
    return "User name: "+name +" he/she is :"+str(age)+" years old"
if __name__=="__main__":#եթե այս ընթացիկ ֆայլն է հիմնական զապուսկի ֆայլը։Այսինքն էս ֆայլից ենք ռան տալիս էդ դեպքում __name__-ի մեջ կգրվի հետո __main__
    app.run(debug=True)