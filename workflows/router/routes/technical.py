from .base_route import BaseRoute

TECHNICAL_ROUTE = BaseRoute(
    name="technical_support",
    description="Technical issues, error messages, or software/hardware problems",
    system_prompt="""You are a technical support specialist. Your role is to:
                    1. Identify the technical issue
                    2. Provide step-by-step troubleshooting
                    3. Explain solutions in clear, technical but accessible language""",
    response_template="""Please provide a detailed technical support response including:
                        1. Problem identification
                        2. Step-by-step troubleshooting steps
                        3. Additional recommendations""",
    confidence_threshold=0.7
)