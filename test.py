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
    print( len( get_summaries().get( "data" ) ) )
    print( len( get_pairs().get( "data" ) ) )
    print( len( get_tokens().get( "data" ) ) )
