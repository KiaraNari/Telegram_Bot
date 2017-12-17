import requests
import misc
import fitness
from time import sleep

token = misc.token
# https://api.telegram.org/bot451338390:AAGyj9QXce1gjyG0CAdHXfOXu6GATVLQOSU/sendmessage?chat_id=380938453&text=Hi
URL = 'https://api.telegram.org/bot' + token + '/' # Формируем строку URL
global last_update_id
last_update_id = 0



def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
    # Отвечать только на новые сообщения
    # Получаем update_id каждого обновления, записываем в переменную и сравнивать с последним

    data = get_updates()

    last_obj = data['result'][-1]
    current_update_id = last_obj['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        chat_id = last_obj['message']['chat']['id'] # Считываем chat_id. Обращаемся к списку result, потом к последнему эмеленту, далее к словарю message, потом к словарю chat и забираем id
        message_text = last_obj['message']['text'] # ...обращаемся к словарю message и забираем текст
        message = {'chat_id': chat_id,
                   'text': message_text}
        last_update_id = current_update_id
        return message
    return None

def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    # d = get_updates() # Получаем обновления

    # with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)




    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            tmp = fitness.get_exer(text)
            send_message(chat_id, tmp)
        else:
            continue
        sleep(2)


if __name__ == '__main__':
    main()