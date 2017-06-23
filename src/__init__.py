from src.handlers import setup_handlers

# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'test_server_extension',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "tree",
        "dest": "src",
        "src": "static",
        "require": "src/tree"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
