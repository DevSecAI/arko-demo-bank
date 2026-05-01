import { Route, Routes } from "react-router-dom";
import { OperatorTickets } from "./OperatorTickets";

export function OperatorHome() {
  return (
    <Routes>
      <Route index element={<OperatorTickets />} />
    </Routes>
  );
}
