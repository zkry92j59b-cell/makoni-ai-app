from fastapi import APIRouter, Depends
from typing import Any

router = APIRouter()

@router.get("/tenants/{tenant_id}", response_model=dict)
async def read_tenant(tenant_id: int) -> Any:
    return {"tenant_id": tenant_id, "name": f"Tenant {tenant_id}"}
