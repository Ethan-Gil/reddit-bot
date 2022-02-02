from webdict_definitions import get_definition
import csv

# Global Homophone Database
database = []


# Importing the homophone data from a CSV file and converting it into a 2D array
def import_data():
    file = '../data/homophone_db.csv'
    data = list(csv.reader(open(file)))
    del data[0]     # Removing the first row of the CSV file since it doesn't contain data
    return data


# Initializing the database
def init_database():
    global database

    # Checking to see if the database is empty. If it is, then the data will be imported into the database variable
    if not database:
        database = import_data()
        return


# Method that will search the word bank for a homophone of a word, and return the
def find_homophone(word):
    found = False

    # Iterating through each row in the CSV file and checking to see if the word exists
    for index, row in enumerate(database):
        if word in row:
            found = True

            # The relation_id is how multiple homophones in the word bank are connected
            # The database is structured so that homophones are grouped together, so if a word has
            # a homophone, it will either be directly above or below it and contain the same relation_id
            relation_id = row[3]

            # Checking the row above the current index
            if index > 0 and relation_id == database[index - 1][3]:
                homophone = database[index - 1][1]

            elif relation_id == database[index + 1][3]:
                homophone = database[index + 1][1]

            # If a word has been found and the definition exists, then that definition is returned.
            # If the definition is not valid though (error code 1) then an Error message will be printed.
            # TODO: Consider using the PyDictionary definition is the Webster's definition isnt available
            if found:
                if get_definition(homophone) == 1:
                    print("Error: Definition not found")
                    return

                return get_definition(homophone)

            else:
                return "No homophone found"


init_database()
print(find_homophone("awhile"))
