from typing import List, Optional, Callable
from .base import BaseChain

class IterativeChain(BaseChain):
    def run(
        self, 
        initial_prompt: str,
        refinement_prompt: str,
        max_iterations: int = 3,
        stop_condition: Optional[Callable[[str, str], bool]] = None
    ) -> List[str]:
        """
        Iteratively refine responses until a condition is met or max iterations reached
        """
        responses = []
        current_response = self.agent.generate_response(initial_prompt)
        responses.append(current_response)
        
        for i in range(max_iterations - 1):
            full_prompt = f"Previous response: {current_response}\n\nTask: {refinement_prompt}"
            new_response = self.agent.generate_response(full_prompt)
            responses.append(new_response)
            
            if stop_condition and stop_condition(current_response, new_response):
                break
                
            current_response = new_response
            
        return responses