# str = "Learning Python is fun!"
# print(len(str.split()))
# print(len(str))

# str = "Bangalore"
# print(str[::-1].upper())

# str = "vinod.co"

# split_str = str.split("@")
# if len(split_str)<2:
#     print("Invalid Email")
# else:
#     print(split_str[1])

# vowels = ['a', 'e', 'i', 'o', 'u']
# text_str = "Vinod Kumar Kayartaya"
# a = 0
# e = 0
# v_i = 0  
# o = 0
# u = 0
# consonant = 0

# for i in range(len(text_str)):
#     char = text_str[i].lower()  # Grab the character and make it lowercase
    
#     if char == 'a':
#         a += 1
#     elif char == 'e':
#         e += 1
#     elif char == 'i':
#         v_i += 1
#     elif char == 'o':
#         o += 1
#     elif char == 'u':
#         u += 1
#     elif char.isalpha():
#         consonant += 1

# print(a)
# print(e)
# print(v_i)
# print(o)
# print(u)
# print(consonant)

# str = "WELCOME TO BANGALORE CITY"
# split_str = str.lower().split()
# result = []
# for word in split_str:
#     capitalized = word[0].upper() + word[1:]
#     result.append(capitalized)
# title_formatted = " ".join(result)
# print(title_formatted)

# str = "Xyz"
# result = ""
# for ch in str:
#     if ch.isupper():
#         result += chr((ord(ch) - ord('A') + 3) % 26 + ord('A'))
#     elif ch.islower():
#         result += chr((ord(ch) - ord('a') + 3) % 26 + ord('a'))
#     else:
#         result += ch
# print(result)

main_str = "banana"
substring = "an"

# parts = main_str.split(substring)

# print(len(parts) - 1)
count = 0
for i in range(len(main_str) - len(substring)+1):
    match = True
    for j in range(len(substring)):
        if main_str[i+j] != substring[j]:
            match = False
            break
        
    if match:
        count +=1
        
# print(count)

str = "Vinod Kumar Kayartaya"
# str = "Bangalore"

# Sample Input: "Vinod Kumar Kayartaya"
# Sample Output: "V. K. Kayartaya"
# Sample Input: "Bangalore"
# Sample Output: "Bangalore"

result = ""
words = str.split()
# print(words)
# if len(words) == 1:
#     print(str)
# else:
#     for word in words[:-1]:
#         result += word[0].upper() + "."
#     result += words[-1]
#     print(result)
    
    
# print(result)
    
    
# str = "babad"
# # output = bab or aba

# longest = ""
# for i in range(len(str)):
#     left = i
#     right = i
    
#     while left >= 0 and right < len(str):
#         if str[left] == str[right]:
#             if right - left + 1 > len(longest):
#                 longest = str[left:right+1]
                
#             left -= 1
#             right += 1
#         else:
#             break
        
#     left = i
#     right = i+1
    
#     while left >= 0 and right < len(str):
#         if str[left] == str[right]:
#             if right - left + 1 > len(longest):
#                 longest = str[left:right+1]
                
#             left -= 1
#             right += 1
#         else:
#             break


# str1 = "aabcccccaaa"
# result = ""
# count = 1
# for i in range(len(str)):
#     if i == len(str1) - 1:
#         result += str1[i] + str(count)
    
#     elif str1[i] == str1[i+1]:
#         count += 1
#     else:
#         res += str1[i] + str(count)
#         count = 1
    
#     if(len(str1) == len(res.split("1")) - 1):
#         res = str1

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
        key = "".join(sorted(word))
        print(f"{key=}")

        if key not in groups:
            groups[key] = []
            print(f'{groups=}')

        groups[key].append(word)
        print(f"{groups=}")

print(list(groups.values()))

def date_valid():
    date = input("Enter the date for validation...")
    
    split_date = str.split('/')
    
    if len(split_date) > 3:
        print(f"Invalid input try in given format")
        return
    
    day = int(split_date[0])
    month = int(split_date[1])
    year = int(split_date[2])
    
    months = ("January", "feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    
    if month > 12 and month < 1:
        print("Invalid month")
        return
    
    leap_year = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0) 
    
    if month == 2:
        if leap_year:
            max_days = 29
        else:
            max_days = 28
            
    elif month == 4 or month == 6 or month == 11:
        max_days = 30
    else:
        max_days = 31
        
    if day <= 0 or day > max_days:
        print('Invalid days')
        return
    print(f"{months[month-1]} {day},  {year}")
    
    
    