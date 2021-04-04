import employee
import pickle

# Constant variables for menu
SEARCH_EMP = 1
ADD_EMP = 2
EDIT_EMP = 3
DELETE = 4
EXIT = 5

# file name to store data
FILENAME = 'employee.txt'


def main():
    # use method load_employees to load employees in
    # a dictionary and store in av_employee
    av_employees = load_employees()

    # Process the results from menu
    choice = 0
    while choice != EXIT:
        choice = retrieve_menu_choice()

        # process the choice
        if choice == SEARCH_EMP:
            # use search_employee method to search what
            # the user has entered
            search_employee(av_employees)
        elif choice == ADD_EMP:
            add_employee(av_employees)
        elif choice == EDIT_EMP:
            edit_employee(av_employees)
        elif choice == DELETE:
            delete_employee(av_employees)

    # done with while loop,
    # save available employee on file
    save_employee_on_file(av_employees)


def load_employees():
    try:
        # open the file - employee.txt
        input_file = open(FILENAME, 'rb')

        # unpickle the dictionary
        employee_dic = pickle.load(input_file)

        # close the file
        input_file.close()
    except IOError:
        # failure to open the file means there is no file
        # create an empty dictionary and return to the caller
        # of this method- the caller will create a new file
        employee_dic = {}  # empty dictionary

    return employee_dic


def retrieve_menu_choice():
    print('Your menu')
    print('******************')
    print('1 Search for employee name')
    print('2 Add new employee')
    print('3 Edit employee details')
    print('4 Delete employee')
    print('5 Exit the system')
    print("")

    choice = int(input('Please enter your choice: choose one from the list above: '))

    # Validation: if the user enters wrong choice from the list above
    # prompt the user to re-enter his/her choice
    while choice < SEARCH_EMP or choice > EXIT:
        choice = int(input('Invalid choice; choose from the list above: '))

    return choice


def search_employee(e_employee):
    id_num = input('Enter employee ID Number: ')

    # search for it in the dictionary
    print(e_employee.get(id_num, 'ID number is not found.'))


# The add_employee function adds a new employee details to a file
def add_employee(e_employee):
    name = input('Name: ')
    id_num = input('ID: ')
    department = input('Department: ')
    job_title = input('Job Title: ')

    # create employee object and fill
    # it with the details above
    new_emp = employee.Employee(name, id_num, department, job_title)

    # if employee's ID number does not exist in the dictionary
    #  add it as a key with new_emp object as the associated value
    if id_num not in e_employee:
        e_employee[id_num] = new_emp
        print('new employee successfully added')
    else:
        print('ID number already on file.')


# edit employee details, employee must be on file
def edit_employee(e_employee):
    id_number = input('Enter employee ID Number: ')

    if id_number in e_employee:
        # get employee new details
        name = input('Enter new name: ')
        department = input('Enter new department: ')
        job_title = input('Enter new job title')

        # Create employee object
        edited_employee = employee.Employee(name, id_number, department, job_title)

        # update details
        e_employee[id_number] = edited_employee
        print('employee details successfully updated')
    else:
        print('ID number supplied is not found.')


def delete_employee(e_employees):
    id_numb = input('Enter employee ID Number: ')

    # if id number supplied by the user is found,
    # delete the entry
    if id_numb in e_employees:
        del e_employees[id_numb]
        print('employee details successfully deleted')
    else:
        print('ID number not on file')


def save_employee_on_file(e_employees):
    output_file = open(FILENAME, 'wb')

    pickle.dump(e_employees, output_file)

    output_file.close()


# call the main function
main()
