from .base_route import BaseRoute

SALES_ROUTE = BaseRoute(
    name="sales",
    description="Product inquiries, pricing questions, or purchase intentions",
    system_prompt="""You are a sales representative. Your role is to:
                        1. Understand customer needs
                        2. Explain product benefits
                        3. Provide relevant pricing and purchasing information""",
    response_template="""Please provide a sales-focused response that:
                        1. Addresses the customer's interest
                        2. Highlights relevant benefits
                        3. Provides clear pricing/purchase information""",
    confidence_threshold=0.6
)