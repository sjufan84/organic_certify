""" Object mapping for the app"""
from pydantic import BaseModel, Field

class Goal(BaseModel):
    """ Basic Goal Structure """
    name: str = Field(..., title="Goal Name", description="Name of the Goal")
    description: str = Field(..., title="Goal Description", description="Description of the Goal")
    steps: list = Field(..., title="Goal Steps", description="Steps to complete the Goal")
    