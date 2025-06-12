Project Title: Iris Flower Classification FastAPI ML API

A machine learning API built with FastAPI that classifies Iris flower species based on sepal and petal measurements. The ML model (GradientBoostingClassifier) is pre-trained and loaded by the API.

List key features:-
  FastAPI for robust API
  Pre-trained scikit-learn model
  Dockerized deployment

How to run locally:
1. Create virtual environment - "python -m venv venv"
2. Activated virtual environment - ".\venv\Scripts\activate"
3. install dependencies - "pip install -r .\requirements.txt"
4. After completed, run uvicorn - "uvicorn app:app --port 5000"
5. Now go to "http://127.0.0.1:5000/docs", your Iris ML API will displayed in the browser

How to run with Docker:
1. Open terminal in the iris_api root directory
2. Build docker image - Run "docker build -t iris-fastapi-app"
3. Run docker container - "docker run -d -p 8000:5000 --name my-iris-container iris-fastapi-app"
4. You can test Containerized API by go to "http://localhost:8000/docs" in your browser
5. Use the "try it out: feature on /v1/iris/predict with your sample JSON data. Example: {"data": [[4.8, 3.1, 4.0, 0.3], [2.1, 3.2, 1.1, 1.5]]}
