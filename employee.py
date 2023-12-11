from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from conn_db import *


class Employee:
    def __init__(self, name, address, contect_no, date, salary, e_id=None):
        self.id = e_id
        self.name = name
        self.address = address
        self.contact_no = contect_no
        self.date = date
        self.salary = salary

    def emp_add(self):
        conn = Database()
        sql = "INSERT INTO employee(employee_name, employee_address, " \
              "employee_contact_no, date_of_joining, salary) " \
              "VALUES (%s, %s, %s, %s, %s)"
        values = (self.name, self.address, self.contact_no, self.date, self.salary)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()

    @staticmethod
    def emp_delete(emp_id):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM employee WHERE employee_id = %s", (emp_id,))
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()

    @staticmethod
    def emp_single(emp_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM employee WHERE employee_id = %s", (emp_id,))
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()


    @staticmethod
    def view_all():
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM employee")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()


    def emp_edit(self, id):
        conn = Database()
        try:
            conn.cursor.execute("UPDATE employee SET employee_name='"+self.name+"', employee_address='"+self.address+"', employee_contact_no='"+self.contact_no+"', date_of_joining='"+self.date+"', salary='"+self.salary+"' WHERE employee_id="+id)
            conn.connection.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

