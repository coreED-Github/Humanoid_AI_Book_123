import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import json

# Step 1: load .env file
load_dotenv()  # ye .env.local se variables load karega

# Step 2: get Qdrant credentials
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# Step 3: Qdrant client
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Step 4: Load book content
with open("book_content.json", "r") as f:
    chapters = json.load(f)

# Step 5: Convert chapters to vectors & upload
for i, chapter in enumerate(chapters):
    client.upsert(
        collection_name="book_vectors",
        points=[
            PointStruct(id=i, vector=chapter['embedding'], payload={"text": chapter['text']})
        ]
    )

print("All chapters uploaded to 'book_vectors' successfully!")

