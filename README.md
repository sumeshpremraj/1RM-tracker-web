# 1RM+ tracker
This is a simple tracker that takes your AMRAP (As Many Reps As Possible) set numbers from Google Sheets as input and 
generates graphs showing progress of your 1RM over time. 

I wrote this for personal use, so it is a very simple, very early version.

### Features
* No dependence on third party paid apps (many of which are abandoned in time)
* Easy to use, develop and extend
* Can be deployed to Heroku free tier

#### Screenshots
![1RM+ history page](screenshots/screenshot-1.png?raw=true)

#### Setup
```
$ git clone git@github.com:sumeshpremraj/1RM-tracker-web.git
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ brew install heroku/brew/heroku
$ heroku login
$ heroku apps:create --addons=heroku-postgresql:hobby-dev --region=<us/eu> <your name>-onerm-tracker
$ git push heroku master
$ heroku config:set FLASK_APP=tracker.py
$ heroku config:set APP_SETTINGS: config.ProductionConfig
$ heroku run flask db init
$ heroku run python
Running python on ⬢ onerm-tracker... up, run.3636 (Free)
[GCC 7.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import db
>>> db.create_all()
# press Ctrl+D to exit Python interpreter
$ heroku logs -t    # tail logs
$ heroku pg:psql    # open a DB shell
$ heroku ps         # check your dyno usage etc
```

#### TO DO
- [ ] Refactor: Use flask blueprints
- [ ] Use Flask-Migrate
- [ ] Use Google SSO
- [ ] Delete lifts
- [ ] Import/export lifts as CSV
- [ ] Integrate Sentry for error tracking
- [ ] Build SPA with React/Vue
