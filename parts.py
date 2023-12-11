from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from conn_db import *

# INSERT INTO `parts` (`part_id`, `part_name`, `part_price`, `brand`) VALUES (NULL, 'Type', '100', 'MRF');
class Parts:
    def __init__(self, part_name, part_price, brand, e_id=None):
        self.id = e_id
        self.part_name = part_name
        self.part_price = part_price
        self.brand = brand
    
   
    def parts_add(self):
        conn = Database()
        sql = "INSERT INTO parts(part_name, part_price, " \
              "brand) " \
              "VALUES (%s, %s, %s)"
        values = (self.part_name, self.part_price, self.brand)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()

    @staticmethod
    def parts_delete(emp_id):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM parts WHERE part_id = %s", (emp_id,))
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
            conn.cursor.execute("SELECT * FROM parts WHERE part_id = %s", (emp_id,))
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
            conn.cursor.execute("SELECT * FROM parts")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

# INSERT INTO `parts` (`part_id`, `part_name`, `part_price`, `brand`) VALUES (NULL, 'Type', '100', 'MRF');
    def parts_edit(self, id):
        conn = Database()
        try:
            conn.cursor.execute("UPDATE parts SET part_name='"+self.part_name+"', part_price='"+self.part_price+"', brand='"+self.brand+"' WHERE part_id="+id)
            conn.connection.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

