import { CircularProgress, Typography } from '@mui/material'

import List from './List'
import React from 'react'

const FetchResults = ({ fetchResults }) => {
    return (
        <>
            {fetchResults.isError &&
                <Typography variant="subtitle2" align="center">
                    Something went wrong during fetching...
                </Typography>
            }

            {fetchResults.isLoading
                ? <CircularProgress align="center" />
                : <List data={fetchResults.data} />
            }
        </>
    )
}

export default FetchResults
