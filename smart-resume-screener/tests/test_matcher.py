from backend.matcher import compute_match

def test_compute_match_basic():
    resume = "Experienced data engineer with Python, SQL, ETL, Airflow"
    jd = "Looking for Python developer with SQL and ETL experience"
    score, justification = compute_match(resume, jd)
    assert isinstance(score, float)
    assert score >= 1.0 and score <= 10.0
    assert 'keywords' in justification.lower() or 'keyword' in justification.lower()
