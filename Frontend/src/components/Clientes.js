import React, { useEffect, useState } from "react";
import axios from "axios";

const Clientes = () => {
    const [clientes, setClientes] = useState([]);
    const [loading, setLoading] = useState(true);  // Para controlar o carregamento
    const [error, setError] = useState(null);      // Para controlar erros

    useEffect(() => {
        // Chamada para a API
        axios.get("http://localhost:8000/clientes")
            .then(response => {
                console.log("Dados recebidos:", response.data); 
                // Verifique se a estrutura da resposta contém a chave 'clientes'
                if (Array.isArray(response.data.clientes)) {
                    setClientes(response.data.clientes);
                } else {
                    setClientes([]); // Caso não encontre dados válidos
                }
                setLoading(false);
            })
            .catch(error => {
                console.error("Erro ao buscar clientes:", error);
                setError("Falha ao carregar os clientes.");
                setLoading(false);
            });
    }, []);

    // Exibição condicional baseada no estado de carregamento e erro
    if (loading) {
        return <p>Carregando...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <div>
            <h1>Lista de Clientes</h1>
            <ul>
                {clientes.length === 0 ? (
                    <p>Nenhum cliente encontrado</p>
                ) : (
                    clientes.map(cliente => (
                        <li key={cliente.id}>
                            {cliente.nome} - {cliente.email}
                        </li>
                    ))
                )}
            </ul>
        </div>
    );
};

export default Clientes;
