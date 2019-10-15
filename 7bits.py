import pymysql
import psycopg2
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from wtforms import  *
app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{root}:{root}@localhost:3306/{7bits}'

app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'shhhh...iAmASecret!'

class employee(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(75)) 
    department = db.Column(db.String(50)) 

@app.route ('/')
def hello_world():
    return render_template("employee.html")

@app.route("/employee",methods=['POST'])
def employee():

    employeedao = employeeDAO()
    employeevo = employeeVO()

    employeevo.name=request.form['emp_name']

    employeevo.department=request.form['department']

    # id=request.form['Id']
    # print(id)
    employeevo.salary=request.form['salary']

    employeedao.insertemployee(employeevo)

    return render_template("display.html")

class employeeDAO:
    def insertemployee(self,employeevo):

        connection=psycopg2.connect(
            host='localhost',
            user='yogi',
            password='root',
            database='sevenbits'
        )


        cursor1 = connection.cursor()
        #Id = request.args.get('id')
        cursor2=connection.cursor()
        cursor3=connection.cursor()
        cursor1.execute("INSERT INTO employee (name,department) VALUES ('"+employeevo.name+"','"+employeevo.department+"')")

        res = cursor1.execute("SELECT * FROM employee WHERE id IN (SELECT MAX(id) FROM employee)")

        rec = cursor1.fetchall()
        record = []
        for i in rec:
            print(i)
            for j in i:
                record.append(j)

        cursor2.execute("INSERT INTO employeesalary (salary,emp_Id) VALUES ('"+employeevo.salary+"','"+str(record[0])+"')")
        cursor3.execute("SELECT * FROM employee")
        tupl = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        cursor2.close()
        cursor3.close()
        connection.close()
        return render_template("display.html", tupl=tupl)



class employeeVO:

    id = IntegerField
    name =StringField
    department = StringField
    salary = IntegerField
    empId = IntegerField

app.run()











# @app.route("/employeesalary",methods=['POST'])
# def employeesalary():
#     empId=request.form['Id']
#     print(empId)
#     salary=request.form['salary']
#     print(salary)
#
#     connection=pymysql.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         db='7bits'
#     )
#

#     cursor1 = connection.cursor()
#     cursor1.execute("INSERT INTO employeesalary (empId,salary) VALUES ('"+empId+"','"+salary+"')")
#     connection.commit()
#     cursor1.close()
#     connection.close()
#     return "done"





