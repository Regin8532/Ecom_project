import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <div style={{ paddingLeft: '150px',position:"fixed",zIndex:"999",width:"90%" }}>
      <nav className="navbar navbar-expand-lg bg-white">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <img src="\flipkart-logo.png" width="60px" />
          </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText">
            <span className="navbar-toggler-icon"></span>
          </button>
  <div style={{ display: "flex", alignItems: "center", border: "1px solid #ccc", borderRadius: "8px", padding: "5px", width: "500px" }}>
  <img src="/search.jpg" alt="Search" style={{ width: "20px", height: "20px", marginRight: "10px" }} />
  <input
    type="text"
    placeholder="Search for products and more"
    style={{
      border: "none",
      outline: "none",
      fontSize: "16px",
      width: "100%"
    }}
  />
</div>

  

  <div className="collapse navbar-collapse">
    <ul className="navbar-nav  mb-2 mb-lg-0 d-flex flex-row gap-4">
      <li
  className="nav-item"
  style={{ display: "flex",alignItems: "center",paddingLeft: "15px", gap: "0", 
  }}
>
  <img src="/login.jpg"alt="Login" style={{ width: "60px", height: "40px",  margin: "0",  padding: "0",
    }}
  />
  <Link className="nav-link text-dark" to="/" style={{  padding: "0" }} >
    Login
  </Link>
</li>

      <li className="nav-item" style={{ display: "flex",alignItems: "center",paddingLeft: "15px", gap: "0", }}>
        <img src='\cart.jpg' style={{ width: "60px", height: "40px",margin: "0",  padding: "0",}}></img>
        <Link className="nav-link text-dark" to="/About" style={{  padding: "0" }}>Cart</Link>
      </li>
      <li className="nav-item" style={{ display: "flex",alignItems: "center",paddingLeft: "15px", gap: "0", }}>
        <img src='\shop1.jpg' style={{ width: "60px", height: "40px",margin: "0",  padding: "0",}}></img>
        <Link className="nav-link text-dark" to="/" style={{  padding: "0" }}>Become a seller</Link>
      </li>
    </ul>
  </div>
          </div>
      </nav>
    </div>
  );
};

export default Navbar;
