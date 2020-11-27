from Oops.EmployeeData import EmployeeDetails
class EmpDetails(EmployeeDetails):
    def empName2(self):
        self.empName()

emp=EmpDetails("Shiva",987654321,"Chennai")
emp.empName2()