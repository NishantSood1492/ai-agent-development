from pydantic import BaseModel, Field
class IdeaContent(BaseModel):
    title: str = Field(description="The title of the idea.")
    problem: str = Field(description="The problem of the idea.")
    solution: str = Field(description="The solution of the idea.")
    category: str = Field(description="The category of the idea.")
    differentiation: str = Field(description="The differentiation of the idea.")
    market: str = Field(description="The market of the idea.")
    model: str = Field(description="The model of the idea.")
    feasibility: str = Field(description="The feasibility of the idea.")