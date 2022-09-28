import ParticlesBg from 'particles-bg'
import React from 'react'
import './Home.scss'
import { Link } from 'react-scroll'
import { BiChevronDownCircle } from 'react-icons/bi'

const Home = ({ data }) => {
  return (
    <div className='home' id='home'>
      <ParticlesBg type='cobweb' bg={true} />
      <div className='content'>
        <h1 className="responsive-headline">{data.name}</h1>
        <h3>{data.description}</h3>
      </div>
      <p className="scrolldown">
        <Link to='about' smooth={true} duration={1000} offset={-70}>
          <BiChevronDownCircle size={38} style={{color: '#ffffff'}} />
        </Link>
      </p>
    </div>
  )
}

export default Home