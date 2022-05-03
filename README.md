Simple FastAPI REST sample

How to install?

1. add venv for project

pip install pip
source venv/bin/activate

2. install FastAPI and Uvicorn (Web server for python)

pip install FastAPI
pip install "uvicorn[standard]"

3. start uvicorn webserver

uvicorn main:app --reload

FAQ:

Q: How to add user by post HTTP method?

A:
curl -X POST http://127.0.0.1:8000/api/v1/users -H "Content-Type: application/json" -d '{"first_name":"Slava","last_name":"Babenko","middle_name":"Sergeevich","gender":"male","roles":["admin","user"]}'



Q: How to get info about methods of API?

A:
Go to 127.0.0.1:8000/docs
