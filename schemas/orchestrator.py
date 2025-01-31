from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Any

class TaskType(Enum):
    CODE = "code"
    RESEARCH = "research"
    ANALYSIS = "analysis"
    SYNTHESIS = "synthesis"

@dataclass
class SubTask:
    id: str
    task_type: TaskType
    description: str
    context: Dict[str, Any]
    dependencies: List[str]
    priority: int
    
@dataclass
class TaskResult:
    task_id: str
    status: str
    result: str
    metadata: Dict[str, Any]