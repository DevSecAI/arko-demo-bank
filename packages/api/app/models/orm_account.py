from sqlalchemy import Column, Integer, String

from app.models.base import Base


class AccountRecord(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    public_id = Column(String(64), index=True)
    balance_cents = Column(Integer, default=0)
    currency = Column(String(8), default="USD")
