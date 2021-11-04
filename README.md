## About
Here we share a pretrained bert model that is aware of math tokens. The math tokens are treated specially and are tokenized using [pya0](https://github.com/approach0/pya0), which adds very limited new tokens for latex markup (total vocabulary is just 31061).

### Usage
Download and try it out
```sh
pip install pya0==0.3.2
wget https://vault.cs.uwaterloo.ca/s/gqstFZmWHCLGXe3/download -O ckpt.tar.gz
mkdir -p ckpt
tar xzf ckpt.tar.gz -C ckpt --strip-components=1
python test.py --test_file test.txt
```

### Test file format
Modify the test examples in `test.txt` to play with it.

The test file is tab separated, the first column is additional positions you want to mask for the right-side sentence (useful for masking tokens in math markups). An zero means no additional mask positions.

### Example output
![](https://i.imgur.com/xpl87KO.png)
