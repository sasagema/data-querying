# data-querying
Flexible and efficient data querying mechanism using FastAPI, Pydantic, and SQLAlchemy.

## Installation

Project is implemented using python=3.12.4 version

- Create virtual environment

```bash
python -m venv .env
```
Mac OS

```bash
source .venv/bin/activate
```
Windows PowerShell
```bash
.venv\Scripts\Activate.ps1
```

Install requirements
```bash
pip install -r requirements.txt
```


To run fastapi API local server

```bash
  uvicorn app.main:app --reload --port=8000 --host=0.0.0.0
```
- API will be availiable on http://localhost:8000/
- API Documentation: http://localhost:8000/docs



