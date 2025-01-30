from typing import Dict, List, Callable
from .base import BaseChain

class BranchingChain(BaseChain):
    def run(
        self, 
        initial_prompt: str,
        branches: Dict[str, List[str]],
        branch_selector: Callable[[str], str]
    ) -> Dict[str, List[str]]:
        """
        Execute different chains based on the initial response
        """
        initial_response = self.agent.generate_response(initial_prompt)
        selected_branch = branch_selector(initial_response)
        
        if selected_branch not in branches:
            raise ValueError(f"Branch '{selected_branch}' not found in available branches")
            
        branch_responses = []
        current_context = initial_response
        
        for prompt in branches[selected_branch]:
            full_prompt = f"Context: {current_context}\n\nTask: {prompt}"
            response = self.agent.generate_response(full_prompt)
            branch_responses.append(response)
            current_context = response
            
        return {
            "initial_response": initial_response,
            "selected_branch": selected_branch,
            "branch_responses": branch_responses
        }