n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

print("helloooo")

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
    #Kept repeating loading module 0
        print("Loading module " + str(loading))
        loading += 1
        #Adds 1 to loading
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1": 
            #added another = 
            print("Current Crew List:")    
            for i in range(len(n)):
            #How many items are in the list because it can update and therw wasnt 10
                print(n[i] + " - " + r[i] + " - " d[i]) 
                #Added the division list too
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)
            #adds crew member to each class (?) not just name
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           
            if rem in n:
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
            else:
            print("Crew member not found.")
            #If the user doesnt mention a name in the list the code wouldn't work

        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": 
                    #added or rank == before "commander"  
                    count = count + 1
            print("High ranking officers: " , count) 
            #Changed + to , because string and number/int
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        #While fuel>0 is useless because it always will be as 'fuel=100'    
        print("Idling...")
        break 
            
        print("End of cycle.")

run_system_monolith()
#Added brackets at the end - syntax
