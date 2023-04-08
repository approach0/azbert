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
This [repository](https://github.com/approach0/azbert) is a boilerplate to push a mask-filling model to the HuggingFace Model Hub.

### Upload to huggingface
Download your tokenizer, model checkpoints, and optionally the training logs (`events.out.*`) to the `./ckpt` directory (do not include any large files except `pytorch_model.bin` and log files `events.out.*`).

Optionally, test model using the MLM task:
```sh
pip install pya0
python test.py \
    --model_name_or_path ./ckpt/to/tokenizer \
    --tokenizer_name_or_path ./ckpt/to/tokenizer
```
> **Note**  
> Modify the test examples in `test.txt` to play with it.
> The test file is tab-separated, the first column is additional positions you want to mask for the right-side sentence (useful for masking tokens in math markups).
> A zero means no additional mask positions.

To upload to huggingface, use the `upload2hgf.sh` script.
Before runnig this script, be sure to check:
* `git-lfs` is installed
* having git-remote named `hgf` reference to `https://huggingface.co/your/repo`
* model contains all the files needed: `config.json` and `pytorch_model.bin`
* tokenizer contains all the files needed: `added_tokens.json`, `special_tokens_map.json`, `tokenizer_config.json`, `vocab.txt` and `tokenizer.json`
* no `tokenizer_file` field in `tokenizer_config.json` (sometimes it is located locally at `~/.cache`)
