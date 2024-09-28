# Using match case

# Less duplication less elifs all over the place

name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                 # _ catches everything else not matched
        print("Who? ")