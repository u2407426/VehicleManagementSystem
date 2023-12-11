from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from conn_db import *

#SELECT `vehicle_id`, `registration_no`, `company`, `model`, `vehicle_type`, `transmission`, `customer_id` FROM `vehicle` WHERE 1
class Vehicle:
    def __init__(self, registration_no, company, model, vehicle_type, transmission,customer_id, e_id=None):
        self.id = e_id
        self.registration_no = registration_no
        self.company = company
        self.model = model
        self.vehicle_type = vehicle_type
        self.transmission = transmission
        self.customer_id=customer_id

    def vehicle_add(self):
        conn = Database()
        sql = "INSERT INTO vehicle(registration_no, company, " \
              "model, vehicle_type, transmission, customer_id) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.registration_no, self.company, self.model, self.vehicle_type, self.transmission,self.customer_id)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()

    @staticmethod
    def vehicle_delete(emp_id):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM vehicle WHERE vehicle_id = %s", (emp_id,))
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
            conn.cursor.execute("SELECT * FROM vehicle WHERE vehicle_id = %s", (emp_id,))
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
            conn.cursor.execute("SELECT * FROM vehicle")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()


    def vehicle_edit(self, id):
        conn = Database()
        try:
            conn.cursor.execute("UPDATE vehicle SET vehicle='"+self.name+"', employee_address='"+self.address+"', employee_contact_no='"+self.contact_no+"', date_of_joining='"+self.date+"', salary='"+self.salary+"' WHERE vehicle_id="+id)
            conn.connection.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

