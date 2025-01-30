from schemas import RouteConfig
from typing import Dict, List, Any

class BaseRouter:
    def __init__(self, agent):
        self.agent = agent
        self.routes = {}
    
    def add_route(self, name, description, system_prompt, response_template, 
                 confidence_threshold=0.5, priority=0):
        self.routes[name] = RouteConfig(
            name=name,
            description=description,
            system_prompt=system_prompt,
            response_template=response_template,
            confidence_threshold=confidence_threshold,
            priority=priority
        )
    
    def _generate_routing_prompt(self, input_text: str) -> str:
        """Generate the routing prompt for the LLM"""
        routes_desc = "\n".join([
            f"- {name}: {route.description}" 
            for name, route in self.routes.items()
        ])
        
        return f"""Given the following input, determine the most appropriate routing(s).

                    Available routes:
                    {routes_desc}

                    Respond in the following JSON format:
                    {{
                        "routes": [
                            {{
                                "name": "route_name",
                                "confidence": 0.0 to 1.0,
                                "reasoning": "brief explanation"
                            }}
                        ]
                    }}

                    Input text: {input_text}

                    Provide route recommendations in order of confidence."""

    def _parse_route_response(self, response: str) -> List[Dict[str, Any]]:
        """Parse the LLM response into structured route data"""
        try:
            start = response.find('{')
            end = response.rfind('}') + 1
            json_str = response[start:end]
            
            result = eval(json_str)
            return result.get('routes', [])
        except Exception as e:
            print(f"Error parsing route response: {e}")
            return []