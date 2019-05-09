import React from 'react';
import { Switch, Route } from 'react-router-dom';

import Home from './components/Home';
import Login from './components/Login';

const Routes = (props) => {
  
  return (
    <div className="app-routes">
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path={"/login"} component={Login} />
      </Switch>
    </div>
  )
};

export default Routes;