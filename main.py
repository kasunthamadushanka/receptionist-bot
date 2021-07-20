from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''𝓗𝓮𝔂, \n\n 𝓘 𝓪𝓶 𝐺𝑅𝑂𝑈𝑃 𝑅𝐸𝐶𝐸𝑃𝑇𝐼𝑂𝑁𝐼𝑆𝑇 𝐵𝑂𝑇. 𝓐𝓭𝓭 𝓶𝓮 𝓽𝓸 𝔂𝓸𝓾𝓻 𝓰𝓻𝓸𝓾𝓹 𝓪𝓷𝓭 𝓶𝓪𝓴𝓮 𝓶𝓮 𝓪𝓼 𝓐𝓭𝓶𝓲𝓷.\n\n👲Powered By : @epusthakalaya_bots''')

def help(updater,context):
 updater.message.reply_text("➠ 𝙰𝚍𝚍  𝙼𝚎  𝚃𝚘  𝙶𝚛𝚘𝚞𝚙\n\n➠ 𝙼𝚊𝚔𝚎  𝙰𝚍𝚖𝚒𝚗  𝙼𝚎\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍  𝙱𝚢 : @BX_Botz")\
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hey {member.user_name} , Welcome to ln Support\n\n💖Thank💖You💖For💖Joining💖')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
