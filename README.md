# Codex Usage for SwiftBar

SwiftBar plugin that shows Codex usage limits from local Codex session data.

It displays:

- 5-hour limit
- weekly limit
- time left until reset
- proportional pace warnings
- colored Codex-style menu bar icons
- smart macOS notifications

## Languages

The plugin uses the main macOS language automatically.

Current interface translations:

- Spanish
- English

Dates and times use the macOS system format.

## Requirements

- macOS
- SwiftBar
- Python 3
- Codex installed and used locally at least once

## Installation

Copy these two files into your SwiftBar plugins folder:

- `plugins/codex-limits.1m.py`
- `plugins/codex-limits-weekly.1m.py`

SwiftBar will show two menu bar items:

- `5h`: 5-hour Codex limit
- `Sem` or `Week`: weekly Codex limit

Both menu items open the same detailed menu with the two limits grouped into separate sections.

## Optional Settings

Force the display language:

```sh
CODEX_LIMITS_LANG=es
CODEX_LIMITS_LANG=en
```

Force the display mode:

```sh
CODEX_LIMITS_MODE=five
CODEX_LIMITS_MODE=weekly
CODEX_LIMITS_MODE=combined
```

## Privacy

The plugin reads only local Codex session files from:

```text
~/.codex/sessions
~/.codex/archived_sessions
```

It does not send usage data anywhere.

