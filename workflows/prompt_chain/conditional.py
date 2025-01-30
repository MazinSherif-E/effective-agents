from typing import Dict, Callable
from .base import BaseChain

class ConditionalChain(BaseChain):
    def run(
        self, 
        initial_prompt: str,
        condition_check: Callable[[str], bool],
        success_prompt: str,
        failure_prompt: str
    ) -> Dict[str, str]:
        """
        Execute different prompts based on the condition of previous responses
        """
        initial_response = self.agent.generate_response(initial_prompt)
        
        if condition_check(initial_response):
            next_prompt = success_prompt
        else:
            next_prompt = failure_prompt
            
        full_prompt = f"Based on the previous response: {initial_response}\n\nTask: {next_prompt}"
        final_response = self.agent.generate_response(full_prompt)
        
        return {
            "initial_response": initial_response,
            "final_response": final_response,
            "path_taken": "success" if condition_check(initial_response) else "failure"
        }