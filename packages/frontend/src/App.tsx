import { Route, Routes } from "react-router-dom";
import { OperatorHome } from "./pages/operator/OperatorHome";
import { CustomerPortalHome } from "./pages/customer/CustomerPortalHome";
import { SupportAnnouncement } from "./components/announcements/SupportAnnouncement";
import { NavigationChrome } from "./components/chrome/NavigationChrome";

export default function App() {
  return (
    <div className="app-shell">
      <NavigationChrome />
      <main className="app-main">
        <Routes>
          <Route path="/" element={<CustomerPortalHome />} />
          <Route path="/operator/*" element={<OperatorHome />} />
          <Route path="/announcement" element={<SupportAnnouncement />} />
        </Routes>
      </main>
    </div>
  );
}
