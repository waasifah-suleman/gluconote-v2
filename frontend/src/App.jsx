import { useEffect, useState } from "react";
import apiClient from "./api/client";

function App() {
  const [status, setStatus] = useState("checking...");

  useEffect(() => {
    apiClient.get("/health")
      .then(res => setStatus(res.data.status))
      .catch(() => setStatus("backend unreachable"));
  }, []);

  return <h1>Backend status: {status}</h1>;
}

export default App;