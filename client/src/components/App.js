import React, { useEffect, useState, createContext } from "react";
import { Switch, Route, useHistory } from "react-router-dom";
import NavBar from "./NavBar";
import Login from "./Login";
import Books from "./Books";
import HomePage from './HomePage';
import BookId from './BookId';
import Edit from './Edit.js';

function App() {
  const [user, setUser] = useState(null);
  const [books, setBooks] = useState([]);
  const [deleted, setDeleted] = useState(false);
  const history = useHistory();

  const UserContext = createContext()

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
  },[deleted]);

  function updateBook(updatedBook) {
    const updatedBooks = books.map(ogBook => {
        if (ogBook.id === updatedBook.id)
            return updatedBook
        else
            return ogBook;
    })
    setBooks(updatedBooks)
  }

function deleteItem(id){
    fetch(`/books/${id}`, { 
      method: 'DELETE' ,
      headers: { 'Content-Type': 'application/json'},
    })
    .then(() => setDeleted(!deleted))
    .then(() => history.push('/BookList'))
  }




  if (!user) return <Login onLogin={setUser} />;

  return (
    <>
      <NavBar user={user} setUser={setUser} />
      <main>
        <UserContext.Provider value={deleteItem}>
          <Switch>

            <Route exact path="/">
              <HomePage />
            </Route>

            <Route path="/BookList">
              <Books books = {books} />
            </Route>

            <Route path="/books/:id">
              <BookId delete={deleteItem}/>
            </Route>

            <Route path="/edit/:id">
              <Edit updateBook = {updateBook} />
            </Route>

          </Switch>
        </UserContext.Provider>
      </main>
    </>
  );
}

export default App;
