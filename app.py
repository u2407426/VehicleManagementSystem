from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
from employee import Employee

app = Flask(__name__)
from customer import Customer

app = Flask(__name__)
from parts import Parts


app = Flask(__name__)
from vehicle import Vehicle

app = Flask(__name__)
from complaints import Complaints

app = Flask(__name__)
from services import Services



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/services")
# def services():
#     return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


#................................Service Data............................................


@app.route("/services")
def services():
    servicesList = Services.view_all()
    return render_template('services.html', rows=servicesList)


@app.route("/addservicesui")
def add_services_ui():
    return render_template("addservices.html")


@app.route("/addservices", methods=['POST', 'GET'])
def addservices():
    # Data will be available from POST submitted by the form
    #SELECT `service_id`, `description`, `service_date`, `distance`, `damages`, `total_price`, `vehicle_id`, `employee_id` FROM `service` WHERE 1
    if request.method == 'POST':
        try:
            description = request.form['description']
            service_date = request.form['service_date']
            distance = request.form['distance']
            damages = request.form['damages']
            total_price = request.form['total_price']
            vehicle_id = request.form['vehicle_id']
            employee_id = request.form['employee_id']

            addemployee = Services(description, service_date, distance, damages, total_price, vehicle_id, employee_id)
            addemployee.service_add()
            msg = "Record Inserted"
        except:
            msg = "Error in the INSERT"
    return render_template('services.html', msg=msg)


@app.route("/editservices", methods=['POST', 'GET'])
def editservices():
    if request.method == 'POST':
        id = request.form['id']
        rows = Employee.emp_single(id)
        return render_template('editemployee.html', rows=rows)


@app.route("/editservicesrecord", methods=['POST', 'GET'])
def editservicesrecord():
    if request.method == 'POST':
        employee_id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        contactno = request.form['contactno']
        salary = request.form['salary']
        joining_date = request.form['joiningDate']

        addemployee = Employee(name, address, contactno, joining_date, salary)
        addemployee.emp_edit(employee_id)

        employeeList = Employee.view_all()
        return render_template('employee.html', msg="record updated", rows=employeeList)


@app.route("/deleteservices", methods=['POST', 'GET'])
def deleteservices():
    if request.method == 'POST':
        rowid = request.form['id']
        Employee.services_delete(rowid)
    employeeList = Employee.view_all()
    return render_template('employee.html', msg="record deleted", rows=employeeList)



#................................Customer Parts............................................

@app.route("/parts")
def parts():
    partList = Parts.view_all()
    return render_template("parts.html",rows=partList);


@app.route("/addpartsui")
def add_parts_ui():
    return render_template("addpart.html")


@app.route("/addparts", methods=['POST', 'GET'])
def addparts():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            name = request.form['name']
            brand = request.form['brand']
            price = request.form['price']
         
    
            addcustomer = Parts(name, price, brand)
            addcustomer.parts_add()
            msg = "Record Inserted"
        except:
            msg = "Error in the INSERT"
    return render_template('parts.html', msg=msg)


@app.route("/editparts", methods=['POST', 'GET'])
def editparts():
    if request.method == 'POST':
        id = request.form['id']
        rows = Customer.emp_single(id)
        return render_template('editcustomer.html', rows=rows)


@app.route("/editcustomerrecord", methods=['POST', 'GET'])
def editpartsrecord():
    if request.method == 'POST':
        employee_id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        contactno = request.form['contactno']
        email = request.form['email']
      

        addemployee = Customer(name, address, contactno, email)
        addemployee.emp_edit(employee_id)

        employeeList = Customer.view_all()
        return render_template('customer.html', msg="record updated", rows=employeeList)


@app.route("/deleteparts", methods=['POST', 'GET'])
def deleteparts():
    if request.method == 'POST':
        rowid = request.form['id']
        Customer.emp_delete(rowid)
    employeeList = Customer.view_all()
    return render_template('customer.html', msg="record deleted", rows=employeeList)




#................................Customer Data............................................

@app.route("/customer")
def customer():
    customerList = Customer.view_all()
    return render_template("customer.html",rows=customerList);



@app.route("/addcustomerui")
def add_customer_ui():
    return render_template("addcustomer.html")


@app.route("/addcustomer", methods=['POST', 'GET'])
def addcustomer():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            contactno = int(request.form['contactno'])
            email = request.form['email']
           

            addcustomer = Customer(name, address, contactno, email)
            addcustomer.cus_add()
            msg = "Record Inserted"
        except:
            msg = "Error in the INSERT"
    return render_template('customer.html', msg=msg)


@app.route("/editcustomer", methods=['POST', 'GET'])
def editcustomer():
    if request.method == 'POST':
        id = request.form['id']
        rows = Customer.emp_single(id)
        return render_template('editcustomer.html', rows=rows)


@app.route("/editcustomerrecord", methods=['POST', 'GET'])
def editcustomerrecord():
    if request.method == 'POST':
        employee_id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        contactno = request.form['contactno']
        email = request.form['email']
      

        addemployee = Customer(name, address, contactno, email)
        addemployee.emp_edit(employee_id)

        employeeList = Customer.view_all()
        return render_template('customer.html', msg="record updated", rows=employeeList)


@app.route("/deletecustomer", methods=['POST', 'GET'])
def deletecustomer():
    if request.method == 'POST':
        rowid = request.form['id']
        Customer.emp_delete(rowid)
    employeeList = Customer.view_all()
    return render_template('customer.html', msg="record deleted", rows=employeeList)



