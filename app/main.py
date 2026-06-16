from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import health, innovate, tenants
from app.core.database import Base, engine

# Create all database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Makoni AI App",
    description="Makoni AI multi-agent platform — Innovation Agent, Tenant Management, and more.",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all agent routers
app.include_router(health.router, tags=["Health"])
app.include_router(innovate.router, prefix="/api/v1", tags=["Innovation Agent"])
app.include_router(tenants.router, prefix="/api/v1", tags=["Tenant Management"])


@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": "Welcome to Makoni AI App!",
        "version": "1.0.0",
        "agents": [
            {"name": "Innovation Agent", "endpoint": "/api/v1/innovate"},
            {"name": "Tenant Management", "endpoint": "/api/v1/tenants/{tenant_id}"},
        ],
        "docs": "/docs",
        "health": "/health",
    }
