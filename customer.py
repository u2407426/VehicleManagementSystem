from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from conn_db import *

# SELECT `customer_id`, `customer_name`, `address`, `contact_no`, `email` FROM `customer` WHERE 1
class Customer:
    def __init__(self, name, address, contect_no, email, e_id=None):
        self.id = e_id
        self.name = name
        self.address = address
        self.contact_no = contect_no
        self.email = email
   
    def cus_add(self):
        conn = Database()
        sql = "INSERT INTO customer(customer_name, address, " \
              "contact_no, email) " \
              "VALUES (%s, %s, %s, %s)"
        values = (self.name, self.address, self.contact_no, self.email)
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
            conn.cursor.execute("DELETE FROM customer WHERE customer_id = %s", (emp_id,))
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
            conn.cursor.execute("SELECT * FROM customer WHERE customer_id = %s", (emp_id,))
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
            conn.cursor.execute("SELECT * FROM customer")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

# SELECT `customer_id`, `customer_name`, `address`, `contact_no`, `email` FROM `customer` WHERE 1
    def emp_edit(self, id):
        conn = Database()
        try:
            conn.cursor.execute("UPDATE customer SET customer_name='"+self.name+"', address='"+self.address+"', contact_no='"+self.contact_no+"', email='"+self.email+"' WHERE customer_id="+id)
            conn.connection.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

