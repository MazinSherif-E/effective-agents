from typing import Dict, Any
import json
from .base import BaseProcessor
from ...schemas.parallel import VotingConfig

class VotingProcessor(BaseProcessor):
    def process_vote(self, base_prompt: str, variation: str, input_text: str) -> Dict[str, Any]:
        prompt = f"""{base_prompt}

Input to analyze: {input_text}

Specific focus: {variation}

Provide your response in JSON format with the following structure:
{{
    "vote": true/false,
    "confidence": 0.0 to 1.0,
    "reasoning": "explanation for your vote"
}}"""
        
        response = self.agent.generate_response(prompt)
        try:
            start = response.find('{')
            end = response.rfind('}') + 1
            result = json.loads(response[start:end])
            result['variation'] = variation
            return result
        except Exception as e:
            return {
                "vote": False,
                "confidence": 0.0,
                "reasoning": f"Error processing vote: {str(e)}",
                "variation": variation
            }

    def process(self, input_text: str, config: VotingConfig) -> Dict[str, Any]:
        results = [
            self.process_vote(config.prompt, variation, input_text)
            for variation in config.variations
        ]
        return self._aggregate_results(results, config)