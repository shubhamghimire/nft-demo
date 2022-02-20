from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_gtype
from metadata.sample_metadata import metadata_template
from pathlib import Path


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
            # image_uri = upload_to_ipfs()
            # collectible_metadata["image"] = image_uri


def upload_to_ipfs():
    pass
