from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''Sorry. This Bot Only Works With 2021 A/L සෙට් එක 🏆. \n\n⚜️Join For Bot Updates⚜️ : @epusthakalaya_bots''')

def help(updater,context):
 updater.message.reply_text("➠ Join This group. \n\n➠ https://t.me/group2021AL\n\n⚜️Powered By⚜️ : @epusthakalaya_bots")\
 

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
