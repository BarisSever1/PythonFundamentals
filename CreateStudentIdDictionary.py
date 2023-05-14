from pprint import pprint
student = {"student_id": {}}
while True:
    process = input("Enter a process: ").lower()
    if process == "exit":
        break
    if process == "create":
        create_key = input("Enter key: ")
        create_value = input("Enter value: ")
        student.get("student_id")[create_key] = create_value
    if process == "delete":
        delete = input("Enter a key to delete it: ")
        student.get("student_id").pop(delete)
    if process == "update":
        update_key = input('Enter a key to update it:  ')
        update_value = input('Enter a value to update the key you have entered: ' )
        student.get("student_id").update({update_key : update_value})
    if process == "read":
        read_key = input("Enter a key to read the value: ")
        print(student.get("student_id").get(read_key))

pprint(student)
