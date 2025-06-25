from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_current_active_user, get_current_active_superuser
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import User as UserSchema, UserUpdate
from app.services import user_service

router = APIRouter()


@router.get("/me", response_model=UserSchema)
def read_user_me(
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.put("/me", response_model=UserSchema)
def update_user_me(
    *,
    db: Session = Depends(get_db),
    password: str | None = None,
    email: str | None = None,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = UserSchema.model_validate(current_user)
    user_in = UserUpdate(**current_user_data.model_dump())
    if password is not None:
        user_in.password = password
    if email is not None:
        user_in.email = email
    user = user_service.update_user(db, db_user=current_user, user_update=user_in)
    return user


@router.get("/{user_id}", response_model=UserSchema)
def read_user_by_id(
    user_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = user_service.get_user(db, user_id=user_id)
    if user == current_user:
        return user
    if not user_service.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user 