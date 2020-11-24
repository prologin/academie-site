import React from 'react';
import userApi from '../api/userApi';
import {LOGIN_URL, LOGOUT_URL, ADMIN_URL, BROWSABLE_API_URL, SWAGGER_URL } from '../api/constants';
import IconButton from '@material-ui/core/IconButton';
import PersonIcon from '@material-ui/icons/Person';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';

const redirectTo = (url, next = false) => {window.location.href = url + (next ? `?next=${window.location.href}` : '')};

function AdminMenuItems({ is_staff }) {
    const toAdmin = () => redirectTo(ADMIN_URL);    
    const toBrowsableApi = () => redirectTo(BROWSABLE_API_URL);
    const toSwagger = () => redirectTo(SWAGGER_URL)
    return ( is_staff ? [
        <MenuItem key={1} onClick={toAdmin}>Django Admin</MenuItem>,
        <MenuItem key={2} onClick={toBrowsableApi}>API Browser</MenuItem>,
        <MenuItem key={3} onClick={toSwagger}>API Swagger</MenuItem>,
    ] : [])
}

function UserMenu() {
    const [anchor, setAnchor] = React.useState(false);
    const [profile, setProfile] = React.useState(null);
    React.useEffect(() => {
        if (profile != null) { return; }
        userApi.getMyProfile()
            .then(profile => setProfile(profile))
            .catch(() => setProfile(false));
    })

    const handleOpen = (event) => { setAnchor(event.currentTarget); };
    const handleClose = () => { setAnchor(null); };
    const [toLogin, toLogout] = [() => redirectTo(LOGIN_URL, true), () => redirectTo(LOGOUT_URL)]

    return (
        <div>
            <IconButton onClick={handleOpen}><PersonIcon /></IconButton>
            { anchor != null && 
            <Menu
                open={Boolean(anchor)}
                anchorEl={anchor}
                keepMounted
                onClose={handleClose}
                anchorOrigin={{
                    vertical: 'bottom',
                    horizontal: 'center',
                }}
                transformOrigin={{
                    vertical: 'top',
                    horizontal: 'right',
                }}
            >
                { profile ? 
                    ([<MenuItem key={0} onClick={handleClose}>{profile.username}</MenuItem>,
                    <AdminMenuItems key={1} is_staff={profile.is_staff} />,
                    <MenuItem key={1000} onClick={toLogout}>Déconnexion</MenuItem>
                    ])
                    : (<MenuItem onClick={toLogin}>Connexion</MenuItem>)
                }
            </Menu> }
        </div>
    )
}

export default UserMenu;