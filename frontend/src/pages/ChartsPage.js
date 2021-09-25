import { Container } from '@mui/material'
import { getChartUrl } from '../constants/urls'
import { useHistory } from 'react-router'
import { useStyles } from './ChartsPage.styles'

const ChartsPage = ({ data }) => {
    const styles = useStyles()
    const history = useHistory()

    return (
        <Container className={styles.container} align="left" >
            {
                data.map((item) =>
                    <button
                        onClick={() => { history.push(`/stocks/${item.ticker}`) }}
                        className={styles.link}
                    >

                        <img
                            className={styles.image}
                            src={getChartUrl(item.ticker, 'm')}
                            alt={item.ticker}
                        />
                    </button>
                )
            }
        </Container>
    )
}

export default ChartsPage
