# Eshop quality reviews

## Deploy

To deploy the project use commands: <br>
###docker-compose build <br> docker-compose up

## Add review

You can post a review in a such way: <br>
`{
"shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/", 
"user": "lana@gmail.com", 
"title": "good shop",
"description": "some text",
"rating": 4 
}`

## Update or Delete review

For an update or delete a review you have to add an ID of a review into URL, as an example:
`http://127.0.0.1:8000/review/1` and then you can update any data of this review or delete it.

## Shop list

Using a link like: `http://127.0.0.1:8000/shop/` you can get a shop list and order them by:
1. Domain - ascending/descending
2. Reviews - ascending/descending
3. Rating - ascending/descending

## Group by user

Using a link `http://127.0.0.1:8000/group_by_user/` we are getting a list of reviews grouped by user email and ordered by created time