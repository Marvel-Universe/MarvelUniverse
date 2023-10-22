# Installation and Configuration Guide
## 1. Clone the Repository

Clone or download the code from the GitHub repository using after that change the directory:

```https://github.com/Marvel-Universe/MarvelUniverse2.git```

``` cd MarvelUniverse```
## 2. Create a Virtual Environment
* ```python -m venv venv```


## 3. Activate the Virtual Environment
- On Windows:
  ```venv\Scripts\activate```
- On macOS and Linux:
  ```source venv/bin/activate```


## 4. Install Dependencies

Install the project dependencies using pip: 

```pip install -r requirements.txt```


## 5. Set Values for Externalized Variables

Configure the app by setting values for externalized variables. Create a `.env` file in the project root and define the following variables:
- SECRET_KEY=your_secret_key
- DEBUG=True # Set to False for production
- DATABASE_URL=your_database_url


## 6. Run Migrations (if python doesn't work use python3 instead)

Apply database migrations to create the database schema: 

```python manage.py migrate```

## 6. Load initial data into database.

```python manage.py loaddata data/marvel_data.json```


## 8. Start the Development Server

Start the development server to run your app: 

```python manage.py runserver```
