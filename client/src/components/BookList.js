import React, { useEffect, useState } from "react";

function BookList({id,name,author,publishDate,genre,link,summary,image}){
    return(
        <div>
            <img src={image}/>
            <h1>{name}</h1>
            <h2>{author}</h2>
            <h3>Publish Date: {publishDate}</h3>
            <h3>Genre: {genre}</h3>
            {/* <p>{link}</p>
            <p>{summary}</p> */}
        </div>
    );
}

export default BookList;