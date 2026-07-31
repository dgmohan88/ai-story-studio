from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.story import create_story
from app.db.deps import get_db
from app.schemas.story import StoryCreate, StoryResponse
from typing import List
from fastapi import HTTPException
router = APIRouter(
    prefix="/stories",
    tags=["Stories"],
)
from app.crud.story import (
    create_story,
    get_stories,
    get_story,
)


@router.post("/", response_model=StoryResponse)
def create_new_story(
    story: StoryCreate,
    db: Session = Depends(get_db),
):
    return create_story(db, story)

@router.get("/", response_model=List[StoryResponse])
def read_stories(db: Session = Depends(get_db)):
    return get_stories(db)


@router.get("/{story_id}", response_model=StoryResponse)
def read_story(story_id: int, db: Session = Depends(get_db)):
    story = get_story(db, story_id)

    if story is None:
        raise HTTPException(
            status_code=404,
            detail="Story not found"
        )

    return story