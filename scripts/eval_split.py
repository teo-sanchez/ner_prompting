import json
import random
import pdb
from typing import List
stop = pdb.set_trace

def remove_punctuation(data : List[dict]) -> List[dict]:
    """ Remove punctuation from each text in data

    Args:
        data (list): List of dicts
        
    Returns:
        list: List of dicts
        
    Examples:
        >>> data = [{'_input_hash': 103874305, 
        ...         '_task_hash': -751625908,
        ...         'timestamp': 1669218953,
        ...         '_view_id': 'blocks'
        ...         '_is_binary': False,
        ...         'answer': 'accept',
        ...         'html': '<img "src=https://storage.googleapis.com/selas-api/000000/000000_000000.jpg" width=500 height=500>',
        ...         'text': "Hello, world! By greg rutkowski.",
        ...         'spans': [{'text': 'Hello, world!', 'start': 0, 'end': 13, token_start: 0, token_end: 5, label: 'subject'},
        ...                   {'text': 'greg rutkowski', 'start': 17, 'end': 3& , token_start: 7, token_end: 11, label: 'influence/artist'},
        >>> remove_punctuation(data)
        [{'_input_hash': 103874305,
            '_task_hash': -751625908,
            'timestamp': 1669218953,
            '_view_id': 'blocks',
            '_is_binary': False,
            'answer': 'accept',
            'html': '<img "src=https://storage.googleapis.com/selas-api/000000/000000_000000.jpg" width=500 height=500>',
            'text': 'Hello world By greg rutkowski',
            'spans': [{'text': 'Hello world', 'start': 0, 'end': 11, 'token_start': 0, 'token_end': 5, 'label': 'subject'},
                    {'text': 'greg rutkowski', 'start': 15, 'end': 29, 'token_start': 7, 'token_end': 11, 'label': 'influence/artist'}],
            'tokens': ['Hello', 'world', 'By', 'greg', 'rutkowski']},
            ...
        ]
    """
    res : List[dict] = []
    for i, d in enumerate(data):
        # copy dict
        d_new =  d.copy()
        # remove punctuation , ; . ! ? ( ) [ ]
        d_new["text"] = d_new["text"].replace(",", "").replace(";", "").replace(".", "").replace("!", "").replace("?", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "")
        # update spans
        for span in d_new["spans"]:
            try:
                span["text"] = d_new["text"][span["start"]:span["end"]]
                span["end"] = span["start"] + len(span["text"])
            except KeyError:
                print(f"KeyError: {i}")
                continue
            span["token_start"] = len(d_new["text"][:span["start"]].split())
            span["token_end"] = len(d_new["text"][:span["end"]].split())
        # update tokens
        for token in d_new["tokens"]:
            token["start"] = d_new["text"].find(token["text"])
            token["end"] = token["start"] + len(token["text"])
        res.append(d)
        res.append(d_new)
    return res


def eval_split(jsonl_path: str, split_ratio: float = 0.2, output_path: str = "/root/ner_prompting/assets/"):
    """ Split eval and train

    Args:
        jsonl_path (str): Path to jsonl file
        split_ratio (_type_): Ratio of eval to train
    """
    with open(jsonl_path) as f:
        data = [json.loads(line) for line in f]
    augmented_data = remove_punctuation(data)
    random.shuffle(augmented_data)
    split_index = int(len(data) * split_ratio)
    with open(output_path + 'ner_prompting_training.jsonl', 'w') as f:
        for line in augmented_data[split_index:]:
            f.write(json.dumps(line) + '')
    with open(output_path + 'ner_prompting_eval.jsonl', 'w') as f:
        for line in augmented_data[:split_index]:
            f.write(json.dumps(line) + '')
            
if __name__ == '__main__':
    # take jsonl path as argument and 
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--jsonl_path', type=str)
    parser.add_argument('--split_ratio', type=float)
    args = parser.parse_args()
    eval_split(args.jsonl_path, args.split_ratio)
    