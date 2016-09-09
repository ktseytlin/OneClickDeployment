import React from 'react';
import AppBar from 'material-ui/AppBar';
import IconButton from 'material-ui/IconButton';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import { cyan500 } from 'material-ui/styles/colors';
import AppIcon from 'material-ui/svg-icons/hardware/mouse';

const muiTheme = getMuiTheme({
  palette: {
    textColor: cyan500,
  },
  appBar: {
    height: 50,
  },
});

const NavBar = () => (
  <div>
    <MuiThemeProvider muiTheme={muiTheme}>
      <AppBar
        title="One Click Deployment"
        iconElementLeft={<IconButton><AppIcon /></IconButton>}
      />
    </MuiThemeProvider>
  </div>
);

export default NavBar;
