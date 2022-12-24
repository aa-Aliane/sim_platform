import faiss, os
from sentence_transformers import SentenceTransformer
import numpy as np
import time, json

model = SentenceTransformer("msmarco-distilbert-base-dot-prod-v3")

index = faiss.read_index("arxiv.index")


with open("idsToDocs.json", "r", encoding="utf8") as f:
    ids_to_docs = json.load(f)
    f.close()


def search(query, top_k, index, model):
    t = time.time()
    query_vector = model.encode([query])
    top_k = index.search(query_vector, top_k)
    print(">>>> Results in Total Time: {}".format(time.time() - t))
    top_k_ids = top_k[1].tolist()[0]
    top_k_ids = list(np.unique(top_k_ids))
    results = [idx for idx in top_k_ids]
    results = [ids_to_docs[str(result)] for result in results]
    return results
