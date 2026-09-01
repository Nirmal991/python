# def greet(student):
#     return f'Welcome {student} how are you'

# message = greet("Nirmal")
# print(message)

def greet(name, city):

    if name.strip() == '':
        return f'Hello freind'

    return f'Hello, {name} How are you in {city}?'

the_message = greet('James', 'Dallas')
print(the_message)

the_message = greet(city="Jab", name="Nirmal")
print(the_message)

the_message = greet(' ', "Jab")
print(the_message)
