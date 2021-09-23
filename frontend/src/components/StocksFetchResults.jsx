import React from 'react'

const StocksFetchResults = ({ stocksData }) => {
    return (
        <>
            {stocksData.isError && <p>Something went wrong...</p>}

            {stocksData.isLoading
                ? <p>Data is loading...</p>
                : stocksData.data.map((stockData) => {
                    return (
                        <p key={stockData.ticker}>{stockData.ticker}</p>
                    )
                })
            }
        </>
    )
}

export default StocksFetchResults
