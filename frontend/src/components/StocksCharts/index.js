import { Container } from '@mui/material'
import React from 'react'
import { useStyles } from './styles'

const getLink = (ticker) => `https://charts2.finviz.com/chart.ashx?t=${ticker}&ta=1&p=d&s=m`


const StocksCharts = ({ data }) => {
    const styles = useStyles()
    return (
        <Container className={styles.container} align="left" >
            {
                data.map((item) =>
                    <img
                        className={styles.image}
                        src={getLink(item.ticker)}
                        alt={item.ticker}
                    />
                )
            }
        </Container>
    )
}

export default StocksCharts
