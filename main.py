import time
import schedule

from tasks import liking_routine_1

# Go through liking routine 3 times a day
schedule.every().day.at("2:35").do(liking_routine_1)
schedule.every().day.at("12:22").do(liking_routine_1)
schedule.every().day.at("19:35").do(liking_routine_1)

# Go through follow routine once in the early morning
# Go through unfollow routine once during 'busisness hours'
# NOTE make sure to continue to like the posts of people who have been unfollowed

while True:
    schedule.run_pending()
    time.sleep(1)