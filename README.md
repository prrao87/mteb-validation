# MTEB embedding model validation

Comparing results of embedding models from the MTEB leaderboard.

THe goal is to study the classes of embeddings models that top the MTEB leaderboard produces high-quality embeddings across domains.

The [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard), or the “Massive Text Embedding Benchmark”, ranks sentence embedding models over a total of 129 total datasets and 113 different languages. Because there are ever more models being added to this leaderboard, it becomes necessary to evaluate specific models on custom datasets of interest.
The goal of this document is to define and describe the target tasks that will be used to evaluate the results of embedding models from the MTEB leaderboard.

## Datasets

Evaluating documents across various domains would be useful to understand the impact of using a particular model (off-the-shelf) prior to fine-tuning for a custom use case. This section lists the various datasets that could be used to evaluate the quality of retrievals from a vector database that stores the underlying embeddings from each of the models.
For each of the cases listed below, a set of 20 questions will be formulated (via human inspection) from these datasets for retrieval via a vector database downstream.

* Wikipedia countries: 194 countries’ descriptions scraped from Wikipedia
* Financial news: 306K [financial news articles](https://www.kaggle.com/datasets/jeet2016/us-financial-news-articles) from Kaggle
* Scientific abstracts: 38K [arXiv paper abstracts](https://www.kaggle.com/datasets/spsayakpaul/arxiv-paper-abstracts) from Kaggle
* Legal texts: 25K [legal cases’ texts](https://www.kaggle.com/datasets/amohankumar/legal-text-classification-dataset) from Kaggle