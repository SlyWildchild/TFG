# Stegomalware

This project develops a set of tools in Python for advanced image manipulation, including steganography (data hiding within images) and the creation of polyglot files (files that are valid in multiple formats).

## Requirements
    python3.8
    PIL (Python Imaging Library)

## Installation

    # Clone this repository
    git clone https://github.com/SlyWildchild/TFG

## Quick Start

    # To enconde a script into an image PNG
    ./stegomalware.py -e 'imgsrc.png' 'script' 'imgout.png'

    # To enconde a script into a new image PNG
    ./stegomalware.py -e 'script'

    # To deconde a script from an image PNG
    ./stegomalware.py -d 'imgsrc.png'

    # To create a JPEG-shellscript polyglot image
    ./stegomalware.py -p 'imgsrc.jpg' 'script.sh' 'imgout.jpg'
