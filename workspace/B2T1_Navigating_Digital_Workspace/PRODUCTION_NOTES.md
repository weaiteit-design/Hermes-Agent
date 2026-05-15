# Production Notes and Blockers

Completed locally:
- English and Marathi content packages.
- English and Marathi PPTX decks.
- Assessment XLSX.
- English silent draft video from slide visuals.
- English voiceover generated using available local TTS provider (Edge), not ElevenLabs.
- English MP4 with voiceover generated from simple slide visuals.
- Marathi silent draft video generated from slide visuals.

Blocked / needs credentials or accessible assets:
- Template folder requires sign-in in this environment, so exact templates could not be downloaded. Created template-ready files instead.
- ELEVENLABS_API_KEY is not present, so official ElevenLabs audio could not be generated from this server. A non-ElevenLabs English draft audio is included.
- SARVAM_API_KEY is not present, so Sarvam Marathi audio could not be generated from this server.
- Remotion is not installed in this project. A Remotion build can be added after templates/audio are available.

Recommended next step:
1. Put these contents into the client templates from the shared template folder.
2. Generate English voiceover from `B2T1_Video_Script_EN.md` using ElevenLabs.
3. Generate Marathi voiceover from `B2T1_Video_Script_MR.md` using Sarvam.
4. Use the PPTX decks as source slides for Remotion animation/video sync.
