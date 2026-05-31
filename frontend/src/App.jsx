import { useEffect, useState } from "react";
import "./App.css";

const API_BASE = "/api";

function App() {
  const [passengers, setPassengers] = useState([]);
  const [message, setMessage] = useState("Loading passengers...");

  async function loadPassengers() {
    try {
      const response = await fetch(`${API_BASE}/passengers`);
      const data = await response.json();
      setPassengers(data);
      setMessage("Passenger data loaded from backend API");
    } catch (error) {
      setMessage("Could not connect to backend API");
    }
  }

  async function checkIn(passengerId) {
    await fetch(`${API_BASE}/checkin/${passengerId}`, { method: "POST" });
    await loadPassengers();
  }

  useEffect(() => {
    loadPassengers();
  }, []);

  return (
    <main className="page">
      <section className="card">
        <h1>Airport Passenger Processing Platform</h1>
        <p>{message}</p>
        <table>
          <thead>
            <tr><th>Passenger ID</th><th>Name</th><th>Flight</th><th>Status</th><th>Action</th></tr>
          </thead>
          <tbody>
            {passengers.map((p) => (
              <tr key={p.passenger_id}>
                <td>{p.passenger_id}</td><td>{p.name}</td><td>{p.flight}</td><td>{p.status}</td>
                <td><button onClick={() => checkIn(p.passenger_id)}>Check in</button></td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </main>
  );
}

export default App;
