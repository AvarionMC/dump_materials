#!/usr/bin/env bash


cd "$(dirname "$0")"
cd mc

mkdir -p plugins

cp ../../../target/MaterialLogger*.jar plugins
echo "eula=true" >> "eula.txt"

java -jar paper-*.jar nogui > output.txt 2>&1
