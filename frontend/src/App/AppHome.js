import { useEffect, useReducer } from 'react';

import AppBody from './AppBody';
import AppHeader from './AppHeader';
import { BrowserRouter } from 'react-router-dom';
import { Container } from '@mui/material';
import dataFetchReducer from '../reducers/dataFetchReducer';
import handleFetchData from '../services/fetchApi';
import { stocks_url } from '../constants/urls';

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
        <AppHeader />
        <AppBody content={stocksData} />
      </BrowserRouter>
    </Container>
  );
}

export default App;
