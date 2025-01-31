from llm_factory.openai_provider import OpenAIProvider
from parallel.processor import ParallelProcessor
from schemas.parallel import ParallelizationType
from schemas.parallel import Section
from schemas.parallel import VotingConfig

def run_sectioning_example():
    """Example of content analysis using sectioning"""
    print("\n=== Running Sectioning Example ===")
    
    # Initialize processor
    agent = OpenAIProvider()
    processor = ParallelProcessor(agent, ParallelizationType.SECTIONING)
    
    # Define sections for analysis
    sections = [
        Section(
            name="technical_analysis",
            system_prompt="""You are a technical content analyst focusing on accuracy and technical depth.
            Your role is to evaluate the technical accuracy, depth, and sophistication of the content.""",
            task_prompt="Analyze the technical aspects of this content, focusing on accuracy and depth:",
            weight=1.0
        ),
        Section(
            name="readability_analysis",
            system_prompt="""You are a readability expert focusing on clarity and accessibility.
            Your role is to evaluate how easily the content can be understood by the target audience.""",
            task_prompt="Analyze the readability and clarity of this content:",
            weight=0.8
        ),
        Section(
            name="engagement_analysis",
            system_prompt="""You are an engagement specialist focusing on user interest and appeal.
            Your role is to evaluate how engaging and interesting the content is for readers.""",
            task_prompt="Analyze the engagement potential of this content:",
            weight=0.6
        )
    ]
    
    # Test content
    test_content = """
    Machine learning algorithms have revolutionized data analysis. 
    Neural networks can process complex patterns in datasets, 
    enabling applications from image recognition to natural language processing.
    These technologies are becoming increasingly accessible to developers,
    with many open-source frameworks available for implementation.
    """
    
    # Process and print results
    results = processor.process(test_content, sections=sections)
    
    print("\nResults from Sectioning Analysis:")
    print("\nOverall Confidence:", results["overall_confidence"])
    print("\nKey Points:")
    for point in results["key_points"]:
        print(f"- {point}")
    
    print("\nDetailed Analysis:")
    for section, analysis in results["detailed_analysis"].items():
        print(f"\n{section.upper()}:")
        print(f"Confidence: {analysis['confidence']}")
        print(f"Analysis: {analysis['analysis']}")
    
    print("\nSummary:", results["summary"])

def run_voting_example():
    """Example of content moderation using voting"""
    print("\n=== Running Voting Example ===")
    
    # Initialize processor
    agent = OpenAIProvider()
    processor = ParallelProcessor(agent, ParallelizationType.VOTING)
    
    # Define voting configuration
    voting_config = VotingConfig(
        prompt="""You are a content moderator. Review the following content for appropriateness.
        Your task is to identify any problematic content that violates community guidelines.""",
        variations=[
            "Focus on hate speech and discriminatory content",
            "Focus on explicit adult content or inappropriate themes",
            "Focus on potentially harmful or dangerous information"
        ],
        threshold=0.7,
        aggregation_method="weighted"
    )
    
    # Test contents with different characteristics
    test_contents = [
        """
        Machine learning algorithms have revolutionized data analysis. 
        Neural networks can process complex patterns in datasets, 
        enabling applications from image recognition to natural language processing.
        """,
        """
        The mixture of chemicals can create a powerful reaction.
        When combined under pressure, the results can be explosive.
        Care must be taken when handling these substances.
        """
    ]
    
    # Process each test content
    for i, content in enumerate(test_contents, 1):
        print(f"\nTesting Content {i}:")
        print(content)
        
        results = processor.process(content, voting_config=voting_config)
        
        print("\nModeration Results:")
        print(f"Decision: {'Flagged' if results['decision'] else 'Safe'}")
        print(f"Confidence: {results['confidence']:.2f}")
        print(f"Vote Ratio: {results['vote_ratio']:.2f}")
        
        print("\nDetailed Votes:")
        for vote in results["detailed_votes"]:
            print(f"\nFocus: {vote['variation']}")
            print(f"Vote: {'Flagged' if vote['vote'] else 'Safe'}")
            print(f"Confidence: {vote['confidence']:.2f}")
            print(f"Reasoning: {vote['reasoning']}")

def main():
    """Run all examples"""
    run_sectioning_example()
    run_voting_example()

if __name__ == "__main__":
    main()