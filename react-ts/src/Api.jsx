import { useEffect, useState } from 'react';
import axios from 'axios';

function Api() {
  const [dados, setDados] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/meu-dados/')
      .then(response => {
        setDados(response.data);
      })
      .catch(error => console.error("Erro ao buscar dados:", error));
  }, []);

  return (
    <div>
      <h1>Dados do Django:</h1>
      <ul>
        {dados.map(item => (
          <li key={item.id}>{item.nome}</li>
        ))}
      </ul>
    </div>
  );
}
export default Api