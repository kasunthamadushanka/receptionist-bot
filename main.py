from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''𝓗𝓮𝔂, \n\n 𝓘 𝓪𝓶 𝐺𝑅𝑂𝑈𝑃 𝑅𝐸𝐶𝐸𝑃𝑇𝐼𝑂𝑁𝐼𝑆𝑇 𝐵𝑂𝑇. 𝓐𝓭𝓭 𝓶𝓮 𝓽𝓸 𝔂𝓸𝓾𝓻 𝓰𝓻𝓸𝓾𝓹 𝓪𝓷𝓭 𝓶𝓪𝓴𝓮 𝓶𝓮 𝓪𝓼 𝓐𝓭𝓶𝓲𝓷.\n𝓗𝓲𝓽 /help  𝓯𝓸𝓻 𝓶𝓸𝓻 𝓲𝓷𝓯𝓸 𝓪𝓫𝓸𝓾𝓽 𝓶𝓮.\n\n⚜️Powered By⚜️ : @epusthakalaya_bots''')

def help(updater,context):
 updater.message.reply_text("➠ 𝙰𝚍𝚍  𝙼𝚎  𝚃𝚘  𝙶𝚛𝚘𝚞𝚙\n\n➠ 𝙼𝚊𝚔𝚎  𝙰𝚍𝚖𝚒𝚗  𝙼𝚎\n\n⚜️Powered By⚜️ : @epusthakalaya_bots")\
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'ආයුබෝවන් 🙏  {member.full_name} , 2021 A/L සෙට් එක 🏆 සමූහයට ඔබව සාදරයෙන් පිලිගන්නවා🤘🏽😍🤗😊.\nලංකාව පුරා විසිරී සිටින Maths,Bio,Tech,Commerce,Art 2021 A/L ලියන ඔයාගෙම සහෝදර සහෝදරියන් මේ සමූහයේ ඉන්නේ...❤️\nසමූහයේ ප්‍රශ්නයක් ආවොත් admin කෙනකුට අනිවාර්යයෙන්ම කියන්න.😎\n\n Bot By:- @epusthakalaya_bots')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
