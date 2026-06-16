from sqlalchemy.orm import Session
from ..models.innovation_run import InnovationRun

def get_innovation_run(db: Session, run_id: int):
    return db.query(InnovationRun).filter(InnovationRun.id == run_id).first()

def create_innovation_run(db: Session, tenant_id: int):
    db_run = InnovationRun(tenant_id=tenant_id)
    db.add(db_run)
    db.commit()
    db.refresh(db_run)
    return db_run
