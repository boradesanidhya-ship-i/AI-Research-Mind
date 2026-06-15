from app.services.vector_store import collection, embedding_model


def retrieve_relevant_chunks(query: str, top_k: int = 3):
    """
    Retrieve most relevant chunks from ChromaDB
    """

    # Convert query into embedding
    query_embedding = embedding_model.encode(query).tolist()

    # Search vector database
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]