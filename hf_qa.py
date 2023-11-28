"""

Q&A over PDF document using HF Pipelines. No chat memory. No RAG.
Questions NOT about the document may result in an unpredictable answer.

"""

from langchain.document_loaders import PyPDFLoader
from transformers import pipeline


# Create a pipeline specifically for Q&A
model_id = "distilbert-base-cased-distilled-squad"
pipe = pipeline("question-answering", model=model_id, max_new_tokens=10, device=1)

# Parse PDF document and load its contents into string
loader = PyPDFLoader("ritchie.pdf")
data = loader.load()
context = ""
# Parse only 8 pages
for el in data[:8]:
    context += el.page_content

questions = [
    "When was Guy Ritchie born?",
    "What is Ritchie's most popular film?",
    "What awards did Guy Ritchie get?",
    "What was Ritchie's first award?",
    "When was film Sherlock Holmes created?",
    "Who did Charlie Hunnam play?",
    "What is Wrath of Man?",
    "How much kilograms are there in a ton?",
    "How far can ducks fly?",
]

# Get the answer for each question
for question in questions:
    res = pipe(question=question, context=context)
    text_res = res["answer"]
    print(f"Question: {question}\nAnswer:{text_res}")
