#!/usr/bin/env bash
# change this for the relevant server
ssh -A -t geri ssh -t sol1 "bash -s" < submit.sh $1
