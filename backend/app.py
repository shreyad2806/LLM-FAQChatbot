from fastapi import FastAPI
from pydantic import BaseModel
from qa_chain import get_qa_chain
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
qa_chain = get_qa_chain()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):
    answer = qa_chain.run(query.question)
    return {"answer": answer}

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


