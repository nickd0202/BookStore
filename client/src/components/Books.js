import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import BookList from "./BookList";
import "../CSS/Books.css"

function Books({books}){

    const bookList = books.map((book) => {
        return (
            <BookList
            key = {book.id}
            id = {book.id}
            name = {book.name}
            author = {book.author}
            publishDate = {book.publishDate}
            genre = {book.genre}
            link = {book.link}
            summary = {book.summary}
            image = {book.image}
            />  
        )
    })



    return(
        <ul className = "books">{bookList}</ul>  
    );
}

export default Books;