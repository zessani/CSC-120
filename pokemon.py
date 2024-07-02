"""
    File: pokemon.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program analyzes a Pokemon file containing data on
             Pokemon types and their attributes. It computes the average
             values for each type's attributes and  addresses a 
             inquiries regarding Pokemon attributes. It provides 
             responses by indicating the Pokemon type(s) with the highest
             average value for each queried attribute.
"""


def read_file():
     
    """
    Read the file of comma-seperated values and convert into a 2D-dictionary
    with Pokemon types in the outer dictionary and pokemon names as keys
    and stats as a list of values in the inner dictionary
  
    Parameters: None
  
    Returns: A dictionary that is a representation of the comma-seperated
    values file

    """
     
    file_name = input()
    myFile = open(file_name,"r")
    pokemon = {}
    for line in myFile:
        if line[0] != "#":
            # convert the lines to a list seperated by a comma
            line_list = line.strip().split(',')
            key = line_list[2]
            name = line_list[1]
            if key in pokemon:
                # slice from 4-11 to get the stats required
                pokemon[key][name] = line_list[4:11]
            else:
                inner_dict = {}
                #add the stats to the inner dictionary according to the names
                inner_dict[name]= line_list[4:11]
                pokemon[key] = inner_dict
    return pokemon

def average_stats(pokemon):
    """
    Calculates the averages of the stats of each type of pokemon
    and puts it into a dictionary
  
    Parameters: A 2d dictionary of all types of pokemons, with their names 
                individual stats
  
    Returns: A 2D dictionary of only the types of pokemons and the average
            stats of all pokemons of the type

    """
    avg_dict = {}
    for poke_type, stats_dict in pokemon.items():
        # extracting the stat values of each type
        stats_list = list(stats_dict.values())
        type_stats = [0] * 7
        # calculate the total stats of all pokemons of the same
        #  type
        for stats in stats_list:
            for j in range(len(stats)):
                type_stats[j] += int(stats[j])
            
        avg_stats = [0] * 7
        for k in range(7):
            #calculate the average stats by dividing the total stats
            # by the number of stats
            avg_stats[k] = type_stats[k] /len(stats_list)
        avg_dict[poke_type] = avg_stats
            

    return avg_dict


def query(avg_dict):

    """

    Prompt the user for a pokemon property and display type(s) with
    the highest average value
  
    Parameters: A 2D dictionary of pokemon types and the average stats of all
                pokemons of the same type.
  
    Returns: None (prints the type and the highest value according to the
                    prompt)

    """

    valid=["total","hp","attack","defense",
           "specialattack","specialdefense","speed"]
    query = None
    highest = None
    while query != "":
        query = input().lower()
        
        if query in valid:
            max = 0
            highest = []
            x = valid.index(query)
            #iterate through the dictionary to check highest value
            for poke_type, avgs in avg_dict.items():
                if avgs[x] >max: 
                    max = avgs[x]
                    highest = [poke_type]
                elif avgs[x] == max:
                    # add type to the list of types of the highest property
                    highest.append(poke_type)
            highest_list = sorted(highest)
            for item in highest_list:
                # display type with highest average value
                print("{}: {}".format(item, max))
       
    



def main():
    pokemon = read_file()
    
    avg_dict = average_stats(pokemon)
    query(avg_dict)
main()