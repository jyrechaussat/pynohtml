import os
import sys
import json
import requests



def get_last_version(lib_name):
    url = f"https://api.cdnjs.com/libraries/{lib_name}?fields=version"
    print(f"Getting last version {url}")
    req = requests.get(url)
    if req.status_code == 200:
        return json.loads(req.text).get("version")
    else:
        raise Exception(f"request returned {req.status_code}")

def get_list_of_files(lib_name, last_version):
    url = f"https://api.cdnjs.com/libraries/{lib_name}/{last_version}"
    print(f"Getting list of files to download {url}")
    req = requests.get(url)
    if req.status_code == 200:
        return json.loads(req.text).get("rawFiles")
    else:
        raise Exception(f"request returned {req.status_code}")

def download_files(lib_name, last_version, files, output_dir="/tmp"):
    # url = "https://cdnjs.cloudflare.com/ajax/libs/uikit/3.6.16/js/uikit.min.js"
    for filename in files:
        url = f"https://cdnjs.cloudflare.com/ajax/libs/{lib_name}/{last_version}/{filename}"
        print(f"Downloading {url}")
        req = requests.get(url)
        if req.status_code == 200:
            path = os.path.join(output_dir, filename)
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            with open(path, "w") as out_file:
                print(f"Writing libs to {path}")
                out_file.write(req.text)
        else:
            raise Exception(f"request returned {req.status_code}")

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print('You have specified too many arguments')
        sys.exit()

    if len(sys.argv) < 3:
        print('You need to specify the path to be listed')
        sys.exit()
    lib_name = sys.argv[1]
    out_dir = sys.argv[2]

    last_version = get_last_version(lib_name)
    files = get_list_of_files(lib_name, last_version)
    download_files(lib_name, last_version, files, out_dir)
