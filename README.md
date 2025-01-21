# Twitter Data Analytics Python
Using the Twitter API, we designed a graphical user interface using Tkinter on Python to help analyze tweet performance. This program has a graphing feature (using matplotlib), several sorting features (using pandas), as well as a CSV download option (which will download all the recorded tweets of a specific username).

Sashreek Kalakota(Backend): Worked with the Twitter API and matplotlib to access, sort, and graph the data of each user.

Sharan Subramanian: Used T-kinter and artistic talent to create a visually appealing GUI. Helped connect the backend code with the GUI.


# How to use the program
1. Use the compiled .exe file (on windows)<br/>
   a. Go to releases, and download "TDA-v1.exe"<br/>
   b. Once you double-click on the file, you should be able to launch your program (if you get an error message, you may need to install Visual C++ Redistributable)<br/>
    
2. Compile the main.py file (on mac, linux)<br/>
   a. Make sure ou are running the latest version of python, and it is installed to PATH<br/>
   b. Install the following prerequistes using the pip package installer<br/>
        - pip install tkinter<br/>
        - pip install tweepy<br/>
        - pip install pandas<br/>
        - pip install matplotlib<br/>
   c. Compile & Run the .py file<br/>
        - Windows: open cmd.exe, navigate to the file directory of the downloaded file, type **python main.py**, press enter key<br/>
        - Mac: open terminal, navigate to the file directory of the downloaded file, type **python3 main.py**, press enter key<br/>
        - Linux: open terminal, navigate to the file directory of the downloaded file, type **python3 main.py**, press enter key<br/>

# Info
1. Enter all information (twitter username, sort by likes min and max, sort by retweet min and max, and sort by date min and max) before interacting with the buttons
2. You can interact with the buttons in whichever order, and do not have to activate all of them
3. The "Save Tweets (CSV)" functions saves all the tweets of the given username with a few other identifiers as a CSV file in the parent folder of the program (either .py or .exe)
4. All the functions (graph, find tweets by likes/retweets/date) all open a popup window with the information
5. The Sort by features all have a scroll bar on the side, only accesible by mouse click/drag- not by mouse wheel

# Demo Pictures
![image](https://user-images.githubusercontent.com/69642402/123537428-4563fb80-d6e4-11eb-8f99-9021371466d0.png)
![image](https://user-images.githubusercontent.com/69642402/123537396-0b92f500-d6e4-11eb-8ce5-7912cdea40e6.png)
![image](https://user-images.githubusercontent.com/69642402/123537440-54e34480-d6e4-11eb-94de-4ebc04857029.png)
