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

    function createCollectible(string memory tokenURI)
        public
        returns (bytes32)
    {
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
    }

    function fulfillRandomness(bytes32 requestId, unit256 randomNumber)
        internal
        override
    {
        GodType gtype = GodType(randomNumber % 3);
        unit256 newTokenId = tokenCounter;
        tonekIdToGodType[??] = gtype;
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);

        tokenCounter = tokenCounter + 1;
    }
}
