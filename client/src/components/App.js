import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import NavBar from "./NavBar";
import Login from "./Login";
import Books from "./Books";

function App() {
  const [user, setUser] = useState(null);
  const [books, setBooks] = useState([])

  useEffect(() => {
    // auto-login
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      }
    });
  }, []);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/books")
    .then(res => res.json())
    .then((data) => setBooks(data))
  },[]);






  if (!user) return <Login onLogin={setUser} />;

  return (
    <>
      <NavBar user={user} setUser={setUser} />
      <main>
        <Switch>
          <Route exact path="/">
            
          </Route>
          <Route path="/BookList">
            <Books books = {books} />
          </Route>
        </Switch>
      </main>
    </>
  );
}

export default App;
