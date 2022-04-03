#!/usr/bin/env python3
"""pancakeswap.pairs

Description:
    Functions for working with pancakeswap-info-api pairs endpoint
"""


from .endpoints import form_url

from requests   import get
from json       import loads
from copy       import deepcopy


def get_pairs():
    """Return pairs call result"""
    _url = form_url( "pairs" )
    _pairs = loads(
        get( _url ).text
        )
    _pairs_data = _pairs[ "data" ]
    # Convert required strings to floats
    for address_pair in deepcopy( _pairs_data ):
        for key in _pairs_data[ address_pair ]:
            if key.endswith( "volume" ) \
            or key.startswith( "liquidity" ) \
            or key == "price":
                _pairs_data[ address_pair][ key ] = float(
                    _pairs_data[ address_pair ][ key ]
                    )
    return _pairs
