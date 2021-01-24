# AndreStockTakeCommercial

This project was developed to function as an in-house product manage tool. The project was developed in the Django Framework.

## Functionallity


* Two levels of user autheniction using decorator functions
  * An admin user who has all rights & permissions to the backend and Django/admin
  * A customer, that is classified as a registered user
* Database functions
  * Creating and updating user profiles
  * Ordering, updating and products
  * Delete and updating exisiting orders
  * Filter orders with respect to datafields


## Deployment 

- Deploy your git repository via the the heroku CLI. Here is a link : https://devcenter.heroku.com/articles/git

## Suggestions

- I am currently having issues with loading my static files directly on heroku dude to pipeline configuration( when Heroku decides to load what).
- I am going to load my files to aws and call them from there. Expect this update shortly.
- Integration with PostgreSQL seems to be straight forward with Heroku and thus i will be moving my local data into PostgresQL.
