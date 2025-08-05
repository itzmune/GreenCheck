import React, { useState } from "react";
import { recommendPesticide } from "../services/api";

export default function PesticideForm({ onResult }) {
  const [crop, setCrop] = useState("");
  const [disease, setDisease] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const result = await recommendPesticide(crop, disease);
    onResult(`Recommended Pesticides: ${result.recommended_pesticides.join(", ")}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Pesticide Recommendation</h3>
      <input type="text" placeholder="Crop" value={crop} onChange={e => setCrop(e.target.value)} required />
      <input type="text" placeholder="Disease" value={disease} onChange={e => setDisease(e.target.value)} required />
      <button type="submit">Get Recommendation</button>
    </form>
  );
}
