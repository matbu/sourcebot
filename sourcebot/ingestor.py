import os
import pickle
import faiss
from pathlib import Path
from urllib.parse import urlparse
from sentence_transformers import SentenceTransformer
import fitz  # PyMuPDF
import requests


class DocumentIngestor:
    def __init__(self, source):
        self.source = source
        self.chunks = []
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)

    def is_url(self, path):
        return urlparse(path).scheme in ("http", "https")

    def load_docs(self):
        texts = []

        if self.is_url(self.source):
            response = requests.get(self.source)
            response.raise_for_status()
            texts.append(response.text)
        else:
            for file in Path(self.source).rglob("*"):
                if file.suffix.lower() in [".md", ".txt", ".rst", ".json"]:
                    try:
                        texts.append(file.read_text(encoding="utf-8"))
                    except Exception as e:
                        print(f"Failed to read {file}: {e}")
                elif file.suffix.lower() == ".pdf":
                    try:
                        with fitz.open(file) as doc:
                            pdf_text = "\n".join(page.get_text() for page in doc)
                            texts.append(pdf_text)
                    except Exception as e:
                        print(f"Failed to read PDF {file}: {e}")
        return texts

    def process(self):
        docs = self.load_docs()
        self.chunks = [doc[i:i+1000] for doc in docs for i in range(0, len(doc), 1000)]
        embeddings = self.model.encode(self.chunks)
        self.index.add(embeddings)

    def save(self, index_path="index.faiss", chunks_path="chunks.pkl"):
        faiss.write_index(self.index, index_path)
        with open(chunks_path, "wb") as f:
            pickle.dump(self.chunks, f)
