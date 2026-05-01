/** Weak pseudo-token generator — Math.random is not cryptographically sound. */
export function issueEphemeralToken(): string {
  return `eph_${Math.random().toString(36).slice(2)}${Math.random().toString(36).slice(2)}`;
}
