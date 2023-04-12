import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'LazyPrincess')
API_ID = int(environ.get('API_ID', '26461352'))
API_HASH = environ.get('API_HASH', 'ab9cc32776ada8335852b50cd96bb8c6')
BOT_TOKEN = environ.get('BOT_TOKEN', "6063181531:AAFWgp_MANYK-TerMDP72aKRsDBypQu8uCg")

#Port
PORT = environ.get("PORT", "8080")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/2992a480cae2bc0de1c39.jpg https://telegra.ph/file/76e7b5e94430b84a3d2b2.jpg https://telegra.ph/file/3544a8773740b0412c9dd.jpg https://telegra.ph/file/4b1c7004ea8bd3fed8df9.jpg https://telegra.ph/file/a02e47d932adc336740fa.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5554564210 6284344479 5069888600 5675198274').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001637710147').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001780415947')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Jeetubot:jeetubot@cluster0.rtmwhtb.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_Files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001433302422'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Apnamovie4')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>Title:</b> <code>{file_caption}</code> <a herf=https://t.me/Moviesadda24_7s>♥️ Movies Adda ♥️</a> \n\n⚙️ <b>Size: </b><i>{file_size}</i>\n\n👉 <b>Join Now : <a herf=https://t.me/Moviesadda24_7s>♥️ Movies Adda ♥️</a></b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "<b>Title:</b> <code>{file_caption}</code> <a herf=https://t.me/Moviesadda24_7s>♥️ Movies Adda ♥️</a> \n\n⚙️ <b>Size: </b><i>{file_size}</i>\n\n👉 <b>Join Now : <a herf=https://t.me/Moviesadda24_7s>♥️ Movies Adda ♥️</a></b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌IMDb: \n\n🏷 Title: {title}\n🌟 Rating : {rating}/10\n🎭 Genres: {genres}\n📆 Year: {year}\n⏰ Duration : {runtime}\n🎙️ Languages : {languages}\n🔖 Plot : {plot}\n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

# _______________________________________________________________________________________________________________ #
# __________________________________________Credit_______________________________________________________________ #
# _______________________________________LazyDeveloper___________________________________________________________ #
# _____________________________A real Developer always gives Credits_____________________________________________ #
# _______________________________________________________________________________________________________________ #

#LazyRenamer Configs
FLOOD = int(environ.get("FLOOD", "50"))
# FLOOD is for renaming files -> set value in [seconds] in this field ! ex : for 30 seconds use 30 --\\ for 1 minute use 60 -------- ! 
LAZY_MODE = bool(environ.get("LAZY_MODE", "False"))
#Add user id of the user in this field those who you want to be Authentic user for file renaming features --------- !
lazy_renamers = [int(lazrenamers) if id_pattern.search(lazrenamers) else lazrenamers for lazrenamers in environ.get('LAZY_RENAMERS', '').split()]
LAZY_RENAMERS = (lazy_renamers + ADMINS) if lazy_renamers else []
# Only Give Value in LAZY_RENAMERS if you have enabled LAZY_MODE ----- !
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', '-1001819161200'))
#   REQ_CHANNEL is for the logs of that content name which is not found in group -- !
URL_MODE = is_enabled((environ.get("URL_MODE", "False")), True)
# Use True false in url mode => Set value true if you want shortlinks - else - use value False ----- !

# URL Shortener
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'shorturllink.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', 'f99384c914477525509f4a85612096610a0')

# Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

# Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 Join Backup Channel 📥"
DOWNLOAD_TEXT_URL = "https://Latest_Movies_FreeOnNet"

# Custom Caption Under Button #
CAPTION_BUTTON = "Get Updates"
CAPTION_BUTTON_URL = "https://t.me/Moviesadda24_7s"

# _______________________________________________________________________________________________________________ #
# __________________________________________Credit_______________________________________________________________ #
# _______________________________________LazyDeveloper___________________________________________________________ #
# _____________________________A real Developer always gives Credits_____________________________________________ #

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
