from typing import Dict, Any, List, Optional
from .base import BaseProcessor
from .sectioning import SectioningProcessor
from .voting import VotingProcessor
from ...schemas.parallel import Section
from ...schemas.parallel import VotingConfig
from ...schemas.parallel import ParallelizationType

class ParallelProcessor(BaseProcessor):
    def process(
        self,
        input_text: str,
        sections: Optional[List[Section]] = None,
        voting_config: Optional[VotingConfig] = None
    ) -> Dict[str, Any]:
        """Process input using either sectioning or voting parallelization"""
        if self.parallel_type == ParallelizationType.SECTIONING:
            if not sections:
                raise ValueError("Sections must be provided for sectioning parallelization")
            processor = SectioningProcessor(self.agent, self.max_workers)
            return processor.process(input_text, sections)
            
        else:  # VOTING
            if not voting_config:
                raise ValueError("Voting config must be provided for voting parallelization")
            processor = VotingProcessor(self.agent, self.max_workers)
            return processor.process(input_text, voting_config)