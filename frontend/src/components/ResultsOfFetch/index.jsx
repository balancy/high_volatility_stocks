import { CircularProgress, Typography } from '@mui/material'

import React from 'react'
import StocksList from './StocksList'

const ResultsOfFetch = ({ results }) => {
    return (
        <>
            {results.isError &&
                <Typography variant="subtitle2" align="center">
                    Something went wrong during fetching...
                </Typography>
            }

            {results.isLoading
                ? <CircularProgress align="center" />
                : <StocksList data={results.data} />
            }
        </>
    )
}

export default ResultsOfFetch
