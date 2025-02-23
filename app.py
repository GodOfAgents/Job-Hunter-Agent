from flask import Flask, request, jsonify
import sqlite3, os
import pdfminer.high_level
import docx
import requests
from flask_cors import CORS
from gemini_parser import parse_resume
from crewai import Agent, Task, Crew

# Remove Agent and Task classes

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)
DATABASE = 'applicants.db'

# Initialize the database
def init_db():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applicants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                phone TEXT,
                location TEXT,
                resume_path TEXT,
                frequency TEXT,
                resume_text TEXT,
                jobs TEXT
            )
        ''')
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Error initializing database: {e}")
    return conn

def extract_text_from_resume(resume_path):
    if resume_path.endswith('.pdf'):
        try:
            text = pdfminer.high_level.extract_text(resume_path)
            return text
        except Exception as e:
            return f"Error extracting text from PDF: {e}"
    elif resume_path.endswith('.docx'):
        try:
            doc = docx.Document(resume_path)
            text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
            return text
        except Exception as e:
            return f"Error extracting text from DOCX: {e}"
    else:
        return "Unsupported resume format"

@app.route('/submit', methods=['POST'])
def submit_application():
    conn = init_db()
    cursor = conn.cursor()
    data = request.form
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    location = data.get('location')
    frequency = data.get('frequency')
    resume = request.files.get('resume')

    # Save the resume file locally
    os.makedirs('resumes', exist_ok=True)
    resume_path = os.path.join('resumes', resume.filename)
    resume.save(resume_path)

    # Extract text from resume
    resume_text = extract_text_from_resume(resume_path)
    
    # Parse resume using Gemini API
    parsed_resume = parse_resume(resume_text)

    # Save data to the database
    cursor.execute('''
        INSERT INTO applicants (name, email, phone, location, resume_path, frequency, resume_text)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, phone, location, resume_path, frequency, resume_text))

    # Search for jobs
    jobs = search_jobs(resume_text, location)
    # Store the jobs as a string in the database
    jobs_str = str(jobs)
    cursor.execute("UPDATE applicants SET jobs = ? WHERE name = ?", (jobs_str, name))
    conn.commit()
    # Verify jobs and compose and send email
    verified_jobs = [job for job in jobs if verify_job(job['link'])]
    email_content = compose_email(verified_jobs)
    send_email(email_content)
    # Return the result
    conn.close()
    return jsonify({'status': 'success'}), 200

def search_jobs(resume_text, location):
    # Placeholder implementation for job search
    # In a real application, this would query external job APIs
    jobs = [
        {'title': 'Software Engineer', 'description': 'Develop web applications', 'link': 'https://example.com/job1'},
        {'title': 'Data Scientist', 'description': 'Analyze data and build models', 'link': 'https://example.com/job2'},
        {'title': 'Project Manager', 'description': 'Manage software projects', 'link': 'https://example.com/job3'}
    ]
    return jobs

@app.route('/jobs', methods=['POST'])
def get_jobs():
    data = request.get_json()
    resume_text = data.get('resume_text')
    location = data.get('location')
    jobs = search_jobs(resume_text, location)
    return jsonify(jobs), 200

def verify_job(job_link):
    try:
        response = requests.get(job_link)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def compose_email(jobs):
    # Placeholder implementation for email composition
    # In a real application, this would compose an email with the job matches
    email_content = f"Here are some job matches for you:\n{jobs}"
    return email_content

def send_email(email_content):
    # Placeholder implementation for email delivery
    # In a real application, this would send the email using SMTP
    print(f"Sending email:\n{email_content}")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/send_jobs', methods=['POST'])
def send_job_matches():
    data = request.get_json()
    resume_text = data.get('resume_text')
    location = data.get('location')
    jobs = search_jobs(resume_text, location)
    email_content = compose_email(jobs)
    send_email(email_content)
    return jsonify({'status': 'success'}), 200

# Remove Agent and Task classes

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO applicants (name, email, phone, location, resume_path, frequency, resume_text, jobs)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, None, None, None, None, message, None))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Data received and saved successfully!'})

if __name__ == '__main__':
    app.run(debug=True)