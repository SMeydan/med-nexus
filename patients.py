from sqlalchemy.orm import Session
from models import Patient
from schemas import PatientCreate, PatientUpdate
def get_patients(db: Session):
    return db.query(Patient).filter(Patient.is_active == True).all()

def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def create_patient(db: Session, patient: PatientCreate):
    db_patient = Patient(name=patient.name, age=patient.age)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(db: Session, patient_id: int, patient: PatientUpdate):
    db_patient = get_patient(db, patient_id)
    if not db_patient:
        return None
    db_patient.name = patient.name
    db_patient.age = patient.age
    db.commit()
    db.refresh(db_patient)
    return db_patient

def soft_delete_patient(db: Session, patient_id: int):
    db_patient = get_patient(db, patient_id)
    if not db_patient:
        return None
    db_patient.is_active = False
    db.commit()
    return db_patient
