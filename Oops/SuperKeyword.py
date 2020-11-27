from Oops.EmployeeData import EmployeeDetails
class EmpDetails(EmployeeDetails):

# Here Emp is available in inherited class also but Local class gets called first.
    def empName(self):
       print("This is super keyword Emp")


    def empName2(self):
        super.empName()

emp=EmpDetails("Shiva",987654321,"Chennai")
emp.empName2()