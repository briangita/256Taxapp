# 256 Tax App

A small Django app that works out an employee's monthly take-home pay in Uganda. Enter a gross monthly salary in UGX and it shows the PAYE tax, the NSSF deduction, total deductions and net pay.

## How PAYE is calculated

Monthly bands for resident individuals:

| Monthly income (UGX) | PAYE |
|---|---|
| Up to 235,000 | Nil |
| 235,001 to 335,000 | 10% of the amount over 235,000 |
| 335,001 to 410,000 | 10,000 + 20% of the amount over 335,000 |
| 410,001 to 10,000,000 | 25,000 + 30% of the amount over 410,000 |
| Over 10,000,000 | As above, plus an extra 10% of the amount over 10,000,000 |

NSSF is the employee's 5% of gross pay. The employer's 10% is paid on top of salary, so it doesn't reduce take-home pay.

The calculation lives in [`taxes/web/views.py`](taxes/web/views.py).

## Run it locally

```bash
git clone https://github.com/briangita/256Taxapp.git
cd 256Taxapp
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cd taxes
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000.

Settings are read from environment variables, so no secrets live in the code:

| Variable | Default | Notes |
|---|---|---|
| `DJANGO_SECRET_KEY` | random per start | Set a fixed value anywhere other than your own machine |
| `DJANGO_DEBUG` | `True` | Set to `False` outside local development |
| `DJANGO_ALLOWED_HOSTS` | empty | Comma-separated hostnames, needed when debug is off |

## Built with

Python, Django 4.2 and Tailwind CSS.
