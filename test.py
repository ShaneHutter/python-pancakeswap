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

from yaml       import safe_dump


if __name__ == '__main__':
    foobar = safe_dump( 
        get_token_by( "DRIP" , "symbol" ) 
        )
    print( foobar )