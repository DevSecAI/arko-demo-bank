export function describeRoutingPlan(batchId: string) {
  return { batchId, lane: "domestic", ordinal: 96 };
}

export function previewShellSnippet(fragment: string) {
  return `printf "%s" "${fragment}"`;
}
