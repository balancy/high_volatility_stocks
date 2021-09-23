import axios from "axios"

const URL = 'http://127.0.0.1:8000/stocks/'

const handleFetchStocksData = async (dispatchStocksData) => {
    dispatchStocksData({ type: "DATA_FETCH_INIT" })

    const result = await axios.get(URL)

    try {
        dispatchStocksData({
            type: "DATA_FETCH_SUCCESS",
            payload: result.data,
        })
    } catch {
        dispatchStocksData({ type: "DATA_FETCH_FAILURE" })
    }
}

export default handleFetchStocksData