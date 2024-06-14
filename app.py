from flask import Flask

app=Flask(__name__) #APP օբեյեկըի ստեղծեւմը Flask  դասից,  փոխանցում ենք հիմնական ֆայլի անունը

@app.route("/")#դեկերատոր ,որը հետևում է URL-ում նշված էջը այս դեպքում՝ գլխավորը
def index():
    return "hi"

@app.route("/about")
def about():
    return "about page"
if __name__=="__main__":#եթե այս ընթացիկ ֆայլն է հիմնական զապուսկի ֆայլը։Այսինքն էս ֆայլից ենք ռան տալիս էդ դեպքում __name__-ի մեջ կգրվի հենտ __main__
    app.run(debug=True)