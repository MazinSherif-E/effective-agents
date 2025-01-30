from typing import List, Dict
from .base import BaseChain

class ParallelChain(BaseChain):
    def run(self, base_prompt: str, follow_up_prompts: List[str]) -> Dict[str, str]:
        """
        Execute a base prompt and then run multiple follow-up prompts in parallel using the base response
        """
        base_response = self.agent.generate_response(base_prompt)
        results = {"base_response": base_response}
        
        for prompt in follow_up_prompts:
            full_prompt = f"Based on this information:\n{base_response}\n\nTask: {prompt}"
            response = self.agent.generate_response(full_prompt)
            results[prompt] = response
            
        return results