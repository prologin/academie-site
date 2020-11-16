import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTwitter, faFacebook, faLinkedin } from '@fortawesome/free-brands-svg-icons';

const useStyles = makeStyles((theme) => ({
  socialMediaIcon: {
    fontSize: 30,
    margin: 10,
  },
  socialMediaLink: {
    color: 'inherit !important',
  },
}));

const SocialNetworks = () => {
  const classes = useStyles();

  return (
    <div>
      <a
        href="https://www.facebook.com/prologin"
        className={classes.socialMediaLink}
        target="_blank"
        rel="noopener noreferrer"
      >
        <FontAwesomeIcon
          className={classes.socialMediaIcon}
          icon={faFacebook}
        />
      </a>
      <a
        href="https://www.twitter.com/prologin"
        className={classes.socialMediaLink}
        target="_blank"
        rel="noopener noreferrer"
      >
        <FontAwesomeIcon className={classes.socialMediaIcon} icon={faTwitter} />
      </a>
      <a
        href="https://www.linkedin.com/company/prologin/"
        className={classes.socialMediaLink}
        target="_blank"
        rel="noopener noreferrer"
      >
        <FontAwesomeIcon className={classes.socialMediaIcon} icon={faLinkedin} />
      </a>
    </div>
  );
};

export default SocialNetworks;
