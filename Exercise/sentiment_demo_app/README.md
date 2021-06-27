A Sentiment Analyzer Demo
=========

### Deep Learning Model

```bash
cd ./server/models

# download data
sh download.sh

# preprocess text & export cleaned data
python preprocess.py

# train & export model
python train.py
```

### Frontend
```bash
~ npm i

~ npm start

~ npm run build
```


### Backend

```bash
~ cd ./server

# create workspace
~ python3 -m venv venv

# activate workspace
~ source venv/bin/activate

# export dependencies
~ pipreqs server

# install dependencies
~ pip install -r requirements.txt

# run server
~ flask run
```

### Deploy to Heroku

```bash
~ heroku login

```