from base import BaseOrchestratorWorker
from llm_factory.openai_provider import OpenAIProvider
from typing import Dict, Any
from planner import TaskPlanner
from executer import TaskExecuter
from synthesiser import Synthesiser

class OrchestratorSystem(BaseOrchestratorWorker):
    def __init__(self, agent: OpenAIProvider, max_workers: int = 3):
        super().__init__(agent, max_workers)
        self.planner = TaskPlanner(agent, max_workers)
        self.executor = TaskExecuter(agent, max_workers)
        self.synthesizer = Synthesiser(agent, max_workers)

    def process_task(self, task: str) -> Dict[str, Any]:
        # Plan subtasks
        subtasks = self.planner.plan_task(task)
        
        # Execute subtasks
        results = self.executor.execute_tasks(subtasks)
        
        # Synthesize results
        final_response = self.synthesizer.synthesize_results(results)
        
        return {
            "final_result": final_response,
            "subtask_results": {key: value.to_dict() for key, value in results.items()},
            "task_breakdown": subtasks
        }
