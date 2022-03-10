# shopSpot

## Introduction

We are making a web application, named ShopSpot, for people with busy routines to have their own personal clothe recommender which recommends according to user’s preferences and interest. The main motivation behind creating this application is to help people struggling with finding their clothes according to their preferences. This application will change the way people find their clothes which suits their taste. Many people understand the importance of dressing up according to their interest and event types. So, they make a lot of effort in finding out clothes they like which suits their taste. Dressing up good is also a part of grooming and clothes are the first thing people note about you. You may say your clothes form your first impression before you even speak. In solution to this problem, we are building a system which not only helps the users to find clothes of their interest but also recommend the suggestions meeting to their taste. Also it recommends products based on the season we are in

## List of features/Functional requirements

- Signup/Login
- Recommend products on the basis of different events
- Search product by image
- Create your wardrobe and add your collection into it.
- Sell your wardrobe collection items as preloved products
- Add any product in Wishlist
- View preloved items and buy them

## Tools and Technologies Used

- Frontend (React)
- Backend (Node.js + Express)
- Database (MongoDb)
- Apache Kafka
- Beautiful Soup (For Scraping data)
- Python (For Deep Learning, Scrapers, Kafka Implementation)
- VS Code
- Spyder
- Jupyter Notebook
- Flask

## Implementation Details and System's Architecture

All the modules and applications work together to provide final useful results. At first the database is updated with the latest data scraped from various clothing brands
i.e. (Gulahmad, J. HSY) and then this data is published into Kafka server. Some data preprocessing and removal of duplicate records is performed at the kafka side. 
In the next stage this data is fetched from kafka servers through consumers and pushed this cleaned data into or mongo database on cloud. Frontend application interact with 
this database through Node Server. User use different features of application and response send back to the client by backend server through Restful API's.

![Kafka Architecture Image](https://github.com/Jilani7/shopSpot/blob/68302fee067b0a6428e18a98c4075b6a73e5e75a/kafka%20Architecture.png)

## How to run this Project?

- First of all clone this repository in your local PC.
- Next make sure that you have set your development environment. it includes Setting up Kafka Server in your machine, installation of Node, python, Tensorflow>=2.0 etc.
- After setting up your environment, create a new database on mongo Atlas and get connection string.
- Add connection string in backend **index-server.js** file and replace connection string with yours. Don't forget to add necessary information in **.env** file.
- Move to ** Search Image** and **Kafka** folder and add database username, password and database name in **offline.py** and **consumer.py** files.
- Then run these files in the order one by one **KafkaHandler.py (Create topics) -> gulahmad_producer.py -> jdot_producer.py -> consumer.py**. At this stage your database will be updated with latest products from these two brands.
- Now move to backend and client root folder and run **npm start** command on separate terminals. Then in Search Image folder run **server.py** file in another terminal window.
- Now all your servers up and running. You can start using this application in your local system.

