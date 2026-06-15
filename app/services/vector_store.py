import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Persistent ChromaDB storage
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="research_documents"
)


def store_chunks(chunks):
    """
    Store chunks into ChromaDB with embeddings
    """

    for index, chunk in enumerate(chunks):

        # Generate embedding
        embedding = embedding_model.encode(chunk).tolist()

        # Store in ChromaDB
        collection.add(
            ids=[str(index)],
            embeddings=[embedding],
            documents=[chunk]
        )

    return len(chunks)