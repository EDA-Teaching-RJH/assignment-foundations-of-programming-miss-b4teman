print("hellooo test")

#1. Init database:
def init_database():
    names = ["Picard", "Riker", "Spock", "Kirk", "Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    divs  = ["Command", "Engineering", "Operations", "Security", "Sciences"]
    ids   = ["SP937215", "SC231427", "S179276SP", "SC9370176CEC", "SC110398"]
    #The 4 lists, ID for crusher made up because I couldnt find one, and took out letters
    return names, ranks, divs, ids
    #Returning the lists

#2. Display menu:
def display_menu():
    user = input("What's your full name? ")
    #Quering full name
    print("1. Add member")
    print("2. Remover member")
    print("3. Update rank")
    print("4. Display roster")
    print("5. Search crew")
    print("6. Filter by division")
    print("7. Calculate payroll")
    print("8. Count officers")
    #Options

#3. Add member:
def add_member(names, ranks, divs, ids):
    newId = input("ID: ")
    #Validates Id is unique
    if newId in ids:
        #Validates rank is a TNG(?) rank
        print("ID already exists.")
        return

    rank = input("Rank: ")
    validRanks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    if rank not in validRanks:
        print("Invalid rank.")
        return

    names.append(input("Name: "))
    ranks.append(rank)
    divs.append(input("Division: "))
    ids.append(newId)
    #Appending data to the 4 lists

#4. Remove member:
def remove_member(names, ranks, divs, ids):
    removeId = int(input("Enter ID: "))
    #Asks for ID
    if removeId in ids:
        index = ids.index(removeId)
        #Finds it in index
        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)
        #Indexes ID (position of ID)
    else:
        print("ID not found")

#5. Update rank:
def update_rank(names, ranks, ids):
    updateID = int(input("ID: "))
    #Asks user for the id to UPDATE
    if updateID in ids:
        index = ids.index(updateID)
        ranks[idx] = input("New Rank: ")
        #Updates the rank string

#6. Display roster:
def display_roster(names, ranks, divs, ids):
    for i in range(len(names)):
        #'Iterates' through list
        print(ids[i], names[i], ranks[i], divs[i])
        #Prints table of all crew 

#7. Search crew:
def search_crew(names, ranks, divs, ids):
    searchTerm = input("Search name: ").lower()
    #Asking for search term
    for i in range(len(names)):
        if term in names[i].lower():
        #Using lower because python is case sensitive
            print(names[i], ranks[i], divs[i], ids[i])

#8. Filter by division:
def filter_by_division(names, ranks, divs, ids):
    searchDiv = input("Division: ").lower()
    #Asks for search term
    for i in range(len(names)):
        if divs[i] == searchDiv:
            print(names[i], ranks[i], ids[i])
            #Printing anything containing term

#9. Calc payroll:
def calculate_payroll(ranks):
    total = 0
    #Starting with 0
    for r in ranks:
        if r == "Captain":
            total += 500
        elif r == "Commander":
            total += 300
        else:
            total += 200
        #Adds 'pay' per diff ranks
    return total

#10. Count officers:
def count_officers(ranks):
    count = 0
    for r in ranks:
        #Adds 1 to count for each time there's captain or commander
        if r == "Captain" or r == "Commander":
            count += 1
    return count

#Main loop: Kinda inspired by the other code
def main():
    names, ranks, divs, ids = init_database()

    while True:
        choice = display_menu()

        if choice == "1":
            add_member(names, ranks, divs, ids)

        elif choice == "2":
            remove_member(names, ranks, divs, ids)

        elif choice == "3":
            update_rank(names, ranks, divs, ids)

        elif choice == "4":
            display_roster(names, ranks, ids)

        elif choice == "5":
            search_crew(names, ranks, divs, ids)

        elif choice == "6":
            filter_by_division(names, ranks, divs, ids)

        elif choice == "7":
            total = calculate_payroll(ranks)
            print("Total payroll:", total)

        elif choice == "8":
            print("Officer count:", count_officers(ranks))

        else:
            print("Invalid choice.")

main()