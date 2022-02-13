// An NFT contract
// Where the tokenURI is one of different gods
// Randomly Selected

// SPDX-License-Identifier: MIT

pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectibel is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    enum GodType {
        SHIVA,
        GANESH,
        HANUMAN
    }
    mapping(uint256 => GodType) public tokenIdToGodType;
    mapping(bytes32 => address) public requestIdToSender;
    event requestCollectible(bytes32 indexed requestId, address requester);
    event godAssigned(uint256 indexes tokenId, GodType gtype);

    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyhash,
        uint256 fee
    )
        public
        VRFConsumerBase(_vrfCoordinator, _linkToken)
        ERC721("Power", "GOD")
    {
        tokenCounter = 0;
        fee = _fee;
    }

    function createCollectible()
        public
        returns (bytes32)
    {
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedCollectible(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, unit256 randomNumber)
        internal
        override
    {
        GodType gtype = GodType(randomNumber % 3);
        uint256 newTokenId = tokenCounter;
        tonekIdToGodType[??] = gtype;
        emit godAssigned(newTokenId, gtype);
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);

        tokenCounter = tokenCounter + 1;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        // ganesh, shiva, hanuman
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: caller is not owner no approved");
        _setTokenURI(tokenId, _tokenURI);
    }
}
