<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Name Entity Recognition for text-to-image prompting

Project to train a evaluate a name entity recognition model to analyzing text-to-image prompts.
The entities comprise 17 categories 7 main categories and 11 subcategories, extracted from a topic analysis made with [BERTopic](https://maartengr.github.io/BERTopic/index.html). The topic analysis can be explored [the following visualization](https://teo-sanchez.github.io/projects/prompting_map.html).

```
Specifier taxonomy
├── medium/
│   ├── photography
│   ├── painting
│   ├── rendering
│   └── illustration
├── influence/
│   ├── artist
│   ├── genre
│   ├── artwork
│   └── repository
├── light
├── color
├── composition
├── detail
└── context/
    ├── era
    ├── weather
    └── emotion
```

Prompt data are from the [diffusionDB](https://poloclub.github.io/diffusiondb/) database and were annotated by hand using [Prodigy](https://prodi.gy/).


## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `install` | Install dependencies, log in to Hugging Face and download a model |
| `preprocess` | Convert the data to spaCy's binary format |
| `pretrain` | Pretrain the embedding on all prompts |
| `train` | Train a named entity recognition model |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model so it can be installed |
| `push_to_hub` | Push the model to the Hub |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `preprocess` &rarr; `pretrain` &rarr; `train` &rarr; `evaluate` &rarr; `package` &rarr; `push_to_hub` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/diffusiondb_raw_prompts.jsonl` | URL | JSONL-formatted of all diffusionDB prompts |
| `assets/ner_prompting.jsonl` | URL | JSONL-formatted development data exported from Prodigy, annotated with 17 entities |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->