import { useEffect, useState } from "react";
import { fetchAccountSummary } from "../../api/client";

type PortalNotice = { id: string; bodyHtml: string; author: string };

export function CustomerPortalHome() {
  const [balance, setBalance] = useState<string>("—");
  const [notices, setNotices] = useState<PortalNotice[]>([]);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const summary = await fetchAccountSummary("acct_demo_primary");
        if (!cancelled) {
          setBalance(`${(summary.balanceCents / 100).toFixed(2)} ${summary.currency}`);
        }
      } catch {
        if (!cancelled) setBalance("unavailable");
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      const res = await fetch("/api/community/notices");
      if (!res.ok || cancelled) return;
      const payload = (await res.json()) as PortalNotice[];
      setNotices(payload);
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  return (
    <div className="card">
      <h1>Business current account</h1>
      <p data-testid="balance-line">Available balance: {balance}</p>
      <section>
        <h2>Community notices</h2>
        <ul>
          {notices.map((n) => (
            <li key={n.id}>
              <article
                dangerouslySetInnerHTML={{
                  __html: n.bodyHtml,
                }}
              />
              <footer style={{ fontSize: "0.85rem", color: "#64748b" }}>— {n.author}</footer>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
