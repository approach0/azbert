---
language: en
tags:
- azbert
- pretraining
- fill-mask
widget:
- text: "$f$ $($ $x$ [MASK] $y$ $)$"
  example_title: "mathy"
- text: "$x$ [MASK] $x$ $equal$ $2$ $x$"
  example_title: "mathy"
- text: "Proof by [MASK] that $n$ $fact$ $gt$ $3$ $n$ for $n$ $gt$ $6$"
  example_title: "mathy"
- text: "Proof by induction that $n$ [MASK] $gt$ $3$ $n$ for $n$ $gt$ $6$"
  example_title: "mathy"
- text: "The goal of life is [MASK]."
  example_title: "philosophical"
license: mit
---

## About
This repository is a boilerplate to push a mask-filling model to the HuggingFace Model Hub.

### Checklist
* `git-lfs` is installed
* tokenizer contains all the files needed: `added_tokens.json`, `special_tokens_map.json`, `tokenizer_config.json`, `vocab.txt` and `tokenizer.json`
* no `tokenizer_file` field in `tokenizer_config.json` (sometimes it is located locally at `~/.cache`)

### Upload
1. Put the model checkpoints and optionally log files (`*.bin` and log files `events.out.*`) to the `./ckpt` directory.
2. Add a branch `hgf` to point to your huggingface repo. For example `git remote add hgf git@hf.co:approach0/mathy-vicuna-13B-FFT`
3. Run the `upload2hgf.sh` script.

### Test the MLM task (an example)
```sh
pip install pya0 # for math token preprocessing
# testing local checkpoints:
python test.py ./ckpt/math-tokenizer ./ckpt/2-2-0/encoder.ckpt
# testing Model Hub checkpoints:
python test.py approach0/coco-mae-220 approach0/coco-mae-220
```
> **Note**  
> Modify the test examples in `test.txt` to play with it.
> The test file is tab-separated, the first column is additional positions you want to mask for the right-side sentence (useful for masking tokens in math markups).
> A zero means no additional mask positions.
