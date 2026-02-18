# State

""" it's a shared data structure that holds the current information or context of the entire application.
In simpler terms, it is like the application's memory where it keeps track of the variables,
the data that nodes can access and modify as they execute. """

# Nodes

""" Nodes are just individual functions or operations that perform specific tasks within the graph. 
So each of these node receives an input which is often just the current state of your application.
It processes it and then produces an output or an updated state. 
"""

# Graph

"""  Graph is just the overarching structure and it maps out how different tasks (nodes) are connected and executed.
So it visually represents the workflow showing the sequence and the conditional parts between various operations."""

# Edges

""" Edges are just the connection between nodes and these determine the flow of execution. 
So, they tell us or tell the application which node should be executed next after the current one completes its task."""

# Conditional Edges

""" Conditional Edges are specialized connections that decide the next node to be executed
 based on the specific condition or logic applied to the current state."""

# Start

""" Start node is a virtual entry point in langraph and this marks where the workflow begins"""

#End 

"""End nodes just signifies the conclusion of the workflow in Langraph"""

#Tools

""" Tools are specialized functions or utilities that nodes can utilize to perform specific tasks.
For example, it could be fetching data from an API.
They basically enhance the capabilities of these nodes by providing additional functionalities.

Nodes are part of the graph structure. Whereas the tools are functionalities used within the nodes. """

#ToolNode

"""A Tool node is just a special kind of a node whose main job is to run a tool. 
it connects the tools output back into the state so other nodes can use that information."""

#StateGraph

"""A State Graph  is a class  in Langgraph to build and compile the graph structure.
It manages the nodes, the edges, the overall state and
it makes sure that the workflow operates in a unified way and all of the data flows correctly between components."""

