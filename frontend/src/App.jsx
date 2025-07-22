// src/App.jsx
import React, { useEffect, useState } from 'react';
import './index.css'; // certifique-se que importa o Tailwind

export default function App() {
  const [message, setMessage] = useState('Carregando…');

  useEffect(() => {
    fetch('http://localhost:8000/api/hello/') // ajuste se seu endpoint for outro
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage('Erro ao buscar API'));
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white shadow-2xl rounded-2xl p-8 max-w-md w-full text-center">
        <h1 className="text-3xl font-bold mb-4 text-indigo-600">Teste Didacus</h1>
        <p className="text-lg mb-6">{message}</p>
        <button
          onClick={() => window.location.reload()}
          className="px-4 py-2 bg-indigo-500 text-white rounded-md hover:bg-indigo-600 transition"
        >
          Recarregar
        </button>
      </div>
    </div>
  );
}
