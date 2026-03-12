# URL Shortener API

A RESTful backend service that converts long URLs into short links using **Django** and **Django REST Framework**.

The system generates a unique short code for each URL and redirects users to the original link when the shortened URL is accessed.

---

## Features

- Generate shortened URLs
- Redirect short links to original URLs
- REST API architecture
- Unique short code generation
- Developer-friendly setup
---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Makefile automation

---
## Project Structure

url_shortener/
│
├── config/ # Django project configuration
├── shortener/ # URL shortener application
├── manage.py # Django entry point
├── requirements.txt
├── Makefile
└── README.md
---

## Installation

Clone the repository:

```bash
git clone https://github.com/ascostic/url-shortener-api.git
cd url-shortener-api
