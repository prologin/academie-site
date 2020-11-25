import React from 'react';

import { ThemeProvider } from '@material-ui/core';
import IconButton from '@material-ui/core/IconButton';
import KeyboardArrowDownIcon from '@material-ui/icons/KeyboardArrowDown';
import PersonIcon from '@material-ui/icons/Person';

import Dropdown from './Dropdown';
import { fetchMyProfile, useTracked } from '../config/store';
import { getMuiThemeConfig } from '../config/theming';
import {
  LOGIN_URL,
  LOGOUT_URL,
  ADMIN_URL,
  BROWSABLE_API_URL,
  SWAGGER_URL,
} from '../api/constants';

function UserMenu() {
  const mounted = React.useRef(false);
  const [state, dispatch] = useTracked();
  const { darkTheme, profile } = state;
  const redirectTo = (url, next = false) => {
    window.location.replace(
      url + (next ? `?next=${window.location.href}` : ''),
    );
  };

  React.useEffect(() => {
    const onComponentMount = () => {
      dispatch(fetchMyProfile());
      mounted.current = true;
    };
    if (!mounted.current) onComponentMount();
  });

  const menu = React.useMemo(() => {
    if (profile == null) {
      return [];
    }
    let res = profile.is_staff
      ? [
          { content: 'Django Admin', onClick: () => redirectTo(ADMIN_URL) },
          {
            content: 'API Browser',
            onClick: () => redirectTo(BROWSABLE_API_URL),
          },
          { content: 'API Swagger', onClick: () => redirectTo(SWAGGER_URL) },
        ]
      : [];
    res.push({ content: 'Déconnexion', onClick: () => redirectTo(LOGOUT_URL) });
    return res;
  }, [profile]);

  return (profile != null ? (
        <ThemeProvider theme={getMuiThemeConfig(darkTheme)}>
          <Dropdown
            items={menu}
            title={profile.username}
            variant="contained"
            buttonProps={{
              endIcon: <KeyboardArrowDownIcon />,
              startIcon: <PersonIcon />,
            }}
          />
        </ThemeProvider>
      ) : (
        <IconButton onClick={() => redirectTo(LOGIN_URL, true)}>
          <PersonIcon />
        </IconButton>
      ));
}

export default UserMenu;
