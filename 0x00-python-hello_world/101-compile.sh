#!/bin/bash

echo "Compiling $PYFILE ..."
python3 -m compileall $PYFILE && mv __pycache__/$(ls __pycache__/) $PYFILE'c' && rmdir __pycache__

