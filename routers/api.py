from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas.fastapi_schema import HumanInfo, SearchInfo, ResponseModel
from graph.workflow import build_workflow
from utils.postgresql import keyword_search, postgre_db_connect, postgres_saver_setup
from utils.milvus import semantic_search
from utils.reranker import rerank_search

import uuid
import logging
import psycopg

router = APIRouter()
logger = logging.getLogger(__name__)







    
    
