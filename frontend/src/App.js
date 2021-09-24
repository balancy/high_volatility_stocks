import './App.css';

import { useEffect, useReducer } from 'react';

import { BrowserRouter } from 'react-router-dom';
import { Container } from '@mui/material';
import SiteBody from './components/SiteBody';
import SiteHeader from './components/SiteHeader';
import dataFetchReducer from './reducers/dataFetch';
import handleFetchData from './services/fetchAPI';
import { stocks_url } from './constants';

const App = () => {
  const [stocksData, dispatchStocksData] = useReducer(
    dataFetchReducer,
    { data: [], isLoading: false, isError: false }
  )

  useEffect(() => {
    handleFetchData(stocks_url, dispatchStocksData)
  }, [])

  return (
    <Container sx={{ width: 1200 }} align="center">
      <BrowserRouter>
        <SiteHeader />
        <SiteBody content={stocksData} />
      </BrowserRouter>
    </Container>
  );
}

export default App;
