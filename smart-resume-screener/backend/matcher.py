from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compute_match(resume_text: str, job_description: str):
    """Compute a similarity score (1-10) and provide a short justification.
    This uses TF-IDF + cosine similarity as a lightweight semantic fallback.
    """
    docs = [resume_text[:20000], job_description[:20000]]  # limit size
    vect = TfidfVectorizer(max_features=2000, stop_words='english')
    try:
        X = vect.fit_transform(docs)
        sim = cosine_similarity(X[0:1], X[1:2])[0][0]
    except Exception:
        sim = 0.0
    score = float(np.clip(sim, 0, 1) * 9.0 + 1.0)  # scale to 1-10
    # justification: top matching terms present in both (by tfidf)
    try:
        feature_names = vect.get_feature_names_out()
        vecs = X.toarray()
        resume_vec = vecs[0]
        jd_vec = vecs[1]
        # choose terms where both > 0, sorted by product
        prod = resume_vec * jd_vec
        top_idx = (-prod).argsort()[:8]
        top_terms = [feature_names[i] for i in top_idx if prod[i] > 0]
    except Exception:
        top_terms = []
    justification = f"Similarity-based score. Top matching keywords: {', '.join(top_terms) if top_terms else 'none'}."
    return round(score, 2), justification
