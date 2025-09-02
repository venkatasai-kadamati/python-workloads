from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# this is a minified implementation with no vector stores used. RAG is a level up from this
# is just to demonstrate how to get document similarity using embeddings

load_dotenv()

embedding = MistralAIEmbeddings(model="mistral-embed")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

# the idea here is to generate the embedding (vectors) for both documents, and the user query
# assumes document vectors as black lines and user query as red line
query_embedding = embedding.embed_query(query)
document_embeddings = embedding.embed_documents(documents)

# here we calculate the cosine similarity between the query and the documents, cosine of red line with black lines
similarity_scores = cosine_similarity([query_embedding], document_embeddings)
print(similarity_scores)
