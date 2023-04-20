import React, {  useState } from "react";
import {  useHistory } from "react-router-dom";
import {Form, Button, Icon} from"semantic-ui-react";

function AddBook (){

    const [name, setName] = useState("");
    const [author, setAuthor] = useState("");
    const [publishDate, setPublishDate] = useState("");
    const [genre, setGenre] = useState("");
    const [link, setLink] = useState("");
    const [summary, setSummary] =useState ("");
    const [image, setImage] = useState("");
    const history = useHistory();
    
    function handleName(name) {
        setName(name.target.value);
      }
    function handleAuthor(author) {
        setAuthor(author.target.value);
      }
    function handlePublishDate(publishDate) {
        setPublishDate(publishDate.target.value);
      }
    function handleGenre(genre) {
        setGenre(genre.target.value);
      }
    function handleImage(image) {
        setImage(image.target.value);
      }
    function handleSummary(summary) {
        setSummary(summary.target.value);
      }
    function handleLink(link) {
        setLink(link.target.value);
      }

      function handleSubmit(){
        fetch("/books", {
            method: "POST",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: name,
                author: author,
                publishDate: publishDate,
                genre: genre,
                link: link,
                summary: summary,
                image: image,
              }),
            }).then((res) => {
                if (res.ok) {
                    res.json().then(() => {
                        history.push('/BookList')
                        window.location.reload();
                    })
                }
            })
      }






    return (
        <div class="add">
        <Form onSubmit={() => handleSubmit()} style={{ maxWidth: '1000px'}}>
        <h3 id ="form-title">Add A Book!</h3>
        <Form.Field >
            <label>Name: </label>
            <input
                type="text"
                name="name"
                placeholder="Enter the Name"
                className = "input-text"
                onChange = {handleName}
                value = {name}
            />
        </Form.Field>
        <Form.Field>
        <label>Author: </label>
        <input
            type="text"
            name = "author"
            placeholder="Enter the Author"
            className = "input-text"
            onChange = {handleAuthor}
            value = {author}
        />
        </Form.Field>
        <Form.Field>
            <label>Publish Date: </label>
            <input
                type="text"
                name = "publishDate"
                placeholder="Enter the Publish Date"
                className = "input-text"
                onChange = {handlePublishDate}
                value = {publishDate} 
            />
        </Form.Field>
        <Form.Field>
            <label>Genre: </label>
            <input
                type="text"
                name = "genre"
                placeholder="Enter the Genre"
                className = "input-text"
                onChange = {handleGenre}
                value = {genre}
            />
        </Form.Field>
        <Form.Field>
            <label>Image URL:</label>
            <input
                type = "text"
                name = "image"
                placeholder="Enter the Image Url"
                className = "input-text"
                onChange = {handleImage}
                value = {image}
            />
        </Form.Field>
        <Form.Field>
            <label>Summary: </label>
            <input 
                type = "text"
                name = "used"
                placeholder="Enter the Summary"
                className = "input-text"
                onChange = {handleSummary}
                value = {summary}
            />
        </Form.Field>
        <Form.Field>
            <label>Link: </label>
            <input 
                type = "text"
                name = "link"
                placeholder="Enter the Link"
                className = "input-text"
                onChange = {handleLink}
                value = {link}
            />
        </Form.Field>
        <Button animated type="submit">
            
            <Button.Content visible>Submit</Button.Content>
            <Button.Content hidden>
            <Icon name='arrow right' />
            </Button.Content>
        </Button>
    </Form>
    </div>
    );
}


export default AddBook;