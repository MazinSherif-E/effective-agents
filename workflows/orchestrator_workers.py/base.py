from llm_factory.openai_provider import OpenAIProvider

class BaseOrchestratorWorker:
    def __init__(self, agent: OpenAIProvider, max_workers: int = 3):
        self.agent = agent
        self.max_workers = max_workers
        self.results = {}