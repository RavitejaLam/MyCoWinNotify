#!/bin/sh

# Update the project credentials from github secrets

sed -i s/BOT_TOKEN_SECRET/"$BOT_TOKEN_SECRET"/g constant.py
sed -i s/CHAT_ID_SECRET/"$CHAT_ID_SECRET"/g constant.py