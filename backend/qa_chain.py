from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from faq_loader import create_vector_store

def get_qa_chain():
    vectorstore = create_vector_store()
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(temperature=0)
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain
