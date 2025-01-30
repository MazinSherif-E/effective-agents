from llm_factory.openai_provider import OpenAIProvider

class BaseChain:
    def __init__(self, agent: OpenAIProvider):
        self.agent = agent