import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
import React, {useState} from 'react'
import {MainContainer, ChatContainer, MessageList, Message, MessageInput, TypingIndicator } from '@chatscope/chat-ui-kit-react'

const API_KEY = "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";


function Aisystem(){
    const [typing, setTyping] =useState(false)
    const [messages, setMessages] = useState([
        {
            message: "Hello, I am ChatGPT!",
            sender: "ChatGPT"
        }
    ])

    const handleSend = async (message) => {
        const newMessage = {
            message: message,
            sender: "user",
            direction: "outgoing"
        }
        const newMessages = [...messages, newMessage];

        setMessages(newMessages)

        setTyping(true)
        await processMessagetoChatGPT(newMessages);


    }

    async function processMessagetoChatGPT(chatMessages){
        let apiMessages = chatMessages.map((messageObject) => {
            let role = "";
            if(messageObject.sender === "ChatGPT"){
                role="assistant"
            } else {
                role ="user"
            }
            return {role:role, content: messageObject.message}
        })


        const systemMessage = {
            role: "system",
            content: ""
        }

        const apiRequestBody = {
            "model": "gpt-3.5-turbo",
            "messages": [
                systemMessage,
                ...apiMessages
            ]
        }

        await fetch("https://api.openai.com/v1/chat/completion", {
            method: "POST",
            headers: {
                "Authorization": "Bearer " + API_KEY,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(apiRequestBody)
        }).then((data) => {
            return data.json();
        }).then((data) => {
            console.log(data);
        })
    }

    return(
        <div>
            <div style={{position: "relative", height: "800px", width: "100ox"}}>
                <MainContainer>
                    <ChatContainer>
                        <MessageList>
                            {typing ? <TypingIndicator content="ChatGPT is typing..." /> : null}
                            {messages.map((message, i) => {
                                return <Message key={i} model={message} />
                            })}
                        </MessageList>
                        <MessageInput placeholder='Type message here' onSend={handleSend} />
                    </ChatContainer>
                </MainContainer>
            </div>
        </div>
    )
}
export default Aisystem;