import requests
import config

api_url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/%s?key={config.API_KEY}'


# Sends a request to the API, handles the response data, and prints the definition of the word
def get_definition(given_word):
    try:
        response = requests.get(api_url % given_word, timeout=3)
        data = response.json()  # Storing the response data, which is a list of dictionaries containing word meanings.
        word_info = data[0]  # We will store the first dictionary into word_info
        definition = word_info['shortdef'][0]  # Since we only want one definition, we will find the first element in the value list corresponding to the shortdef key

        if definition:
            return f'Webster\'s Dictionary Defines {given_word} as "{definition}"'

        else:
            return 'Definition not found'

    # TODO:  More Specific Exception Handling
    except IndexError as error:
        # raise IndexError('Fee Fi Fo Fum, someone got the Index wrong!')
        return 1

    except requests.Timeout as error:
        print(error)

    # except Exception as error:
    #     print("General Error")
