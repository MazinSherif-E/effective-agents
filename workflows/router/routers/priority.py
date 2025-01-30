from .base import BaseRouter
from schemas import RouteConfig

class PriorityRouter(BaseRouter):
    def process_input(self, input_text: str) -> str:
        routing_response = self.agent.generate_response(
            self._generate_routing_prompt(input_text)
        )
        route_recommendations = self._parse_route_response(routing_response)
        
        if not route_recommendations:
            return "Unable to categorize request..."
            
        sorted_recommendations = sorted(
        route_recommendations,
        key=lambda x: self.routes.get(x['name'], RouteConfig("", "", "", "", priority=0)).priority,
            reverse=True
        )
            
        for route_rec in sorted_recommendations:
            route_config = self.routes.get(route_rec['name'])
            if route_config and route_rec['confidence'] >= route_config.confidence_threshold:
                try:
                    return self._generate_final_response(input_text, route_config)
                except Exception as e:
                    print(f"Handler {route_rec['name']} failed: {e}")
                    continue

        return "I apologize, but I'm unable to properly process your request at this time."
