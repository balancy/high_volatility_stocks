import { Container } from '@mui/material'
import { getChartUrl } from '../constants/urls'
import { useStyles } from './ChartsPage.styles'

const ChartsPage = ({ data }) => {
    const styles = useStyles()

    return (
        <Container className={styles.container} align="left" >
            {
                data.map((item) =>
                    <img
                        className={styles.image}
                        src={getChartUrl(item.ticker)}
                        alt={item.ticker}
                    />
                )
            }
        </Container>
    )
}

export default ChartsPage
