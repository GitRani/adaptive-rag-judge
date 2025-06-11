# 사용하고자 하는 생성형 클래스로 생성
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama
from pydantic import BaseModel

import ollama
import os

class DeepSeek:
    def __init__(self, schema: BaseModel = None, model_name: str = "deepseek-r1:14b", temperature: int = 0, **kwargs):
        self.model_name = model_name
        self.temperature = temperature
        self.schema = schema
        self.kwargs = kwargs


    def get_structed_model(self) -> ChatOllama:
        model = ChatOllama(
            model=self.model_name, 
            base_url=os.getenv("OLLAMA_BASE_URL"),
            **self.kwargs    
        )

        return model.with_structured_output(self.schema)
    
    def get_model(self) -> ChatOllama:
        model = ChatOllama(
            model=self.model_name, 
            base_url=os.getenv("OLLAMA_BASE_URL"),
            **self.kwargs    
        )

        return model