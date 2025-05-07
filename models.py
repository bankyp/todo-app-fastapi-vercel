from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    completed = Column(Boolean, default=False)

    # Example placeholders for future relationships:
    # user_id = Column(Integer, ForeignKey("users.id"))
    # user = relationship("User", back_populates="todos")