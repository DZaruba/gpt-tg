import openai
import json
from base64 import b64decode
import key

#пишем нужный нам запрос
prompt = 'Последнее лето на моей земле'
openai.api_key = key.api_gpt
openai.api_base = "https://api.proxyapi.ru/openai/v1"

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='1024x1024',
    response_format='b64_json'
)

with open('data.json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)

image_data = b64decode(response['data'][0]['b64_json'])
file_name = '_'.join(prompt.split(" "))

with open(f"./images/{file_name}.png", 'wb') as file:
    file.write(image_data)