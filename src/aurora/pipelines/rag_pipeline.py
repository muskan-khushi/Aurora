
import chromadb
from chromadb.utils import embedding_functions

class RAGPipeline:
    def __init__(self, persist_directory="db/"):
        """Initializes the RAG Pipeline with a persistent ChromaDB client."""
        # Initialize a persistent client to save the database to disk
        self.client = chromadb.PersistentClient(path=persist_directory)

        # Use the default sentence-transformer model for embeddings
        self.embedding_function = embedding_functions.DefaultEmbeddingFunction()

        # Get or create the collection to store research data
        self.collection = self.client.get_or_create_collection(
            name="aurora_research_collection",
            embedding_function=self.embedding_function,
            metadata={"hnsw:space": "cosine"} # Specifies using cosine similarity
        )

    def add_documents(self, documents: list[str], metadatas: list[dict], ids: list[str]):
        """
        Adds documents to the ChromaDB collection.
        ChromaDB will automatically handle tokenization and embedding.
        """
        print(f"INFO: Adding {len(documents)} documents to the collection.")
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

    def query_collection(self, query_text: str, n_results: int = 5) -> dict:
        """Performs a similarity search on the collection."""
        print(f"INFO: Querying collection for: '{query_text}'")
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results