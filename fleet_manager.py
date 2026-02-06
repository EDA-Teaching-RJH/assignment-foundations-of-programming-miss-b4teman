print("hellooo test")

#Init database
def init_database():
    names = ["Picard", "Riker", "Spock", "Kirk", "Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    divs  = ["Command", "Engineering", "Operations", "Security", "Sciences"]
    ids   = [SP937215, SC231427, S179276SP, SC9370176CEC, SC110398]
    #The 4 lists, ID for crusher made up because I couldnt find one, and took out letters
    return names, ranks, divs, ids
    #Returning the lists