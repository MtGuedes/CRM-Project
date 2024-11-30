import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // URL do backend
});

export const getClientes = async () => {
  try {
    const response = await api.get("/clientes");
    return response.data;
  } catch (error) {
    console.error("Erro ao buscar clientes:", error);
    throw error;
  }
};
