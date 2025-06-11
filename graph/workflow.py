# nodes와 edges를 기반으로 workflow 정의
# memorysaver를 db 관리화 한다면 기능 이전 필요
from langgraph.graph import StateGraph, START, END

from schemas.state_schema import ManagingState

from graph.edges import (
    route_vector_or_websearch, 
    route_hallucination_check,
    route_generate_by_relevance
)

from graph.nodes import (
    initialize_query,
    retrieve,
    grade_documents,
    rewrite_query,
    generate,
    first_judgement,
    second_judgement,
    third_judgement,
    fourth_judgement,
    manager

)
import logging

logger = logging.getLogger(__name__)

def build_workflow():
    # retrieval subgraph
    retrieval_graph = StateGraph(ManagingState)
    retrieval_graph.add_node("retrieve", retrieve)
    retrieval_graph.add_node("grade_documents", grade_documents)
    retrieval_graph.add_node("rewrite_query", rewrite_query)

    retrieval_graph.add_edge(START, "retrieve")
    retrieval_graph.add_edge("retrieve", "grade_documents")
    retrieval_graph.add_edge("rewrite_query", "retrieve")

    retrieval_graph.add_conditional_edges(
        "grade_documents",
        route_generate_by_relevance,
        {"relevant": END, "irrelevant": "rewrite_query"}
    )

    # judgment subgraph
    judgment_graph = StateGraph(ManagingState)
    judgment_graph.add_node("generate", generate)
    judgment_graph.add_node("first_judgement", first_judgement)
    judgment_graph.add_node("second_judgement", second_judgement)
    judgment_graph.add_node("third_judgement", third_judgement)
    judgment_graph.add_node("fourth_judgement", fourth_judgement)
    judgment_graph.add_node("manager", manager)

    judgment_graph.add_edge(START, "generate") 
    judgment_graph.add_edge("generate", "first_judgement")
    judgment_graph.add_edge("generate", "second_judgement")
    judgment_graph.add_edge("generate", "third_judgement")
    judgment_graph.add_edge("generate", "fourth_judgement")
    judgment_graph.add_edge("first_judgement", "manager")
    judgment_graph.add_edge("second_judgement", "manager")
    judgment_graph.add_edge("third_judgement", "manager")
    judgment_graph.add_edge("fourth_judgement", "manager")
    judgment_graph.add_edge("manager", END)

    # main graph
    main_workflow = StateGraph(ManagingState)
    main_workflow.add_node("initialize_query", initialize_query)  # 초기화 노드 추가
    main_workflow.add_node("retrieval", retrieval_graph.compile())

    main_workflow.add_node("judgment", judgment_graph.compile())

    # 메인 그래프 엣지
    main_workflow.add_edge(START, "initialize_query")
    main_workflow.add_conditional_edges(
        "initialize_query",
        route_vector_or_generate,
        {"vector": "retrieval", "generate": "judgment"}
    )
    main_workflow.add_edge("retrieval", "judgment")
    main_workflow.add_edge("judgment", END)







