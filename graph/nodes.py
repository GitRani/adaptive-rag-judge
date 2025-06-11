# 노드 관련 함수 정의
from langchain_core.documents import Document
from langchain_core.messages import AIMessage
from schemas.fastapi_schema import HumanInfo
from chains.rag_chain import (
    generate_chain,
    rewrite_query_chain,
    grade_documents_chain
)
from utils.postgresql import keyword_search
from utils.milvus import semantic_search
from utils.reranker import rerank_search

from vectorstore.pdf import PDFRetrievalChain
from pathlib import Path

from schemas.state_schema import ManagingState

import os
import logging
import re

logger = logging.getLogger(__name__)

def initialize_query(state: ManagingState):
    '''입력받은 질문을 기존 이력 여부에 따라 변형하는 노드'''
    logger.info('======== [NODE] INITIALIZE_QUERY ========')
    
    return ''

def retrieve(state: ManagingState):
    '''질문을 기반으로 Retriever 검색을 수행하는 노드'''
    logger.info('======== [NODE] RETRIEVE ========')
    
    return ''

def grade_documents(state: ManagingState):
    '''검색된 문서의 관련성을 평가하는 노드'''
    logger.info('======== [NODE] GRADE_DOCUMENTS ========')
    
    return ''

def rewrite_query(state: ManagingState):
    '''질문을 의미 기반으로 재작성하는 노드'''
    logger.info('======== [NODE] REWRITE_QUERY ========')
    
    return ''

def generate(state: ManagingState):
    '''컨텍스트를 기반으로 답변을 생성하는 노드'''
    logger.info('======== [NODE] GENERATE ========')
    
    return ''

def first_judgement(state: ManagingState):
    '''생성된 답변을 판단하는 첫번째 노드'''
    logger.info('======== [NODE] FIRST_JUDGEMENT ========')
    
    return ''

def second_judgement(state: ManagingState):
    '''생성된 답변을 판단하는 두번째 노드'''
    logger.info('======== [NODE] SECOND_JUDGEMENT ========')
    
    return ''

def third_judgement(state: ManagingState):
    '''생성된 답변을 판단하는 세번째 노드'''
    logger.info('======== [NODE] THIRD_JUDGEMENT ========')
    
    return ''

def fourth_judgement(state: ManagingState):
    '''생성된 답변을 판단하는 네번째 노드'''
    logger.info('======== [NODE] FOURTH_JUDGEMENT ========')
    
    return ''

def manager(state: ManagingState):
    '''답변을 취합하는 노드'''
    logger.info('======== [NODE] MANAGER ========')
    
    return ''
