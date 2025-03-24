from model.screener import get_resume_score

# Sample inputs
resume_text = """
Experienced Python developer with hands-on experience in Flask, Pandas, and Machine Learning.
Worked on building REST APIs and deploying AI models.
"""

job_description = """
Looking for a Data Scientist with strong skills in Python, Flask, Machine Learning, and model deployment.
Should have experience in API development and data analysis using Pandas.
"""

# Get similarity score
score = get_resume_score(resume_text, job_description)

# Output the result
print(f"📊 Resume Match Score: {score}%")
