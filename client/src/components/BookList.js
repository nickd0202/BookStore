import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom"
import { Card, Icon, Image } from 'semantic-ui-react'


function BookList({id,name,author,publishDate,genre,link,summary,image}){

    const linkStyle= { 
        textDecoration: "none"
    }




    return(
            <Card as={Link} to={`/books/${id}`}>
                <Image src={image} wrapped ui={false} />
                <Card.Content>
                    <Card.Header>{name}</Card.Header>
                    <Card.Description>By: {author}</Card.Description>
                    <Card.Description>Publish Date: {publishDate}</Card.Description>
                    <Card.Description>Genre: {genre}</Card.Description>
                </Card.Content>
            </Card>
                // <div className = "BookId">
                //     <Link to={`books/${id}`} style={linkStyle}>
                        
                //         <img src={image} alt={name}/>
                    
                //         <h1>{name}</h1>
                //         <h2>{author}</h2>
                //         <h3>Publish Date: {publishDate}</h3>
                //         <h3>Genre: {genre}</h3>
                //     </Link>
                // </div>
    
        
    );
}

export default BookList;