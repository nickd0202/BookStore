import React, { useEffect, useState } from "react";
import { Switch, Route, useHistory, useParams } from "react-router-dom";
import NavBar from "./NavBar";
import Login from "./Login";
import Books from "./Books";
import HomePage from './HomePage';
import BookId from './BookId';
import Edit from './Edit.js';
import AddBook from "./AddBook";
import Review from "./Review";
import UserContext from "./User";
import NavPage from "./NavPage";
import Snake from "./Snake";



function App() {
  const { id } = useParams();
  const [user, setUser] = useState(null);
  const [books, setBooks] = useState([]);
  const [deleted, setDeleted] = useState(false);
  const history = useHistory();
  const [reviews, setReviews] = useState([]);


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

      useEffect(() => {
        fetch(`/reviews`)
        .then(res => res.json())
        .then((data) => setReviews(data))
      },[]);

    // function getReview(reviews){
    //     reviews.map((review) => {
    //         if (review.book.id.toString() === id){
    //             return (review.review)
    //         }
    //     })
    // }




  if (!user) return <Login onLogin={setUser} />;

  return (
    <>
    <UserContext.Provider value={user}>
      <main>
        <Switch>

          <Route exact path="/">
            <NavBar />
            <HomePage />
          </Route>

          <Route path="/BookList">
            <NavBar />
            <Books books = {books} />
          </Route>

          <Route path="/books/:id">
            <NavBar />
            <BookId deleteItem={deleteItem}/>
            <Review reviews = {reviews}/>
           </Route>

          <Route path="/edit/:id">
            <NavBar />
            <Edit updateBook = {updateBook} />
          </Route>

          <Route path="/AddBook">
            <NavBar />
            <AddBook />
          </Route>

          <Route path="/Nav">
            <NavPage user={user} setUser={setUser}/>
          </Route>

          <Route path="/EasterEgg">
            <NavBar />
            <Snake />
          </Route>

        </Switch>
      </main>
      </UserContext.Provider>
    </>
  );
}

export default App;
