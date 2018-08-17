#!/usr/bin/env bash
# change all relevant info
root="/home/ravishankar/personal_work_troja/<PROJECT>"
cd $root
git pull

echo "$root/venv/bin/python -u $root/Runner.py --data $root/data" > parse.sh
qsub -e "$root/.logs/err" -o "$root/.logs/$1" -N "$1" -q gpu-ms.q@dll[256] -l gpu=1,gpu_cc_min3.5=1,gpu_ram=6G parse.sh
rm parse.sh
