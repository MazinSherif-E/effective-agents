from typing import Dict, Any, List
from ...schemas.parallel import VotingConfig

def aggregate_sections(results: List[Dict[str, Any]], agent) -> Dict[str, Any]:
    total_weight = sum(result['weight'] for result in results)
    weighted_confidence = sum(
        result['confidence'] * result['weight'] 
        for result in results
    ) / total_weight
    
    all_key_points = []
    detailed_analysis = {}
    
    for result in results:
        all_key_points.extend(result['key_points'])
        detailed_analysis[result['section_name']] = {
            'analysis': result['analysis'],
            'confidence': result['confidence']
        }
    
    return {
        "overall_confidence": weighted_confidence,
        "key_points": list(set(all_key_points)),
        "detailed_analysis": detailed_analysis,
        "summary": generate_summary(results, agent)
    }

def aggregate_votes(results: List[Dict[str, Any]], config: VotingConfig) -> Dict[str, Any]:
    total_votes = len(results)
    positive_votes = sum(1 for r in results if r['vote'])
    total_confidence = sum(r['confidence'] for r in results)
    average_confidence = total_confidence / total_votes
    
    decision = False
    if config.aggregation_method == "majority":
        decision = (positive_votes / total_votes) >= config.threshold
    elif config.aggregation_method == "unanimous":
        decision = positive_votes == total_votes
    elif config.aggregation_method == "weighted":
        weighted_positive = sum(r['confidence'] for r in results if r['vote'])
        decision = (weighted_positive / total_confidence) >= config.threshold
    
    return {
        "decision": decision,
        "confidence": average_confidence,
        "vote_ratio": positive_votes / total_votes,
        "detailed_votes": [
            {
                "variation": r['variation'],
                "vote": r['vote'],
                "confidence": r['confidence'],
                "reasoning": r['reasoning']
            }
            for r in results
        ]
    }

def generate_summary(results: List[Dict[str, Any]], agent) -> str:
    summary_prompt = f"""Based on the following analyses, provide a concise summary:

{json.dumps(results, indent=2)}

Provide a coherent summary that integrates all perspectives."""
    
    return agent.generate_response(summary_prompt)