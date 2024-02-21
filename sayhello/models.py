from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from sayhello import db


class Message(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    body: Mapped[str] = mapped_column(String(200))
    name: Mapped[str] = mapped_column(String(20))
    timestamp = mapped_column(DateTime, default=datetime.now, index=True)
