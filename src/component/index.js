import React from 'react'
// import Header from './Header/Header'
// import About from './About/About'
import Home from './homepage/Home'
// import Footer from './Footer/Footer'
import './index.css'

function Page () {
  return(
    <div>
      <div>
        <section id="hero" className="d-flex flex-column justify-content-center">
          {/* <Header /> */}
        </section>
      </div>
      <Home/>
      <section id="footer" className="footer">
        <div>
          {/* <Footer /> */}
        </div>
      </section>
    </div>
  )
}

export default Page
