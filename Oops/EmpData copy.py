from Oops.EmployeeData import EmployeeDetails


class EmpDetails(EmployeeDetails):

    def empName(self):
        print("This is a Emp")

    def empName2(self):
     self.empName()


emp = EmpDetails("Anil", 9876543210, "India")

emp.empName2()
#print(emp.company)
emp.empCompany()
