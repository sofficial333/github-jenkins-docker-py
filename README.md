# github-jenkins-docker-py
Simple Python Flask application for practicing:

- GitHub
- Jenkins
- Docker
- Docker Hub
- CI/CD

## Run locally

Install dependencies:

pip install -r requirements.txt

Run application:

python app.py

Open:

http://localhost:5000

## Run with Docker

Build image:

docker build -t python-jenkins-demo .

Run container:

docker run -p 5000:5000 python-jenkins-demo

Open:

http://localhost:5000
