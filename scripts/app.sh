#!/bin/bash
set -e

path="$(dirname "$(realpath "$0")")"
app_path="$path"/..

export PYTHONPATH="$app_path"/src

cd "$app_path"
# This is necessary because powershell does not recognize the uv command
username=$(whoami)
uv_path="/home/$username/.local/bin/uv"
$uv_path run -m src.main
#############################################