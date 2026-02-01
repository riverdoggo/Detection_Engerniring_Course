\# W3D5 — Alert Wiring



\## Path Used

Simulation (Azure payload replay + local POST)



\## What Worked

\- FastAPI receiver accepted POST requests

\- JSON payloads were written to disk

\- Endpoint remained stable under repeated requests



\## What Surprised Me

\- PowerShell `curl` alias behaves differently from Linux curl

\- Payload structure is deeply nested

\- Logging requires pre-creating directories



\## What Broke Initially

\- Missing \_\_init\_\_.py caused import failure

\- uvicorn not installed in the active Python environment

\- Incorrect assumptions about curl syntax on Windows



\## Outcome

End-to-end alert delivery from simulated Azure payload to local detection bot is verified.



