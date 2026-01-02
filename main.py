from orchestrator.fire_flow import run_fire
from memory.FIRE_conversation_state import ConversationState

state = ConversationState()

print("👋 Hi! Ask me about FIRE planning.\n")

while not state.completed:
    user_input = input("You: ")

    response = run_fire(user_input, state)

    print("\nAssistant:")
    print(response["message"])

    print(response)

