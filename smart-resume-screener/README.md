# Smart Resume Screener

**Objective:** Intelligently parse resumes, extract skills & structured data, and match them with job descriptions.

## Features
- Upload PDF/Text resumes and job descriptions
- Parse resume text using PyMuPDF
- Compute semantic match score (1-10) using TF-IDF cosine similarity
- Store parsed data and results in SQLite
- Simple frontend to upload files and request matching

## Quick start (local)
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS / Linux
   venv\Scripts\activate     # Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Run the backend:
   ```bash
   cd backend
   uvicorn app:app --reload --port 8000
   ```
4. Open `frontend/index.html` in your browser to use the simple UI.

## Project structure
```
smart-resume-screener/
├── backend/
│   ├── app.py
│   ├── resume_parser.py
│   ├── matcher.py
│   ├── database.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── styles.css
├── data/
│   ├── sample_resumes/
│   └── job_descriptions/
├── tests/
│   ├── test_parser.py
│   └── test_matcher.py
└── README.md
```

## Notes
- The matcher uses TF-IDF similarity as a simple, dependency-light fallback to produce an interpretable score.
- If you want to integrate an LLM (OpenAI), update `matcher.py` to call the API and include prompts (see code comments).
- Add real sample resumes under `data/sample_resumes/` before running tests or demos.

## License
MIT
