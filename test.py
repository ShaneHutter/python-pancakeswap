#!/usr/bin/env python3
"""This is a test script for working out ideas with making a Pancakeswap python module

Ideas:
    - Call API endpoint to get data
    - store data in various dictionaries
    - Attempt to work out calculations to determine things such as farm APR
    - etc...
"""

#from pancakeswap.endpoints  import *
from pancakeswap.tokens     import *
from pancakeswap.pairs      import *
from pancakeswap.summary    import *

from yaml       import safe_dump


if __name__ == '__main__':
    """
    summaries = get_summaries()
    print(
        safe_dump( summaries )
    )
    """

    _summary_addr = "0x8076C74C5e3F5852037F31Ff0093Eeb8c8ADd8D3_0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
    summary = get_summary( _summary_addr )
    print(
        safe_dump( summary )
    )