from .base_route import BaseRoute

CUSTOMER_ROUTE = BaseRoute(
    name="customer_service",
    description="General inquiries, account issues, or policy questions",
    system_prompt="""You are a customer service representative. Your role is to:
                        1. Address customer concerns empathetically
                        2. Provide clear policy information
                        3. Offer solutions that align with company policies""",
    response_template="""Please provide a customer-friendly response that:
                        1. Acknowledges the customer's concern
                        2. Explains relevant policies
                        3. Offers clear next steps""",
    confidence_threshold=0.6
)