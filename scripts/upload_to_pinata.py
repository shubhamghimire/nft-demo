import os
from pathlib import Path
import requests

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
# Change this filepath
filepath = ["./img/shiva.png", "./img/ganesh.png", "./img/hanuman.png"]

headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def main():
    for fpath in filepath:
        filename = fpath.split("/")[-1:][0]
        with Path(fpath).open("rb") as fp:
            image_binary = fp.read()
            response = requests.post(
                PINATA_BASE_URL + endpoint,
                files={"file": (filename, image_binary)},
                headers=headers,
            )
            print(response.json())


# Results of running the script
# {'IpfsHash': 'QmRwBXmXSyP1j7TP2t6LFn5511wxH7Qn5oGFFw4QrqXepk', 'PinSize': 486607, 'Timestamp': '2022-02-20T08:22:47.153Z', 'isDuplicate': True}
# {'IpfsHash': 'QmYSgvBUJQg9AyMzqDvFfC6fJ391aiByCDqPF9amt69A7G', 'PinSize': 195001, 'Timestamp': '2022-02-21T10:32:54.264Z'}
# {'IpfsHash': 'Qmcwqf5pDoYcpN7CNUbyCbKXVTW9wQopP8wirfn5SD2FGK', 'PinSize': 1232530, 'Timestamp': '2022-02-21T10:33:05.706Z'}


if __name__ == "__main__":
    main()
