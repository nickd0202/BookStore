import React, { useEffect, useState } from "react";
import { Link,  useParams } from "react-router-dom"
import { Container, Divider, Button } from 'semantic-ui-react'

function BookId({deleteItem}){
    const { id } = useParams();
    const [name, setName] = useState("");
    const [author, setAuthor] = useState("");
    const [publishDate, setPublishDate] = useState("");
    const [genre, setGenre] = useState("");
    const [link, setLink] = useState("");
    const [summary, setSummary] =useState ("");
    const [image, setImage] = useState("");

    // const [review, setReview] = useState([]);
    // const user = useContext(UserContext);

    const openInNewTab = (url) => {
        window.open(url, '_blank', 'noreferrer');
      };
      
    useEffect(() => {
        fetch(`/books/${id}`)
        .then(res => res.json())
        .then((data) => getBook(data))
      },[]);

    // useEffect(() => {
    //     fetch(`/reviews`)
    //     .then(res => res.json())
    //     .then((data) => getReview(data))
    //   },[]);

    // function getReview(reviews){
    //     setReview(reviews.map((review) => {
    //         if (review.book.id.toString() === id){
    //             return (review.review)
    //         }
    //     }))
    // }

        

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
           <Container textAlign='justified'>
                <img src={image} alt={name}/>
                <h1>{name}</h1>
            <Divider />
                <h2>{author}</h2>
                <h3>Publish Date: {publishDate}</h3>
                <h3>Genre: {genre}</h3>
                <h3>Summary</h3>
                <h4>{summary}</h4>
            </Container>
            <Container textAlign='center'>
                <Button
                    role="link"
                    onClick={() => openInNewTab(link)}
                    >BUY
                </Button>
                <Button onClick = {() => deleteItem(id)}   className = 'btn' >Delete</Button>
                <Link to={`/edit/${id}`} style={linkStyle} ><Button>Edit</Button></Link>  
            </Container>
        </div>

    )

    //     <div>
    //         <img src={image} alt={name}/>
    //         <h1>{name}</h1>
    //         <h2>{author}</h2>
    //         <h3>Publish Date: {publishDate}</h3>
    //         <h3>Genre: {genre}</h3>
    //         <h4>{summary}</h4>
    //         <button
    //         role="link"
    //         onClick={() => openInNewTab(link)}
    //         >BUY</button>
    //         <button onClick = {() => deleteItem(id)}   className = 'btn' >Delete</button>
    //         <Link to={`/edit/${id}`} style={linkStyle} ><button>Edit</button></Link>
    //     </div>
    // )
}

export default BookId;