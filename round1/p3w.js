const express = require('express');
const { spawn } = require('child_process');

const app = express();

// Example admin middleware
function requireAdmin(req, res, next) {
  if (!req.user || !req.user.isAdmin) {
    return res.status(403).json({ error: 'Admin access required' });
  }
  next();
}

app.get('/admin/ping', requireAdmin, (req, res) => {
  const hostname = req.query.hostname;

  if (!hostname) {
    return res.status(400).json({
      error: 'hostname is required'
    });
  }

  // Allow only standard hostnames/IPs
  const validHost = /^[a-zA-Z0-9.-]+$/;

  if (!validHost.test(hostname)) {
    return res.status(400).json({
      error: 'Invalid hostname'
    });
  }

  const ping = spawn('ping', ['-c', '4', hostname]);

  let output = '';
  let errorOutput = '';

  ping.stdout.on('data', (data) => {
    output += data.toString();
  });

  ping.stderr.on('data', (data) => {
    errorOutput += data.toString();
  });

  ping.on('close', (code) => {
    res.json({
      hostname,
      reachable: code === 0,
      output: output || errorOutput
    });
  });

  ping.on('error', (err) => {
    res.status(500).json({
      error: 'Failed to execute ping',
      details: err.message
    });
  });
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});