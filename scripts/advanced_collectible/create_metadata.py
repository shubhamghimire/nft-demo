from brownie import AdvancedCollectible
from scripts.helpful_scripts import get_gtype


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_advanced_collectibles} collectibles! ")
    for token_id in range(number_of_advanced_collectibles):
        gtype = get_gtype(advanced_collectible.tokenIdToGodType(token_id))
