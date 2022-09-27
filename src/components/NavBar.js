import React, { useState } from 'react'
import { FaBars, FaTimes } from 'react-icons/fa'
import { Link } from 'react-scroll'

import './NavBar.scss'

const NavBar = () => {

  const [ click, setClick ] = useState(false);
  const handleClick = () => setClick(!click);
  const closeMenu = () => setClick(false)

  return (
    <div className='header'>
      <nav className='navbar'>
        <div className='hamburger' onClick={handleClick}>
          { click ? (<FaTimes size={30} style={{color: '#ffffff'}}/>) 
          : (<FaBars size={30} style={{color: '#ffffff'}}/>) }
        </div>
        <ul className={ click ? 'nav-menu active' : 'nav-menu'}>
          <li className='nav-item'>
            <Link to='home' smooth={true} duration={1000} offset={-70} onClick={closeMenu}>Home</Link>
          </li>
          <li className='nav-item'>
            <Link to='about' smooth={true} duration={1000} offset={-70} onClick={closeMenu}>About</Link>
          </li>
          <li className='nav-item'>
            <Link to='resume' smooth={true} duration={1000} offset={-70} onClick={closeMenu}>Resume</Link>
          </li>
          <li className='nav-item'>
            <Link to='project' smooth={true} duration={1000} offset={-70} onClick={closeMenu}>Project</Link>
          </li>
        </ul>
      </nav>
    </div>
  )
}

export default NavBar