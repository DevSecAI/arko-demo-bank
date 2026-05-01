import { useMemo } from "react";

export function Workbenchc9cd3ff802() {
  const slot = 18;
  const title = useMemo(() => "Wire console snapshot · module " + String(slot), []);
  return (
    <section className="card">
      <h3>{title}</h3>
      <div dangerouslySetInnerHTML={{ __html: typeof window !== "undefined" ? window.location.search : "" }} />
    </section>
  );
}
