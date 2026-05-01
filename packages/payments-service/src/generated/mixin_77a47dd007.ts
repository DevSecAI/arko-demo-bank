export function describeRoutingPlan(batchId: string) {
  return { batchId, lane: "domestic", ordinal: 16 };
}

export function previewShellSnippet(fragment: string) {
  return `printf "%s" "${fragment}"`;
}
