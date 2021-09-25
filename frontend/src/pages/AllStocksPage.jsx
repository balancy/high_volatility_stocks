import { CircularProgress, Typography } from "@mui/material"
import { useEffect, useReducer } from "react"

import ChartsPage from "./ChartsPage"
import StocksTablePage from "./StocksTablePage"
import dataFetchReducer from "../reducers/dataFetchReducer"
import handleFetchData from "../services/fetchApi"
import { stocksUrl } from "../constants/urls"

const AllStocksPage = ({ variant }) => {
    const [stocksData, dispatchStocksData] = useReducer(
        dataFetchReducer,
        { data: [], isLoading: false, isError: false }
    )

    useEffect(() => {
        handleFetchData(stocksUrl, dispatchStocksData)
    }, [])

    return (
        <>
            {stocksData.isError &&
                <Typography variant="subtitle2" align="center">
                    Something went wrong during fetching...
                </Typography>
            }

            {stocksData.isLoading
                ? <CircularProgress align="center" size="20%" />
                : variant === "charts"
                    ? <ChartsPage data={stocksData.data} />
                    : <StocksTablePage data={stocksData.data} />
            }
        </>
    )
}

export default AllStocksPage
