#!/usr/bin/env bash

source activate oa

python init_container.py

echo "library"
cd library
cvtoa
python upload_post.py
cd ..

echo "binarize"
cd binarize
cvtoa
python upload_post.py
python upload_prov.py
python upload_article.py
cd ..

echo "expe1"
cd expe1
cvtoa
python upload_post.py
python upload_prov.py
cd ..

echo "expe2"
cd expe2
cvtoa
python upload_post.py
python upload_prov.py
cd ..
