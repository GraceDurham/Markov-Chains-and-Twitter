import os
import sys
import twitter
from random import choice
# from unidecode import unidecode
import io


def open_and_read_file(filenames):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    body = ""

    for filename in filenames:
        text_file = io.open(filename, encoding="utf-8")
        body = body + text_file.read()
        text_file.close

    return body 


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains."""

    chains = {}

    words = text_string.split()
    print words

    # my_clean_list = [unidecode(x.decode('utf8')) for x in words]
    # print my_clean_list


    # for i in range(len(my_clean_list) - 2):
    #     key = (my_clean_list[i], my_clean_list[i + 1])
    #     value = my_clean_list[i + 2]
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]
      
        if key not in chains:
            chains[key] = []

        chains[key].append(value)
       

    return chains



def make_text(chains):
    
    key = choice(chains.keys())

    words = [key[0], key[1]]

    while key in chains:
        word = choice(chains[key])
        if len(" ".join(words)) + len(word) < 140:
            words.append(word)
            key = (key[1], word)
        else:
            break

    return " ".join(words)



def tweet(chains):

    api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])


    while True:
        status = api.PostUpdate(make_text(chains))
        print status
        print status.text
        print #blank line
        response = raw_input("Enter to tweet again [q to quit] > ")
        if response.lower() == "q":
            break


filenames = sys.argv[1:]
#sys.argv is a list in Python, which contains the command-line arguments passed to the script. 


# Open the file and turn it into one long string
input_text = open_and_read_file(filenames)

# Get a Markov chain
chains = make_chains(input_text)
print chains

make_text(chains)

tweet(chains)

