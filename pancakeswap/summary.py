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
    return