from .base import BaseRouter

class MultiRouter(BaseRouter):
    def process_input(self, input_text: str) -> str:
        routing_response = self.agent.generate_response(
            self._generate_routing_prompt(input_text)
        )
        route_recommendations = self._parse_route_response(routing_response)
        
        if not route_recommendations:
            return "Unable to categorize request..."
            
        responses = []
        for route_rec in route_recommendations:
            route_config = self.routes.get(route_rec['name'])
            if route_config and route_rec['confidence'] >= route_config.confidence_threshold:
                response = self._generate_final_response(input_text, route_config)
                responses.append(response)
        return responses if responses else ["No suitable routes found for your request."]
