'''
    CSC 120 (A2)
    File: pokemon.py
    Author: Aditya Gupta
    Purpose: a program to read in Pokemon data from a file
            and organize it according to Pokemon type
            Data is structured in a 2D dictionary,
            User enter the input, and calculates
            high avg. type and value
'''

def add_max_val(avg_data):
    '''
    add_max_val adds all max. values
    of query into different dictionaries
    with their types

    Parameters:
        avg_data - dictionary w all avg data

    Returns:
        attribute_dict - dicitionary w attributes
        attribute_type - dictionary w types
    '''
    attribute_dict = {}
    attribute_type_dict = {}

    for i, j in avg_data.items():
        for type, value in j.items():
            if type not in attribute_dict:
                attribute_dict[type] = []
                attribute_type_dict[type] = []

            attribute_dict[type].append(value)
            attribute_type_dict[type].append(i)

    return attribute_dict, attribute_type_dict

def add_max_dict(attribute_dict, attribute_type_dict):
    '''
    add_max_dict adds all data from given two
    dictionaries containing types/attributes
    to another dictionaries which return max.
    values

    Parameters:
        attribute_dict - dicitionary w attributes
        attribute_type - dictionary w types

    Returns:
        vals - dicitionary w max. attribute value
        types - dictionary w max. type value
    '''
    vals = {}
    types = {}

    for val in attribute_dict:
        vals[val] = []
        types[val] = []
        
        temp_max = max(attribute_dict[val])

        for j in range(len(attribute_dict[val])):
            if attribute_dict[val][j] == temp_max or \
                attribute_dict[val][j] > temp_max:
                vals[val].append(attribute_dict[val][j])
                types[val].append(attribute_type_dict[val][j])

    return vals, types

def average_calculator(data, avg_data):
    '''
    average_calculator takes dictionary and file data
    and all max. avg. values on basis of input to the dictionary
    on basis of respective types and returns highest avg.

    Parameters - 
        data - 2D dictionary based on types/attributes
        avg_data - empty dictionary

    Returns:
        avg_data - dictionary w avg values
    '''
    dict = {'total': 4, 'hp': 5,
            'attack': 6, 'defense': 7, 
            'specialattack': 8, 'specialdefense': 9 ,
            'speed': 10}
    
    for key in data:
        if key not in avg_data:
            avg_data[key] = {}
        records = data[key]

        for record in records.values():
            for attribute in dict.keys():
                if attribute not in avg_data[key]:
                    avg_data[key][attribute] = 0
                avg_data[key][attribute] += int(record[attribute])
    
    for type in avg_data:
        for i in avg_data[type].keys():
            avg_data[type][i] = avg_data[type][i] / len(data[type])

    return avg_data

def filereader(filename):
    '''
    filereader reads the data from file
    and puts it into dictionary as required
    and on basis of attributes

    Parameters:
        filename - str, file name

    Returns:
        data - 2D dictionary
    '''
    data = {}
    file = open(filename, 'r')
    file.readline()

    for line in file:
        line = line.strip().split(',')
        name = line[1]
        type = line[2]
        strength = int(line[4])
        hp = int(line[5])
        attack = int(line[6])
        defense = int(line[7])
        special_attack = int(line[8])
        special_defense = int(line[9])
        speed = int(line[10])
        if type not in data:
            data[type] = {}

        data[type][name] = { 'total': strength, 'hp': hp, 
                              'attack': attack, 'defense': defense,
                              'specialattack': special_attack, 
                              'specialdefense': special_defense,
                              'speed': speed
                              }
    file.close()
    return data

def print_data(attribute_dict, attribute_type_dict):
    '''
    print_data is used to print data from the dictionaries,
    on basis of user input which is the commands given by the
    user.

    Parameters:
        attribute_dict - dictionary which contains all attributes
        attribute_type_dict - dictionary containing all attribute types

    Returns: None
    '''
    user_input = input().lower().strip()
    data = ['speed', 'attack', 'defense', 'hp', 
                  'total', 'specialattack', 'specialdefense']

    while user_input != '':
        type = []
        val = []
        
        if user_input == '':
            break
        while user_input not in data:
            user_input = input().lower().strip()

        for key in attribute_dict:
            type.append(attribute_type_dict[user_input])
            val.append(attribute_dict[user_input])

        type = list(type[0])
        val = list(val[0])
        if len(val) > 1:
            type = sorted(type)
            for i in range(len(val)):
                print("{}: {}".format(type[i], val[i]))
        else:
            index = val.index(max(val))
            print("{}: {}".format(type[index], max(val)))
        user_input = input().lower().strip()

def main():
    avg_data = {}
    filename = input()
    data = filereader(filename)
    avg_data = average_calculator(data, avg_data)
    attribute_dict, attribute_type_dict = add_max_val(avg_data)
    dict, type_dict = add_max_dict(attribute_dict, attribute_type_dict)
    print_data(dict, type_dict)
    
main()