import { Link } from "react-router-dom";

export function NavigationChrome() {
  return (
    <header
      style={{
        borderBottom: "1px solid #e2e8f0",
        padding: "0.75rem 1.5rem",
        background: "#fff",
      }}
    >
      <nav style={{ display: "flex", gap: "1rem", alignItems: "center" }}>
        <strong>ArkoBank</strong>
        <Link to="/">Business portal</Link>
        <Link to="/operator">Operator console</Link>
      </nav>
    </header>
  );
}
