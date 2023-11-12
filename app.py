from flask import Flask,render_template,request,redirect,url_for,session
import sqlite3

app = Flask(__name__)
app.secret_key = "hello"

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
        username = request.form['username']
        password = request.form['password']
        c_password = request.form['c_password']
        # เก็บใน databaase
        if password == c_password:
            connect = sqlite3.connect('echo.db')
            cursor = connect.cursor()
            cursor.execute(f"insert into members(fname,lname,email,username,password) values('{fname}','{lname}','{email}','{username}','{password}')")
            connect.commit()
            cursor.execute(f"create table {username} ('date'text,'event'text, 'status' INTEGER DEFAULT 0);")
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
        username = request.form['username']
        password = request.form['password']
        query = f"select username,password from members where username= '{username}' and password='{password}'"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 0:
            return redirect(url_for('signin'))
        else:
            session["user"] = username
            return redirect(url_for('dashboard'))
    else:
        if "user" in session:
            return redirect(url_for('dashboard'))
    return render_template('signin.html')

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        username = session["user"]
        return render_template('dashboard.html',data=username)
    else:
        return redirect(url_for('signin'))


@app.route("/logout")
def logout():
    # เคลีย session
    session.pop('user',None)
    return redirect(url_for('signin'))

@app.route("/calendar")
def calendar():
    if "user" in session:
        username = session["user"]
        return render_template("calendar.html")
    else:
        return redirect(url_for('signin'))

@app.route("/input")
def input():
    if "user" in session:
        username = session["user"]
        return render_template("input.html")
    else:
        return redirect(url_for('signin'))

@app.route("/about")
def about():
    if "user" in session:
        username = session["user"]
        return render_template("about.html")
    else:
        return redirect(url_for('signin'))
    

            

if __name__ == "__main__":
    app.run(debug=True)