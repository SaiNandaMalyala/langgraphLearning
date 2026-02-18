import os
os.environ["LANGCHAIN_TRACING_V2"] = "false"


from typing import TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict): # Our state schema, we can give any name
    message : str 


def greeting_node(state: AgentState) -> AgentState:
    """Simple node that adds a greeting message to the state"""

    state['message'] = "Hey " + state["message"] + ", how is your day going?"

    return state 

graph = StateGraph(AgentState)

graph.add_node("greeter", greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()
result = app.invoke({"message": "Bob"})
print(result["message"])