from superhero import Super_hero
from pprint import pprint
import requests


thanos = Super_hero()
thanos.name = 'Thanos'
iron_man = Super_hero()
iron_man.name = 'Iron Man'
hulk = Super_hero()
hulk.name = 'Hulk'
cap = Super_hero()
cap.name = 'Captain America'

# pprint(thanos.find_the_hero())
# pprint(hulk.find_the_hero())
# pprint(cap.find_the_hero())

# pprint(thanos.find_intelligence())
# pprint(hulk.find_intelligence())
# pprint(cap.find_intelligence())
# pprint(iron_man.find_intelligence())

# print(cap.find_the_most_intelligent(hulk, thanos))


class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path):
        href = self._get_upload_link(disk_file_path=file_path).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    file_path = ""
    uploader = YaUploader(token="")
    uploader.upload(file_path)