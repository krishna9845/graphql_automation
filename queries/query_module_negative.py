def queries_negative():
    query = """
    query Test1($input: TokensInput!) {
      Tokens(input: $input_data) {
        Token {
          id
          address
          chainId
          name
          symbol
          type
          totalSupply
          decimals
          baseURI
          lastTransferTimestamp
          lastTransferBlock
          lastTransferHash
          contractMetaData {
            description
          }
          logo {
            medium
            original
          }
          tokenBalances {
            tokenId
            amount
            blockchain
          }
        }
        pageInfo {
          prevCursor
          nextCursor
        }
      }
    }
    """
    return query