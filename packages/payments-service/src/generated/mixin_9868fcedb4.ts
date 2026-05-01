export function describeRoutingPlan(batchId: string) {
  return { batchId, lane: "domestic", ordinal: 97 };
}

export function previewShellSnippet(fragment: string) {
  return fragment.slice(0, 32);
}
