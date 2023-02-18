import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
import openpyxl
import os
from datetime import datetime

# Define conversation states
EMOTION, TRIGGER, NOTES = range(3)

# Define command handlers
def start(update, context):
    update.message.reply_text('Welcome to the diary card! To start, please enter your emotion.')
    return EMOTION

def cancel(update, context):
    update.message.reply_text('Diary card canceled.')
    return ConversationHandler.END

# Define message handlers
def emotion(update, context):
    user_id = update.effective_user.id
    context.user_data['user_id'] = user_id
    context.user_data['emotion'] = update.message.text
    update.message.reply_text('What triggered your emotion?')
    return TRIGGER

def trigger(update, context):
    context.user_data['trigger'] = update.message.text
    update.message.reply_text('Do you have any notes you want to add?')
    return NOTES

def notes(update, context):
    context.user_data['notes'] = update.message.text
    context.user_data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Write diary card data to Excel file
    filename = f'user_{context.user_data["user_id"]}.xlsx'
    if os.path.isfile(filename):
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
    else:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(['Emotion', 'Trigger', 'Notes', 'Timestamp'])
    row_data = [context.user_data['emotion'], context.user_data['trigger'], context.user_data['notes'], context.user_data['timestamp']]
    sheet.append(row_data)
    workbook.save(filename)
    update.message.reply_text('Diary card saved!')
    keyboard = [[InlineKeyboardButton("Add emotion", callback_data='add_emotion')],[InlineKeyboardButton("Download", callback_data='download')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('What would you like to do next?', reply_markup=reply_markup)
    return ConversationHandler.END

def add_emotion_callback(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Please enter your emotion.')
    return EMOTION

def download(update, context):
    user_id = update.effective_user.id
    filename = f'user_{user_id}.xlsx'
    if os.path.isfile(filename):
        update.message.reply_document(open(filename, 'rb'))
    else:
        update.message.reply_text('You have not saved any diary card data yet.')
    return ConversationHandler.END

# Define main function
def main():
    # Set up logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up bot
    token = 'TOKEN'
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Define conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            EMOTION: [MessageHandler(Filters.text & ~Filters.command, emotion)],
            TRIGGER: [MessageHandler(Filters.text & ~Filters.command, trigger)],
            NOTES: [MessageHandler(Filters.text & ~Filters.command, notes)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dp.add_handler(conv_handler)

    # Define command handlers
    dp.add_handler(CommandHandler('download', download))

    # Define callback handlers
    dp.add_handler(CallbackQueryHandler(add_emotion_callback, pattern='add_emotion'))

    # Start the bot
    updater.start_polling()
    logger.info('Bot started')
    updater.idle()

if __name__ == '__main__':
    main()
