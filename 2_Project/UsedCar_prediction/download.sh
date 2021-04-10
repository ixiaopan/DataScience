#!/usr/bin/env bash
#
# Script to download data for book
#

kaggle datasets download -d austinreese/craigslist-carstrucks-data -p data

unzip data/craigslist-carstrucks-data.zip -d data
