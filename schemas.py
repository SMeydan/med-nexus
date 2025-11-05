from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    age: int

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class ReportBase(BaseModel):
    content: str

class ReportCreate(ReportBase):
    patient_id: int

class ReportUpdate(ReportBase):
    pass

class ReportResponse(ReportBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool
    reports: list[ReportResponse] = []

    class Config:
        orm_mode = True

class AskRequest(BaseModel):
    patient_id: int
    question: str

class AnalyzeRequest(BaseModel):
    patient_id: int
