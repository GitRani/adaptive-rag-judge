from typing import TypedDict, Annotated, List, Optional, Dict, Any
from langchain.schema import HumanMessage, AIMessage, BaseMessage

from langgraph.graph.message import add_messages

class ManagingState(TypedDict):
    question: str
    chat_history: Annotated[List[BaseMessage], add_messages]
    retrieved_docs: Optional[List[str]]
    rewritten_question: Optional[str]
    rewrite_count: int
    answer: Optional[str]
    evaluation_results: Optional[Dict[str, str]]
    final_decision: Optional[str]
    logs: Optional[List[Dict[str, Any]]]
    error: Optional[Dict[str, str]]
    metadata: Optional[Dict[str, Any]]
    summary: Optional[str]


    