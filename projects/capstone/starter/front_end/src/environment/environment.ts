export const environment = {
    production: false,
    apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
    auth0: {
      url: 'starinmaking.us.auth0.com', // the auth0 domain prefix
      audience: 'http://localhost:5000', // the audience set for the auth0 app
      clientId: 'EvGd8yIZKVFlmei0qvwWWGntcHp9kpn7', // the client id generated for the auth0 app
      callbackURL: 'http://localhost:3000', // the base url of the running react application. 
    }
  };
  