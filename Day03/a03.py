# container = ["staff", "potion", "spellbook"]

# new_item = input("Enter the new item: ")

# ejected_item = container.pop()
# print("Portal transition activated!")
# print("Ejected oldest item: ", ejected_item)
# container.append(new_item)
# print(container)


# playlist = ["Inception", "The Matrix", "Interstellar"]


# new_song = input("Enter the song to add:  ")
# if new_song in playlist:
#     print("Already Added! ")
    
# playlist.append(new_song)
# playlist.sort()
# print(playlist)

# wagons = ["coal", "iron", "gold", "coal", "timber", "coal"]

# res = input("Enter the resources: ")

# if res in wagons:
#     index = wagons.index(res)
#     count = wagons.count(res)
#     print("Count: ", count)
#     print("First resource is: ", index + 1)
# else: 
#     print("Resource not found !!")

guests = ["Guido", "Esha", "Rajan", "Kishori"]

# new_guest = input("Enter the name of bouncer: ")

# if new_guest in guests:
#     print(f"{new_guest} moved in front...")
#     guests.remove(new_guest)
#     guests.insert(0,new_guest)
#     print(guests)
# else:
#     print("Access denied. Not on the VIP list.")
#     print(guests) 

str = "Meet me at midnight"

# words = str.split()

# # reverse_list = []
# # for i in words:
# #     reverse = i[::-1]
# #     reverse_list.append(reverse)

# reverse_list = [i[::-1] for i in words]
    
# result = " ".join(reverse_list)
# print(result)

# Original = [45, 88, 30, 98, 50]

# result = [min(i + 5, 100) if i > 50 else i + 10 for i in Original]

# print(result)


# coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]

# result = [i for i in coords if i[0] >= 0 and i[1] >= 0]

# print(result)

# cart = ["apple", "banana", "apple", "orange", "banana", "banana"]

# result = list({c for c in cart})

# print(result)

# N = 5
# K = 2

# soldiers = list(range(1, N+1))

# print("Soldier circle initialized:", soldiers)

# index = 0


# while len(soldiers) > 1:
#     index = (index + K - 1) % len(soldiers)
    
#     eliminated = soldiers.pop(index)
    
#     print(f"Eliminated soldier: {eliminated} (Remaining: {soldiers})")
    
# print("The sole survivor is:", soldiers[0])


grid = [["." for _ in range(5)] for _ in range(5)]

grid[2][3] = "F"
# print(grid)

row = int(input("Enter row (0-4): "))
col = int(input("Enter column (0-4): "))

if 0 <= row <= 4 and 0 <= col <= 4:

    grid[row][col] = "S"

    if row == 2 and col == 3:
        print("Yum! The snake ate the food!")

    for r in grid:
        print(" ".join(r))

else:
    print("Invalid coordinates!")

    
    



