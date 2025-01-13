from datetime import datetime
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel
from sqlalchemy import DateTime, func
from sqlmodel import Field, SQLModel, Relationship, Column
from sqlalchemy_utils import EmailType, PasswordType
from .courses import Course

# Enums
class UserTypeEnum(str, Enum):
    USER = "USER"
    AUTHOR = "AUTHOR"
    BUSINESS = "BUSINESS"

class SubscriptionPlanEnum(str, Enum):
    FREE = "FREE"
    BASIC = "BASIC"
    PREMIUM = "PREMIUM"

# UserAuth Model
class UserAuth(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(EmailType, index=True, unique=True)
    password: str = Field(PasswordType, index=False)
    user_role: UserTypeEnum = Field(default=UserTypeEnum.USER)
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime, default=func.now(), onupdate=func.now())) 

    # create the relationship with UserProfile
    profile: Optional["UserProfile"] = Relationship(back_populates="auth")

# UserProfile Model
class UserProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="userauth.id", unique=True, index=True)
    first_name: str
    last_name: str
    is_active: bool = Field(default=False, index=True)
    subscription_plan: SubscriptionPlanEnum = Field(default=SubscriptionPlanEnum.FREE)
    phone: Optional[str] = Field(default=None, index=True, unique=True)
    address: Optional[str] = Field(default=None, index=True)
    country: Optional[str] = Field(default=None, index=True)
    state: Optional[str] = Field(default=None, index=True)
    city: Optional[str] = Field(default=None, index=True)
    zip_code: Optional[str] = Field(default=None, index=True)
    profile_picture: Optional[str] = Field(default=None, index=True)
    bio: Optional[str] = Field(default=None, index=True)

    # create the relationship with UserAuth
    auth: Optional[UserAuth] = Relationship(back_populates="profile")

    # create the relationship with Course
    courses: List["Course"] = Relationship(back_populates="author")

# User Response Model
class UserResponseType(BaseModel):
    data: List[UserProfile]
    total_count: int
    status: str