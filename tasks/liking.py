from instapy import InstaPy
import random
import schedule
import time

word_ban_list = [
    'nsfw',
    'sexy',
    'drugs',
    'aggression',
    'breasts',
    'blood',
    'gore',
    'sport',
    'wrestling',
    'competition',
    'weed',
    'high'
]

smart_hashtags = [
    'tarotcards',
    'lightworker',
    'fullyraw'
]

influencers = [
    'goddessprovisions',
    'serpentfire',
    'wildfoodsco',
    'spiritnectar',
    '_theopaque_',
    'awake_spiritual',
    'we_are_spiritual',
    'thewildunknown',
]

competition = [
    'eatingevolved',
    'dandelionchocolate',
    'greenandblacks',
    'tarachocolate',
    'theochocolate',
    'zazubean'
]

def liking_routine_1():
    try:
        session = InstaPy(username='raw_magic_chocolate', password='Dragon93', use_firefox=True, page_delay=20)

        session.set_switch_language(False)    
        session.login()
        session.set_upper_follower_count(limit=5000)
        session.set_lower_follower_count(limit=25)
        session.set_dont_like(word_ban_list)

        # Like by smart hashtag
        session.set_smart_hashtags(smart_hashtags, limit=random.randint(1,10), sort='top', log_tags=True)
        session.like_by_tags(amount=random.randint(1,5), use_smart_hashtags=True)

        # Like posts on your person feed
        session.like_by_feed(amount=random.randint(15,30), randomize=True, interact=True)

        # Interact with other users followers
        session.set_user_interact(amount=10, randomize=True, percentage=50, media='Photo')
        session.set_do_follow(enabled=False, percentage=70)
        session.set_do_like(enabled=True, percentage=80)
        session.set_comments(["Cool", "Super!"])
        session.set_do_comment(enabled=False, percentage=80)
        random_influencers = random.sample(influencers, 2)
        session.interact_user_followers(random_influencers, amount=10, randomize=True)

        session.end()
    except:
        import traceback
        print(traceback.format_exc())
