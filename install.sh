#!/usr/bin/env bash
set -euo pipefail

# Universal installer for the /synapse skill across AI coding and research agents.
# Usage:
#   ./install.sh [agent|custom-path] [--project]
#
# Supported agents:
#   claude       -> ~/.claude/skills/synapse (or .claude/skills/synapse with --project)
#   cursor       -> ~/.cursor/skills/synapse (or .cursor/skills/synapse with --project)
#   antigravity  -> ~/.gemini/antigravity/skills/synapse (or .agent/skills/synapse with --project)
#   gemini       -> ~/.gemini/skills/synapse (or .gemini/skills/synapse with --project)
#   windsurf     -> ~/.codeium/windsurf/skills/synapse (or .windsurf/skills/synapse with --project)
#   cline        -> ~/.cline/skills/synapse (or .cline/skills/synapse with --project)
#   codex        -> ~/.agents/skills/synapse (or .agents/skills/synapse with --project)
#   all          -> Installs globally for all supported agents above

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SOURCE_DIR="$SCRIPT_DIR/synapse"


if [ ! -d "$SOURCE_DIR" ]; then
  echo "Error: Could not find skill source directory at $SOURCE_DIR" >&2
  exit 1
fi

MODE="global"
AGENT=""

for arg in "$@"; do
  case "$arg" in
    --project|-p)
      MODE="project"
      ;;
    --help|-h)
      sed -n '3,16p' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *)
      AGENT="$arg"
      ;;
  esac
done

install_to() {
  local target="$1"
  mkdir -p "$target/references" "$HOME/notes"
  cp -r "$SOURCE_DIR"/* "$target/"
  echo "  [OK] Installed /synapse -> $target"
}

if [ -z "$AGENT" ]; then
  echo "Select target agent to install /synapse ($MODE):"
  echo "  1) All supported agents (global)"
  echo "  2) Claude Code"
  echo "  3) Cursor"
  echo "  4) Antigravity"
  echo "  5) Gemini CLI"
  echo "  6) Windsurf"
  echo "  7) Cline"
  echo "  8) Codex / Generic Agents (~/.agents)"
  read -rp "Enter choice [1-8] (default: 1): " choice
  case "${choice:-1}" in
    1) AGENT="all" ;;
    2) AGENT="claude" ;;
    3) AGENT="cursor" ;;
    4) AGENT="antigravity" ;;
    5) AGENT="gemini" ;;
    6) AGENT="windsurf" ;;
    7) AGENT="cline" ;;
    8) AGENT="codex" ;;
    *) echo "Invalid choice." >&2; exit 1 ;;
  esac
fi

echo "Installing /synapse skill ($MODE mode)..."

case "$AGENT" in
  all)
    if [ "$MODE" = "project" ]; then
      install_to ".claude/skills/synapse"
      install_to ".cursor/skills/synapse"
      install_to ".agent/skills/synapse"
      install_to ".gemini/skills/synapse"
      install_to ".windsurf/skills/synapse"
      install_to ".cline/skills/synapse"
      install_to ".agents/skills/synapse"
    else
      install_to "$HOME/.claude/skills/synapse"
      install_to "$HOME/.cursor/skills/synapse"
      install_to "$HOME/.gemini/antigravity/skills/synapse"
      install_to "$HOME/.gemini/skills/synapse"
      install_to "$HOME/.codeium/windsurf/skills/synapse"
      install_to "$HOME/.cline/skills/synapse"
      install_to "$HOME/.agents/skills/synapse"
    fi
    ;;
  claude)
    [ "$MODE" = "project" ] && install_to ".claude/skills/synapse" || install_to "$HOME/.claude/skills/synapse"
    ;;
  cursor)
    [ "$MODE" = "project" ] && install_to ".cursor/skills/synapse" || install_to "$HOME/.cursor/skills/synapse"
    ;;
  antigravity)
    [ "$MODE" = "project" ] && install_to ".agent/skills/synapse" || install_to "$HOME/.gemini/antigravity/skills/synapse"
    ;;
  gemini)
    [ "$MODE" = "project" ] && install_to ".gemini/skills/synapse" || install_to "$HOME/.gemini/skills/synapse"
    ;;
  windsurf)
    [ "$MODE" = "project" ] && install_to ".windsurf/skills/synapse" || install_to "$HOME/.codeium/windsurf/skills/synapse"
    ;;
  cline)
    [ "$MODE" = "project" ] && install_to ".cline/skills/synapse" || install_to "$HOME/.cline/skills/synapse"
    ;;
  codex|agents)
    [ "$MODE" = "project" ] && install_to ".agents/skills/synapse" || install_to "$HOME/.agents/skills/synapse"
    ;;
  *)
    install_to "$AGENT"
    ;;
esac

echo ""
echo "Central knowledge vault ready at: $HOME/notes/"
echo "Open a new session in your agent and run: /synapse <topic>"
