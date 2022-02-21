# nft-demo
1. Uploading an Image to IPFS.
2. Creating the IPFS URL to create NFT.
3. Uploading the NFT to OpenSea.

# setup
- Run the following script to deploy the Advanced collectible contract.
    ```
    brownie run scripts/advanced_collectible/deploy_and_create.py --network kovan
    ```

- Now create collectible. If you have three collectibles, run the script three times.
    ```
    brownie run scripts/advanced_collectible/create_colletible.py --network kovan
    ```

- Now create metadata by running the follwing scripts. To create metadata plese run IPFS node by using 'ipfs daemon' command and then upload the image files and create metadata json files. Also upload the metadata json files.
    ```
    brownie run scripts/advanced_collectible/create_metadata.py --network kovan  
    ```

- Now run the settoken uri script and see the NFTS at created OpenSea URLS.
    ```
    brownie run scripts/advanced_collectible/set_tokenuri.py --network kovan
    ```

Note: Sometimes there is a problem with a certain network so if things are not working with kovan the try once with rinkeby to check.