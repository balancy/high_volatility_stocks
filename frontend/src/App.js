import './App.css';

import { useEffect, useReducer } from 'react';

import { Container } from '@mui/material';
import ResultsOfFetch from './components/ResultsOfFetch';
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
    <Container maxWidth="lg">
      <ResultsOfFetch results={stocksData} />
    </Container>
  );
}

export default App;
