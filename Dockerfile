FROM python:3.8-slim-buster
WORKDIR /.
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "flask", "--app" , "new_flask_app.py", "run", "--host=0.0.0.0"]