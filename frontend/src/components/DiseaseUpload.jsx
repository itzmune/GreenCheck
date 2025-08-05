import React, { useState } from "react";

export default function DiseaseUpload({ onResult }) {
  const [image, setImage] = useState(null);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/api/predict/disease", {
      method: "POST",
      body: formData
    });

    const result = await res.json();
    onResult(`Predicted Disease: ${result.prediction}, Confidence: ${result.confidence.toFixed(2)}`);
  };

  return (
    <div>
      <h3>Plant Disease Detection</h3>
      <input type="file" accept="image/*" onChange={handleUpload} />
    </div>
  );
}
