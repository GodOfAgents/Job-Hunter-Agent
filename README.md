# Multi-Agent Job Matching System

## 📌 Overview
The Multi-Agent Job Matching System is an automated solution designed to help job seekers find relevant opportunities based on their resumes. It extracts key information from resumes, searches for job postings, verifies job availability, and sends personalized recommendations via email. The system is built using Flask, integrates with the Gemini API for resume parsing, and employs CrewAI for task orchestration.

---

## 🚀 Features
- **Resume Upload & Parsing** – Extracts text from PDF and DOCX resumes using the Gemini API.
- **Automated Job Search** – Queries external job APIs or scrapes job listings.
- **Job Verification** – Ensures job postings are active before recommending them.
- **Email Notifications** – Sends job recommendations to applicants based on their preferred frequency.
- **Database Storage** – Stores applicant details, resume text, and job matches in SQLite.
- **RESTful API** – Provides endpoints for submitting applications and retrieving job matches.
- **User Preferences Management** – Allows users to update email frequency or unsubscribe.
- **Logging & Error Handling** – Implements structured logging and error tracking.

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **AI Integration:** Gemini API (Google)
- **Orchestration:** CrewAI (Manual alternative available)
- **Database:** SQLite
- **Job Search:** External APIs / Web Scraping
- **Email Delivery:** SMTP (MailHog for local testing)
- **Frontend (Future Scope):** React.js or Vue.js for a job search dashboard.

---

## 📂 Project Structure
```
├── app.py                # Main Flask backend
├── requirements.txt      # Dependencies
├── plan.md               # Development plan
├── resumes/              # Directory for storing uploaded resumes
├── templates/            # Frontend HTML templates (if applicable)
├── logs/                 # Application logs
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/job-matching-system.git
cd job-matching-system
```

### 2️⃣ Set Up Virtual Environment
```bash
python -m venv venv  
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask Server
```bash
python app.py
```

### 5️⃣ Test Job Submission
- Use **Postman** or a frontend form to submit an applicant’s data and resume.
- Verify job recommendations are received via email.

---

## 🔧 API Endpoints
### 1️⃣ Submit a Job Application
```http
POST /submit
```
**Parameters:**
- `name` (string)
- `email` (string)
- `phone` (string)
- `location` (string)
- `resume` (file upload)
- `frequency` (daily/weekly/monthly)

### 2️⃣ Retrieve Job Matches
```http
POST /jobs
```
**Request Body:**
```json
{
  "resume_text": "Extracted text from resume",
  "location": "Job search location"
}
```

### 3️⃣ Send Job Email Manually
```http
POST /send_jobs
```
**Request Body:**
```json
{
  "resume_text": "Extracted text from resume",
  "location": "Job search location"
}
```

### 4️⃣ Update Email Preferences
```http
POST /update_preferences
```
**Request Body:**
```json
{
  "email": "user@example.com",
  "frequency": "weekly"
}
```

### 5️⃣ Unsubscribe from Emails
```http
POST /unsubscribe
```
**Request Body:**
```json
{
  "email": "user@example.com"
}
```

---

## 🛠️ Future Improvements
✅ **Enhance Job Search with AI-powered Matching**  
✅ **Deploy on Cloud Services (AWS, Google Cloud, or Heroku)**  
✅ **Implement a UI Dashboard for Applicants**  
✅ **Introduce User Authentication and Profile Management**  
✅ **Support for Multiple Resume Formats**  
✅ **Optimize Search with Machine Learning-Based Ranking**  

---

## 🤝 Contributing
We welcome contributions! If you’d like to improve the project, feel free to fork the repository and submit a pull request.

---

## 📜 License
This project is licensed under the MIT License.

---

💡 *If you have any questions or suggestions, feel free to open an issue!*

