from dataclasses import dataclass

@dataclass
class BaseRoute:
    name: str
    description: str
    system_prompt: str
    response_template: str
    confidence_threshold: float = 0.5
    priority: int = 0