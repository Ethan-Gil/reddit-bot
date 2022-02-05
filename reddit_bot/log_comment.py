from datetime import date, datetime
import csv


# Given a comment, this method will add that comment, along with the current date and time to the log file.
def log_comment(comment):
    log_directory = '../data/comment_log.csv'

    current_date = date.today()
    current_time = datetime.now().strftime("%H:%M:%S")

    with open(log_directory, 'a', newline='') as log_file:
        writer = csv.writer(log_file)
        writer.writerow([comment, current_date, current_time])
