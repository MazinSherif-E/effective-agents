from router.routers.routing import create_workflow
from schemas.routing_schema import RouteType

if __name__ == "__main__":
    workflow = create_workflow(RouteType.SINGLE)
    
    test_inputs = [
        "My laptop won't turn on after the latest update",
    ]
    
    for test_input in test_inputs:
        print(f"\n{'='*50}")
        print(f"Input: {test_input}")
        result = workflow.process_input(test_input)
        print(f"Response: {result}")