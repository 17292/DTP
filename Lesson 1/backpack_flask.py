from flask import Flask,g, render_template, request, redirect  
import sqlite3

app = Flask(__name__)

DATEBASE = "backpack.db"

def get_db():
    db= getattr(g, "_datebase", None)
    if db is None:
        db = g._datebase = sqlite3.connect(DATEBASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_datebase", None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    cursor = get_db().cursor()
    sql = "SELECT * FROM contents"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

@app.route("/add", methods= ["GET","POST"])
def add():
    if request.method == "POST":
        cursor = get_db().cursor()
        new_name = request.form["item_name"]
        new_desciption = request.form["item_description"]
        sql = "INSERT INTO contents(name,description) VALUES (?,?)"
        cursor.execute(sql, (new_name, new_desciption))
        get_db().commit()
    return redirect('/')

@app.route('/delete', methods= ["GET","POST"])
def delete():
    if request.method == "POST":
        #get the item and delte from database
        cursor = get_db().cursor()
        id = int(request.form["item_name"])
        sql = "DELETE FROM contents WHERE id=?"
        cursor.execute(sql,(id,))
        get_db().commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)