Team37-CodePlayground
=====================


[Project management tool link](https://team37capstone.atlassian.net/jira/software/projects/TEAM/boards/1)


CodePlayground is an online platform for students to create and solve programming exercises in Python.
Link for final report: (https://docs.google.com/document/d/1ILwpUfKEMQNF5twTq_Ow0fjQKBUPlCuFh7RORAHZmyI/edit?usp=sharing)

Technologies used
-----------------

* Python
* Visual Studio Code
* Canva and Adobe XD for prototyping and design
* Vanilla Javascript (HTML, CSS, Javascript) 
* Ace Code Editor
* Github
* Jobe/Jobeserver and restapi 
* Web application framework: Django  Version:3.2.15
* Database: MySQL  Version:5.7.36
* Database development tool: Navicat Premium  Version:15.0.23
* Web Server: Tencent Cloud Server


Installation instructions and setup requirements:
-------------------------------------------------

**Requirements**
* Python 3.7 or higher
* Database: MySQL  Version:5.7.36
* Database development tool: Navicat Premium or other database tools

**pip install list:**

* pip install django==3.2.*
* pip install mysqlclient
* pip install Pillow

main program: codeplayground/manage.py

**Installation instructions to compile the code and run the website onto local machine:**

1. Go to the codeplayground document directory

2. Edit codeplayground\codeplayground\settings.py with IDLE

3. Line 83, configure your own mysql database information, or create a new database named "codeplayground", Character set: utf8, Collation: utf8_general_ci

4. In the directory of manage.py, open cmd

5. Run in a command line window: manage.py makemigrations

6. and then Run in a command line window: manage.py migrate

7. Open codeplayground\codeplayground\database, and import the corresponding data into the database you just created (category must be imported, others may not be imported)

5. Run in a command line window: manage.py runserver 0.0.0.0:8000 (or other ports)

6. Open the browser and enter the URL: http:/localhost:8000 port access




## Use cases and Steps

1. Head to CodePlayground website and sign up to an account, this will take you to the **landing page**
2. Nagivate and choose between the **creation page** to create code or **questions page** to solve code
3. Once you are on the **creation page**, create your own question by writing the title, topic, code description and then input your code to submit. (include hint --> write a descriptive text to explain each line of your code)
4. Solve questions created by your peers on the question page. Select through the questions and work through the programming exercises. There is a code editor to write your code and a hint button to help you solve the question.
5. If you have any queries, click on the discussions page to start a forum on a topic you are interested in
6. Check your profile to see how many questions you have attempted and passed!

Video walkthrough of website usage: (https://drive.google.com/file/d/1aBoB9FLQ7AKSc1avzdg07_exfIIVSl-t/view)

Website URL: (http://www.codeplayground.club/)
Public IP: (http://81.71.47.196/)

Future plan
-----------

* Video tutorial option to explain your programming exercise
* Responsive, mobile first development
* Support multiple languages 
* Badge system for deeper gamification and rewards
* Fluent animation and interactive UI  


Acknowledgements
----------------
Richard Lobb - Jobe

Paul Denny - Project idea

Asma Shakil - Guidance on planning and project build
