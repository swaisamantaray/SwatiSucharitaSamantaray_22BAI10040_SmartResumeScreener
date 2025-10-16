from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil, os, uuid, json
from .resume_parser import parse_resume_text
from .matcher import compute_match
from .database import init_db, save_resume, save_result

app = FastAPI(title="Smart Resume Screener")

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
UPLOADS = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOADS, exist_ok=True)
init_db()

@app.get("/")
def home():
    return {"message": "✅ Smart Resume Screener API is running. Visit /docs to test endpoints."}


@app.post('/upload_resume')
async def upload_resume(file: UploadFile = File(...), candidate_name: str = Form(None)):
    # save uploaded file
    file_ext = os.path.splitext(file.filename)[1]
    uid = str(uuid.uuid4())
    dst = os.path.join(UPLOADS, f"{uid}{file_ext}")
    with open(dst, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = parse_resume_text(dst)
    resume_id = save_resume(candidate_name or file.filename, file.filename, text)
    return JSONResponse({"resume_id": resume_id, "text_excerpt": text[:800]})

@app.post('/match')
async def match_resume_with_jd(resume_text: str = Form(...), job_description: str = Form(...)):
    score, justification = compute_match(resume_text, job_description)
    result_id = save_result(score, justification, resume_text, job_description)
    return JSONResponse({"score": score, "justification": justification, "result_id": result_id})

@app.post('/match_by_resume_id')
async def match_by_resume_id(resume_id: int = Form(...), job_description: str = Form(...)):
    from .database import get_resume_text
    resume_text = get_resume_text(resume_id)
    if resume_text is None:
        return JSONResponse({"error": "resume_id not found"}, status_code=404)
    score, justification = compute_match(resume_text, job_description)
    result_id = save_result(score, justification, resume_text, job_description)
    return JSONResponse({"score": score, "justification": justification, "result_id": result_id})
