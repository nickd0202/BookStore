import React from "react";
import { useParams } from "react-router-dom";

function ReviewBreak({review}){
    const { id } = useParams();
    // const [newRev, setNewRev] = useState("")

    // function handleRev(newRev){
    //     setNewRev(newRev)
    // }

    // function handleSubmit(){
    //     fetch("/reviews", {
    //         method: "POST",
    //         headers: {
    //           Accept: "application/json",
    //           "Content-Type": "application/json",
    //         },
    //         body: JSON.stringify({
    //             review: newRev,
    //             book_id: id
    //           }),
    //         }).then((res) => {
    //             if (res.ok) {
    //                 res.json().then(() => {
    //                     // history.push('/BookList')
    //                     window.location.reload();
    //                 })
    //             }
    //         })
    //   }


    return(
        <h1>{review}</h1>
    )
}

export default ReviewBreak;