import './App.css';
import About from './components/About';
import Footer from './components/Footer';
import Home from './components/Home';
import NavBar from './components/NavBar';
import Project from './components/Project';
import Resume from './components/Resume';

function App() {
  return (
    <div className="App">
      <NavBar />
      <Home />
      <About />
      <Resume />
      <Project />
      <Footer />
    </div>
  );
}

export default App;
