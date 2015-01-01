## Attribution App

Simple app to track sales attribution, based on IBB Consulting business rules

Heroku notes - create production environment

Create a new heroku environment called "attribution-prod"
```$ heroku create attribution-prod```

Add the new environment as a git remote for pushing code to
"heroku-prod" is the remote alias, "attribution-prod" is the Heroku git repository (same as just created)
```$ git remote add heroku-prod mileshq@heroku.com:attribution-prod.git```

Push latest git commits to remote Heroku git
```$ git push heroku-prod master```

Set environment variables on Heroku environment
```$ heroku config:set APP_SETTINGS=config.ProductionConfig --remote prod```