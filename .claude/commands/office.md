---
description: Save changes made on the office page (looks and seats) into office/index.html. Usage /office {json from the page}
argument-hint: "{ \"agent-id\": { \"look\": {...}, \"at\": 3 } }"
---

The user pasted changes from the office page: $ARGUMENTS

1. Read it as JSON: `{ "<agent id>": { "look": { ... }, "at": <desk slot 0-8>, "where": <spot> } }`. Not valid JSON? Say so and stop.
2. In `office/index.html`, inside the `<script id="team" type="application/json">` block, for each id that matches an agent's `"id"`:
   - `look`: merge it into that agent's `"look"` object (create it if missing). Keep only these keys: `style` (short, bob, long, ponytail, bun, curly), `head` (none, cap, beanie, headset), `glasses` (none, glasses, shades), `facial` (none, stubble, mustache, beard), `accessory` (none, watch, lanyard, earring), and the colors `hair`, `skin`, `shirt`, `pants`, `shoes`, `cap` as `#rrggbb`. Drop anything else.
   - `at`: set that agent's `"at"` (which desk slot is theirs, 0-8).
   - `where`: where they are now: `"couch-1"`, `"couch-2"`, `"couch-3"`, `"pantry-1"`, `"pantry-2"`, `"cooler"`, or an `[x, z]` floor spot. `null` means back at their desk: remove their `"where"`.
   Unknown ids: skip them and say which.
3. Never add, remove or reorder agents, and never change a `seed`, `id` or `name`. Keep the JSON valid.
4. If `brain/00-Core/about-me.md` has an office page link, publish the office again to that same link.
5. Tell the user it's saved and to reload the page. The "Changed in this browser only" note goes away on its own.
