# python_pg

## How to run Flask server

You can run the flask server from <project> root directory. First of all you need to setup environment variable and then simply run <flask run> command. Flask server should be up and running. For any reason if you close the terminal window, flask server will be shutdown and you won't be able to access the application.      
### Commands to Run Flask Apps

```
kaiseralam@MacBook-Pro api % pwd
/Users/kaiseralam/python_pg/api
kaiseralam@MacBook-Pro api % export FLASK_APP=app.py
kaiseralam@MacBook-Pro api % flask run              
 * Serving Flask app "app"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now that your flask app is running, you can access the app from browser or Postman. Just follow the steps below, you should be able to make GET call to the app.

```
Option 1: from another terminal window, you can run the below cURL command.
    $curl --location --request GET 'localhost:5000/friends'

Option 2: from Postman, run GET call
    localhost:5000/friends

Option 3: from browser, access the below url
    http://localhost:5000/friends
```