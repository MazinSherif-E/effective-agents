from typing import Dict, Any, List
import json
from .base import BaseProcessor
from ...schemas.parallel import Section

class SectioningProcessor(BaseProcessor):
    def process_section(self, section: Section, input_text: str) -> Dict[str, Any]:
        prompt = f"""{section.system_prompt}

Input: {input_text}

{section.task_prompt}

Provide your response in JSON format with the following structure:
{{
    "analysis": "your detailed analysis",
    "key_points": ["list", "of", "key", "points"],
    "confidence": 0.0 to 1.0
}}"""
        
        response = self.agent.generate_response(prompt)
        try:
            start = response.find('{')
            end = response.rfind('}') + 1
            result = json.loads(response[start:end])
            result['section_name'] = section.name
            result['weight'] = section.weight
            return result
        except Exception as e:
            return {
                "section_name": section.name,
                "analysis": f"Error processing section: {str(e)}",
                "key_points": [],
                "confidence": 0.0,
                "weight": section.weight
            }

    def process(self, input_text: str, sections: List[Section]) -> Dict[str, Any]:
        results = [self.process_section(section, input_text) for section in sections]
        return self._aggregate_results(results)