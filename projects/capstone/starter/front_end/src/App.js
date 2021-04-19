import React, { useEffect, useState } from "react";
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
  const [actors, setActors] = useState([]);
  const [recent_movies, setRecentMovies] = useState([]);
  const [upcoming_movies, setUpcomingMovies] = useState([]);

  useEffect(() => {
    updateActors();
    updateRecentMovies();
    updateUpcomingMovies();
  }, []);

  const updateActors = async () => {
    const res = await fetch('/actors');
    const data = await res.json();
    console.log('Received response from API');
    console.log(data);
    setActors(data.actors);
  }

  const updateRecentMovies = async () => {
    const res = await fetch('/movies');
    const data = await res.json();
    console.log('Received response from API');
    console.log(data);
    setRecentMovies(data.recent_movies);
  }

  const updateUpcomingMovies = async () => {
    const res = await fetch('/movies');
    const data = await res.json();
    console.log('Received response from API');
    console.log(data);
    setUpcomingMovies(data.upcoming_movies);
  }


  return (
    <Router>
      <div>
        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/actors">
            <Actor actors={actors} />
          </Route>
          <Route path="/contact">
            <Contact />
          </Route>
          <Route path="/movies">
            <Movie recent_movies={recent_movies} 
            upcoming_movies={upcoming_movies} />
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
