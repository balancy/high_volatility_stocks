const backendHost =
    (process.env.REACT_APP_BACKEND_HOST_IP === '0.0.0.0')
        ? 'http://127.0.0.1'
        : process.env.REACT_APP_BACKEND_HOST_IP
const backendPort = process.env.REACT_APP_BACKEND_PORT
const fullBackendIP = `${backendHost}:${backendPort}`

export const stocksUrl = `${fullBackendIP}/stocks/`
export const getChartUrl = (ticker, size) =>
    `https://charts2.finviz.com/chart.ashx?t=${ticker}&ta=1&p=d&s=${size}`

export const getVolatilityMetricsUrl = (ticker) =>
    `${fullBackendIP}/options-overview/${ticker}`