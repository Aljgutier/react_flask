# React Flask API Example <!-- omit from toc -->

# Contents <!-- omit from toc -->
- [Introduction](#introduction)
- [Backend](#backend)
  - [Create the backend directory](#create-the-backend-directory)
  - [Python Environment](#python-environment)
  - [Backend Server](#backend-server)
- [Frontend](#frontend)
  - [Create the React App](#create-the-react-app)
  - [Proxy](#proxy)
  - [Fetching data from the API](#fetching-data-from-the-api)
- [Run the Application](#run-the-application)
- [References](#references)


# Introduction

Start by creating a "basic" minimally functional API with a "backend" and "frontend" that returns some basic data from the backend.

Second, dockerize the basic application and serve it on Google Cloud.

Next, add functionality to our API, such as querying Big Query, and some ML functionality.

Git releases will be published along the way to enable picking up the functionality as it is developed. 

# Backend

## Create the backend directory

```sh
$ mkdir backend
$ cd backend
```

## Python Environment
In the top directory create the python hvirtual environment and package.json


```sh
$ python -m venv venv
$ source venv/bin/activate
$ pip install flask
```

## Backend Server

To get started setup the Flask backend. 
* https://*www.geeksforgeeks.org/how-to-connect-reactjs-with-flask-api/

```python
# Import flask and datetime module for showing date and time
from flask import Flask
import datetime
 
x = datetime.datetime.now()
 
# Initializing flask app
app = Flask(__name__)
 
 
# Route for seeing a data
@app.route('/data')
def get_time():
 
    # Returning an api for showing in  reactjs
    return {
        'Name':"Alpha Beta", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }
 
# Running app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

Note the server at port 5001 since my MAC uses port 5000 for Airplay. The default port is 5000. Exclude the "port=5001" to default to 5000, or just change the port to 5000 instead of 5001. 



# Frontend

At the top level above backend and frontend directories create the react app. You must have previously installed npm, node, and react.

## Create the React App

```sh
$ npx create-react-app frontend
```

cd to frontend directory

```sh
$ cd ./frontend
```


## Proxy
Add a proxy to `package.json` which sets the port that the frontend hits to make backend requests. The frontend sits at port 3000 (by default) and will be directed to the port indicated in the proxy for backend requests. Change the port in the proxy line to 5000 if you leave the backend above at the default port of 5000.

Put the following line into the `package.json`

```js
"proxy":"http://localhost:5001/"
```

package.json
```js
{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "proxy":"http://localhost:5001/",
...
}
```

## Fetching data from the API

* `useState` - for setting data from the API and providing it to JSX for rendering.
* `useEffect` - for calling the fetch method on a single reload.


App.js
```js

// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";
 
function App() {
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
        name: "",
        age: 0,
        date: "",
        programming: "",
    });
 
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("/data").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    name: data.Name,
                    age: data.Age,
                    date: data.Date,
                    programming: data.programming,
                });
            })
        );
    }, []);
 
    return (
        <div className="App">
            <header className="App-header">
                <h1>React and flask</h1>
                {/* Calling a data from setdata for showing */}
                <p>{data.name}</p>
                <p>{data.age}</p>
                <p>{data.date}</p>
                <p>{data.programming}</p>
 
            </header>
        </div>
    );
}
 
export default App;
```

# Run the Application

In the backend directory
* make sure the python environment is started (`source venv/bin/activate`)
* run `python server.py` in a terminal window.

In a different terminal window, in the frontend directory run `npm start`

In a browser go to http://localhost:3000 and you should see the following

![Basic React Flask API](./images/basic_react_flask_api.png)
  

# References 
* Geek for Geeks, Connect React JS with Flask, https://www.geeksforgeeks.org/how-to-connect-reactjs-with-flask-api/

