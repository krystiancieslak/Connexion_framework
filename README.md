# Connexion_framework
This repository is an exercise for connexion framework
To run it type ``` bash flask_new_app_script.sh ```
To enter entrypoint type ``` http://localhost:[PORT]/v1.0/[name_of_entrypoint] ``` in your browser
To add new book use this request template in Terminal ```curl -X POST "http://localhost:5001/v1.0/books" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"title\": \"title of the book\", \"name\": \"author's name\", \"surname\": \"author's surname\"}"```
