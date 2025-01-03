# Recipe Chatbot : Chef_Chatter

## Project Overview
The project integrates a conversational interface to assist users in exploring various recipes. It combines a user-friendly frontend with a robust backend, utilizing static assets, a database, and interactive views. 

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap.
- **Backend**: Django, SQLite
- **Machine Learning Model**: Pandas, scikit-learn (TfidfVectorizer, k-NearestNeighbors), Random
- **Data Handling**: CSV Files, Django ORM, Pandas
- **Deployment**: Django framework

## Setup and Installation

1. Clone the repository:
   ```bash
   https://github.com/shrawani287/Recipe_Chatbot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Reciepe_Chatbot
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application in your browser at `http://127.0.0.1:8000`.

## Repository File Structure

```
reciepe_chatbot/
├── db.sqlite3              # SQLite database file
├── manage.py               # Django project management script
├── recipe/                 # Django app folder
│   ├── migrations/         # Database migration files
│   ├── static/             # Static assets (images, styles, etc.)
│   ├── templates/          # HTML templates
│   ├── views.py            # Application views
│   ├── models.py           # Database models
│   └── ...
├── userproject/            # Main project folder
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL routing
│   └── ...
```

## Features
- Search recipes based on ingredients.
- Interactive and user-friendly chatbot interface.
- Responsive design for multiple device compatibility.
- Integration with a database for storing and retrieving recipes.

## Usage
1. Launch the application using the development server.
2. Interact with the chatbot to explore recipes.
3. Use the search feature to find recipes by ingredient.
4. Browse detailed instructions for preparing selected dishes.

---

Feel free to contribute for improving the application!
