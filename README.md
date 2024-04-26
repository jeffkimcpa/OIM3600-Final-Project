**Group: Jeff & Gahyeon**
Project Overview: We wanted to Create a Web-App that would use the Spotify API to create a
playlist that generates a Saved Weekly playlist based on the user's temporary and automatically generated Discover Weekly playlist.

**Project URL: https://oim3600-final-project.onrender.com/**

**1. Project Overview**
We decided to use the Spotify functionality that already created a Discover weekly playlist, but would re-save over the playlist weekly. So our goal was to save the songs that were generated in that playlist so that it would hold your Discover weekly songs and add to them as the weeks went by. We also wanted the playlist to focus on top songs and artists, and because it is continuous we wanted the songs to not be repeated in the playlist should they appear multiple times. We also wanted to use Flask to create a website visual element that allowed you to login, and see whether or not the playlist creation was succesful. 

**2. Usage Guidelines**
The user must be first logged in to spotify, then when they run the code and open the website, they just have to click on the link that says "login with spotify" If they succesfully login they will see a success visual, and can check their account to see the playlist has been made. Ohterwise they will get an error message, asking them to login to their spotify account, or if they have already made the playlist they will get a message that the playlist has already been made. 

**3. Dependencies**
The API We used for this project is the Spotify API, but we also used the spotipy library to make it easier to use the api and access aspects of it in python. We also used flask for our website segment. 

**4. Project Structure**
In making this project, we mainly used the discoverWeekly.py file to handle the bulk of the work. Though it is a simple script it uses the flask framework to interact with the Spotify API. We have made several html templates to deploy on a website, but it still is a working progress that needs a resolution for the redirect uri. We have been trying to solve this issue, but it's been rough. However, after careful error processing and persistence, we made it work!!

**5. Collaboration Information**
We began by having a meeting about what we wanted to accomplish in the project, and then seperated the tasks we needed to complete between the two of us. After outlining our hypothetical code together, we created a shared repository as well as the necessary files we would need. we passed off writing segments of the code, and fixing bugs. Whoever completed more sections of the main code then passed off the html and front end to the other person. 

**6. Acknowledgments**
- Flask
- Spotipy 
- Spotify API 
- SpotifyOAuth
- time

**7. Reflection**
To start with, we initially had the idea to do some sort of board game as an online version, but we quickly ran into barriers in the amount of coding experiance we had as well as the sheer amount of code we would have to write. It just wasn't a project we could accomplish in the time span. So after looking into quite a few APIs we landed on using the spotify api to create some sort of playlist, but we really wanted it personalized in some way to the user. Because spotify already has a few personalized features, we decided to play with their weekly rotating playlists to create somehting more permanent that builds on itslef, and we could actually impliment within someones account. 
We had a few challenges trying to reach the API, so we did some research into other people's use of spotify's api and found Spotipy which ended up helping out with a lot of our more dense code. I think it would have been super helpful to do that sort of research before we even started our project because it would have saved us a lot of time expirementing with the API. 
But, I think even that expirementing helped us learn a lot about how to parse through an API and figure out exactly how to get what you're looking for. I also think this project helped us to understand that it's really important to sturggle sometimes, because our breakthroughs continuiously happened after a day or hours of frustration. 
To be honest, while we used ChatGPT to try to help with some bug fixes, especially in our original project idea and before we used spotipy, it wasn't the most helpful when it came to our code, because of the amount of different html files and APIs we were referencing, but I think we learned how to ask better questions, and use the integrated bug fixer in VS code which was more helpful in the long run. 

 

