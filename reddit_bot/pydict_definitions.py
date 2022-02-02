from PyDictionary import PyDictionary

# Creating a dictionary instance
dictionary = PyDictionary()


def get_pydict_definition(word):
    dictionary_meaning = dictionary.meaning(word)
    # TODO: Exception handling for words not in the dictionary

    # Converting the meaning list (a python dict) into a list and extracting the first definition
    meaning_list = list(dictionary_meaning.values())[0]
    definition = meaning_list[0]

    return f'The word "{word}" is defined as {definition}'

