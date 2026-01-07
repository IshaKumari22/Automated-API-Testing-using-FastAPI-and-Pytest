# Automated API Testing Framework

This project demonstrates automated API testing using Python.  
It focuses on testing REST APIs built with FastAPI, covering manual testing concepts, automated test cases, and CI/CD integration using GitHub Actions.

The goal of this project is to showcase **QA / SDET skills**, including test design, validation testing, and continuous integration.

---

## 🚀 Tech Stack
- Python
- FastAPI
- Pytest
- httpx
- GitHub Actions (CI)

---


---

## 🧪 Test Coverage

The following test scenarios are covered:

### Registration API
- Successful user registration
- Duplicate user registration
- Missing required fields
- Invalid input handling

### Login API
- Successful login
- Login with wrong password
- Login with non-existent user
- Validation errors (missing fields, wrong data types)

Both **positive and negative test cases** are included.

---

## 🧠 Testing Concepts Demonstrated
- Manual test case design
- Automated API testing using pytest
- Use of pytest fixtures for test setup and reuse
- Validation testing vs business logic testing
- Understanding of HTTP status codes (200, 422)
- Negative and edge-case testing

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/IshaKumari22/Automated-API-Testing-using-FastAPI-and-Pytest
cd Automated-API-Testing-using-FastAPI-and-Pytest

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Start the FastAPI server
uvicorn app.main:app --reload

5️⃣ Run automated tests
pytest
