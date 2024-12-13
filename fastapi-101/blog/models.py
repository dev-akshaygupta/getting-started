from sqlmodel import Field, SQLModel

# Blog Table
class Blog(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    title: str
    body: str