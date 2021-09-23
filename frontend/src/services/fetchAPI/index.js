import axios from "axios"

const handleFetchData = async (url, dispatchData) => {
    dispatchData({ type: "DATA_FETCH_INIT" })

    const result = await axios.get(url)

    try {
        setTimeout(() => {
            dispatchData({
                type: "DATA_FETCH_SUCCESS",
                payload: result.data,
            })
        }, 1000)
    } catch {
        dispatchData({ type: "DATA_FETCH_FAILURE" })
    }
}

export default handleFetchData