import { Router, Route, browserHistory } from 'react-router';
import React from 'react';
import App from '../containers/App';

class Routes extends React.Component {

  constructor(props) {
    super(props);
    this.loginRequired = this.loginRequired.bind(this);
  }

  render() {
    return (
      <Router history={browserHistory}>
        <Route path="/" component={App} />
      </Router>
    );
  }
}

export default Routes;
