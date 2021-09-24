import './App.css';

import { Route, Switch } from 'react-router';
import { useEffect, useReducer } from 'react';

import { BrowserRouter } from 'react-router-dom';
import { Container } from '@mui/material';
import { STOCKS_URL } from './constants';
import SiteBody from './components/SiteBody';
import SiteHeader from './components/SiteHeader';
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
    <Container align="center">
      <BrowserRouter>
        <SiteHeader />
        <SiteBody content={stocksData} />
      </BrowserRouter>
    </Container>
  );
}

export default App;
