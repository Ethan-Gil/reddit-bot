from webdict_definitions import get_definition
import csv

# Global homophone database and word list.
# The word list will simply be a list of every word in the database,
# whereas the database is a table with each row containing the word id, word, and it's relation id.
database = []
word_list = []


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


# Creating a simple list that contains all the words in the database
def create_word_database():
    global word_list
    for index, row in enumerate(database):
        word_list.append(row[1])            # In the database, words are kept in the 2nd column


# Method that will search the word bank for a homophone of a word, and return it if found
def find_associated_homophone(word):

    # Iterating through each row in the CSV file and checking to see if the word exists
    for index, row in enumerate(database):
        if word in row:
            relation_id_col = 2

            # The relation_id is how multiple homophones in the word bank are connected
            # The database is structured so that homophones are grouped together, so if a word has
            # a homophone, it will either be directly above or below it and contain the same relation_id
            relation_id = row[relation_id_col]

            # Checking the rows above and below the current row
            if index > 0 and relation_id == database[index - 1][relation_id_col]:
                homophone = database[index - 1][1]

            elif relation_id == database[index + 1][relation_id_col]:
                homophone = database[index + 1][1]

            # If a word has been found and the definition exists, then that definition is returned.
            # If the definition is not valid though (error code 1) then an Error message will be printed.
            if homophone:
                if get_definition(homophone, word) == 1:
                    print("Error:\t\tDefinition-Not-Found Error")
                    print("Homophone: " + homophone)
                    print("Original Word: " + word)
                    return

                elif get_definition(homophone, word) == 2:
                    print("Error:\t\tTimeout Error")
                    return

                elif get_definition(homophone, word) == 3:
                    print("Error:\t\tGeneral Error")
                    return

                return get_definition(homophone, word)

            else:
                return "Error: No homophone found"


# Returns true if the given word is a homophone (it's in the word list)
def is_homophone(word):
    if word in word_list:
        return True

    return


# Given a list of words (from a reddit comment) this method will check to see which words in the list
# are homophones, and then return the longest one.
# If there are no homophones in the comment, false is returned
def find_longest_homophone(comment_words):
    homophones = []
    for word in comment_words:
        if is_homophone(word):
            homophones.append(word)

    # Returning the longest homophone in the list
    if homophones:
        return max(homophones, key=len)

    return False


# Initiating the global database and the word list
init_database()
create_word_database()
