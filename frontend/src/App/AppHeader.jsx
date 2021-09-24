import { AppBar, Button, Toolbar } from '@mui/material'

import OutlinedButton from '../components/UI/buttons/OutlinedButton';
import { useStyles } from './AppHeader.styles';

const AppHeader = () => {
    const styles = useStyles();

    return (
        <AppBar
            position="sticky"
            color="transparent"
            className={styles.appBar}
        >
            <Toolbar variant="dense" className={styles.toolBar}>
                <OutlinedButton path="/" text="Stocks" />
                <OutlinedButton path="/charts" text="Charts" />
            </Toolbar>
        </AppBar>
    )
}

export default AppHeader
