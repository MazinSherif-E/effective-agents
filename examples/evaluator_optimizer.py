from llm_factory.openai_provider import OpenAIProvider
from schemas.evaluator_optimizer import EvaluationType, EvaluationCriteria
from workflows.evaluator_optimizer.optimizer import EvaluatorOptimizer

def run_translation_example():
    """Example of translation evaluation and optimization"""
    print("\n=== Running Translation Example ===")
    
    agent = OpenAIProvider()
    
    translation_criteria = [
        EvaluationCriteria(
            name="accuracy",
            description="Accuracy of meaning translation",
            weight=1.0
        ),
        EvaluationCriteria(
            name="fluency",
            description="Natural flow in target language",
            weight=0.8
        ),
        EvaluationCriteria(
            name="cultural_adaptation",
            description="Appropriate cultural context adaptation",
            weight=0.6
        )
    ]
    
    # Create evaluator
    translation_evaluator = EvaluatorOptimizer(
        agent=agent,
        eval_type=EvaluationType.TRANSLATION,
        criteria=translation_criteria,
        max_iterations=3,
        target_score=0.9
    )
    
    # Test content
    translation_task = """
    Translate the following English text to French, maintaining the professional tone:
    'Our innovative approach to artificial intelligence combines cutting-edge technology 
    with ethical considerations, ensuring responsible development of AI solutions.'
    """
    
    print("\nTask:")
    print(translation_task)
    
    # Run optimization
    result = translation_evaluator.optimize(translation_task)
    
    # Display results
    print("\nOptimization Results:")
    print("\nFinal Translation:")
    print(result["final_result"])
    print("\nFinal Score:", result["final_score"])
    
    print("\nImprovement Summary:")
    for criterion, scores in result["improvement_summary"]["criteria_improvements"].items():
        print(f"\n{criterion}:")
        print(f"Initial Score: {scores['initial_score']:.2f}")
        print(f"Final Score: {scores['final_score']:.2f}")
        print(f"Improvement: {scores['improvement']:.2f}")
    
    print("\nOverall Improvement:", result["improvement_summary"]["overall_improvement"])
    print("Iterations Required:", result["improvement_summary"]["iterations_required"])

def run_writing_example():
    """Example of technical writing evaluation and optimization"""
    print("\n=== Running Technical Writing Example ===")
    
    # Initialize agent
    agent = OpenAIProvider()
    
    # Define writing criteria
    writing_criteria = [
        EvaluationCriteria(
            name="clarity",
            description="Clear and easy to understand",
            weight=1.0
        ),
        EvaluationCriteria(
            name="coherence",
            description="Logical flow and structure",
            weight=0.8
        ),
        EvaluationCriteria(
            name="engagement",
            description="Engaging and interesting content",
            weight=0.6
        ),
        EvaluationCriteria(
            name="technical_accuracy",
            description="Accurate technical information",
            weight=1.0
        )
    ]
    
    writing_evaluator = EvaluatorOptimizer(
        agent=agent,
        eval_type=EvaluationType.WRITING,
        criteria=writing_criteria,
        max_iterations=3,
        target_score=0.9
    )
    
    writing_task = """
    Write a technical blog post explaining the concept of quantum computing
    to software developers who are new to the field. Include:
    - Basic principles
    - Key differences from classical computing
    - Potential applications
    - Current limitations
    """
    
    print("\nTask:")
    print(writing_task)
    
    result = writing_evaluator.optimize(writing_task)
    
    print("\nOptimization Results:")
    print("\nFinal Article:")
    print(result["final_result"])
    print("\nFinal Score:", result["final_score"])
    
    print("\nImprovement Summary:")
    for criterion, scores in result["improvement_summary"]["criteria_improvements"].items():
        print(f"\n{criterion}:")
        print(f"Initial Score: {scores['initial_score']:.2f}")
        print(f"Final Score: {scores['final_score']:.2f}")
        print(f"Improvement: {scores['improvement']:.2f}")
    
    print("\nOverall Improvement:", result["improvement_summary"]["overall_improvement"])
    print("Iterations Required:", result["improvement_summary"]["iterations_required"])

def run_iteration_analysis():
    """Analyze the iteration process for both examples"""
    print("\n=== Running Iteration Analysis ===")
    
    agent = OpenAIProvider()
    
    test_criteria = [
        EvaluationCriteria(
            name="quality",
            description="Overall quality of the content",
            weight=1.0
        )
    ]
    
    evaluator = EvaluatorOptimizer(
        agent=agent,
        eval_type=EvaluationType.WRITING,
        criteria=test_criteria,
        max_iterations=5,
        target_score=0.95
    )
    
    test_task = "Write a one-paragraph explanation of machine learning."
    
    print("\nRunning iteration analysis...")
    result = evaluator.optimize(test_task)
    
    print("\nIteration Analysis:")
    for iteration in result["iterations"]:
        print(f"\nIteration {iteration['iteration']}:")
        print(f"Score: {iteration['evaluation']['overall_score']:.2f}")
        print("Suggestions:", len(iteration['evaluation']['suggestions']))

def main():
    """Run all examples"""
    try:
        run_translation_example()
        run_writing_example()
        run_iteration_analysis()
    except Exception as e:
        print(f"Error running examples: {e}")

if __name__ == "__main__":
    main()