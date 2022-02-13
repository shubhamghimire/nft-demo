from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import AdvancedCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"

print(get_account())


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy({"from": account})


def main():
    deploy_and_create()
