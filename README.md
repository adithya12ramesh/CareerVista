# CareerVista 🚀

*Where passion meets profession.*

CareerVista is a career guidance tool that helps students discover career paths
suited to their interests, passions, and background, using a simple
machine-learning model trained on student profile data.

> 🚧 **Status: early prototype.** This is the first working version — a
> student data-entry form, a first-pass ML career predictor, and an early
> login screen mockup. More features (real authentication, a full profile
> system, and a proper dashboard) are in progress.

## What's here so far

- `main.py` — Tkinter form for entering student data (age, passion,
  location) into a MySQL database.
- `career_predictor.py` — A K-Nearest Neighbors model that suggests a career
  based on age, passion, and location.
- `login_preview.py` — An early visual mockup of the login screen.

## Setup

```bash
pip install -r requirements.txt
```

Set up a local MySQL database and create a `.env` file (see `.env.example`)
with your own credentials — **do not commit real credentials**.

```bash
python main.py
```

## Tech stack

- Python, Tkinter (GUI)
- MySQL (data storage)
- pandas, scikit-learn (ML)
