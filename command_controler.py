from telegram.ext import Updater
from telegram.ext import CommandHandler
from mybot_detail import *

updater = Updater(token=mybot_token(),
                  use_context=True)
dispatcher = updater.dispatcher

from UOS_notice import *

general_notice = get_general_notice()
academic_notice = get_academic_notice()
scholarship_notice = get_scholarship_notice()

total_notice = general_notice + academic_notice + scholarship_notice

general_notice = format_notice(general_notice)
academic_notice = format_notice(academic_notice)
scholarship_notice = format_notice(scholarship_notice)

total_notice = format_notice(total_notice)

from UOS_food import *

food = uos_food()


# bot_response by command

# 1. base
# 1.2 checker
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="안녕하세요! 시립대 봇입니다!")
    return None


# 1.1. helper
def bot_helper(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="/hi -> 안녕하세요\n"
                                  "\n/notice_total -> 일반, 학사, 장학공지\n"
                                  "      /notice_general      -> 일반 공지\n"
                                  "      /notice_academic     -> 학사 공지\n"
                                  "      /notice_scholarship  -> 장학 공지\n"
                                  "\n/food -> 학식\n"
                                  "\n/lib -> 도서관 홈페이지\n"
                                  "\n/map ->학교지도")
    return None


# 2. UOS
# 2.1 notice
def uos_notice_total(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=total_notice[1:-1])
    return None


def uos_notice_general(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=general_notice[1:-1])
    return None


def uos_notice_academic(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=academic_notice[1:-1])
    return None


def uos_notice_scholarship(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=scholarship_notice[1:-1])
    return None


# 2.2 map
def uos_map(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open("dir_img/uos_map.jpeg", 'rb'))


# 2.3 food
def uos_food(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=food)


# 2.3 links

def uos_library(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='https://library.uos.ac.kr/')
    return None


hello_handler = CommandHandler('hi', hello)
helper_handler = CommandHandler('help', bot_helper)

notice_total_handler = CommandHandler('notice_total', uos_notice_total)
notice_general_handler = CommandHandler('notice_general', uos_notice_general)
notice_academic_handler = CommandHandler('notice_academic', uos_notice_academic)
notice_scholarship_handler = CommandHandler('notice_scholarship', uos_notice_scholarship)

food_handler = CommandHandler('food', uos_food)

library_handler = CommandHandler("lib", uos_library)
map_handler = CommandHandler('map', uos_map)

dispatcher.add_handler(hello_handler)
dispatcher.add_handler(helper_handler)

dispatcher.add_handler(notice_total_handler)
dispatcher.add_handler(notice_general_handler)
dispatcher.add_handler(notice_academic_handler)
dispatcher.add_handler(notice_scholarship_handler)

dispatcher.add_handler(food_handler)

dispatcher.add_handler(library_handler)

dispatcher.add_handler(map_handler)

# bot_response by command

updater.start_polling()
