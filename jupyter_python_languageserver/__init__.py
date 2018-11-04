#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Project Jupyter.
# Distributed under the terms of the Modified BSD License.

from notebook.utils import url_path_join

from ._version import __version__
from .langserver import LanguageServerWebSocketHandler

        
def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    print("Loading Jupyter Python Language Server")
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/lsp/python')
    web_app.add_handlers(host_pattern, [(route_pattern, LanguageServerWebSocketHandler)])
