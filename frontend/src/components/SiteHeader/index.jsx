import { Button, Toolbar } from '@mui/material'

import React from 'react'
import { useHistory } from 'react-router-dom';
import { useStyles } from './styles';

const SiteHeader = () => {
    const classes = useStyles();
    const history = useHistory()

    return (
        <Toolbar variant="dense" className={classes.toolBar}>
            <Button
                className={classes.button}
                variant="outlined"
                size="small"
                onClick={() => history.push(`/`)}
            >Fundamentals</Button>
            <Button
                className={classes.button}
                variant="outlined"
                size="small"
                onClick={() => history.push(`/charts`)}
            >Charts</Button>
        </Toolbar>
    )
}

export default SiteHeader
