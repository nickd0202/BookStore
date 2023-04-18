import React, { useEffect, useState, createContext } from "react";
import { Switch, Route, useHistory, useParams } from "react-router-dom";
import {Form} from"semantic-ui-react";
import ReviewBreak from "./ReviewBreak";

function Review({reviews}){
    const { id } = useParams();
    const revList = reviews.map((review) => {
        if (review.book.id.toString() === id){
            return (
            <ReviewBreak 
            key = {review.id}
            review = {review.review}
            />
            
        )}
    })

    const [newRev, setNewRev] = useState("")

    function handleRev(newRev){
        setNewRev(newRev.target.value)
    }


    function handleSubmit(){
        fetch("/reviews", {
            method: "POST",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
                review: newRev,
                book_id: id
              }),
            }).then((res) => {
                if (res.ok) {
                    res.json().then(() => {
                        // history.push('/BookList')
                        window.location.reload();
                    })
                }
            })
      }


    return( 
        <div>
            <ul className = "reviews">{revList}</ul>
            <Form onSubmit={() => handleSubmit(id)} style={{ maxWidth: '1000px' }}>
            <Form.Field>
                <label>Review: </label>
                <input
                    type="text"
                    name="review"
                    placeholder="Create A Review"
                    className = "input-text"
                    onChange = {handleRev}
                    value = {newRev}
                />
            </Form.Field>
            <input type="submit" />
            </Form>
        </div>
    )
}

export default Review;