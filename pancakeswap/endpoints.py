#!/usr/bin/env python3
"""pancakeswap.endpoints

Description:
    Variables containing information for hitting various pancakeswap-info-api endpoints
"""
PANCAKESWAP_URI = {
    "api": "api.pancakeswap.info/api",
    }

PANCAKESWAP_ENDPOINTS_V2 = {
    "summary": "/v2/summary",
    "tokens": "/v2/tokens",
    "token": "/v2/tokens/{token_address}",
    "pairs": "/v2/pairs",
    }