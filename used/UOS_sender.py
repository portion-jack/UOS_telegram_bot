import telegram as tel
from UOS_Handler import *
from datetime import date

# telegram_bot and id setting
bot = tel.Bot(token="5781653416:AAHY5lYxGeYk6jYItuZvZm3DH5TXTdIkO80")
chat_id = 5056533977

# bot.sendMessage(chat_id=chat_id, text='Test Message')

# uos 공지 가져오기 #
# 일반공지
general_notice = "https://www.uos.ac.kr/korNotice/list.do?list_id=FA1"
notice_1 = get_general_notice(general_notice)

# 학사공지
academic_notice = "https://www.uos.ac.kr/korNotice/list.do?list_id=FA2"
notice_2 = get_academic_notice(academic_notice)

# 장학공지
schoolarship_notice = "https://scholarship.uos.ac.kr/scholarship/notice/notice/list.do?brdBbsseq=1"
notice_3 = get_scholarship_notice(schoolarship_notice)

notice_1.insert(0, ",---일반 공지사항---")
notice_2.insert(0, ",---학사 공지사항---")
notice_3.insert(0, ",---장학 공지사항---")

notice = notice_1 + notice_2 + notice_3
notice.insert(0, "🔥{}의 공지!🔥".format(date.today()))
notice = str(notice).replace(',', '\n').replace("'", "")



bot.sendMessage(chat_id=chat_id,
                text=notice[1:-1])
