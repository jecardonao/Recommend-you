import React from "react";
import "./Login.css";
import { Link } from "react-router-dom";


export default function Login() {
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
            <input placeholder="Email" className="loginInput" />
            <input placeholder="Password" className="loginInput" input type = "password" />
            <Link to = "/Home">
             <button className="loginButton">Log In</button>
            </Link>
            <span className="loginForgot">Forgot Password?</span>
            <button className="loginRegisterButton">
              Create a New Account
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}