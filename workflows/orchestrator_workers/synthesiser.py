from base import BaseOrchestratorWorker
from schemas.orchestrator import TaskResult
import json
from typing import Dict

class Synthesiser(BaseOrchestratorWorker):
    def _generate_synthesis_prompt(self, results: Dict[str, TaskResult]) -> str:
        """Generate prompt for synthesizing results"""
        results_dict = {task_id: result.to_dict() for task_id, result in results.items()}
        
        return f"""Synthesize the following subtask results into a coherent final response:

Results:
{json.dumps(results_dict, indent=2)}

Provide a comprehensive response that:
1. Integrates all subtask results
2. Resolves any conflicts
3. Presents a clear final solution
4. Includes relevant details from subtasks
"""

    def synthesize_results(self, results: Dict[str, TaskResult]) -> str:
        synthesis_prompt = self.generate_synthesis_prompt(results)
        return self.agent.generate_response(synthesis_prompt)