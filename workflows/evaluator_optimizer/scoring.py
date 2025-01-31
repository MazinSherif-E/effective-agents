from typing import Dict, List, Any
from base import BaseEvaluatorOptimizer

class ScoreCalculator(BaseEvaluatorOptimizer):
    def calculate_overall_score(self, scores: Dict[str, float]) -> float:
        total_weight = sum(c.weight for c in self.criteria)
        weighted_sum = sum(
            scores[c.name] * c.weight
            for c in self.criteria
            if c.name in scores
        )
        return weighted_sum / total_weight

    def generate_improvement_summary(self, history: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not history:
            return {}
            
        first_eval = history[0]["evaluation"]
        last_eval = history[-1]["evaluation"]
        
        improvements = {}
        for criterion in self.criteria:
            name = criterion.name
            if name in first_eval['scores'] and name in last_eval['scores']:
                improvements[name] = {
                    "initial_score": first_eval['scores'][name],
                    "final_score": last_eval['scores'][name],
                    "improvement": last_eval['scores'][name] - first_eval['scores'][name]
                }
        
        return {
            "criteria_improvements": improvements,
            "overall_improvement": last_eval['overall_score'] - first_eval['overall_score'],
            "iterations_required": len(history)
        }