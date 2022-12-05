from instabot import Bot

bot = Bot()

bot.login(user_name="user_name", password="user-password")

bot.upload_photo("your_post.jpg", caption="Caption of the post here")

bot.upload_video("your_video.mp4", caption="caption of the video")
