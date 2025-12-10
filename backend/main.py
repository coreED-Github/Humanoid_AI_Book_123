from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from qdrant_client import QdrantClient
import openai
import os
from dotenv import load_dotenv

# Step 1: load .env file
load_dotenv()  # ye .env.local se variables read karega

# Step 2: get API keys from environment
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Step 3: initialize FastAPI
app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Step 4: Qdrant client
qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Step 5: OpenAI API key
openai.api_key = OPENAI_API_KEY

# Step 6: endpoint
@app.get("/ask")
def ask(question: str):
    try:
        query_vector = [0.0] * 1536  # temporary vector for testing

        # search in Qdrant collection
        results = qdrant.search_points(
            collection_name="book_vectors",
            query_vector=query_vector,
            limit=3
        )

        # combine text from results
        context_text = " ".join([point.payload["text"] for point in results])

        # call OpenAI (Claude)
        response = openai.Completion.create(
            model="claude-instant-v1",
            prompt=f"Answer the question based on the following text:\n{context_text}\n\nQuestion: {question}"
        )
        return {"answer": response.choices[0].text}

    except Exception as e:
        return {"error": str(e)}