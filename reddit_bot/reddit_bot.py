import praw
import config
import time
from log_comment import log_comment
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
subreddit = reddit.subreddit('All')

# Iterating through the current five hottest submissions in a subreddit
# Complexity O(n^3), though realistically it is far less since two of the loops contain limit constraints
# O(m * 10 * n) = O(n)
for submission in subreddit.hot(limit=50):
    print("Title:\t" + submission.title)

    # Iterating through the first ten comments in a submission
    for index, comment in enumerate(submission.comments):
        if index < 10 and hasattr(comment, 'body'):
            comment_words = str(comment.body.lower()).split()   # Converting a comment to a lowercase list of words

            # If a comment contains a homophone, then it'll be printed onto the console.
            # If there are multiple homophones, then the longest one will be printed
            target_word = find_longest_homophone(comment_words)     # Complexity: O(n)
            if target_word:

                # Printing for testing purposes
                print("\t>" + str(find_associated_homophone(target_word)))

                # Commenting
                comment_reply = find_associated_homophone(target_word)
                comment.reply(comment_reply)
                log_comment(comment_reply)

                time.sleep(30)  # Sleeping for 30 seconds
                break

    print()


