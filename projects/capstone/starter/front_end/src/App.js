import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";

import Home from './pages/Home';
import About from './pages/About';
import Actor from './pages/Actor';
import Movie from './pages/Movie';
import Contact from './pages/Contact';
import './App.css';

function App() {
  // const [setHome] = useState([{}])
  // useEffect(() => {
  //   fetch('/about').then(response => response.json()).then(data => {
  //     setHome(data);
  //   }).catch(error => {
  //     console.log(error)
  //   })

  // }, [])
    return(
    <Router>
      <div>
        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/actors">
            <Actor />
          </Route>
          <Route path="/contact">
            <Contact />
          </Route>
          <Route path="/movies">
            <Movie />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}


export default App;
