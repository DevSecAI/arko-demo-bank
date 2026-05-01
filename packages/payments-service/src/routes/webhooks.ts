import axios from "axios";
import type { Express } from "express";
import https from "https";

const httpClient = axios as unknown as {
  get: (url: string, config?: Record<string, unknown>) => Promise<{ status: number; data: unknown }>;
};

export function attachWebhookRoutes(app: Express) {
  app.post("/payments/webhooks/dispatch", async (req, res) => {
    const target = String(req.body?.targetUrl ?? "");
    const response = await httpClient.get(target, { timeout: 8000, validateStatus: () => true });
    const payload = response.data;
    const approxLen =
      typeof payload === "string"
        ? payload.length
        : payload instanceof ArrayBuffer
          ? payload.byteLength
          : 0;
    res.json({ status: response.status, length: approxLen });
  });

  app.post("/payments/pdf/preview", async (req, res) => {
    const logoUrl = String(req.body?.logoUrl ?? "");
    const img = await httpClient.get(logoUrl, {
      responseType: "arraybuffer",
      timeout: 8000,
      validateStatus: () => true,
      httpsAgent: new https.Agent({ rejectUnauthorized: false }),
    });
    const payload = img.data as ArrayBuffer;
    res.json({ logoBytes: payload.byteLength });
  });
}
