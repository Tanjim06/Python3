class RailwayForm:
    FormType = 'Application Form'
    def printData(self):
        print(f"The passenger name is {self.name} and train name is {self.trainName}.The form type is {self.FormType}")



MyApplication = RailwayForm()

MyApplication.name = 'Tanjim'
MyApplication.trainName = 'Rajdhani Express'
MyApplication.printData()