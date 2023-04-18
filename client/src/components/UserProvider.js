import React, {createContext, useEffect, useState} from 'react';

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    useEffect (() => {
        fetch("/check_session").then ((r) => {
            if (r.ok) {
                r.json().then((user) => setUser(user));
            }
        });
    }, []);

    console.log('From:')
    console.log(user)

    return(
        <UserContext.Provider value={[user,setUser]}>
            {children}
        </ UserContext.Provider>
    )
}

export default UserProvider;