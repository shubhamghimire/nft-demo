from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_gtype
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os

gtype_to_image_uri = {
    "SHIVA": "https://ipfs.io/ipfs/QmRwBXmXSyP1j7TP2t6LFn5511wxH7Qn5oGFFw4QrqXepk?filename=shiva.png",
    "GANESH": "https://ipfs.io/ipfs/QmYSgvBUJQg9AyMzqDvFfC6fJ391aiByCDqPF9amt69A7G?filename=ganesh.png",
    "HANUMAN": "https://ipfs.io/ipfs/Qmcwqf5pDoYcpN7CNUbyCbKXVTW9wQopP8wirfn5SD2FGK?filename=hanuman.png",
}


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_advanced_collectibles} collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        gtype = get_gtype(advanced_collectible.tokenIdToGodType(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{gtype}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = gtype
            collectible_metadata["description"] = f"A mighty {gtype} god!"
            image_path = "./img/" + gtype.lower().replace("_", "-") + ".png"

            image_uri = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_uri = upload_to_ipfs(image_path)
            image_uri = image_uri if image_uri else gtype_to_image_uri[gtype]

            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        # "./img/0-SHIVA.png" -> "0-SHIVA.png"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
