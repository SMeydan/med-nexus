from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    reports = relationship("Report", back_populates="patient")


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    content = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    patient = relationship("Patient", back_populates="reports")
