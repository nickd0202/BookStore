import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom"


function BookList({id,name,author,publishDate,genre,link,summary,image}){

    const linkStyle= { 
        textDecoration: "none"
    }




    return(
        <div className = "BookId">
            <Link to={`books/${id}`} style={linkStyle}>
                <img src={image} alt={name}/>
                <h1>{name}</h1>
                <h2>{author}</h2>
                <h3>Publish Date: {publishDate}</h3>
                <h3>Genre: {genre}</h3>
            </Link>
            {/* <p>{link}</p>
            <p>{summary}</p> */}
        </div>
    );
}

export default BookList;