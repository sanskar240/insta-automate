from instabot import Bot
bot = Bot()
bot.login(username="holy_nutt", password="XXXXXXXXX")

######  upload a picture #######
bot.upload_photo("starship.jpg", caption="elon sends one of those to space again")

######  follow someone #######
bot.follow("elonrmuskk")

######  send a message #######
bot.send_message("Hello from Dhaval", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("sanskarsays")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()