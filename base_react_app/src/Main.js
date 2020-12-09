import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import FirstAttempt from './Components/Home/FirstAttempt';

class Main extends Component {
    state = {}
    render() {
        return (
            <BrowserRouter>
                <Route exact='/' component={FirstAttempt} />

            </BrowserRouter>
        );
    }
}

export default Main;