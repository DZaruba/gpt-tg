import openai
import requests
import schedule
import time
import key

openai.api_key = key.api_gpt
openai.api_base = "https://api.proxyapi.ru/openai/v1"
#openai.default_headers = {"x-foo": "true"}


chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {
            "role": "user", 
            #"content": "write a clever wolf quote"
            "content": "Напиши волчью цитату о жизни по-русски"
        }
    ]
)

text_mess = chat_completion.choices[0].message.content[1:-1]
print(text_mess)

tg_token = key.tg_token
id_chat = key.tg_chat

req = requests.get(f'https://api.telegram.org/bot{tg_token}/sendMessage?chat_id={id_chat}&text={text_mess}')