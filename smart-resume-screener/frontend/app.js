const uploadBtn = document.getElementById('uploadBtn');
const matchBtn = document.getElementById('matchBtn');

uploadBtn.onclick = async () => {
  const file = document.getElementById('resumeFile').files[0];
  const name = document.getElementById('candidateName').value;
  if (!file) { alert('Choose a file'); return; }
  const fd = new FormData();
  fd.append('file', file);
  fd.append('candidate_name', name);
  const res = await fetch('http://localhost:8000/upload_resume', { method: 'POST', body: fd });
  const js = await res.json();
  document.getElementById('uploadRes').textContent = JSON.stringify(js, null, 2);
  if (js.text_excerpt) document.getElementById('resumeText').value = js.text_excerpt;
};

matchBtn.onclick = async () => {
  const resumeText = document.getElementById('resumeText').value;
  const jobDesc = document.getElementById('jobDesc').value;
  if (!resumeText || !jobDesc) { alert('Provide both resume text and job description'); return; }
  const fd = new FormData();
  fd.append('resume_text', resumeText);
  fd.append('job_description', jobDesc);
  const res = await fetch('http://localhost:8000/match', { method: 'POST', body: fd });
  const js = await res.json();
  document.getElementById('matchRes').textContent = JSON.stringify(js, null, 2);
};
