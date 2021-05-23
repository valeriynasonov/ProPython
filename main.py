from data_photos.send_photos_data import send_albums_id
from data_photos.send_photos_data import send_photos_data
from bot_VK.bot import write_msg
from data_users.send_data_users import send_data_bdate
from data_users.send_data_users import send_data_yourself
from data_users.send_data_users import send_data_users
from data_users.send_data_users import send_users_city
from data_users.send_data_users import send_users_relation
from data_users.send_data_users import send_personal_value
from database.former_database import former_database

token = input("Введите токен")
yours_id = input("Введите ваш id")
from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = input('Token: ')

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")

if __name__ == "__main__":
    send_data_yourself(token, yours_id)
    send_data_users(token, yours_id)
    send_data_bdate(token, yours_id)
    send_users_city(token, yours_id)
    send_users_relation(token, yours_id)
    send_personal_value(token, yours_id)
    send_albums_id(token, yours_id)
    send_photos_data(token, yours_id)
    former_database(token, yours_id)





