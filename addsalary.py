import pymysql
import psycopg2

from flask import *
app=Flask(__name__)


# @app.route ("/")
# def login():
#     return render_template ("employee.html")


@app.route ('/')
def register():
    connection = psycopg2.connect (
        host='localhost',
        user='yogi',
        password="root",
        database='sevenbits'
    )

    cursor1 = connection.cursor()
    cursor1.execute("SELECT * FROM employeesalary")
    tup = cursor1.fetchall()
    connection.commit()
    cursor1.close()
    connection.close()
    return render_template("displaysalary.html", tup=tup)


@app.route ('/deletesalary', methods=["GET"])
def deletesalary():
    connection = psycopg2.connect (
        host="localhost",
        user="yogi",
        password="root",
        database="sevenbits"
    )

    cursor1 = connection.cursor()
    id = request.args.get ("id")
    print (id)
    cursor1.execute ("DELETE FROM employeesalary WHERE Id='"+id+"'")
    connection.commit ()
    cursor1.close ()
    connection.close ()
    return "delete"


@app.route ('/editsalary', methods=["GET"])
def editsalary():
    connection = psycopg2.connect (
        host="localhost",
        user="yogi",
        password="root",
        database="sevenbits"
    )

    cursor1 = connection.cursor ()
    id = request.args.get ('id')

    cursor1.execute ("SELECT * FROM employeesalary WHERE id=" + id + "")
    id1 = cursor1.fetchall ()
    connection.commit ()
    cursor1.close ()
    connection.close ()
    return render_template ("updatesalary.html", tup=id1)

@app.route("/updatesalary",methods=['POST'])
def updatesalary():
    connection=psycopg2.connect(
        host="localhost",
        user="yogi",
        password="root",
        database="sevenbits"
    )

    id=request.form["id"]
    # Name=request.form["emp_name"]
    salary=request.form["salary"]

    cursor1 = connection.cursor ()
    cursor1.execute ("UPDATE employeesalary SET salary='"+salary+"' WHERE id=" + id + "")
    cursor1.execute ("SELECT * FROM employee")
    tup = cursor1.fetchall ()
    connection.commit ()
    cursor1.close ()
    connection.close ()
    return render_template("displaysalary.html",tup=tup)

app.run()