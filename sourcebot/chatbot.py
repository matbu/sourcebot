import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from langdetect import detect
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings


class ChatBot:
    def __init__(self, index_path="index.faiss", chunks_path="chunks.pkl"):
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.read_index(index_path)
        with open(chunks_path, "rb") as f:
            self.chunks = pickle.load(f)
        Settings.llm = Ollama(model="dolphin-mixtral", temperature=0.2)

    def ask(self, query):
        query_vector = self.embedding_model.encode([query])
        D, I = self.index.search(np.array(query_vector), k=4)
        retrieved_chunks = [self.chunks[i] for i in I[0]]

        lang = detect(query)
        system_prompt = (
            "Tu es un assistant utile. Réponds uniquement avec le contexte ci-dessous, en français."
            if lang == "fr"
            else "You are a helpful assistant. Use ONLY the context below to answer."
        )

        context = "\n\n---\n\n".join(retrieved_chunks)
        prompt = f"""{system_prompt}

Context:
{context}

Question: {query}
Answer:"""

        response = Settings.llm.complete(prompt)
        return response.text.strip()
