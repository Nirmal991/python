from pprint import pprint
# # 1. Empty dictionary
# empty_dict_1 = {}
# empty_dict_2 = dict()

# # 2. Dictionary literal with data
# student = {
#     "name": "Arham",
#     "age": 21,
#     "course": "PGCP-AI",
#     "grades": [85, 90, 88]
# }

# # 3. Using the dict() constructor with keyword arguments
# employee = dict(name="Lisa", id=1042, department="R&D")

# # 4. Using dict() with list of tuples (key-value pairs)
# colors = dict([("red", "#FF0000"), ("green", "#00FF00"), ("blue", "#0000FF")])

# print("Student:", student)
# print("Employee:", employee)
# print("Colors:", colors)

# # Acessing Elements:
# profile = {"username": "vinod_k", "role": "admin"}

# print(profile['username'])

# try:
#     print(profile['email'])
# except KeyError as e:
#     print(f"KeyError caught: Key {e} does not exist.")


# Dict comprehension

def main(): 
    # emps = [
    #     "1928,Kumar,ADMIN,32000",
    #     "9383,Harish Rao,ACCOUNTING,42000",
    #     "8178,James,TRAINING,33000",
    #     "7442,Krihna Kumar,ADMIN,33000",
    #     "8273,Ramesh Iyer,ACCOUNTING,35000",
    # ]

    # emp_dicts = {
    #     emp.split(",")[0]: emp.split(',')[1:]
    #     for emp in emps
    # }

    # print(emp_dicts)

    # while True:
    #     emp_id = input("Enter employee id to search (press RETURN to quit): ")

    #     if emp_id == "":
    #         break

    #     print(emp_dicts.get(emp_id, "No emp found "))

    # students = {
    # "A": 10,
    # "B": 20,
    # "C": 30
    # }

    # result = {value: key for key, value in students.items()}
    # print(result)

    p1 = {}
    p2 = dict()

    print(f'{p1=}')
    print(f'{p2=}')

    p3 = {"name": "Vinod", "city": "Bangalore", "email": ["vinod@vinod.co", "vinod@cyblore.com"]}
    p4 = dict(name = "Shyam", emails = ["shyam@gmail.com"])

    print(f"{p3=}")
    print(f"{p3=}")

    print(p3["city"])
    pass
main()
