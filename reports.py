from .models import Patient, Report
from sqlalchemy.orm import Session
from schemas import ReportCreate, ReportUpdate

def get_reports_by_patient(db: Session, patient_id: int):
    return db.query(Report).filter(
        Report.patient_id == patient_id,
        Report.is_active == True
    ).all()

def create_report(db: Session, report: ReportCreate):
    db_report = Report(patient_id=report.patient_id, content=report.content)
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

def update_report(db: Session, report_id: int, report: ReportUpdate):
    db_report = db.query(Report).filter(Report.id == report_id).first()
    if not db_report:
        return None
    db_report.content = report.content
    db.commit()
    db.refresh(db_report)
    return db_report

def soft_delete_report(db: Session, report_id: int):
    db_report = db.query(Report).filter(Report.id == report_id).first()
    if not db_report:
        return None
    db_report.is_active = False
    db.commit()
    return db_report
