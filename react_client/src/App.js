
// Filename - App.js
 
// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";
 
function App() {
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
        name: "",
        date: "",
        environment:"",
        port:"",
    });
 
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("/api/data").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    name: data.Name,
                    date: data.Date,
                    environment: data.Environment,
                    port: data.Port
                });
            })
        );
    }, []);
 
    return (
        <div className="App">
            <header className="App-header">
                <p>Name: {data.name}</p>
                <p>Datetime: {data.date}</p>
                <p>API port: {data.port}</p>
                <p>Environment: {data.environment}</p>
            </header>
        </div>
    );
}
 
export default App;
