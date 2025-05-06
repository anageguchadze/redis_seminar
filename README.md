# redis_seminar

This project demonstrates how to use Django REST Framework (DRF) with Redis for caching API responses, particularly for list views with filters and search functionality.

---

## 📦 Features

- Django 5.2 + DRF
- Redis caching for performance
- Filter and search support using `django-filter`
- Category and Animal models with RESTful endpoints
- Logging system for debugging cache hits/misses

---

## 📁 Project Structure

redis_pro/
├── redis_pro/ # Project settings
├── redis_app/ # Main application (models, views, serializers)
└── manage.py

---

## ⚙️ Setup Instructions

### 1. Clone and enter project

git clone https://github.com/anageguchadze/redis_seminar.git
cd redis_seminar

2. Create virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Example requirements.txt:
Django==5.2
djangorestframework
django-filter
redis

3. Start Redis Server (if not already)
# On Ubuntu:
sudo service redis-server start
# or using docker
docker run -p 6379:6379 redis

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Run development server
python manage.py runserver

🔌 API Endpoints
Categories
GET /categories/ - List all categories

POST /categories/ - Create a new category

GET /categories/<id>/ - Retrieve a category

PUT /categories/<id>/ - Update a category

DELETE /categories/<id>/ - Delete a category

Animals
GET /animals/ - List all animals (cached, searchable, filterable)

POST /animals/ - Create a new animal

GET /animals/<id>/ - Retrieve an animal

PUT /animals/<id>/ - Update an animal

DELETE /animals/<id>/ - Delete an animal

🔍 Filtering & Searching
Search fields: name, diet

Filtering: implemented via custom AnimalFilter (you can extend this further)

Example:
GET /animals/?search=lion
GET /animals/?diet=herbivore

🚀 Redis Caching
Implemented in AnimalList view.

Cached using request query parameters as cache key.

Cache TTL: 5 minutes.

Logs output whether data was from cache or DB.

Log messages:
INFO data retrieved from cache
INFO data retrieved from db

🛠 Logging
Logging is configured for both Django and your app (redis_app). Messages are printed to the console.

To add more logs, use:
import logging
logger = logging.getLogger(__name__)
logger.info("Your message")

📚 References
Django Docs: https://docs.djangoproject.com/en/5.2/

DRF Docs: https://www.django-rest-framework.org/

Redis: https://redis.io/docs/

