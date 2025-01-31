from base import BaseOrchestratorWorker
from typing import List
from schemas.orchestrator import SubTask, TaskResult, TaskType
import json
from typing import Dict

class TaskExecuter(BaseOrchestratorWorker):
    def _generate_worker_prompt(self, subtask: SubTask) -> str:
        """Generate prompt for worker based on task type and context"""
        base_prompt = f"""Complete the following subtask:
Description: {subtask.description}

Context:
{json.dumps(subtask.context, indent=2)}

Provide your response in JSON format with:
{{
    "result": "your detailed result",
    "confidence": 0.0 to 1.0,
    "metadata": {{"key": "value"}}
}}
"""
        
        if subtask.task_type == TaskType.CODE.value:
            base_prompt += "\nProvide code changes as git-style patches or complete file contents."
        elif subtask.task_type == TaskType.RESEARCH.value:
            base_prompt += "\nProvide sources, key findings, and confidence levels."
        elif subtask.task_type == TaskType.ANALYSIS.value:
            base_prompt += "\nProvide detailed analysis with supporting evidence."
        
        return base_prompt
    
    def _execute_tasks(self, subtasks: List[SubTask]) -> Dict[str, TaskResult]:
        """Execute all subtasks respecting dependencies"""
        pending_tasks = {task.id: task for task in subtasks}
        completed_tasks = {}
        
        while pending_tasks:
            # Find tasks with satisfied dependencies
            ready_tasks = [
                task for task in pending_tasks.values()
                if not task.dependencies or all(dep in completed_tasks for dep in task.dependencies)
            ]
            
            if not ready_tasks:
                raise ValueError("Circular dependency detected in tasks")
            
            # Execute ready tasks sequentially
            for task in ready_tasks:
                result = self._process_subtask(task)
                completed_tasks[task.id] = result
                del pending_tasks[task.id]
        
        return completed_tasks
    
    def _process_subtask(self, subtask: SubTask) -> TaskResult:
        """Process a single subtask using a worker"""
        prompt = self._generate_worker_prompt(subtask)
        response = self.agent.generate_response(prompt)
        
        try:
            result_json = json.loads(response[response.find('{'):response.rfind('}')+1])
            return TaskResult(
                task_id=subtask.id,
                status="completed",
                result=result_json["result"],
                metadata=result_json.get("metadata", {})
            )
        except Exception as e:
            return TaskResult(
                task_id=subtask.id,
                status="failed",
                result=str(e),
                metadata={"error": str(e)}
            )