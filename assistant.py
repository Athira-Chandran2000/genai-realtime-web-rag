from langchain_community.llms import Ollama

# Initialize the local LLM via Ollama
llm = Ollama(
    model="llama3:8b",
    temperature=0.3
)

print("🤖 Hello! I'm your local AI assistant.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("🤖 Goodbye!")
        break

    print("🤖 Thinking...\n")
    response = llm.invoke(user_input)
    print(f"🤖 {response}\n")

