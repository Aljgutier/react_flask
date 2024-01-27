

# References 
* https://www.geeksforgeeks.org/how-to-connect-reactjs-with-flask-api/

* https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9



# Backend

Not, we are placing the server at port 5001 since the MAC uses port 5000 for Airplay server

In the top end create the virtual environment and package.json

```sh
$ python -m venv venv
$ source venv/bin/activate
$ pip install flask
```

```sh
$ mkdir backend
$ cd backend
```

server.py as exemplified in Geeks for Geeks 
* https://*www.geeksforgeeks.org/how-to-connect-reactjs-with-flask-api/
* change the port to 5001. https://www.geeksforgeeks.org/how-to-change-port-in-flask-app/
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
        'Name':"geek", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }
 
     
# Running app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
```


# Frontend

At the top level (above backend and frontend directories). when we request into the javascript web server which serves the react frontend will automatically be redirected to the proxy key. In this case, it will be our flask server. 


```sh
$ npx create-react-app frontend
```

cd to frontend directory

```sh
$ cd ./frontend
```

Add a proxy to `package.json`

```js
"proxy":"http://localhost:5001/"
```


# Fetching the API

* `useState` - for setting  data from the API and providing into the jsx for showing the data.
* `useEffect` - for rendering a fetch method on a single reload.


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

* python server.py in a terminal window in the backend directory

```
$ python server.py
```
* in another terminal window in the frontend directory
  
```sh
$ npm start
```