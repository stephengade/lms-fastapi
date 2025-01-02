import random
import uuid
from sqlmodel import Session, select, SQLModel

def generate_slug(session: Session, model: SQLModel) -> str:
    # Generate initial slug with a random number and short UUID
    slug = str(random.randint(100000, 999999)) + uuid.uuid4().hex[:5]
    
    # Retry logic: Check slug existence with a limit
    max_retries = 10
    retries = 0
    while retries < max_retries:
        existing_slug = session.exec(select(model).filter(model.slug == slug)).first()
        if not existing_slug:
            break  # If slug is unique, exit loop
        slug = str(random.randint(100000, 999999)) + uuid.uuid4().hex[:5]  # Regenerate slug
        retries += 1
    
    if retries == max_retries:
        # Optional: Raise an error or handle it as needed
        raise ValueError("Failed to generate a unique slug after multiple attempts")
    
    return slug
