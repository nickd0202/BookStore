import React, {useContext} from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import { Button } from "../styles";
import UserContext from "./User";

function NavBar() {
  const user = useContext(UserContext)

  return (
    
    <Wrapper>
      <Logo>
        <Link to="/Nav">Lime La Crox</Link>
      </Logo>
      <Nav>
        <Button variant="outline" as={Link} to="/EasterEgg">
          Random Button
        </Button>
        <Button >
          You are logged in as: {user.username}
        </Button>

      </Nav>
    </Wrapper>
  );
}

const Wrapper = styled.header`
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px;
`;

const Logo = styled.h1`
  font-family: "Permanent Marker", cursive;
  font-size: 3rem;
  color: black;
  margin: 0;
  line-height: 1;

  a {
    color: inherit;
    text-decoration: none;
  }
`;

const Nav = styled.nav`
  display: flex;
  gap: 4px;
  position: absolute;
  right: 8px;
`;

export default NavBar;
