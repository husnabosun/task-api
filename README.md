# task API
a very simple REST API for managing tasks, built with express.js, with a full python suite validating it against a written contract


## why this project 
this project was built to practice both side of API development writing the API itself, and testing it

## contract-first approach
before writing test assertions, I wrote [`API_CONTRACT.md`](./API_CONTRACT.md) — a specification of exactly what each endpoint should return, including status codes and response shapes.

## Tech stack
- **API:** Node.js, Express
- **Tests:** Python, pytest, requests
- **CI:** GitHub Actions (runs the full test suite on every push)

## Running the API
From the `task-api` root:
```bash
npm install
node index.js
```
Server runs on `http://localhost:3000`. Leave this running — it needs to stay active while you run the tests below.

## Running the tests
The tests require the server to be running (see above), in a **separate terminal**.

From the `task-api` root, navigate into the test folder:

```bash
cd python-tests
```
Create and activate a virtual environment (isolates Python dependencies for this project):

**Create the virtual environment** (only needs to be done once, ever, for this project):

```bash
python3 -m venv venv
```

**Activate the virtual environment** (needs to be done every time you open a new terminal to work on this project):

```bash
# macOS/Linux:
source venv/bin/activate

# Windows (PowerShell):
venv\Scripts\Activate.ps1
```
ripts\Activate.ps1
```

Install the required Python packages, listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
pytest -v
```