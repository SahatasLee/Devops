#!/bin/bash
password=$(tr -dc 'A-Za-z0-9!?%=' < /dev/urandom | head -c 10)
echo "$password"