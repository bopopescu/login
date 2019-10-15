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
    cursor1.execute("SELECT * FROM employee")
    tupl = cursor1.fetchall()
    connection.commit()
    cursor1.close()
    connection.close()
    return render_template("display.html", tupl=tupl)


@app.route ('/delete', methods=["GET"])
def delete():
    connection = psycopg2.connect (
        host="localhost",
        user="yogi",
        password="root",
        database="sevenbits"
    )

    cursor1 = connection.cursor()
    Id = request.args.get ('Id')
    print (Id)
    cursor1.execute("DELETE FROM employeesalary WHERE id='"+Id+"'")
    cursor1.execute ("DELETE FROM employee WHERE id='"+Id+"'")
    connection.commit ()
    cursor1.close ()
    connection.close ()
    return "delete"


@app.route ('/edit', methods=["GET"])
def edit():
    connection = psycopg2.connect (
        host="localhost",
        user="yogi",
        password="root",
        database="sevenbits"
    )

    cursor1 = connection.cursor ()
    Id = request.args.get ('Id')

    cursor1.execute ("SELECT * FROM employee WHERE id=" + Id + "")
    id1 = cursor1.fetchall ()
    connection.commit ()
    cursor1.close ()
    connection.close ()
    return render_template ("update.html", tupl=id1)

@app.route("/update",methods=['POST'])
def update():
    connection=psycopg2.connect(
        host="localhost",
        user="yogi",
        password="root",
        database="sevenbits"
    )

    Id=request.form["Id"]
    Name=request.form["emp_name"]
    #salary=request.form["salary"]

    cursor1 = connection.cursor ()
    cursor1.execute ("UPDATE employee SET name='"+Name+"' WHERE id=" + Id + "")
    cursor1.execute ("SELECT * FROM employee")
    tupl = cursor1.fetchall ()
    connection.commit ()
    cursor1.close ()
    connection.close ()
    return render_template("display.html",tupl=tupl)



# @app.route ('/deletesalary', methods=["GET"])
# def deletesalary():
#     connection = pymysql.connect (
#         host="localhost",
#         user="root",
#         password="root",
#         db="7bits"
#     )
#
#     cursor1 = connection.cursor()
#     id = request.args.get ("id")
#     print (id)
#     cursor1.execute ("DELETE FROM employeesalary WHERE Id='"+id+"'")
#     connection.commit ()
#     cursor1.close ()
#     connection.close ()
#     return "delete"
#
#
# @app.route ('/editsalary', methods=["GET"])
# def editsalary():
#     connection = pymysql.connect (
#         host="localhost",
#         user="root",
#         password="root",
#         db="7bits"
#     )
#
#     cursor1 = connection.cursor ()
#     id = request.args.get ('id')
#
#     cursor1.execute ("SELECT * FROM employeesalary WHERE id=" + id + "")
#     id1 = cursor1.fetchall ()
#     connection.commit ()
#     cursor1.close ()
#     connection.close ()
#     return render_template ("update.html", tup=id1)
#
# @app.route("/updatesalary",methods=['POST'])
# def updatesalary():
#     connection=pymysql.connect(
#         host="localhost",
#         user="root",
#         password="root",
#         db="7bits"
#     )
#
#     id=request.form["id"]
#     # Name=request.form["emp_name"]
#     salary=request.form["salary"]
#
#     cursor1 = connection.cursor ()
#     cursor1.execute ("UPDATE employeesalary SET salary='"+salary+"' WHERE id=" + id + "")
#     cursor1.execute ("SELECT * FROM employee")
#     tupl = cursor1.fetchall ()
#     connection.commit ()
#     cursor1.close ()
#     connection.close ()
#     return render_template("displaysalary.html",tup=tupl)


app.run()