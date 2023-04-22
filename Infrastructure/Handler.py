import logging
import time

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters

from .TextWriter import TextWriter

class Handler:
    def __init__(self):
        with open("APIToken.txt", "r") as f:
            self.token = f.readline().strip()
        self.TextWriter = TextWriter()
        self.updater = Updater(self.token)
        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_handler(CommandHandler("on", self.On))
        self.dispatcher.add_handler(CommandHandler("off", self.Off))

    def Off(self, update: Update, context: CallbackContext):
        self.TextWriter.Write("off")
        update.message.reply_text("off")

    def On(self, update: Update, context: CallbackContext):
        self.TextWriter.Write("on")
        update.message.reply_text("on")

    def Run(self):
        self.updater.start_polling()

