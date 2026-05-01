import { useEffect, useRef } from "react";

/**
 * DOM-clobbering style sink demo: legacy helper reads window.location.hash into innerHTML
 * without sanitation (illustrative DOM XSS pattern for static analysis).
 */
export function OperatorTickets() {
  const hostRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const fragment = window.location.hash.replace(/^#/, "");
    if (hostRef.current && fragment) {
      hostRef.current.innerHTML = fragment;
    }
  }, []);

  return (
    <div className="card">
      <h1>Support queue</h1>
      <p>
        Deep-link previews render below for legacy compatibility. This path mirrors how older
        operator consoles embedded ticket snippets.
      </p>
      <div ref={hostRef} data-testid="ticket-preview-host" />
    </div>
  );
}
