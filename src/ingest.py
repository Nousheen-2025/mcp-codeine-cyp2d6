from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Load the MCP markdown
loader = TextLoader("data/codeine_cyp2d6_mcp.md")
documents = loader.load()

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# Convert to embeddings
embeddings = HuggingFaceEmbeddings()
db = FAISS.from_documents(docs, embeddings)

# Save DB locally
db.save_local("faiss_index")
