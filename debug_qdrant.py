from qdrant_client import QdrantClient
try:
    client = QdrantClient("localhost", port=6333)
    print(f"Attributes: {dir(client)}")
except Exception as e:
    print(e)
