from llm_factory.openai_agent import OpenAIAgent
from ..orchestrator.system import OrchestratorSystem

def run_code_task_example():
    """Example of processing a code-related task"""
    print("\n=== Running Code Task Example ===")
    
    agent = OpenAIAgent()
    orchestrator = OrchestratorSystem(agent)
    
    code_task = """
    Add input validation to the user registration form in our web app.
    The form should validate:
    - Email format
    - Password strength (min 8 chars, numbers, special chars)
    - Username (alphanumeric, 3-20 chars)
    Update both frontend validation and backend API validation.
    """
    
    print("\nProcessing Code Task:")
    print(f"Task Description:\n{code_task}")
    
    result = orchestrator.process_task(code_task)
    
    print("\nTask Breakdown:")
    for subtask in result["task_breakdown"]:
        print(f"\nSubtask: {subtask.id}")
        print(f"Type: {subtask.task_type}")
        print(f"Description: {subtask.description}")
        print(f"Dependencies: {subtask.dependencies}")
    
    print("\nSubtask Results:")
    for task_id, task_result in result["subtask_results"].items():
        print(f"\nTask ID: {task_id}")
        print(f"Status: {task_result['status']}")
        print(f"Result Summary: {task_result['result'][:200]}...")
    
    print("\nFinal Result:")
    print(result["final_result"])

def run_research_task_example():
    """Example of processing a research-related task"""
    print("\n=== Running Research Task Example ===")
    
    agent = OpenAIAgent()
    orchestrator = OrchestratorSystem(agent)
    
    research_task = """
    Research the impact of AI on healthcare in the last 5 years.
    Focus on:
    - Diagnostic applications
    - Treatment planning
    - Patient care optimization
    Provide concrete examples and statistics where available.
    """
    
    print("\nProcessing Research Task:")
    print(f"Task Description:\n{research_task}")
    
    result = orchestrator.process_task(research_task)
    
    print("\nTask Breakdown:")
    for subtask in result["task_breakdown"]:
        print(f"\nSubtask: {subtask.id}")
        print(f"Type: {subtask.task_type}")
        print(f"Description: {subtask.description}")
        print(f"Dependencies: {subtask.dependencies}")
    
    print("\nSubtask Results:")
    for task_id, task_result in result["subtask_results"].items():
        print(f"\nTask ID: {task_id}")
        print(f"Status: {task_result['status']}")
        print(f"Result Summary: {task_result['result'][:200]}...")
    
    print("\nFinal Result:")
    print(result["final_result"])

def run_analysis_task_example():
    """Example of processing an analysis task"""
    print("\n=== Running Analysis Task Example ===")
    
    agent = OpenAIAgent()
    orchestrator = OrchestratorSystem(agent)
    
    analysis_task = """
    Analyze the performance impact of different caching strategies in a high-traffic web application.
    Consider:
    - In-memory caching
    - Distributed caching
    - Database query caching
    Provide recommendations based on different traffic patterns and data types.
    """
    
    print("\nProcessing Analysis Task:")
    print(f"Task Description:\n{analysis_task}")
    
    result = orchestrator.process_task(analysis_task)
    
    print("\nTask Breakdown:")
    for subtask in result["task_breakdown"]:
        print(f"\nSubtask: {subtask.id}")
        print(f"Type: {subtask.task_type}")
        print(f"Description: {subtask.description}")
        print(f"Dependencies: {subtask.dependencies}")
    
    print("\nSubtask Results:")
    for task_id, task_result in result["subtask_results"].items():
        print(f"\nTask ID: {task_id}")
        print(f"Status: {task_result['status']}")
        print(f"Result Summary: {task_result['result'][:200]}...")
    
    print("\nFinal Result:")
    print(result["final_result"])

def main():
    """Run all examples"""
    try:
        run_code_task_example()
        run_research_task_example()
        run_analysis_task_example()
    except Exception as e:
        print(f"Error running examples: {e}")

if __name__ == "__main__":
    main()