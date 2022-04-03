#!/usr/bin/env python3
"""pancakeswap.summary

Description:
    Functions for working with the pancakeswap-info-api summary endpoint
"""

from .          import REQUEST_HEADERS
from .endpoints import form_url

from requests   import get
from json       import loads
from copy       import deepcopy

def get_summaries( protocol = "https" ):
    """Return summary call results"""
    _url = form_url( 
        endpoint = "summary",
        protocol = protocol,
        )
    _summary = loads(
        get( _url , headers = REQUEST_HEADERS ).text
        )
    _summary_data = _summary[ "data" ]
    # Convert required strings to floats
    for summary in deepcopy( _summary_data ):
        for key in _summary_data[ summary ]:
            _summary_data[ summary ][ key ] = float(
                _summary_data[ summary ][ key ]
                )
    return _summary

def get_summary( address ):
    """Return a specific summary"""
    _summaries = get_summaries()
    _ret = {
        "data": _summaries.get( "data" ).get( address ),
        "updated_at": _summaries.get( "updated_at" ),
        }
    _ret[ "data" ].update(
        { "summary_address": address }
        )
    return _ret