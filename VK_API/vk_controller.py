from VK_API.vk_requests import VKRequests
import json

with open('config\\vk_config.json', 'r', encoding='utf-8') as jvk:
    vk_cfg = json.load(jvk)

vk_api = VKRequests(vk_cfg)


def take_new_post(domain):
    # http = requests.get(url=f'https://api.vk.com/method/wall.get?domain={domain}&access_token={vk_cfg["token"]}&v=5.131')
    # print(http)
    # get_json = http.json()
    vk_api.create_require('MDK', 'wall.get', {'domain': domain})
    get_json = vk_api.send_request('MDK')
    id_group: str = get_json['response']['items'][0]['from_id']
    id_post: str = get_json['response']['items'][1]['id']
    return f'http://vk.com/wall{id_group}_{id_post}'

    """
    vk_api.get_request(method, params)
    # id_group = vk_api.pull_from_response('id_group')
    # id_post = vk_api.pull_from_response('id_post', 1)
    return f'http://vk.com/wall{id_group}_{id_post}'
    
    """


