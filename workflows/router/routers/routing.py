from llm_factory.openai_provider import OpenAIProvider
from schemas import RouteType
from ..routes.technical import TECHNICAL_ROUTE
from ..routes.customer import CUSTOMER_ROUTE
from ..routes.sales import SALES_ROUTE
from .single import SingleRouter
from .multi import MultiRouter
from .priority import PriorityRouter


def create_workflow(route_type: RouteType = RouteType.SINGLE):
    agent = OpenAIProvider()
    
    router_classes = {
        RouteType.SINGLE: SingleRouter,
        RouteType.MULTI: MultiRouter,
        RouteType.PRIORITY: PriorityRouter
    }
    
    workflow = router_classes[route_type](agent)
    
    workflow.add_route(TECHNICAL_ROUTE)
    workflow.add_route(CUSTOMER_ROUTE)
    workflow.add_route(SALES_ROUTE)
    
    return workflow