from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base, int_pk, str_uniq


class Car(Base):
    id: Mapped[int_pk]
    driver_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    plate_number: Mapped[str_uniq]
    status: Mapped[int] = mapped_column(ForeignKey("statuses.id"), nullable=False)
    location: Mapped[int] = mapped_column(ForeignKey("locations.id"), nullable=False)

    extend_existing = True
