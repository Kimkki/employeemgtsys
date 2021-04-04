class Employee:
    # init method to initialize the attributes
    def __init__(self, name, iD_num, department, job_title):
        self.__name = name
        self.__iD_num = iD_num
        self.__department = department
        self.__job_title = job_title

        # sets name attribute

    def set_name(self, name):
        self.__name = name

        # sets id number attribute

    def set_id_num(self, iD_num):
        self.__iD_num = iD_num

    # sets department attribute
    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    # returns the name attribute
    def get_name(self):
        return self.__name

    # returns the phone attribute
    def get_id_num(self):
        return self.__iD_num

    # returns the email attribute
    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        return "Name: " + self.__name + \
               "\nID Number: "+ self.__iD_num + \
               "\nDepartment: " + self.__department + \
               "\nJob title: " + self.__job_title
