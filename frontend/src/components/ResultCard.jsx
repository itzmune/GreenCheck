import React from "react";

export default function ResultCard({ result }) {
  if (!result) return null;

  return (
    <div style={{
      padding: "10px",
      background: "#f0f0f0",
      marginTop: "20px",
      borderRadius: "8px"
    }}>
      <strong>Result:</strong> <p>{result}</p>
    </div>
  );
}
