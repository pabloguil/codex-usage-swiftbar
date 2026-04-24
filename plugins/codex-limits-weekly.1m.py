#!/usr/bin/env python3
# <xbar.title>Codex weekly limit</xbar.title>
# <xbar.version>1.1.0</xbar.version>
# <xbar.author>Pablo Guil</xbar.author>
# <xbar.author.github>pabloguil</xbar.author.github>
# <xbar.desc>Shows the weekly Codex limit as a separate menu bar item.</xbar.desc>
# <xbar.dependencies>python3</xbar.dependencies>
import os
import subprocess
import sys
from pathlib import Path

plugin = Path(__file__).resolve().with_name("codex-limits.1m.py")
if not plugin.exists():
    plugin = Path.home() / "Library/Application Support/SwiftBar/Plugins/codex-limits.1m.py"
env = dict(os.environ)
env["CODEX_LIMITS_MODE"] = "weekly"
raise SystemExit(subprocess.run([sys.executable, str(plugin)], env=env).returncode)
