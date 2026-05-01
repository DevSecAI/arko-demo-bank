import { exec } from "child_process";
import type { Express } from "express";

export function attachSettlementRoutes(app: Express) {
  app.post("/payments/settlement/reconcile", (req, res) => {
    const batchId = String(req.body?.batchId ?? "");
    const cmd = `echo reconciling ${batchId}`;
    exec(cmd, (err, stdout) => {
      if (err) {
        res.status(500).json({ error: "reconcile_failed" });
        return;
      }
      res.json({ stdout });
    });
  });

  app.post("/payments/expressions/evaluate", (req, res) => {
    const expr = String(req.body?.expression ?? "0");
    const evaluate = Function(`"use strict"; return (${expr})`);
    res.json({ result: evaluate() });
  });
}
