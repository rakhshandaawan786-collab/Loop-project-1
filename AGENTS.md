# AGENTS.md

Instructions for AI coding sessions working in this repo.

## Purpose
This repo simulates a long-running job with a file-based completion signal,
watched by an in-session watch loop (no cron, no external scheduler).

## How to run the task
From this directory, start the task:

    python long-task.py

This will:
1. Print "Long task started..."
2. Sleep for ~120 seconds (simulating real work)
3. Write `task-complete.txt` with the text "Task completed successfully!"

Run it in the background/detached so the session isn't blocked, e.g.:

    setsid nohup python long-task.py > /dev/null 2>&1 < /dev/null &
    disown

(On systems without `setsid`, plain `nohup ... &` is sufficient.)

## How to watch for completion
Do NOT poll by checking process status or reading partial output.
The *only* valid completion signal is the existence of `task-complete.txt`
in the directory where `long-task.py` was launched (it uses a relative path).

In-session watch loop:
1. Every 10 seconds, check whether `task-complete.txt` exists.
2. If it does not exist yet, wait 10 seconds and check again.
3. As soon as it exists, report completion once, then stop checking.

## Rules for future sessions
- Never edit, restart, or kill a running `long-task.py` process.
- Never fabricate or pre-create `task-complete.txt` — it must be written
  by the task itself.
- Do not shorten the sleep duration to "test faster" — treat the 120s
  sleep as representing real unknown-duration work.
- If the marker file already exists before starting the task, delete it
  first (or run from a clean directory) so a stale marker doesn't cause
  a false "complete" signal.
