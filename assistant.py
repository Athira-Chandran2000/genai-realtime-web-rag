from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# LLM via Ollama
import os

llm = OllamaLLM(
    model="llama3:8b",
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
)




# Free web search tool
search = DuckDuckGoSearchRun()

# Prompt template
prompt = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.
Answer the question using ONLY the search results below.
If the answer is not found, say:
"I could not find information on that."

Search Results:
{context}

Question:
{question}
"""
)

# RAG chain (LCEL)
chain = (
    RunnablePassthrough.assign(
        context=lambda x: search.run(x["question"])
    )
    | prompt
    | llm
)

print("🌐 Real-Time AI Assistant (Web RAG)")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("🤖 Goodbye!")
        break

    print("🤖 Searching the web...\n")
    response = chain.invoke({"question": user_input})
    print(f"🤖 {response}\n")
