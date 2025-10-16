from backend.resume_parser import parse_resume_text
import os

def test_parse_text_file(tmp_path):
    p = tmp_path / "sample.txt"
    p.write_text("John Doe\nSkills: Python, SQL\nExperience: 2 years")
    txt = parse_resume_text(str(p))
    assert 'John Doe' in txt
    assert 'Python' in txt
