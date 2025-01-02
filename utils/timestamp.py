from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.orm import declarative_mixin
from sqlmodel import Field, Column

@declarative_mixin
class Timestamp:
   created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
   updated_at: datetime = Field(sa_column=Column(DateTime, default=func.now(), onupdate=func.now()))