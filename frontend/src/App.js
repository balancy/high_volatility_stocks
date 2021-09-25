import AppHeader from './components/AppComponents/AppHeader';
import AppRouter from './routers/AppRouter';
import { BrowserRouter } from 'react-router-dom';
import { Container } from '@mui/material';

const App = () => {
  return (
    <BrowserRouter>
      <Container sx={{ width: 1200 }} align="center">
        <AppHeader />
        <AppRouter />
      </Container>
    </BrowserRouter>
  );
}

export default App;
