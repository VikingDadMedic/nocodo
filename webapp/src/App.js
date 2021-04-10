import { BrowserRouter, Switch, Route } from "react-router-dom";

import Admin from "screens/Admin";
import Content from "screens/Content";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/nocodo">
          <Admin />
        </Route>

        <Route path="/">
          <Content />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
