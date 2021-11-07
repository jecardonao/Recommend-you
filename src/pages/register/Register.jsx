import React from "react";
import "./Register.css";
import {Link} from "react-router-dom";

export default function Register() {
  return (
    <div className="login">
      <div className="loginWrapper">
        <div className="loginLeft">
          <h3 className="loginLogo">Recommend-you</h3>
          <span className="loginDesc">
          Connect with friends and the enterprise with Recommend-you
          </span>
        </div>
        <div className="loginRight">
          <div className="loginBox">
            <input placeholder="Username" className="loginInput" />
            <input placeholder="Email" className="loginInput" />
            <input placeholder="Password" className="loginInput" input type = "password"/>
            <input placeholder="Password Again" className="loginInput" input type = "password"/>
            <Link to = "/Login">
             <button className="loginButton">Sign Up</button>
            </Link>
            <button className="loginRegisterButton">
              Log into Account
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}