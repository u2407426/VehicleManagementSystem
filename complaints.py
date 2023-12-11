from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from conn_db import *

# SELECT `com_id`, `name`, `email`, `phone`, `msg`, `dat` FROM `complaints` WHERE 1
class Complaints:
    def __init__(self, name, email, phone, msg, dat, e_id=None):
        self.id = e_id
        self.name = name
        self.email = email
        self.phone = phone
        self.msg = msg
        self.dat = dat
   
    def complaints_add(self):
        conn = Database()
        sql = "INSERT INTO complaints(name, email, " \
              "phone, msg, dat) " \
              "VALUES (%s, %s, %s, %s, %s)"
        values = (self.name, self.email, self.phone, self.msg, self.dat)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()

    @staticmethod
    def complaints_delete(emp_id):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM complaints WHERE com_id = %s", (emp_id,))
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
            conn.cursor.execute("SELECT * FROM complaints WHERE com_id = %s", (emp_id,))
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
            conn.cursor.execute("SELECT * FROM complaints")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

# SELECT `customer_id`, `customer_name`, `address`, `contact_no`, `email` FROM `customer` WHERE 1
    def complaints_edit(self, id):
        conn = Database()
        try:
            conn.cursor.execute("UPDATE complaints SET name='"+self.name+"', address='"+self.address+"', contact_no='"+self.contact_no+"', email='"+self.email+"' WHERE com_id="+id)
            conn.connection.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

