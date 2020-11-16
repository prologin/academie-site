import './App.css';
import SocialNetworks from './components/SocialNetworks';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="/images/logo_cube.png" className="App-logo" alt="logo" />
        <h1>Coming soon !</h1>
        <p>
          Le lancement de ce site sera annoncé sur nos réseaux, alors si vous
          <br />
          souhaitez apprendre la programmation, suivez nous sur nos réseaux !
        </p>
        <SocialNetworks />
      </header>
    </div>
  );
}

export default App;
