#!/bin/bash
mkdir data/routes
wget https://data.ouka.fi/data/dataset/d2ba0440-1bee-47d9-9e7a-8c33a4eb879b/resource/f1812df3-6b9b-43d1-a6b5-ea5efb0b4772/download/paa_ja_aluereitit.zip
unzip -o paa_ja_aluereitit.zip -d data/routes
rm paa_ja_aluereitit.zip
wget https://data.ouka.fi/data/dataset/fe64d13c-6fdd-478b-8414-730663a66d33/resource/6d40bb9a-41c5-4512-a9e0-c61680addcaa/download/brandireitit.zip
unzip -o brandireitit.zip -d data/routes
rm brandireitit.zip