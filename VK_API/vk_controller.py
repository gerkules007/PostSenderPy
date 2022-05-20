import requests
import token_config


api_token = token_config.vk


def take_new_post(domain):
    http = requests.get(url=f'https://api.vk.com/method/wall.get?domain={domain}&access_token={api_token}&v=5.131')
    print(http)
    get_json = http.json()
    id_group: str = get_json['response']['items'][0]['from_id']
    id_post: str = get_json['response']['items'][1]['id']
    return f'http://vk.com/wall{id_group}_{id_post}'


