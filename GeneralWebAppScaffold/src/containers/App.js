import React from 'react';
import AppBar from 'material-ui/AppBar';
import IconButton from 'material-ui/IconButton';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import { cyan500 } from 'material-ui/styles/colors';
import AppIcon from 'material-ui/svg-icons/hardware/mouse';

/* TODO: Put in slider that goes through gifs
 npm install react-gif v0.1.0
 npm install slick-carousel v1.6.0 */

const muiTheme = getMuiTheme({
  palette: {
    textColor: cyan500,
  },
  appBar: {
    height: 50,
  },
});

const App = () => (
  <MuiThemeProvider muiTheme={muiTheme}>
    <AppBar
      title="One Click Deployment"
      iconElementLeft={<IconButton><AppIcon /></IconButton>}
    />
  </MuiThemeProvider>
);

export default App;
