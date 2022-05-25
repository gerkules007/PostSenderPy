import requests


class VKRequests:
    _http = None
    _base_api = None
    _version_token = None
    _list_request = {}

    def __init__(self, cfg):
        self._base_api = f'{cfg["base_api"]["protocol"]}://' \
                         f'{cfg["base_api"]["domain"]}/' \
                         f'{cfg["base_api"]["path_to_methods"]}'
        self._version_token = f'access_token={cfg["token"]}&v={cfg["version"]}'

    def print(self):
        print(self._base_api)
        print(self._version_token)

    def send_request(self, name_source):
        # http = requests.get(url=f'https://api.vk.com/method/wall.get?domain={domain}&access_token={api_token}&v=5.131')
        _http = requests.get(url=self._list_request[name_source])
        return _http.json()

    def create_require(self, name, method, params: dict):
        # wall.get, { domain : mudakoff }
        url = f'{self._base_api}/{method}?'
        for k, v in params.items():
            url += f'{k}={v}&'
        url += self._version_token
        self._list_request[name] = url


