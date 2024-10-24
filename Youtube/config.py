import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7843842374:AAFa7lA_iFJukJCqOsVSxKTKCRIgKtedOkI")
    API_ID = int(os.environ.get("API_ID", "25933717" ))
    API_HASH = os.environ.get("API_HASH", "1a7c143efae3a4e2c988c4a0eb8e8d00")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "@frhanzv")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
