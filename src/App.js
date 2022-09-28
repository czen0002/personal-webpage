import './App.css';
import { useEffect, useState } from 'react'
import About from './components/About';
import Footer from './components/Footer';
import Home from './components/Home';
import NavBar from './components/NavBar';
import Project from './components/Project';
import Resume from './components/Resume';

function App() {

  const [personData, setPersonData] = useState();

  const fetchData = async () => {
    try {
      const response = await fetch('./personData.json');
      const data = await response.json();
      setPersonData(data);
    } catch (err) {
      console.log(err);
    }
  }

  useEffect(() => {
    fetchData();
  }, [])

  return (
    <div className="App">
      {personData && 
        <div>
          <NavBar />
          <Home data={personData.home}/>
          <About />
          <Resume />
          <Project />
          <Footer />
        </div>
      }
    </div>
    
  );
}

export default App;
