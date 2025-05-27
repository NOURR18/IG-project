import json
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams
import openai

#openai.api_key ="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"

def embed(text):
    return openai.Embedding.create(
        input=[text],
        model="text-embedding-ada-002"
    )['data'][0]['embedding']

client = QdrantClient(":memory:")

client.recreate_collection(
    collection_name="travel_chunks",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
)

with open("processed_chunks.json") as f:
    data = json.load(f)

points = []
for i, item in enumerate(data):
    vector = embed(item['text'])
    points.append(PointStruct(
        id=i,
        vector=vector,
        payload={**item['metadata'], "text": item['text']}
    ))

client.upsert(collection_name="travel_chunks", points=points)

def search(query):
    vector = embed(query)
    hits = client.search(
        collection_name="travel_chunks",
        query_vector=vector,
        limit=5
    )
    return [hit.payload["text"] for hit in hits]