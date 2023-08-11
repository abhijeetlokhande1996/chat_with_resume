from pathlib import Path

from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

if Path("./.env").is_file():
    from dotenv import load_dotenv
    load_dotenv()



if __name__ == "__main__":
    loader = PyPDFLoader(file_path=FILEPATH)
    raw_document = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=40,
        separators=["\n\n", "\n", " ", ""])
    docs = text_splitter.split_documents(raw_document)

    embedding = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embedding)
    db.save_local(INDEX_NAME)

