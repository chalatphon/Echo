from flask import Flask,render_template,request,redirect,url_for,session
import sqlite3
from datetime import date

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
        notetable = "note"+ username
        # เก็บใน databaase
        if password == c_password:
            connect = sqlite3.connect('echo.db')
            cursor = connect.cursor()
            cursor.execute(f"insert into members(fname,lname,email,username,password) values('{fname}','{lname}','{email}','{username}','{password}')")
            connect.commit()
            cursor.execute(f"create table {username} ('date'text,'event'text, 'status' INTEGER DEFAULT 0);")
            connect.commit()
            cursor.execute(f"create table {notetable} ('title'text,'note'text)")
            connect.close()
            return redirect(url_for('signin'))
        # else:
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
        connection = sqlite3.connect('echo.db')
        cursor = connection.cursor()
        today = date.today()
        cursor.execute(f"select event from {username} where date ='{today}'")
        event_today = cursor.fetchall()
        count_event = len(event_today)
        return render_template('dashboard.html', event_today=event_today,count_event=count_event)
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
        connect = sqlite3.connect('echo.db')
        cursor = connect.cursor()
        cursor.execute(f"select date,event from {username}")
        events = cursor.fetchall()
        return render_template("calendar.html", events=events)
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

@app.route("/note")
def note():
    if "user" in session:
        username = session["user"]
        connect = sqlite3.connect('echo.db')
        cursor = connect.cursor()
        notetable = "note"+ username
        cursor.execute(f"select title,note from '{notetable}'")
        all_note = cursor.fetchall()
        return render_template("note.html",all_note=all_note)
    else:
        return redirect(url_for('signin'))


@app.route("/insert", methods=['GET','POST'])
def insert():
    if "user" in session:
        connect = sqlite3.connect('echo.db')
        cursor = connect.cursor()
        username = session["user"]
        if request.method == "POST":
            date = request.form["date"]
            event = request.form["event"]
            cursor.execute(f"insert into {username}(date, event)values('{date}','{event}')")
            connect.commit()
            connect.close()
            return redirect(url_for('dashboard'))

@app.route("/addnote", methods=['GET','POST'])
def addnote():
    if "user" in session:
        username = session["user"]
        notetable = "note"+ username
        connect = sqlite3.connect('echo.db')
        cursor = connect.cursor()
        title = request.form["title"]
        note = request.form["note"]
        cursor.execute(f"insert into {notetable}(title,note) values('{title}','{note}')")
        connect.commit()
        connect.close()
        return redirect(url_for('note'))
    else:
        return redirect(url_for('signin'))
    
@app.route("/profile")
def profile():
    if "user" in session:
        username = session["user"]
        connect = sqlite3.connect('echo.db')
        cursor = connect.cursor()
        cursor.execute(f"select fname,lname,email,username from members where username = '{username}'")
        all_profile = cursor.fetchall()
        return render_template("profile.html",all_profile=all_profile)
    else:
        return redirect(url_for('signin'))

@app.route("/delete_event", methods=['POST'])
def delete_event():
    if "user" in session:
        username = session["user"]
        want_delete = request.json.get('myString')
        connect = sqlite3.connect('echo.db')
        cursor = connect.cursor()
        cursor.execute(f"delete from '{username}' where event = '{want_delete}'")
        connect.commit()
        connect.close()
        return redirect(url_for('dashboard'))
    
@app.route("/delete_note", methods=['POST'])
def delete_note():
    if "user" in session:
        username = session["user"]
        want_delete = request.json.get('myString')
        notetable = "note"+ username
        connect = sqlite3.connect('echo.db')
        cursor = connect.cursor()
        cursor.execute(f"delete from '{notetable}' where title = '{want_delete}'")
        connect.commit()
        return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)