// An NFT contract 
// Where the tokenURI is one of different gods
// Randomly Selected

// SPDX-License-Identifier: MIT

pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol"

contract AdvancedCollectibel is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;

    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyhash, uint256 fee) public
    VRFConsumerBase(_vrfCoordinator, _linkToken)
    ERC721("Power", "GOD") {
        tokenCounter = 0;
        fee = _fee;
    }

    function createCollectible(string memory tokenURI) public returns (bytes32)
    
}