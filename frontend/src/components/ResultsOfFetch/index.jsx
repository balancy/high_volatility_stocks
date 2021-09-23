import { CircularProgress, Typography } from '@mui/material'

import React from 'react'
import StocksList from './StocksList'

const ResultsOfFetch = ({ results }) => {
    return (
        <div>
            {results.isError &&
                <Typography variant="subtitle2" align="center">
                    Something went wrong during fetching...
                </Typography>
            }

            {results.isLoading
                ? <CircularProgress align="center" size="20%" />
                : <StocksList data={results.data} />
            }
        </div>
    )
}

export default ResultsOfFetch
