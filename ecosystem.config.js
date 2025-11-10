module.exports = {
  apps: [
    {
      name: "mednexus",
      script: "/home/shitshowinmypanties/venv/bin/uvicorn",
      args: "main:app --host 0.0.0.0 --port 8080",
      interpreter: "none", // PM2'ye kendi shell'ini kullanmasını söyler
      cwd: "/home/shitshowinmypanties/actions-runner/_work/med-nexus/med-nexus",
      autorestart: true,
      watch: false,
      max_restarts: 10,
      env: {
        PYTHONPATH: "/home/shitshowinmypanties/venv/lib/python3.11/site-packages",
        PATH: "/home/shitshowinmypanties/venv/bin:/usr/bin:/bin",
        VIRTUAL_ENV: "/home/shitshowinmypanties/venv",
        PORT: 8080,
      },
      out_file: "/home/shitshowinmypanties/.pm2/logs/mednexus-out.log",
      error_file: "/home/shitshowinmypanties/.pm2/logs/mednexus-error.log",
      merge_logs: true,
      log_date_format: "YYYY-MM-DD HH:mm:ss",
    },
  ],
};
