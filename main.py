from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base
from schemas import PatientBase, ReportResponse, AskRequest, AnalyzeRequest, PatientResponse, PatientCreate, PatientUpdate, ReportCreate, ReportUpdate
from patients import get_patients, get_patient, create_patient, update_patient, soft_delete_patient
from reports import get_reports_by_patient, create_report, update_report, soft_delete_report

app = FastAPI()
Base.metadata.create_all(bind=engine)

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Return Index HTML
@app.get("/", response_class=HTMLResponse)
def serve_html():
    with open("static/index.html") as f:
        html_content = f.read()
    return html_content

# List Patients
@app.get("/patient-list", response_model=list[PatientResponse])
def patient_list(db: Session = Depends(get_db)):
    return get_patients(db)

# Patient Detail
@app.get("/patient/{patient_id}", response_model=PatientResponse)
def patient_detail(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

# Create Patient
@app.post("/create-patient", response_model=PatientResponse)
def create_patient(req: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, req)

# Update Patient
@app.put("/update-patient/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, req: PatientUpdate, db: Session = Depends(get_db)):
    result = update_patient(db, patient_id, req)
    if not result:
        raise HTTPException(status_code=404, detail="Patient not found")
    return result

# Soft Delete Patient
@app.delete("/delete-patient/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    result = soft_delete_patient(db, patient_id)
    if not result:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted"}

# Send Mail Dummy
@app.post("/contact")
async def contact(request: str):
    return {"message": f"Contact form submitted"}

# User Login Dummy
@app.post("/login")
async def login(username: str, password: str):
    if username == "admin" and password == "password":
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/patient/{patient_id}/reports", response_model=list[ReportResponse])
def patient_reports(patient_id: int, db: Session = Depends(get_db)):
    return get_reports_by_patient(db, patient_id)

# Create Report
@app.post("/report", response_model=ReportResponse)
def create_new_report(req: ReportCreate, db: Session = Depends(get_db)):
    return create_report(db, req)

# Update Report
@app.put("/report/{report_id}", response_model=ReportResponse)
def update_report(report_id: int, req: ReportUpdate, db: Session = Depends(get_db)):
    res = update_report(db, report_id, req)
    if not res:
        raise HTTPException(status_code=404, detail="Report not found")
    return res

# Soft delete Report
@app.delete("/report/{report_id}")
def delete_report(report_id: int, db: Session = Depends(get_db)):
    res = soft_delete_report(db, report_id)
    if not res:
        raise HTTPException(status_code=404, detail="Report not found")
    return {"message": "Report deleted"}


@app.post("/ask")
async def ask(req: AskRequest, db: Session = Depends(get_db)):
    patient = get_patient(db, req.patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return {"answer": "Bu soruya şu an cevap veremiyorum."}

@app.post("/analyze")
async def analyze(req: AnalyzeRequest, db: Session = Depends(get_db)):
    reports = get_reports_by_patient(db, req.patient_id)

    if not reports:
        raise HTTPException(status_code=404, detail="No reports for this patient")
    return {
        "patient_id": req.patient_id,
        "diabetes": 14.2,
        "etc" : "..."
    }
