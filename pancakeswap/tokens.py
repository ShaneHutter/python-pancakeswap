#!/usr/bin/env python3
"""pancakeswap.tokens

Description:
    Functions for pulling current token information.
"""

from .          import REQUEST_HEADERS
from .endpoints import form_url

from requests   import get
from json       import loads
from copy       import deepcopy


def _resort_data( data , key , protocol = "https" ):
    """Internal function used to resort the returned dictionaries"""
    _ret = {
        "data": {}
        }
    _tokens = get_tokens( protocol = protocol )
    _tokens_data = _tokens.get( "data" )
    for token_addr in deepcopy( _tokens_data ):
        _token = _tokens_data[ token_addr ]
        _token.update( 
            { "address": token_addr }
            )
        _key = _token.pop( key )
        _ret[ "data" ].update(
            { _key: _token }
            )
    _ret.update(
        {
            "updated_at": _tokens.get( "updated_at" )
            }
        )
    return _ret


def get_tokens( protocol = "https" ):
    """Get current token data"""
    _url = form_url(
        endpoint = "tokens",
        protocol = protocol,
        )
    _tokens = loads( 
        get( _url , headers = REQUEST_HEADERS ).text 
        )
    _tokens_data = _tokens[ "data" ]
    # Convert price strings to floats
    for token in deepcopy( _tokens_data ):
        for key in _tokens_data[ token ]:
            if key.startswith( "price" ):
                _tokens_data[ token ][ key ] = float( 
                    _tokens_data[ token ][ key ] 
                    )
    return _tokens


def get_token( token_address , protocol = "https" ):
    """Get current token data"""
    _url = form_url(
        endpoint = "tokens",
        protocol = protocol,
        ).format( token_address = token_address )
    _token = loads( 
        get( _url , headers = REQUEST_HEADERS ).text 
        )
    _token_data = _token[ "data" ]
    # Convert price strings to floats
    for key in deepcopy( _token_data ):
        if key.startswith( "price" ):
            _token_data[ key ] = float(
                _token_data[ key ]
                )
    return _token 


def get_tokens_by( key , protocol = "https" ):
    """Create new dictionaries specifying a new key, instead of the default address"""
    return _resort_data(
        data=get_tokens( protocol = protocol ),
        key=key,
        )

def get_token_by( token , key , protocol = "https" ):
    """Get a single token by a key other than it's address"""
    _tokens = get_tokens_by(
        key = key,
        protocol = protocol,
        )
    return {
        "data": _tokens[ "data" ].get( token ),
        "updated_at": _tokens.get( "updated_at" ),
        }