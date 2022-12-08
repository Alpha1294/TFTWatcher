# TFT Watcher

### https://youtu.be/EfB8R9E7EkM

### Description
This project is a web page application where i used mainly python but also the help of the html ,css(bootsrap),a couple of javascript functions and jinja and flask to link everything togheter and make the page run.

In my website folder i have the most important parts of the app,starting with __init.py__ wich is usefull to make all that folder to be like a "package" so i can import code i need.
What we got first is the static folder,where i have my css file and the javascript file with very little code since i used bootstrap to make the web prettier and i have a javascript method for the delete note function.

Next i have templates folder where i have all the templates of the web page,i first made a "base" template which is called base.html ,there i have my bootstrap link and how i want my others template to be using the jinja code.All the other templates are using this base to be much easy to do,they have slight differences but goes on the same base.
I have the edit_note file which is onyl for editing the notes, the authentications files for the account management and the tft file for the TFT Watcher feature.

Next we go with the auth.py file ,here we have all the related with the account creation ,login ,log out .I used the werkzeug security package for the password i linked the html files with flaskto the methods that i will create for them

Speaking a bit more about the init.py file,i also created there my database with sqlAlchemy wich comes from flask ,its a very light database but is good enough for such a little project ,it doesnt use sql syntax if u dont want so its pretty attractive.In here i also "linked" the html routes with Blue print so i can acces them easier.

In Models is where i actually give shape to the database , is pretty straight forward i have 2 tables ,one for the accounts and one for the notes.

Views is for the pages that are not related to the authentication and some methods like the delete one. What gave me the most work is the tft page / method.
I had to connect to the riot api using a wrapper called Riot Watcher ,it uses a key that expires every 24h and then u can connect and retrieve all the data you want.
What was really really dificult in here was dealing with how the data arrived to me,in a dictionary which seems simple at first,but that dictionary is full of others dictionaries wich have more dictionaries or lists and so on .

When i finnaly get in how to select the data i  wanted i also had some hard times "parsing" that data into my html file using the jinja code and some loops.
So to wrap up i tried to make a dictionary ,i read that  big companies have big dictionaries to make stuff like "TFT8_name_" be like "name" ,and i gave up mainly of 2 reasons,the time i got for the final day to send the project and the fact that for what i heard i should make all that dictionary split into objects and would be "easier" to deal with it once you have it.Since i didnt had the time to do it ,i tried it during a few days and gave up.

It has been an experience and i learned SO MUCH during this project,the feeling was "i never know how to do something,but still, i learn so much everyday".I gues is what i will find for the rest of my carrer and im happy about it,i like problem solving and i like challenges,otherwise its get boring fast :)