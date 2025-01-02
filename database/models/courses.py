from datetime import datetime
from typing import Any, Optional, List
from sqlmodel import Field, SQLModel, Relationship, Column, Session
from sqlalchemy import DateTime, func
from utils.generate_slug import generate_slug
from utils.timestamp import Timestamp

# Course Model
class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    author_id: int = Field(foreign_key="userprofile.id", index=True) 
    title: str
    slug: str = Field(default=None, unique=True) 
    currency: str
    price: float
    is_approved: bool = Field(default=False)
    description: Optional[str] = None
    cover_video_url: str
    cover_image_url: str
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime, default=func.now(), onupdate=func.now()))


    # Relationship with CourseItem
    items: List["CourseItem"] = Relationship(back_populates="course")

    # Relationship with UserProfile
    author: Optional[Any] = Relationship(back_populates="courses")


# CourseItem Model
class CourseItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    course_id: int = Field(foreign_key="course.id", index=True)
    author_id: int = Field(foreign_key="userprofile.id", index=True) 
    title: str
    slug: str = Field(default=None, unique=True)
    description: Optional[str] = None
    is_published: bool = Field(default=False)
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime, default=func.now(), onupdate=func.now()))

    # Relationship with Course
    course: Optional[Course] = Relationship(back_populates="items")

    # Relationship with UserProfile
    author: Optional[Any] = Relationship(back_populates="course_items")


# Pydantic Models
class CourseBase(SQLModel):
    title: str
    slug: str
    description: Optional[str] = None


class CourseCreate(CourseBase):
    currency: str
    price: float
    cover_video_url: str
    cover_image_url: str


class CourseUpdate(CourseBase):
    title: Optional[str] = None
    description: Optional[str] = None


class CourseInDBBase(CourseBase):
    id: int


    class Config:
        orm_mode: True


class CourseResponse(CourseInDBBase):
    pass


class CourseInDB(CourseInDBBase):
    pass


# Class method for creating the course
@classmethod
def create(cls, session: Session, **kwargs):
        # Generate the numeric-only slug before saving
        kwargs['slug'] = generate_slug(session, cls)
        course = cls(**kwargs)
        session.add(course)
        session.commit()
        session.refresh(course)
        return course
