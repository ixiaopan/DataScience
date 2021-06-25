A Sentiment Analyzer Demo
=========


## Install 


### Frontend
```
~ npm i

~ npm start

~ npm run build
```


### Server

```
~ cd ./server

# create workspace
~ python3 -m venv venv

# activate workspace
~ source venv/bin/activate

# install dependencies
~ pip install -r requirements.txt

# run blog
~ export FLASK_APP='flasky.py'
~ flask run

# run test api
# http://127.0.0.1:5000/api/v1/todos/
~ export FLASK_APP='flasky-api.py'
~ flask run
```

