from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route("/index/")
def index():
    return render_template("index.html")
from test import MyDate
@app.route("/userinfo/")
def userinfo():
    obj = MyDate()
    result = obj.get_date()

    return render_template("userinfo.html",**locals())






if __name__ == '__main__':
    app.run(debug=True)