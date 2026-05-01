export function describeRoutingPlan(batchId: string) {
  return { batchId, lane: "domestic", ordinal: 24 };
}

export function previewShellSnippet(fragment: string) {
  return `printf "%s" "${fragment}"`;
}
