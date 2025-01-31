from typing import Dict, Any, Optional
import json
from .base import BaseEvaluator
from .prompt_generator import PromptGenerator
from .scoring import ScoreCalculator
from schemas.evaluator_optimizer import EvaluationResult

class EvaluatorOptimizer(BaseEvaluator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt_generator = PromptGenerator(*args, **kwargs)
        self.score_calculator = ScoreCalculator(*args, **kwargs)

    def optimize(self, task: str, initial_result: Optional[str] = None) -> Dict[str, Any]:
        current_result = initial_result
        history = []
        
        for iteration in range(self.max_iterations):
            if not current_result:
                optimizer_prompt = self.prompt_generator.generate_optimizer_prompt(task)
                current_result = self.agent.generate_response(optimizer_prompt)
            
            evaluator_prompt = self.prompt_generator.generate_evaluator_prompt(task, current_result)
            evaluation_response = self.agent.generate_response(evaluator_prompt)
            
            try:
                evaluation = json.loads(
                    evaluation_response[
                        evaluation_response.find('{'):evaluation_response.rfind('}')+1
                    ]
                )
                
                evaluation_result = EvaluationResult(
                    scores=evaluation["scores"],
                    feedback=evaluation["feedback"],
                    overall_score=evaluation["overall_score"],
                    suggestions=evaluation["suggestions"],
                    iteration=iteration + 1
                )
                
                history.append({
                    "iteration": iteration + 1,
                    "result": current_result,
                    "evaluation": evaluation_result.to_dict()
                })
                
                if evaluation_result.overall_score >= self.target_score:
                    break
                
                optimizer_prompt = self.prompt_generator.generate_optimizer_prompt(
                    task,
                    current_result,
                    evaluation
                )
                current_result = self.agent.generate_response(optimizer_prompt)
                
            except Exception as e:
                print(f"Error in iteration {iteration + 1}: {e}")
                break
        
        return {
            "final_result": current_result,
            "iterations": history,
            "final_score": history[-1]["evaluation"]["overall_score"] if history else 0.0,
            "improvement_summary": self.score_calculator.generate_improvement_summary(history)
        }