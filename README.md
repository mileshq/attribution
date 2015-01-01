# Attribution App

Simple app to track sales attribution, based on IBB Consulting business rules

Heroku notes - create production environment (example: prod)
$ heroku create attribution-prod
$ git remote add prod mileshq@heroku.com:attribution.git
$ git push prod master
$ heroku config:set APP_SETTINGS=config.ProductionConfig --remote prod