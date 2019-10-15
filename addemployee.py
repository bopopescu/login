import pymysql
import psycopg2
from flask import Flask,render_template,request,redirect
from wtforms import  *
app = Flask (__name__)


@app.route ('/')
def hello_world():
    return render_template("employee.html")

@app.route("/employee",methods=['POST'])
def employee():

    employeedao = employeeDAO()
    employeevo = employeeVO()

    employeevo.name=request.form['emp_name']

    employeevo.department=request.form['department']

    employeevo.salary=request.form['salary']

    employeedao.insertemployee(employeevo)

    return render_template("employee.html")

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
        cursor1.execute("INSERT INTO employee (name,department) VALUES ('"+employeevo.name+"','"+employeevo.department+"')")

        res = cursor1.execute("SELECT * FROM employee WHERE id IN (SELECT MAX(id) FROM employee)")

        rec = cursor1.fetchall()
        record = []
        for i in rec:
            print(i)
            for j in i:
                record.append(j)

        cursor2.execute("INSERT INTO employeesalary (salary,emp_id) VALUES ('"+employeevo.salary+"','"+str(record[0])+"')")
        connection.commit()
        cursor1.close()
        cursor2.close()
        connection.close()


class employeeVO:

    id = IntegerField
    name =StringField
    department = StringField
    salary = IntegerField
    empId = IntegerField

app.run()






