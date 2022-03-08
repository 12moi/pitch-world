# pitch-world
### Author
Moi Shadrack

## Description
This is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application



### User Story
1. Comment on the different pitches posted py other uses.<br>
2. See the pitches posted by other uses.<br>
3. Vote on s pitch they have viwed by giving it a upvote or a downvote.<br>
4. Register to be allowed to log in to the application<br>
5. View pitches from the different categories.<br>
6. Submit a pitch to a specific category of their choice.

### BDD
Behaviour                 |   Input                              |Output
-------------------------------------------------------------------------------
Load the page             | On page load                         | Get all post, select between sign up and login
-------------------------------------------------------------------------------
Select signup             |Email,username,password               |redirect to login
-------------------------------------------------------------------------------


### Development Installation
To get the code.. <br>

1. Cloning the repository:<br>
https://github.com/12moi/pitch-world.git<br>

2. Move to the folder and install requirements <br>
cd  pitch-world<br>
pip install -r requirements.txt <br>

3. Exporting Configurations <br>
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

4. Running the application
python3.8 manage.py server
Testing the application
python3.8 manage.py test


### Technology used
Python3.8<br>
Flask<br>
Heroku

### Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug
Contact Information
If you have any question or contributions, please email me at [moi.shadrack@student.moiringaschool@gmail.com]


### Contact Information
If you have any question or contributions, please email me at [moi.shadrack@student.moiringaschoolgmail.com]


 ### License
MIT License:
Copyright (c) 2022 Moi Shadrack