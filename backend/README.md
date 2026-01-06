# Backend (gov-procurement-ai)

This backend serves the API under `/api/` and, if present, will serve the static frontend from the repository's `dashboard/` directory at `/`.

Quick start (development):

1. Create & activate venv
   - Windows: `python -m venv .venv && .venv\Scripts\activate`
2. Install dependencies
   - `pip install -r backend/requirements.txt`
3. Run the app
   - `uvicorn app.main:app --reload --app-dir backend/app`
4. Open the frontend
   - Visit `http://127.0.0.1:8000/` to view the dashboard (index.html served from `dashboard/`)

API endpoints (examples):
- `GET /api/tenders` — list tenders
- `POST /api/tenders` — create tender (JSON)
- `POST /api/upload` — upload a file and create a tender from it

Notes:
- The application uses an SQLite database by default (`backend.db`). Configure `DATABASE_URL` to change it.
- Static frontend is intentionally minimal and accessible (ARIA attributes, simple layout) — expand as needed.
