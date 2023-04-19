import React from 'react'
import '../CSS/NavBar2.css';

function NavPage({ user, setUser }){

    function handleLogoutClick() {
        fetch("/logout", { method: "DELETE" }).then((r) => {
          if (r.ok) {
            setUser(null);
          }
        });
      }

    return(
        <body class="chris">
            <nav class="navMenu">
                <a href="/">HomePage</a>
                <a href="/BookList">BookList</a>
                <a href="/AddBook">Add Book</a>
                <a href="/" onClick={handleLogoutClick}>Logout</a>
                <div class="dot"></div>
            </nav>
        </body>
    )
}

export default NavPage;