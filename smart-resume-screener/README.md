*Smart Resume Screener

Objective:
I built an intelligent system to parse resumes, extract skills and structured data, and match them with job descriptions to help recruiters quickly identify the best candidates.

Features

* Upload resumes (PDF/Text) and job descriptions.
* Parse resume content using **PyMuPDF** for accurate text extraction.
* Compute a **semantic match score (1-10)** using TF-IDF cosine similarity.
* Store parsed data and matching results in **SQLite**.
* Simple frontend for uploading files and requesting match results.

Project Structure

```
smart-resume-screener/
├── backend/
│   ├── app.py             # FastAPI backend
│   ├── resume_parser.py   # Logic to extract text and structured info from resumes
│   ├── matcher.py         # TF-IDF similarity and matching logic
│   ├── database.py        # SQLite database setup and operations
│   └── requirements.txt   # Python dependencies
├── frontend/
│   ├── index.html         # Simple upload interface
│   ├── app.js             # Frontend logic for file uploads
│   └── styles.css         # Basic styling
├── data/
│   ├── sample_resumes/    # Store sample resumes for testing
│   └── job_descriptions/  # Store job descriptions
├── tests/
│   ├── test_parser.py     # Tests for resume parsing
│   └── test_matcher.py    # Tests for matching logic
└── README.md



