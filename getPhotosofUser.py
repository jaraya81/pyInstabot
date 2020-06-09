
import argparse
import os
import sys
from instabot import Bot  # noqa: E402

sys.path.append(os.path.join(sys.path[0], "../"))

#parser = argparse.ArgumentParser(add_help=True)
#parser.add_argument("username", type=str, help="@username")
#args = parser.parse_args()

#if args.username[0] != "@":  # if first character isn't "@"
#    args.username = "@" + args.username
username="@photostockin"
bot = Bot()
bot.login()
medias = bot.get_total_user_medias(username)
bot.download_photos(medias)
