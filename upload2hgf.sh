#!/bin/bash
set -ex
git lfs install
find ckpt -type f | xargs -I{} cp {} .
git lfs track events.out.*
git lfs track pytorch_model.bin
tmp_branch=hgf-`uuidgen`
git checkout -b $tmp_branch
git add .
git commit -am 'update model'
git push -f hgf $tmp_branch:main
git checkout -
git branch -D $tmp_branch
