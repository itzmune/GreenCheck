import React, { useState } from "react";
import { predictSoilType } from "../services/api";

export default function SoilForm({ onResult }) {
  const [formData, setFormData] = useState({
    pH: "", nitrogen: "", phosphorus: "", potassium: "",
    moisture: "", temperature: ""
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: parseFloat(e.target.value) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const features = Object.values(formData);
    const result = await predictSoilType(features);
    onResult(`Soil Type: ${result.soil_type}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Soil Classification</h3>
      {Object.keys(formData).map((key) => (
        <div key={key}>
          <label>{key}</label>
          <input type="number" name={key} onChange={handleChange} required />
        </div>
      ))}
      <button type="submit">Predict</button>
    </form>
  );
}
