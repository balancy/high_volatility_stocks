import './App.css';

import { useEffect, useReducer } from 'react';

import StocksFetchResults from './components/StocksFetchResults';
import dataFetchReducer from './reducers/dataFetch';
import handleFetchStocksData from './API/fetchStocksData';

const App = () => {
  const [stocksData, dispatchStocksData] = useReducer(
    dataFetchReducer,
    { data: [], isLoading: false, isError: false }
  )

  useEffect(() => {
    handleFetchStocksData(dispatchStocksData)
  }, [])

  return (
    <div>
      <h1>App</h1>

      <hr />
      <StocksFetchResults stocksData={stocksData} />
    </div>
  );
}

export default App;
