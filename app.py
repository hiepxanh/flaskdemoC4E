from flask import (Flask, render_template)
from firebase import firebase






# --Flask render template--
app = Flask(__name__)
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)
@app.route("/")
def index():
        return render_template("index.html")





#test post method
from flask import request
@app.route('/postman', methods=['GET', 'POST'])
def template():
    if request.method == 'POST':
        x=request.form['dinhmenh']
        print(x)
        return "Ôi ra rồi sướng quá anh "+ x +" ơi "
    return render_template('postman.html')


if __name__ == '__main__':
    app.run()
