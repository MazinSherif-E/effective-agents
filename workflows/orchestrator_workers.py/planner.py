from base import BaseOrchestratorWorker
from llm_factory.openai_provider import OpenAIProvider
from typing import List
from schemas.orchestrator import SubTask
import json

class TaskPlanner(BaseOrchestratorWorker):
    def _generate_task_planning_prompt(self, task: str) -> str:
        """Generate prompt for the orchestrator to plan subtasks"""
        return f"""As an orchestrator, break down the following task into subtasks.
Respond in JSON format with the following structure:
{{
    "subtasks": [
        {{
            "id": "unique_id",
            "task_type": "code|research|analysis|synthesis",
            "description": "detailed description",
            "context": {{"key": "value"}},
            "dependencies": ["dependency_task_ids"],
            "priority": 0-10
        }}
    ],
    "reasoning": "explanation of the breakdown"
}}

Task: {task}

Consider:
1. Dependencies between subtasks
2. Required context for each subtask
3. Priority of execution
"""

    def plan_tasks(self, task: str) -> List[SubTask]:
        planning_prompt = self._generate_task_planning_prompt(task)
        planning_response = self.agent.generate_response(planning_prompt)
        print(f"Planning response: {planning_response}")
        
        try:
            plan = json.loads(planning_response[planning_response.find('{'):planning_response.rfind('}')+1])
            subtasks = [
                SubTask(**task_dict)
                for task_dict in plan["subtasks"]
            ]
        except Exception as e:
            raise ValueError(f"Failed to parse task planning response: {e}")