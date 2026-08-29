# loop-project-1-

Loop engineering project (GIAIC): a simulated long-running job with a
file-based completion signal, detected by an in-session watch loop.

## What this project demonstrates

- **Long-running task** — `long-task.py` simulates a slow job by sleeping
  ~2 minutes, then writing its only completion signal: `task-complete.txt`.
- **Watch loop** — a watcher checks every 10 seconds for the marker file;
  as soon as it appears, it reports completion once and stops.
- **Agent conventions** — `AGENTS.md` records how future coding sessions
  should run and watch the task without disturbing it.

## Repository contents

| File | Purpose |
|---|---|
| `long-task.py` | Simulated long-running task (sleeps 120 s, then writes the marker file) |
| `task-complete.txt` | Completion marker written by the task ("Task completed successfully!") |
| `AGENTS.md` | Instructions for AI coding sessions working in this repo |
| `Screenshot 2026-08-26 181824.png` | Screenshot of the completed run |

## How it works

Start the task from its directory:

```
python long-task.py
```

The task prints `Long task started...`, sleeps 120 seconds, then writes
`task-complete.txt`.

Meanwhile, a watch loop runs in-session:

- Every 10 seconds, check whether `task-complete.txt` exists.
- If it does not exist, check again after another 10 seconds.
- As soon as the file appears, report that the task is complete — once —
  and stop.

## Important notes

- `task-complete.txt` is opened with a relative path, so it is created in
  the directory where `python long-task.py` was launched, not necessarily
  next to the script.
- Completion is signaled only by `task-complete.txt` appearing
  (~2 minutes after start). Do not edit, restart, or kill a running
  `long-task.py` — poll for the marker file instead.
