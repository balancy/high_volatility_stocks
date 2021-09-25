import { useHistory, useParams } from 'react-router'

import { Container } from '@mui/material'
import OutlinedButton from '../components/UI/buttons/OutlinedButton'
import VolatiltityMetricsBlock from '../components/StockPageElements/VolatilityMetricsBlock'
import { getChartUrl } from '../constants/urls'
import { useStyles } from './StockPage.styles'

const StockPage = () => {
    const history = useHistory()
    const { ticker } = useParams()
    const styles = useStyles()

    return (
        <>
            <img
                src={getChartUrl(ticker, 'l')}
                alt={ticker}
                className={styles.main}
            />
            <VolatiltityMetricsBlock ticker={ticker} />
            <Container className={styles.main} align="right">
                <OutlinedButton method={() => history.goBack()} text="Go back" />
            </Container>
        </>
    )
}

export default StockPage
