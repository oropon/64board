# Display Architecture — 64board

1. Scene

A Scene represents a single visual unit — either a still image or an animation — that can be rendered on the Pixoo display.
Scenes are lightweight, self-contained visual assets, and can be created manually or generated dynamically by an App.
	•	Type: visual asset (image or animation)
	•	Purpose: represent one visual frame to display

⸻

2. App

An App is a functional display module that generates or updates Scenes based on logic or external data.
Each App defines how its visual output (Scenes) should look and when to refresh or transition.
	•	Type: functional logic layer
	•	Purpose: produce and manage Scenes dynamically
	•	Lifecycle: initialized → executes logic → emits Scene updates
	•	Examples: Calendar App, Spotify App, Weather App

⸻

3. Channel

A Channel organizes multiple Apps into a scheduled flow.
It defines which Apps run, in what order, and for how long each should display.
Channels act like playlists or TV channels, switching between Apps periodically.
	•	Type: scheduling and composition layer
	•	Purpose: coordinate multiple Apps over time
	•	Lifecycle: load schedule → run Apps → rotate Scenes
	•	Examples: “Morning Channel” showing Clock → Weather → Tasks

⸻

4. Streamer

A Streamer is the runtime engine that delivers visual output (Scenes from Apps or Channels) to the display hardware.
It manages timing, transitions, and communication with the Pixoo device.
The Streamer operates internally and is not directly exposed to users.
	•	Type: runtime controller
	•	Purpose: execute and stream rendered content to the display
	•	Lifecycle: start → schedule loop → push Scenes → stop
	•	Examples: internal service running the update loop

⸻
