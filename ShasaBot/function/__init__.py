from telethon.tl import functions
from telethon.tl import types
from ShasaBot import tbot
import ShasaBot.modules.sql.elevated_sql as sql
from ShasaBot.modules.sql.chats_sql import add_chat, rmchat, is_chat, get_all_chat_id
from ShasaBot.modules.sql.setbio_sql import set_bio, rm_bio, check_bio_status, is_bio, get_all_bio_id


async def is_admin(event, user):
    try:
        sed = await event.client.get_permissions(event.chat_id, user)
        is_mod = bool(sed.is_admin)
    except:
        is_mod = False
    return is_mod

async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True

async def can_approve_users(message):
    result = await tbot(
        functions.channels.GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (
        isinstance(p, types.ChannelParticipantAdmin) and p.admin_rights.add_admins
    )

async def can_change_info(message):
    result = await tbot(
        functions.channels.GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (
        isinstance(p, types.ChannelParticipantAdmin) and p.admin_rights.change_info
    )


def sudo(iid):
    k = iid
    return bool(sql.is_sudo(k))

def bio(iid):
    k = iid
    return bool(is_bio(k))
