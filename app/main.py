from fastapi import FastAPI
from fastapi.responses import RedirectResponse
try:
    from app.endpoints.validation import router as jwt_router
    from app.endpoints.health import router as health
except ModuleNotFoundError:
    from endpoints.validation import router as jwt_router
    from endpoints.health import router as health
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')

app.include_router(jwt_router)
app.include_router(health, include_in_schema=False)
Instrumentator().instrument(app).expose(app)