import chromadb

client = chromadb.EphemeralClient()

collection = client.create_collection("my_collection")

collection.add(
    ids=["1", "2", "3"],
    documents=["document 1", "document 2", "document 3"],
    metadatas=[{"source": "foo"}, {"source": "bar"}, {"source": "baz"}],
)

results = collection.query(
    query_texts=["document 11"],
    n_results=2,
)

print(results)