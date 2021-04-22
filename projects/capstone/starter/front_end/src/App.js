import React, { useEffect, useState } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useHistory
} from "react-router-dom";

import Home from './pages/Home';
import About from './pages/About';
import Actor from './pages/Actor';
import Movie from './pages/Movie';
import Contact from './pages/Contact';
import './App.css';

function App() {
  let userSession;
  const history = useHistory();
  const [actors, setActors] = useState([]);
  const [recent_movies, setRecentMovies] = useState([]);
  const [upcoming_movies, setUpcomingMovies] = useState([]);

  useEffect(() => {
    let params = new URLSearchParams(window.location.search);
    const auth_code = params.get('code');
    if (auth_code && auth_code.length > 0) {
      fetchTokens(auth_code).then(res => {
        console.log(res);
        if (!res.error) {
          userSession = res;
          window.sessionStorage.setItem('userSession', JSON.stringify(res));
          initData();
        }
      });
    } else {
      userSession = JSON.parse(window.sessionStorage.getItem('userSession'));
      console.log(userSession);
      if (!userSession) {
        redirectToLogin();
      } else {
        initData();
      }
    }
  }, []);

  const initData = () => {
    updateActors().then(res => {
      console.log('Received response from Actors API');
      console.log(res);
      setActors(res.actors);
    }).catch(err => {
      handleError(err);
    });

    updateMovies().then(res => {
      console.log('Received response from Movies API');
      console.log(res);
      setRecentMovies(res.recent_movies);
      setUpcomingMovies(res.upcoming_movies);
    }).catch(err => {
      handleError(err);
    });
  }

  const updateActors = async () => {
    const res = await fetch('/actors', {
      method: 'GET', headers: {
        'Authorization': 'Bearer ' + userSession.access_token
      }
    });

    return await res.json();
  }

  const updateMovies = async () => {
    const res = await fetch('/movies', {
      method: 'GET', headers: {
        'Authorization': 'Bearer ' + userSession.access_token
      }
    });
    return await res.json();
  }

  const fetchTokens = async (auth_code) => {
    const data = {
      'grant_type': 'authorization_code',
      'client_id': 'EvGd8yIZKVFlmei0qvwWWGntcHp9kpn7',
      'client_secret': 'jC905OeKFFgTOCas_nxrjMH5rkGcFo9P1IDBlrnKAsDsdQH2PiJE6fuYSMkXJ2Or',
      'code': auth_code,
      'redirect_uri': 'http://localhost:3000/authorize'
    };

    let finalRequestData = [];
    for (let property in data) {
      let encodedKey = encodeURIComponent(property);
      let encodedValue = encodeURIComponent(data[property]);
      finalRequestData.push(encodedKey + "=" + encodedValue);
    }
    finalRequestData = finalRequestData.join("&");
    const response = await fetch('https://starinmaking.us.auth0.com/oauth/token', {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: finalRequestData // body data type must match "Content-Type" header
    });
    return await response.json();
  }

  const redirectToLogin = () => {
    window.location.href = "https://starinmaking.us.auth0.com/authorize?response_type=code&client_id=EvGd8yIZKVFlmei0qvwWWGntcHp9kpn7&redirect_uri=http://localhost:3000&scope=openid%20profile&audience=http://localhost:5000&state=alpha1993";
  }

  const handleError = (err) => {
    console.error(err);
    if (err.error === 401) {
      redirectToLogin();
    }
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
          <Route path="/" component={Home} />
        </Switch>
      </div>
    </Router>
  );
}


export default App;
