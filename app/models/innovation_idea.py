from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..core.database import Base

class InnovationIdea(Base):
    __tablename__ = "innovation_ideas"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer, ForeignKey("innovation_runs.id"))
    idea_text = Column(Text)
    score = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())

    innovation_run = relationship("InnovationRun")
