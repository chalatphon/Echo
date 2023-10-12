from flask import Flask,render_template,request,redirect,url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        # รับ ข้อมูล จาก sign-up
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        c_password = request.form['c_password']
        # เก็บใน databaase
        if password == c_password:
            connect = sqlite3.connect('echo.db')
            cursor = connect.cursor()
            cursor.execute(f"insert into member(fname,lname,email,password) values('{fname}','{lname}','{email}','{password}')")
            connect.commit()
            connect.close()
            return redirect(url_for('signin'))
        # else --> ถ้าเกิด password กับ confirm-password ไม่ตรงกันให้ทำอะไร
    return render_template('signup.html')

@app.route("/signin", methods=['GET','POST'])
def signin():
    if request.method == "POST":
        connection = sqlite3.connect('echo.db')
        cursor = connection.cursor()
        email = request.form['email']
        password = request.form['password']
        query = f"select email,password from member where email= '{email}' and password='{password}'"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 0:
            print("Incorrect Password")
        else:
            return render_template('dashboard.html',data=email)
    return render_template('signin.html')

if __name__ == "__main__":
    app.run(debug=True)