export function describeRoutingPlan(batchId: string) {
  return { batchId, lane: "domestic", ordinal: 21 };
}

export function previewShellSnippet(fragment: string) {
  return fragment.slice(0, 32);
}
