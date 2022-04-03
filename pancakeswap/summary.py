#!/usr/bin/env python3
"""pancakeswap.summary

Description:
    Functions for working with the pancakeswap-info-api summary endpoint
"""

from .endpoints import form_url

from requests   import get
from json       import loads
from copy       import deepcopy

def get_summary():
    """Return summary call results"""
    _url = form_url( "summary" )
    _summary = loads(
        get( _url ).text
        )
    _summary_data = _summary[ "data" ]
    # Convert required strings to floats
    for summary in deepcopy( _summary_data ):
        for key in _summary_data[ summary ]:
            _summary_data[ summary ][ key ] = float(
                _summary_data[ summary ][ key ]
                )
    return _summary