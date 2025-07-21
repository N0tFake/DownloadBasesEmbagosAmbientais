import ssl
import certifi
import mimetypes
from urllib.request import urlretrieve, urlopen
from pathlib import Path


#! WARNING
ssl._create_default_https_context = ssl._create_unverified_context
""""
Se estiver usando um ambiente Python gerenciado (como Conda ou virtualenv), atualize os certificados com:
>>  pip install --upgrade certifi

USE:

context = ssl.create_default_context(cafile=certifi.where())
with urlopen(url, context=context) as response:
    content_type = response.headers.get("Content-Type")
    print(f"Content-Type: {content_type}")
"""

# TODO Obter os links de download dos arquivos
file_name = "teste.zip"


# def get_mine_type(file_name):
#     mimetype = mimetypes.guess_extension(file_name)
#     return mimetype


# with urlopen(url) as response:
#     content_type = response.headers.get("Content-Type")
#     print(f"Content-Type: {content_type}")

# path, headers = urlretrieve(url, file_name)

# print(f"Type file: {get_mine_type(file_name)}")

# for name, value in headers.items():
#   print(f"{name}: {value}")
  
class Downloader:
    def download(self, url, file_name, file_path):
        output = Path(file_path).joinpath(file_name)
        try:
            # print(f"Downloading {file_name} from {url}...")
            path, header = urlretrieve(url, output)
            return {
                'success': True,
                'path': path, 
                'header': header
            }
        except Exception as e:
            # print(f"Error downloading {file_name}: {e}")
            return {
                'success': False,
                'error': str(e)
            }