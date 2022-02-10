import praw
import config
import time
from log_comment import log_comment
from log_exception import log_exception
from homophone import find_associated_homophone, find_longest_homophone

# Creating a Reddit instance
reddit = praw.Reddit(
    client_id=config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    user_agent='<console:MistakenBot:1.0>',
    username=config.USERNAME,
    password=config.PASSWORD
)

# We will be looking through the Python Subreddit
subreddit = reddit.subreddit('memes')

comment_limit = 10  # The number of comments in a submission that should be read
time_limit = 20

# Iterating through the current five hottest submissions in a subreddit
# Complexity O(n^3), though realistically it is far less since two of the loops contain limit constraints
# O(m * 10 * n) = O(n)
for submission in subreddit.rising(limit=200):
    for index, comment in enumerate(submission.comments):

        try:
            if index < comment_limit and hasattr(comment, 'body'):
                comment_words = str(comment.body.lower()).split()   # Converting a comment to a lowercase list of words

                # If a comment contains a homophone, then it'll be printed onto the console.
                # If there are multiple homophones, then the longest one will be printed
                target_word = find_longest_homophone(comment_words)     # Complexity: O(n)
                if target_word:

                    # Printing for testing purposes
                    print("Title:\t\t\t" + submission.title)
                    print("Bot Reply:\t\t" + str(find_associated_homophone(target_word)))
                    print()

                    # Commenting
                    # comment_reply = find_associated_homophone(target_word)    # Complexity: O(n)
                    # comment.reply(comment_reply)
                    # log_comment(str(submission.title), comment_reply)

                    time.sleep(time_limit)  # Sleeping for 30 seconds
                    break

        except Exception as e:
            # log_exception(str(e))
            print("\nException:")
            print(e)
            pass




