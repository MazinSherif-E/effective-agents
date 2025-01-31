from typing import Dict, Any, Optional
import json
from base import BaseEvaluatorOptimizer

class PromptGenerator(BaseEvaluatorOptimizer):
    def _format_criteria(self) -> str:
        return "\n".join([
            f"- {c.name} (weight: {c.weight}): {c.description}"
            for c in self.criteria
        ])

    def generate_optimizer_prompt(
        self,
        task: str,
        previous_result: Optional[str] = None,
        feedback: Optional[Dict[str, Any]] = None
    ) -> str:
        base_prompt = f"""Task: {task}

Evaluation Type: {self.eval_type.value}

Criteria to consider:
{self._format_criteria()}"""

        if previous_result and feedback:
            base_prompt += f"""

Previous Result:
{previous_result}

Feedback Received:
{json.dumps(feedback, indent=2)}

Please improve the result based on the feedback while maintaining the original intent.
Focus especially on areas with lower scores.
"""
        
        return base_prompt

    def generate_evaluator_prompt(self, task: str, result: str) -> str:
        return f"""Evaluate the following result based on specified criteria.

Task: {task}
Evaluation Type: {self.eval_type.value}

Result to evaluate:
{result}

Criteria:
{self._format_criteria()}

Provide evaluation in JSON format:
{{
    "scores": {{
        "criteria_name": score (0.0 to 1.0)
    }},
    "feedback": {{
        "criteria_name": "detailed feedback"
    }},
    "overall_score": 0.0 to 1.0,
    "suggestions": [
        "specific improvement suggestions"
    ]
}}

Ensure feedback is specific and actionable."""