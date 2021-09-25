import { CircularProgress, Typography } from '@mui/material'
import { useEffect, useReducer } from 'react'

import VolatilityMetrtics from './VolatilityMetrics'
import dataFetchReducer from '../../reducers/dataFetchReducer'
import { getVolatilityMetricsUrl } from '../../constants/urls'
import handleFetchData from '../../services/fetchApi'

const VolatilityMetricsBlock = ({ ticker }) => {
    const [volatiltyInfo, dispatchVolatilityInfo] = useReducer(
        dataFetchReducer,
        { data: [], isLoading: false, isError: false }
    )

    useEffect(() => {
        const url = getVolatilityMetricsUrl(ticker)
        handleFetchData(url, dispatchVolatilityInfo)
    }, [ticker])

    return (
        <>
            {volatiltyInfo.isError &&
                <Typography variant="subtitle2" align="center">
                    Something went wrong during fetching...
                </Typography>
            }

            {volatiltyInfo.isLoading
                ? <CircularProgress align="center" size="20%" />
                : <VolatilityMetrtics data={volatiltyInfo.data} />
            }
        </>
    )
}

export default VolatilityMetricsBlock
