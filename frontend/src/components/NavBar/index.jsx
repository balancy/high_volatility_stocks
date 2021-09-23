import { Button, Toolbar } from '@mui/material'

import React from 'react'
import { useStyles } from './styles';

const NavBar = () => {
    const classes = useStyles();
    return (
        <Toolbar variant="dense" className={classes.toolBar}>
            <Button
                className={classes.button}
                variant="outlined"
                size="small"
            >Fundamentals</Button>
            <Button
                className={classes.button}
                variant="outlined"
                size="small"
            >Charts</Button>
        </Toolbar>
    )
}

export default NavBar
