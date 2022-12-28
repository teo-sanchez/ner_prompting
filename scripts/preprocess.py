import typer
import json
from pathlib import Path
from spacy.util import get_words_and_spaces
from spacy.tokens import Doc, DocBin
import spacy
import pdb
stop = pdb.set_trace


def main(
    input_path: Path = typer.Argument(..., exists=True, dir_okay=False),
    output_path: Path = typer.Argument(..., dir_okay=False),
):
    nlp = spacy.load("en_core_web_lg")
    doc_bin = DocBin(attrs=["ENT_IOB", "ENT_TYPE"])
    with open(input_path, "r") as f:
        egs = [json.loads(line) for line in f]
    for eg in egs:
        if eg["answer"] != "accept": # type: ignore
            continue
        tokens = [token["text"] for token in eg["tokens"]] # type: ignore
        words, spaces = get_words_and_spaces(tokens, eg["text"]) # type: ignore
        doc = Doc(nlp.vocab, words=words, spaces=spaces)
        doc.ents = [
            doc.char_span(s["start"], s["end"], label=s["label"]) # type: ignore
            for s in eg.get("spans", []) # type: ignore
        ]
        doc_bin.add(doc)
    doc_bin.to_disk(output_path)
    # print(f"Processed {len(doc_bin)} documents: {output_path.name}")


if __name__ == "__main__":
    typer.run(main)
