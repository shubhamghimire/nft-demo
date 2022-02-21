from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import get_account, get_gtype, OPENSEA_URL

# File uploaded to IPFS and took the
god_metadata_dic = {
    "SHIVA": "https://ipfs.io/ipfs/QmULNZ8umdtXYAUB5y9UpaLXBNmN7SCgcpnMbEdx5eSEyi?filename=0-SHIVA.json",
    "GANESH": "https://ipfs.io/ipfs/QmXx7UhfFnSrFmGhDsPurdLQEC1Dv4yZPkYfx4E5aAmh68?filename=1-GANESH.json",
    "HANUMAN": "https://ipfs.io/ipfs/Qmf4TKekSuWnJ1reqWqju5KakLa4QA546VzP5cWdSXFVNp?filename=2-HANUMAN.json",
}


def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectibles} tokenIds")
    for token_id in range(number_of_collectibles):
        gtype = get_gtype(advanced_collectible.tokenIdToGodType(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, advanced_collectible, god_metadata_dic[gtype])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    print(
        f"You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
