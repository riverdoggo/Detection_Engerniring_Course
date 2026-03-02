# Detection Tuning Log

Initial Thresholds:
- Horizontal: 20 IPs / 5 min
- Vertical: 10 ports / 5 min
- Volume: 3x baseline

Noise Cases:
1. Patch server burst
2. Dev automation scan
3. Backup volume spike

Final Thresholds:
- Horizontal: 25 IPs / 5 min
- Vertical: 15 ports / 5 min
- Volume: 3x + percentile
