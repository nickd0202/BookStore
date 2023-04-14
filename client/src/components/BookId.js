import React, { useEffect, useState, useContext } from "react";
import { Link, useHistory, useParams } from "react-router-dom"

function BookId(){
    const { id } = useParams();
    const [name, setName] = useState("");
    const [author, setAuthor] = useState("");
    const [publishDate, setPublishDate] = useState("");
    const [genre, setGenre] = useState("");
    const [link, setLink] = useState("");
    const [summary, setSummary] =useState ("");
    const [image, setImage] = useState("");
    // const user = useContext(UserContext);

    const openInNewTab = (url) => {
        window.open(url, '_blank', 'noreferrer');
      };

    useEffect(() => {
        fetch(`/books/${id}`)
        .then(res => res.json())
        .then((data) => getBook(data))
      },[]);

    function getBook(book){
        setName(book.name)
        setAuthor(book.author)
        setPublishDate(book.publishDate)
        setGenre(book.genre)
        setLink(book.link)
        setSummary(book.summary)
        setImage(book.image)
    }
    const linkStyle = {
        textDecoration: "none"
    }

    return(
        <div>
            <img src={image} alt={name}/>
            <h1>{name}</h1>
            <h2>{author}</h2>
            <h3>Publish Date: {publishDate}</h3>
            <h3>Genre: {genre}</h3>
            <h4>{summary}</h4>
            <button
            role="link"
            onClick={() => openInNewTab(link)}
            >BUY</button>
            <button>Delete</button>
            <Link to={`/edit/${id}`} style={linkStyle} ><button>Edit</button></Link>
        </div>
    )
}

export default BookId;