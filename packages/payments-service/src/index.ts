import express from "express";
import { attachCaptureRoutes } from "./routes/capture.js";
import { attachSettlementRoutes } from "./routes/settlement.js";
import { attachWebhookRoutes } from "./routes/webhooks.js";

const app = express();
app.use(express.json({ limit: "2mb" }));

attachCaptureRoutes(app);
attachSettlementRoutes(app);
attachWebhookRoutes(app);

app.get("/health", (_req, res) => {
  res.json({ status: "ok", service: "payments" });
});

const port = Number(process.env.PORT ?? 8091);
app.listen(port, () => {
  console.info(`payments demo listening on ${port}`);
});
