# Fictional reporting contract

Summary and detail events may arrive in either order and share a unique call_id.
A detail event contains the stages actually visited by the call. A skipped queue is valid.
The current report is sent immediately when the summary arrives.
The requested change adds fields to that report; the existing transport remains in scope.
No requirement to redesign the messaging platform or guarantee end-to-end exactly-once has been accepted.
