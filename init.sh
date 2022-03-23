#!/usr/bin/env bash
URL="https://s3.us-east-2.amazonaws.com/embeddings.net/embeddings/frWiki_no_phrase_no_postag_1000_skip_cut100.bin"
BIN_PATH="data/source.bin"

if [ ! -f "$BIN_PATH" ]; then
    curl "$URL" --output $BIN_PATH
fi
echo "👍 $BIN_PATH downloaded"
