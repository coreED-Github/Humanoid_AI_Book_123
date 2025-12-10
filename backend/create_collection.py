# Step 1: import necessary modules
import os                 # os module environment variables ke liye zaruri hai
from dotenv import load_dotenv  # .env file read karne ke liye
from qdrant_client import QdrantClient

# Step 2: load .env file
load_dotenv()  # ye .env.local se variables load karega

# Step 3: get API values from environment variables
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# Step 4: connect to Qdrant
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

# Step 5: create collection
client.recreate_collection(
    collection_name="book_vectors",
    vector_size=1536,  # jitne dimension aapke embeddings ke hain
    distance="Cosine"
)

print("Collection 'book_vectors' created successfully!")
