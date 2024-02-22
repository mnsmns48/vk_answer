import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType

from config import hidden_vars

vk_session = vk_api.VkApi(token=hidden_vars.vk_api_token)
session_api = vk_session.get_api()

long_poll = VkLongPoll(vk_session)

text = 'мы больше не отвечаем в этой группе ВКонтакте.\n' \
       'Любые вопросы пишите в Telegram:\n\n' \
       '🎲 Наличие и цены смотрите здесь: https://t.me/CifrotechBot' \
       '👨‍💻 Связь с администратором: https://t.me/tser88\n' \
       '🛠 По стоимости ремонта пишите сюда: https://t.me/tser88\n'


def get_username(id):
    vk = vk_session.get_api()
    user_get = vk.users.get(user_ids=(id))
    user_get = user_get[0]
    first_name = user_get['first_name']
    last_name = user_get['last_name']
    full_name = first_name + " " + last_name
    return full_name


for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            user_id = event.user_id
            vk_session.method('messages.send',
                              {
                                  'user_id': user_id,
                                  'message': f"Здравствуйте, {get_username(user_id)}, {text}",
                                  'random_id': 0
                              }
                              )