from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_gtype
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests


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
            print(image_path)
            image_uri = upload_to_ipfs(image_path)
            # collectible_metadata["image"] = image_uri


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        print(response.json())
        ipfs_hash = response.json()["Hash"]
        # "./img/0-SHIVA.png" -> "0-SHIVA.png"
        filename = filepath.split("/")[-1:][0]
        print(filename)
        print("filename printed")
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
