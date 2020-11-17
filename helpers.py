# -*- coding: utf-8 -*-
#
# Copyright 2020 Ingo Breßler
#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.

import sys, os
import requests # for HTTP requests
import json

def assertEnvVarExists(varname, purpose=""):
    if varname not in os.environ:
        print(f"No {purpose} ('{varname}' environment variable) provided!")
        sys.exit(1)

def makeRequest(method, baseurl, path, verbose=False, **kwargs):
    """Sends a web API request with the given path and method from python requests module."""
    url = baseurl + path
    if verbose:
        print(method, url)
    response = method(url, **kwargs)
    if verbose:
        print(" ", "Status:", response.status_code)
    try:
        return response.json(), response.status_code
    except json.decoder.JSONDecodeError:
        return response, response.status_code

def jsonPrettyPrint(parsed, **kwargs):
    print(json.dumps(parsed, indent=2, sort_keys=True), **kwargs)

# vim: set ts=4 sw=4 sts=4 tw=0 et:
