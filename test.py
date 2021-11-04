import re
import os
import fire
import torch
from functools import partial
from transformers import BertTokenizer
from transformers import BertForPreTraining
from pya0.preprocess import preprocess_for_transformer


def highlight_masked(txt):
    return re.sub(r"(\[MASK\])", '\033[92m' + r"\1" + '\033[0m', txt)


def classifier_hook(tokenizer, tokens, topk, module, inputs, outputs):
    unmask_scores, seq_rel_scores = outputs
    MSK_CODE = 103
    token_ids = tokens['input_ids'][0]
    masked_idx = (token_ids == torch.tensor([MSK_CODE]))
    scores = unmask_scores[0][masked_idx]
    cands = torch.argsort(scores, dim=1, descending=True)
    for i, mask_cands in enumerate(cands):
        top_cands = mask_cands[:topk].detach().cpu()
        print(f'MASK[{i}] top candidates: ' +
            str(tokenizer.convert_ids_to_tokens(top_cands)))


def test(
    test_file='test.txt',
    ckpt_bert='ckpt/bert-pretrained-for-math-7ep/6_3_1382',
    ckpt_tokenizer='ckpt/bert-tokenizer-for-math'
    ):

    tokenizer = BertTokenizer.from_pretrained(ckpt_tokenizer)
    model = BertForPreTraining.from_pretrained(ckpt_bert,
        tie_word_embeddings=True
    )
    with open(test_file, 'r') as fh:
        for line in fh:
            # parse test file line
            line = line.rstrip()
            fields = line.split('\t')
            maskpos = list(map(int, fields[0].split(',')))
            # preprocess and mask words
            sentence = preprocess_for_transformer(fields[1])
            tokens = sentence.split()
            for pos in filter(lambda x: x!=0, maskpos):
                tokens[pos-1] = '[MASK]'
            sentence = ' '.join(tokens)
            tokens = tokenizer(sentence,
                padding=True, truncation=True, return_tensors="pt")
            #print(tokenizer.decode(tokens['input_ids'][0]))
            print('*', highlight_masked(sentence))
            # print unmasked
            with torch.no_grad():
                display = ['\n', '']
                classifier = model.cls
                partial_hook = partial(classifier_hook, tokenizer, tokens, 3)
                hook = classifier.register_forward_hook(partial_hook)
                model(**tokens)
                hook.remove()


if __name__ == '__main__':
    os.environ["PAGER"] = 'cat'
    fire.Fire(test)
