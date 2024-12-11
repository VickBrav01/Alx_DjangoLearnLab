Creating a socialmedia Api using Django

First install django, then install the required packeges (restframework, JWT, Pillow, Djangi-filters)
Then install User app which will hold the logic for users actions (registration, login) etc
To register, you have to enter your username, password and email ; these are the required fields
Other fields include bio, profile picture, followers. But since we are registering a new user, followers need to be null or empty

When you want to login, you will be given a token which you will use for authorization. This is possible due to restframework-simplejwt
