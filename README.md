# Manual Test Cases – User Registration API

## Test Case ID: TC_REG_01
Title: Register user with valid email and password

Precondition:
- FastAPI server is running

Steps:
1. Open browser
2. Go to http://127.0.0.1:8000/docs
3. Select POST /register
4. Click "Try it out"
5. Enter valid email and password
6. Click "Execute"

Test Data:
{
  "email": "test@gmail.com",
  "password": "123456"
}

Expected Result:
- Status code should be 200
- Response should contain success message and email



## Test Case ID: TC_REG_02
Title: Register user without email

Precondition:
- FastAPI server is running

Steps:
1. Open http://127.0.0.1:8000/docs
2. Select POST /register
3. Click "Try it out"
4. Enter request body without email
5. Click "Execute"

Test Data:
{
  "password": "123456"
}

Expected Result:
- Status code should be 422
- Error message should indicate missing email field


## Test Case ID: TC_REG_03
Title: Register user with password as number

Precondition:
- FastAPI server is running

Steps:
1. Open http://127.0.0.1:8000/docs
2. Select POST /register
3. Click "Try it out"
4. Enter password as number
5. Click "Execute"

Test Data:
{
  "email": "test@gmail.com",
  "password": 12345
}

Expected Result:
- Status code should be 422
- Error message should indicate invalid data type
