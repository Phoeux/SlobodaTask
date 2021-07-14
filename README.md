# Eshop quality reviews

## Deploy

To deploy the project use commands:

### docker-compose build <br> docker-compose up

## Add review

With a link `http://127.0.0.1:8000/review/` you can post a review in a such way: <br>
`{
    "shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/",
    "user": "lana@gmail.com",
    "title": "good shop",
    "description": "some text",
    "rating": 4 
}`
and here you can filter data by fields `user` or `shop_link` in a such way: `http://127.0.0.1:8000/review/?search=lana`
and you will receive all lana's reviews.

## Update review

For an update a review you have to add an ID of a review into URL, as an example:
`http://127.0.0.1:8000/review/1` and then you can update any data of this review by using PUT or PATCH HTTP Methods.
Example of an update data:
`{
"rating": 1 
}`

## Delete review

To delete a review use the same link as for an update by using DELETE HTTP Method.

## Shop list

Using a link like: `http://127.0.0.1:8000/shop/` you can get a shop list and order them by:

1. Domain - ascending/descending    `http://127.0.0.1:8000/shop/?ordering=domain` or `-domain`
2. Reviews - ascending/descending   `http://127.0.0.1:8000/shop/?ordering=reviews` or `-reviews`
3. Rating - ascending/descending    `http://127.0.0.1:8000/shop/?ordering=avg_rate` or `-avg_rate`

## Group by user

Using the link `http://127.0.0.1:8000/group_by_user/` we are getting a list of reviews grouped by user email and ordered
by created time.