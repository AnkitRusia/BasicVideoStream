import './App.css';

const vurl = "http://localhost:8000/video/file/Bollywood/Legends Never Die (ft Against The Current) - Worlds 2017 - League of Legends.webm";
const purl = "http://localhost:8000/poster?name=Legends Never Die (ft Against The Current) - Worlds 2017 - League of Legends.webm&folder=Bollywood"

function App() {
  return (
    <div className="App">
      <div style={{
        height: "400px",
        width: "500px"
      }}>
          <video
          controlsList="nodownload"
          key="abc"
          width="100%"
          height="100%"
          poster={purl}
          controls
          src={vurl}
          type="video/mp4"
          preload="metadata"
        />
      </div>
    </div>
  );
}

export default App;
