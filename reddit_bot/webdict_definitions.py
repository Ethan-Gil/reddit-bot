from random import randrange
import random
import requests
import config

api_url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/%s?key={config.API_KEY}'

# TODO: Consider drawing definition strings from a file instead of encoding them here.
definition_templates = [
    'Webster\'s dictionary defines %s as "%s" - oh wait, did you mean "%s"? That\'s my bad, I am often mistaken.',
    'At first I was confused and thought you meant %s, which of course is defined as "%s". Took me a minute to realize that you really meant "%s" though.',
    'Fun fact: %s is defined as "%s"... and I am now realizing that you said "%s", that\'s my bad.'
    'Beep Boop. %s is defined as "%s", in case anyone was wondering. No need to thank me, just doing my duty - wait you meant "%s"... I wish I wasn\'t mistaken so often.'
]


# Sends a request to the API, handles the response data, and prints the definition of the word
def get_definition(given_word, original_word):
    try:
        response = requests.get(api_url % given_word, timeout=3)
        data = response.json()  # Storing the response data, which is a list of dictionaries containing word meanings.
        word_info = data[0]  # We will store the first dictionary into word_info
        definition = word_info['shortdef'][
            0]  # Since we only want one definition, we will find the first element in the value list corresponding to the shortdef key

        if definition:
            return f'Webster\'s Dictionary Defines {given_word} as "{definition}" - oh wait, did you mean "{original_word}"? That\'s my bad, I am often mistaken.'
            # random_index = randrange(len(definition_templates))
            # temp = definition_templates[random_index]
            # print(temp)
            # print(definition_templates[random_index] % (given_word, definition, original_word))

        else:
            return 'Definition not found'

    # TODO:  More Specific Exception Handling
    except IndexError:
        return 1

    except requests.Timeout:
        return 2

    except:
        return 3
