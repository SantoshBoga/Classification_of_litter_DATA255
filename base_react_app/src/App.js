import React, { Component } from "react";

import './App.css';
import { Switch, BrowserRouter as Router } from "react-router-dom";
import Main from './Main'
class App extends Component {
  state = {
    loggedIn: false,
  };


  render() {
    return (
      <div>

        <div className="App">
          <Router>
            <Switch>
              <Main />
            </Switch>
          </Router>

        </div>
      </div>
    );
  }
}

export default App;
