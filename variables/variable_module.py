
def variables():
    """
    Define the variables as a Python dictionary

    :return:
    """
    variable = {
                "input": {
                    "blockchain": "ethereum",
                    "limit": 10,
                    "cursor": "",
                    "filter": {
                        "address": {
                            "_eq": "0x60e4d786628fea6478f785a6d7e704777c86a7c6"
                        }
                    }
                }
            }

    return variable

