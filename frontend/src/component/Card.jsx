import React, { useEffect, useState } from "react";
import axios from "axios";
import './Card.css';

function Card() {
  const [products, setProducts] = useState([]);
  console.log(products)

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/api/products")
    
      .then(res => setProducts(res.data))
      .catch(err => {
        console.error("Error fetching products:", err.message);
      });
  }, []);

  return (
    <div className="app" style={{paddingLeft:"150px",paddingRight:"200px"}}>
      <center>
        <header className="header">
          <h1>🛍️ Product Collection</h1>
          <p>Discover the latest items in our store</p>
        </header>
      </center>
      <div className="card-container">
        {products.map(product => (
          <div className="card" key={product.id}>
            <img src={product.image_url} alt={product.name} />
            <div className="card-content">
              <h2>{product.name}</h2>
              <p className="price">Rs. {product.price}</p>
              <p className="stock"><strong>In stock:</strong> {product.stock}</p>
              <p className="description">{product.description}</p>
              <button style={{ marginRight: '10px' }}>Add to cart</button>
              <button>Buy Now</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Card;
