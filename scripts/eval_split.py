import json
import random

def eval_split(jsonl_path: str, split_ratio: float = 0.2, output_path: str = "/root/ner_prompting/assets/"):
    """ Split eval and train

    Args:
        jsonl_path (str): Path to jsonl file
        split_ratio (_type_): Ratio of eval to train
    """
    with open(jsonl_path) as f:
        data = [json.loads(line) for line in f]
    random.shuffle(data)
    split_index = int(len(data) * split_ratio)
    with open(output_path + 'ner_prompting_training.jsonl', 'w') as f:
        for line in data[split_index:]:
            f.write(json.dumps(line) + '')
    with open(output_path + 'ner_prompting_eval.jsonl', 'w') as f:
        for line in data[:split_index]:
            f.write(json.dumps(line) + '')
            
if __name__ == '__main__':
    # take jsonl path as argument and 
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--jsonl_path', type=str)
    parser.add_argument('--split_ratio', type=float)
    args = parser.parse_args()
    eval_split(args.jsonl_path, args.split_ratio)
    