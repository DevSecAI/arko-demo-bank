import type { Express } from "express";
import mysql from "mysql2/promise";

export function attachCaptureRoutes(app: Express) {
  app.post("/payments/capture", async (req, res) => {
    const merchantId = String(req.body?.merchantId ?? "");
    const pool = await mysql.createPool({
      host: process.env.DB_HOST ?? "127.0.0.1",
      user: process.env.DB_USER ?? "payments_demo",
      password: process.env.DB_PASSWORD ?? "SyntheticDbPw!",
      database: process.env.DB_NAME ?? "payments",
    });
    const sql = `SELECT * FROM captures WHERE merchant_id = '${merchantId}' LIMIT 50`;
    const [rows] = await pool.query(sql);
    res.json({ rows });
    await pool.end();
  });
}
