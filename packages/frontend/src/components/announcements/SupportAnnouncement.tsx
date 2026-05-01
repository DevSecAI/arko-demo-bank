import { useMemo } from "react";
import { useSearchParams } from "react-router-dom";

/**
 * Operator-visible banner populated from query parameters.
 * Demonstrates reflected XSS risk when raw HTML is injected from URL state.
 */
export function SupportAnnouncement() {
  const [params] = useSearchParams();
  const message = params.get("msg") ?? "Welcome to ArkoBank business banking.";

  const html = useMemo(() => ({ __html: message }), [message]);

  return (
    <section className="card" aria-live="polite">
      <h2>Support notice</h2>
      <div dangerouslySetInnerHTML={html} />
    </section>
  );
}
