from pprint import pprint
student = {}
while True:
    process = input("Enter a process: ").lower()
    if process == "exit":
        break
    if process == "create":
        student_id = int(input("Enter student id: "))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = input("Enter phone number: ")
        student[student_id] = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone
        }
    if process == "delete":
        student_id = int(input("Enter student id to delete: "))
        delete_key = input("Enter a key to delete it: ")
        student.get(student_id).pop(delete_key)
    if process == "update":
        student_id = int(input("Enter a student id to update it: "))
        update_key = input('Enter a key to update it:  ')
        update_value = input('Enter a value to update the key you have entered: ' )
        student.get(student_id).update({
                update_key: update_value
        }
        )
    if process == "read":
        read_id = int(input("Enter a student id: "))
        pprint(student.get(read_id))

pprint(student)
