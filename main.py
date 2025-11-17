from agent.agent_setup import create_agent

def main():
    print("🌦 Smart Weather Chatbot ready! Type 'exit' to quit.")
    session_id = "user_1"
    agent = create_agent(session_id)

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break

        try:
            response = agent.invoke({"input": user_input})
            print("Bot:", response["output"])
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()