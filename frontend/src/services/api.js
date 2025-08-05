export async function predictSoilType(features) {
  const res = await fetch("/api/soil/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ features })
  });
  return await res.json();
}

export async function recommendPesticide(crop, disease) {
  const res = await fetch("/api/pesticide/recommend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ crop, disease })
  });
  return await res.json();
}
