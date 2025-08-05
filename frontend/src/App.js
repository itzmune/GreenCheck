import React, { useState } from 'react';
import './App.css';
import Dashboard from './components/Dashboard';
import PlantAnalysis from './components/PlantAnalysis';
import SoilAnalysis from './components/SoilAnalysis';
import ChatBot from './components/ChatBot';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [analysisResults, setAnalysisResults] = useState([]);

  const addAnalysisResult = (result) => {
    setAnalysisResults(prev => [...prev, { ...result, id: Date.now() }]);
  };

  const renderActiveComponent = () => {
    switch (activeTab) {
      case 'dashboard':
        return <Dashboard analysisResults={analysisResults} />;
      case 'plant-analysis':
        return <PlantAnalysis onAnalysisComplete={addAnalysisResult} />;
      case 'soil-analysis':
        return <SoilAnalysis onAnalysisComplete={addAnalysisResult} />;
      case 'chat':
        return <ChatBot />;
      default:
        return <Dashboard analysisResults={analysisResults} />;
    }
  };

  return (
    <div className="App">
      <header className="app-header">
        <div className="header-content">
          <h1 className="app-title">🌱 GreenCheck</h1>
          <p className="app-subtitle">AI-Powered Plant & Soil Analysis System</p>
        </div>
      </header>

      <nav className="navigation">
        <div className="nav-container">
          <button
            className={`nav-button ${activeTab === 'dashboard' ? 'active' : ''}`}
            onClick={() => setActiveTab('dashboard')}
          >
            📊 Dashboard
          </button>
          <button
            className={`nav-button ${activeTab === 'plant-analysis' ? 'active' : ''}`}
            onClick={() => setActiveTab('plant-analysis')}
          >
            🌿 Plant Analysis
          </button>
          <button
            className={`nav-button ${activeTab === 'soil-analysis' ? 'active' : ''}`}
            onClick={() => setActiveTab('soil-analysis')}
          >
            🌍 Soil Analysis
          </button>
          <button
            className={`nav-button ${activeTab === 'chat' ? 'active' : ''}`}
            onClick={() => setActiveTab('chat')}
          >
            💬 AI Assistant
          </button>
        </div>
      </nav>

      <main className="main-content">
        {renderActiveComponent()}
      </main>

      <footer className="app-footer">
        <p>&copy; 2024 GreenCheck - Powered by AI for Sustainable Agriculture</p>
      </footer>
    </div>
  );
}

export default App;