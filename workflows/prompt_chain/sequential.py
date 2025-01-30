from typing import List
from .base import BaseChain

class SequentialChain(BaseChain):
    def run(self, prompts: List[str], context: str = "") -> List[str]:
        """
        Execute prompts in sequence, where each response becomes context for the next prompt
        """
        responses = []
        current_context = context
        
        for prompt in prompts:
            full_prompt = f"Context: {current_context}\n\nTask: {prompt}" if current_context else prompt
            response = self.agent.generate_response(full_prompt)
            responses.append(response)
            current_context = response
            
        return responses