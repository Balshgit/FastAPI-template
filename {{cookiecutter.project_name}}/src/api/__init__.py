from fastapi import APIRouter

from src.api.httpbin import URL_PREFIX as httpbin_prefix
from src.api.httpbin import router as httpbin_router
{% if cookiecutter.add_redis == "True" -%}
from src.api.redis_api import URL_PREFIX as redis_prefix
from src.api.redis_api import router as redis_router
{% endif %}

api_router = APIRouter()

api_router.include_router(
    router=httpbin_router, prefix=httpbin_prefix, tags=['HTTPBin']
)
{% if cookiecutter.add_redis == "True" -%}
api_router.include_router(
    router=redis_router, prefix=redis_prefix, tags=["redis"]
)
{% endif %}
