# main.py

from core.tool_registry import build_agent

def main():
    print("🧠 ABHYUM AI - LangChain Agent Test")

    agent = build_agent()

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        try:
            response = agent.invoke({"input": user_input})
            print("\n🤖 ABHYUM AI says:\n", response["output"])
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    main()