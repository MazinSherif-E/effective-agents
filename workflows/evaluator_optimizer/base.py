from llm_factory.openai_provider import OpenAIProvider
from typing import List
from schemas.evaluator_optimizer import EvaluationType, EvaluationCriteria

class BaseEvaluatorOptimizer:
    def __init__(
        self,
        agent: OpenAIProvider,
        eval_type: EvaluationType,
        criteria: List[EvaluationCriteria],
        max_iterations: int = 3,
        target_score: float = 0.9
    ):
        self.agent = agent
        self.eval_type = eval_type
        self.criteria = criteria
        self.max_iterations = max_iterations
        self.target_score = target_score
        
    