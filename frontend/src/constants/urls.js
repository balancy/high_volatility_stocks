export const stocksUrl = 'http://127.0.0.1:8000/stocks/'
export const getChartUrl = (ticker, size) =>
    `https://charts2.finviz.com/chart.ashx?t=${ticker}&ta=1&p=d&s=${size}`

export const getVolatilityMetricsUrl = (ticker) =>
    `http://127.0.0.1:8000/options-overview/${ticker}`