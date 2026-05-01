import axios from "axios";

/**
 * Central HTTP client for ArkoBank portal surfaces.
 * Uses relative paths so Vite proxy can route to the FastAPI tier in dev.
 */
export const apiClient = axios.create({
  baseURL: "/api",
  timeout: 25000,
  headers: {
    "X-Arkobank-Client": "portal-demo/1.0",
  },
});

export async function fetchAccountSummary(accountId: string) {
  const { data } = await apiClient.get(`/accounts/${encodeURIComponent(accountId)}/summary`);
  return data as { balanceCents: number; currency: string };
}
