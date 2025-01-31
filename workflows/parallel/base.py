from typing import Dict, Any
from llm_factory.openai_provider import OpenAIProvider
from ..schemas.types import ParallelizationType

class BaseProcessor:
    def __init__(
        self,
        agent: OpenAIProvider,
        parallel_type: ParallelizationType,
        max_workers: int = 3
    ):
        self.agent = agent
        self.parallel_type = parallel_type
        self.max_workers = max_workers