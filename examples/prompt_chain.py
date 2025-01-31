from llm_factory.openai_provider import OpenAIProvider
from workflows.prompt_chain.sequential import SequentialChain
from workflows.prompt_chain.parallel import ParallelChain
from workflows.prompt_chain.conditional import ConditionalChain
from workflows.prompt_chain.iterative import IterativeChain
from workflows.prompt_chain.branching import BranchingChain

if __name__ == "__main__":
    agent = OpenAIProvider()
    
    # Example 1: Sequential Chain
    print("\n=== Sequential Chain Example ===")
    sequential = SequentialChain(agent)
    sequential_prompts = [
        "Write a short story about a robot",
        "Transform the previous story into a poem",
        "Create a movie script outline based on the poem"
    ]
    sequential_results = sequential.run(sequential_prompts)
    for i, result in enumerate(sequential_results):
        print(f"\nStep {i+1}:\n{result}")

    # Example 2: Parallel Chain
    print("\n=== Parallel Chain Example ===")
    parallel = ParallelChain(agent)
    base_prompt = "Describe a futuristic city in the year 2150"
    follow_up_prompts = [
        "What are the main transportation methods in this city?",
        "Describe the housing architecture in this city",
        "What energy sources power this city?"
    ]
    parallel_results = parallel.run(base_prompt, follow_up_prompts)
    print(f"\nBase Response:\n{parallel_results['base_response']}")
    for prompt, response in parallel_results.items():
        if prompt != "base_response":
            print(f"\nFollow-up: {prompt}\nResponse: {response}")

    # Example 3: Conditional Chain
    print("\n=== Conditional Chain Example ===")
    conditional = ConditionalChain(agent)
    
    def check_positive_sentiment(text: str) -> bool:
        # Simple check for positive words
        positive_words = ["good", "great", "excellent", "amazing", "wonderful", "positive"]
        return any(word in text.lower() for word in positive_words)
    
    conditional_results = conditional.run(
        initial_prompt="What do you think about renewable energy?",
        condition_check=check_positive_sentiment,
        success_prompt="Elaborate on the benefits of renewable energy",
        failure_prompt="Address common concerns about renewable energy"
    )
    print(f"\nInitial Response:\n{conditional_results['initial_response']}")
    print(f"\nPath Taken: {conditional_results['path_taken']}")
    print(f"\nFinal Response:\n{conditional_results['final_response']}")

    # Example 4: Iterative Chain
    print("\n=== Iterative Chain Example ===")
    iterative = IterativeChain(agent)
    
    def check_improvement(prev: str, new: str) -> bool:
        # Stop if the new response is significantly longer
        return len(new) > len(prev) * 1.5
    
    iterative_results = iterative.run(
        initial_prompt="Write a one-sentence story",
        refinement_prompt="Expand the story by adding more details",
        max_iterations=3,
        stop_condition=check_improvement
    )
    for i, result in enumerate(iterative_results):
        print(f"\nIteration {i}:\n{result}")

    # Example 5: Branching Chain
    print("\n=== Branching Chain Example ===")
    branching = BranchingChain(agent)
    
    def select_branch(response: str) -> str:
        # Simple branch selection based on keywords
        if "technology" in response.lower():
            return "tech_branch"
        elif "nature" in response.lower():
            return "nature_branch"
        else:
            return "general_branch"
    
    branches = {
        "tech_branch": [
            "Describe future technological implications",
            "Discuss potential challenges and solutions"
        ],
        "nature_branch": [
            "Explore environmental impacts",
            "Suggest conservation strategies"
        ],
        "general_branch": [
            "Provide a general analysis",
            "Offer broad recommendations"
        ]
    }
    
    branching_results = branching.run(
        initial_prompt="What is the most pressing challenge facing humanity?",
        branches=branches,
        branch_selector=select_branch
    )
    print(f"\nInitial Response:\n{branching_results['initial_response']}")
    print(f"\nSelected Branch: {branching_results['selected_branch']}")
    print("\nBranch Responses:")
    for i, response in enumerate(branching_results['branch_responses']):
        print(f"\nStep {i+1}:\n{response}")