from sqlalchemy.orm import Session

from app.db.models import Story
from app.schemas.story import StoryCreate


def create_story(db: Session, story: StoryCreate):
    db_story = Story(
        title=story.title,
        content=story.content,
    )

    db.add(db_story)
    db.commit()
    db.refresh(db_story)

    return db_story
def get_stories(db: Session):
    return db.query(Story).all()


def get_story(db: Session, story_id: int):
    return db.query(Story).filter(Story.id == story_id).first()