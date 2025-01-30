from .base import BaseRouter

class SingleRouter(BaseRouter):
    def process_input(self, input_text: str) -> str:
        routing_response = self.agent.generate_response(
            self._generate_routing_prompt(input_text)
        )
        route_recommendations = self._parse_route_response(routing_response)
        
        if not route_recommendations:
            return "Unable to categorize request..."
            
        top_route = route_recommendations[0]
        route_config = self.routes.get(top_route['name'])
        
        if route_config and top_route['confidence'] >= route_config.confidence_threshold:
            return self._generate_final_response(input_text, route_config)