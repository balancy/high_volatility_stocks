import { Route, Switch } from 'react-router'

import AllStocksPage from '../pages/AllStocksPage'
import StockPage from '../pages/StockPage'

const AppRouter = () => {
    return (
        <Switch>
            <Route exact path={["/", "/stocks"]}>
                <AllStocksPage variant="table" />
            </Route>
            <Route exact path="/stocks/:ticker">
                <StockPage />
            </Route>
            <Route exact path="/charts">
                <AllStocksPage variant="charts" />
            </Route>
        </Switch>
    )
}

export default AppRouter