#................................Complaints Data............................................



@app.route("/complaints")
def complaints():
    complaintsList = Complaints.view_all()
    return render_template("complaints.html",rows=complaintsList);

@app.route("/addcomplaintsui")
def add_complaints_ui():
    return render_template("addcomplaints.html")


@app.route("/addcomplaints", methods=['POST', 'GET'])
def addcomplaints():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            phone = (request.form['phone'])
            msg = request.form['msg']
            dat = request.form['dat']

            addcustomer = Complaints(name, email, phone, msg, dat)
            addcustomer.complaints_add()
            msg = "Record Inserted"
        except:
            msg = "Error in the INSERT"
    return render_template('complaints.html', msg=msg)


@app.route("/editcomplaints", methods=['POST', 'GET'])
def editcomplaints():
    if request.method == 'POST':
        id = request.form['id']
        rows = Customer.emp_single(id)
        return render_template('editcustomer.html', rows=rows)


@app.route("/editcomplaintsrecord", methods=['POST', 'GET'])
def editcomplaintsrecord():
    if request.method == 'POST':
        employee_id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        contactno = request.form['contactno']
        email = request.form['email']
      

        addemployee = Customer(name, address, contactno, email)
        addemployee.emp_edit(employee_id)

        employeeList = Customer.view_all()
        return render_template('complaints.html', msg="record updated", rows=employeeList)


@app.route("/deletecomplaints", methods=['POST', 'GET'])
def deletecomplaints():
    if request.method == 'POST':
        rowid = request.form['id']
        Customer.emp_delete(rowid)
    employeeList = Customer.view_all()
    return render_template('complaints.html', msg="record deleted", rows=employeeList)



#................................Vehicle Data............................................

@app.route("/vehicle")
def vehicle():
    vehicleList = Vehicle.view_all()
    return render_template('vehicle.html', rows=vehicleList)


@app.route("/addvehicleui")
def add_vehicle_ui():
    return render_template("addvehicle.html")


@app.route("/addvehicle", methods=['POST', 'GET'])
def addvehicle():
    #SELECT `vehicle_id`, `registration_no`, `company`, `model`, `vehicle_type`, `transmission`, `customer_id` FROM `vehicle` WHERE 1
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            registration_no = request.form['registration_no']
            company = request.form['company']
            model = request.form['model']
            vehicle_type = request.form['vehicle_type']
            transmission = request.form['transmission']
            customer_id = int(request.form['customer_id'])

            

            addemployee = Vehicle(registration_no, company, model, vehicle_type, transmission,customer_id)
            addemployee.vehicle_add()
            msg = "Record Inserted"
        except:
            msg = "Error in the INSERT"
    return render_template('vehicle.html', msg=msg)


@app.route("/editvehicle", methods=['POST', 'GET'])
def editvehicle():
    if request.method == 'POST':
        id = request.form['id']
        rows = Vehicle.emp_single(id)
        return render_template('editemployee.html', rows=rows)


@app.route("/editvehiclerecord", methods=['POST', 'GET'])
def editvehiclerecord():
    if request.method == 'POST':
        employee_id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        contactno = request.form['contactno']
        salary = request.form['salary']
        joining_date = request.form['joiningDate']

        addemployee = Vehicle(name, address, contactno, joining_date, salary)
        addemployee.emp_edit(employee_id)

        employeeList = Vehicle.view_all()
        return render_template('employee.html', msg="record updated", rows=employeeList)


@app.route("/deletevehicle", methods=['POST', 'GET'])
def deletevehicle():
    if request.method == 'POST':
        rowid = request.form['id']
        Vehicle.emp_delete(rowid)
    employeeList = Vehicle.view_all()
    return render_template('employee.html', msg="record deleted", rows=employeeList)



#................................Employeee Data............................................
@app.route("/employee")
def employee():
    employeeList = Employee.view_all()
    return render_template('employee.html', rows=employeeList)


@app.route("/addemployeeui")
def add_employee_ui():
    return render_template("addemployee.html")


@app.route("/addemployee", methods=['POST', 'GET'])
def addemployee():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            contactno = int(request.form['contactno'])
            salary = int(request.form['salary'])
            joining_date = request.form['joiningDate']

            addemployee = Employee(name, address, contactno, joining_date, salary)
            addemployee.emp_add()
            msg = "Record Inserted"
        except:
            msg = "Error in the INSERT"
    return render_template('employee.html', msg=msg)


@app.route("/editemployee", methods=['POST', 'GET'])
def editemployee():
    if request.method == 'POST':
        id = request.form['id']
        rows = Employee.emp_single(id)
        return render_template('editemployee.html', rows=rows)


@app.route("/editemployeerecord", methods=['POST', 'GET'])
def editemployeerecord():
    if request.method == 'POST':
        employee_id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        contactno = request.form['contactno']
        salary = request.form['salary']
        joining_date = request.form['joiningDate']

        addemployee = Employee(name, address, contactno, joining_date, salary)
        addemployee.emp_edit(employee_id)

        employeeList = Employee.view_all()
        return render_template('employee.html', msg="record updated", rows=employeeList)


@app.route("/deleteemployee", methods=['POST', 'GET'])
def deleteemployee():
    if request.method == 'POST':
        rowid = request.form['id']
        Employee.emp_delete(rowid)
    employeeList = Employee.view_all()
    return render_template('employee.html', msg="record deleted", rows=employeeList)


if __name__ == '__main__':
    app.run()
