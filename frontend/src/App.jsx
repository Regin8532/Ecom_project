import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';

import Navbar from './component/Navbar';


import Footer from './component/Footer';


function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />

      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
,