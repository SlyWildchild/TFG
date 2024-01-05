# Stegomalware

## Requirements
    python3.8
    PIL (Python Imaging Library)

## Installation

    #Clone this repo
    git clone https://github.com/SlyWildchild/TFG

## Quick Start

    # To enconde a script into an image PNG
    ./stegomalware.py -e 'imgsrc' 'script' 'imgout'

    # To enconde a script into a new image PNG
    ./stegomalware.py -e 'script'

    # To denconde a script from an image PNG
    ./stegomalware.py -d 'imgsrc'

    # To create a JPEG polyglot image
    ./stegomalware.py -p 'imgsrc' 'script' 'imgout'
