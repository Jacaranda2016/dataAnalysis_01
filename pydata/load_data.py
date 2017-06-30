# coding:utf-8
import json
import pprint
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, UnicodeText
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

reload(sys)
sys.setdefaultencoding('utf-8')

user = 'root'
password = ''
host = 'localhost'
database = 'test'
charset = 'utf8'
engine_url = 'mysql+pymysql://{}:{}@{}/{}?charset={}'.format(
    user, password, host, database, charset)
# base class
Base = declarative_base()
engine = create_engine(engine_url)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
'''
#selfdefined class named PaymentLog,extended from Base
class PaymentLog(Base):
	__tablename__ = 'PaymentLog'
	id = Column(Integer, primary_key=True)
	productId = Column(String(255))
	productName = Column(String(255))
	userId = Column(String(255))

if __name__ == '__main__':
	payment_logs = session.query(PaymentLog).all()
	for payment_log in payment_logs:
		user_id = payment_log.userId
		product_name = payment_log.productName
		print('{} buys {}'.format(user_id, product_name))
'''


class GameUser:
    user_id = ''
    action1_count = 0
    action2_count = 0
    action3_count = 0
    action4_count = 0
    action5_count = 0
    action6_count = 0
    action7_count = 0
    action8_count = 0
    target_label = 0

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "{},{},{},{},{},{},{},{},{},{}".format(self.user_id, self.action1_count, self.action2_count,
                                                      self.action3_count, self.action4_count, self.action5_count,
                                                      self.action6_count,
                                                      self.action7_count, self.action8_count, self.target_label)
        # user id %s action 1 count %d" % (self.user_id,self.action1_count)


class ActionLog(Base):
    __tablename__ = "ActionLog"
    id = Column(Integer, primary_key=True)
    action = Column(String(255))
    userId = Column(String(255))


# target_label=Column(Integer())

if __name__ == '__main__':
    action_logs = session.query(ActionLog).all()
    user_dict = {}
    for action_log in action_logs:
        user_id = action_log.userId
        game_user = GameUser(user_id)
        try:
            game_user = user_dict[user_id]
        except KeyError:
            user_dict[user_id] = game_user

        if action_log.action == '领取了7日登陆礼包':
            game_user.action1_count += 1
        elif action_log.action == '领取了等级礼包':
            game_user.action2_count += 1
        elif action_log.action == '领取了在线奖励':
            game_user.action3_count += 1
        elif action_log.action == '领取了每日充值活动奖励':
            game_user.action4_count += 1
        elif action_log.action == '进行了金币大满贯抽取':
            game_user.action5_count += 1
        elif action_log.action == '进行积分抽卡':
            game_user.action6_count += 1
        elif action_log.action == '等级限时特卖购买道具':
            game_user.action7_count += 1
        elif action_log.action == '领取了充值返利活动奖励':
            game_user.action8_count += 1


class PaymentLog(Base):
    __tablename__ = "PaymentLog"
    id = Column(Integer, primary_key=True)
    userId = Column(String(255))


if __name__ == '__main__':
    payment_logs = session.query(PaymentLog).all()
    for payment_log in payment_logs:
        if payment_log.userId in user_dict.keys():
            user_dict[payment_log.userId].target_label = 1



user_dict_paid = []
user_dict_unpaid = []
i = 0
j = 0
for user_id in user_dict:
    if user_dict[user_id].target_label == 1:
        user_dict_paid.append({})
        user_dict_paid[i]["userid"] = user_id
        user_dict_paid[i]["features:"] = {}
        user_dict_paid[i]["target_label:"] = 1
        user_dict_paid[i]["features:"]["领取了7日登陆礼包"] = user_dict[user_id].action1_count
        user_dict_paid[i]["features:"]["领取了等级礼包"] = user_dict[user_id].action2_count
        user_dict_paid[i]["features:"]["领取了在线奖励"] = user_dict[user_id].action3_count
        user_dict_paid[i]["features:"]["领取了每日充值活动奖励"] = user_dict[user_id].action4_count
        user_dict_paid[i]["features:"]["进行了金币大满贯抽取"] = user_dict[user_id].action5_count
        user_dict_paid[i]["features:"]["进行积分抽卡"] = user_dict[user_id].action6_count
        user_dict_paid[i]["features:"]["等级限时特卖购买道具"] = user_dict[user_id].action7_count
        user_dict_paid[i]["features:"]["领取了充值返利活动奖励"] = user_dict[user_id].action8_count
        i+=1
    else:
        user_dict_unpaid.append({})
        user_dict_unpaid[j]["userid"] = user_id
        user_dict_unpaid[j]["features:"] = {}
        user_dict_unpaid[j]["target_label:"] = 0
        user_dict_unpaid[j]["features:"]["领取了7日登陆礼包"] = user_dict[user_id].action1_count
        user_dict_unpaid[j]["features:"]["领取了等级礼包"] = user_dict[user_id].action2_count
        user_dict_unpaid[j]["features:"]["领取了在线奖励"] = user_dict[user_id].action3_count
        user_dict_unpaid[j]["features:"]["领取了每日充值活动奖励"] = user_dict[user_id].action4_count
        user_dict_unpaid[j]["features:"]["进行了金币大满贯抽取"] = user_dict[user_id].action5_count
        user_dict_unpaid[j]["features:"]["进行积分抽卡"] = user_dict[user_id].action6_count
        user_dict_unpaid[j]["features:"]["等级限时特卖购买道具"] = user_dict[user_id].action7_count
        user_dict_unpaid[j]["features:"]["领取了充值返利活动奖励"] = user_dict[user_id].action8_count
        j=j+1



with open('action_paid.json', 'w') as f:
    json.dump(user_dict_paid, f, ensure_ascii=False, indent=2)

with open('action_unpaid.json', 'w') as f:
    json.dump(user_dict_unpaid, f, ensure_ascii=False, indent=2)


