from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import UnstructuredPDFLoader

local_path = "graphql_org_learn_queries.pdf"

# Local PDF file upload handling
if local_path:
    loader = UnstructuredPDFLoader(file_path=local_path)
    data = loader.load()
else:
    print("Upload a PDF file")

# Preview first page content
if data:
    print(data[0].page_content)  # Ensure this prints the content correctly

# Split and chunk the documents
if data:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=100)
    chunks = text_splitter.split_documents(data)
else:
    chunks = []

# Initialize embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text", show_progress=True)

# Initialize Chroma with a collection name
chroma_instance = Chroma(collection_name="local-rag")

# Add documents to the vector database
if chunks:
    for chunk in chunks:
        embeddings_result = embeddings.embed_documents([chunk.page_content])
        chroma_instance.add_documents(
            documents=[chunk],
            embeddings=embeddings_result
        )
    # Optionally, print or log success message
    print("Documents successfully added to Chroma database.")
else:
    print("No valid chunks found to process.")