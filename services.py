from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from conn_db import *

#SELECT `service_id`, `description`, `service_date`, `distance`, `damages`, `total_price`, `vehicle_id`, `employee_id` FROM `service` WHERE 1
class Services:
    def __init__(self, description, service_date, distance, damages, total_price, vehicle_id,employee_id, e_id=None):
        self.id = e_id
        self.description = description
        self.service_date = service_date
        self.distance = distance
        self.damages = damages
        self.total_price = total_price
        self.vehicle_id = vehicle_id
        self.employee_id = employee_id

    def service_add(self):
        conn = Database()
        sql = "INSERT INTO service(description, service_date, " \
              "distance, damages, total_price, vehicle_id, employee_id) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (self.description, self.service_date, self.distance, self.damages, self.total_price, self.vehicle_id, self.employee_id)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()

    @staticmethod
    def service_delete(emp_id):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM service WHERE service_id = %s", (emp_id,))
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()

    @staticmethod
    def service_single(emp_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM service WHERE service_id = %s", (emp_id,))
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
            conn.cursor.execute("SELECT * FROM service")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()


    def service_edit(self, id):
        conn = Database()
        try:
            conn.cursor.execute("UPDATE service SET employee_name='"+self.name+"', employee_address='"+self.address+"', employee_contact_no='"+self.contact_no+"', date_of_joining='"+self.date+"', salary='"+self.salary+"' WHERE service_id="+id)
            conn.connection.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

