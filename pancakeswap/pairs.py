#!/usr/bin/env python3
"""pancakeswap.pairs

Description:
    Functions for working with pancakeswap-info-api pairs endpoint
"""

from .          import REQUEST_HEADERS
from .endpoints import form_url

from requests   import get
from json       import loads
from copy       import deepcopy


def get_pairs( protocol = "https" ):
    """Return pairs call results"""
    _url = form_url( 
        endpoint = "pairs",
        protocol = protocol,
        )
    _pairs = loads(
        get( _url , headers = REQUEST_HEADERS ).text
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


def get_pairs_by( pair , key , protocol = "https" ):
    """Return pairs based on a specific key

    Args:
        pair: (str)     The identifier for the pair.  For example if the
                        key is "base_symbol" then the pair could be "DRIP",
                        and this would return all pairs with the base_symbol
                        of DRIP.
        key: (str)      The key to match for the returned pairs

    Returns:
        A list of all pairs that match the query
    
    """
    _ret = []
    _pairs = get_pairs( protocol = protocol )
    _pairs_data = _pairs[ "data" ]
    for _pair in deepcopy( _pairs_data ):
        _pair_key = _pairs_data.get( _pair ).get( key )
        if _pair_key is not None \
        and _pair_key == pair:
            _pair_ret = _pairs_data.get( _pair )
            _pair_ret[ "pair_address" ] = _pair
            _ret.append( _pair_ret )
    return _ret