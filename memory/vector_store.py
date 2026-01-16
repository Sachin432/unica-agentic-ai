import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim=384):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embedding, text):
        self.index.add(np.array([embedding]))
        self.texts.append(text)

    def search(self, embedding, k=3):
        D, I = self.index.search(np.array([embedding]), k)
        return [self.texts[i] for i in I[0]]
