from fastapi import FastAPI
from fastapi.responses import RedirectResponse
try:
    from app.endpoints.validation import router as jwt_router
except ModuleNotFoundError:
    from endpoints.validation import router as jwt_router

app = FastAPI()

@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')

app.include_router(jwt_router)
