from ShasaBot.mongo import client as db_x

lydia = db_x["CHATBOT"]
talkmode = db_x["TALKMODE"]


def add_chat(chat_id):
    if stark := lydia.find_one({"chat_id": chat_id}):
        return False
    lydia.insert_one({"chat_id": chat_id})
    return True


def remove_chat(chat_id):
    if stark := lydia.find_one({"chat_id": chat_id}):
        lydia.delete_one({"chat_id": chat_id})
        return True
    else:
        return False


def get_session(chat_id):
    star = talkmode.find_one({"chat_id": chat_id})
    return False if not star else star