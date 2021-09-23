import './App.css';

import { useEffect, useReducer } from 'react';

import Button from '@mui/material/Button';
import FetchResults from './components/FetchResults';
import { STOCKS_URL } from './constants';
import dataFetchReducer from './reducers/dataFetch';
import handleFetchData from './services/fetchAPI';

const App = () => {
  const [stocksData, dispatchStocksData] = useReducer(
    dataFetchReducer,
    { data: [], isLoading: false, isError: false }
  )

  useEffect(() => {
    handleFetchData(STOCKS_URL, dispatchStocksData)
  }, [])

  return (
    <div>
      <h1>App</h1>
      <Button variant="contained">Hello World</Button>

      <hr />
      <FetchResults fetchResults={stocksData} />
    </div>
  );
}

export default App;
