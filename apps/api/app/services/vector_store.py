from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
from typing import List, Dict
import os

class VectorStore:
    def __init__(self):
        self.client = QdrantClient("localhost", port=6333)
        self.collection_name = "gst_knowledge"
        # Use a small, fast model for local embeddings
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        self._ensure_collection()

    def _ensure_collection(self):
        collections = self.client.get_collections()
        exists = any(c.name == self.collection_name for c in collections.collections)
        
        if not exists:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=384,  # Dimension for all-MiniLM-L6-v2
                    distance=models.Distance.COSINE
                )
            )

    def upsert_documents(self, documents: List[str], metadatas: List[Dict] = None):
        if not documents:
            return
            
        embeddings = self.model.encode(documents)
        points = []
        
        for idx, (doc, vector) in enumerate(zip(documents, embeddings)):
            payload = {"text": doc}
            if metadatas and idx < len(metadatas):
                payload.update(metadatas[idx])
                
            points.append(models.PointStruct(
                id=idx,  # Simple ID generation for demo
                vector=vector.tolist(),
                payload=payload
            ))
            
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(self, query: str, limit: int = 3) -> List[Dict]:
        vector = self.model.encode(query).tolist()
        try:
            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=vector,
                limit=limit
            )
        except AttributeError:
            # Fallback to query_points (v1.x)
            results = self.client.query_points(
                collection_name=self.collection_name,
                query=vector,
                limit=limit
            ).points
            
        return [hit.payload for hit in results]

vector_store = VectorStore()
