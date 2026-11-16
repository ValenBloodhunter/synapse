#!/usr/bin/env bash
set -euo pipefail

# Universal installer for the /teachme skill across AI coding and research agents.
# Usage:
#   ./install.sh [agent|custom-path] [--project]
#
# Supported agents:
#   claude       -> ~/.claude/skills/teachme (or .claude/skills/teachme with --project)
#   cursor       -> ~/.cursor/skills/teachme (or .cursor/skills/teachme with --project)
#   antigravity  -> ~/.gemini/antigravity/skills/teachme (or .agent/skills/teachme with --project)
#   gemini       -> ~/.gemini/skills/teachme (or .gemini/skills/teachme with --project)
#   windsurf     -> ~/.codeium/windsurf/skills/teachme (or .windsurf/skills/teachme with --project)
#   cline        -> ~/.cline/skills/teachme (or .cline/skills/teachme with --project)
#   codex        -> ~/.agents/skills/teachme (or .agents/skills/teachme with --project)
#   all          -> Installs globally for all supported agents above

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/teachme"

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
  echo "  [OK] Installed /teachme -> $target"
}

if [ -z "$AGENT" ]; then
  echo "Select target agent to install /teachme ($MODE):"
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

echo "Installing /teachme skill ($MODE mode)..."

case "$AGENT" in
  all)
    if [ "$MODE" = "project" ]; then
      install_to ".claude/skills/teachme"
      install_to ".cursor/skills/teachme"
      install_to ".agent/skills/teachme"
      install_to ".gemini/skills/teachme"
      install_to ".windsurf/skills/teachme"
      install_to ".cline/skills/teachme"
      install_to ".agents/skills/teachme"
    else
      install_to "$HOME/.claude/skills/teachme"
      install_to "$HOME/.cursor/skills/teachme"
      install_to "$HOME/.gemini/antigravity/skills/teachme"
      install_to "$HOME/.gemini/skills/teachme"
      install_to "$HOME/.codeium/windsurf/skills/teachme"
      install_to "$HOME/.cline/skills/teachme"
      install_to "$HOME/.agents/skills/teachme"
    fi
    ;;
  claude)
    [ "$MODE" = "project" ] && install_to ".claude/skills/teachme" || install_to "$HOME/.claude/skills/teachme"
    ;;
  cursor)
    [ "$MODE" = "project" ] && install_to ".cursor/skills/teachme" || install_to "$HOME/.cursor/skills/teachme"
    ;;
  antigravity)
    [ "$MODE" = "project" ] && install_to ".agent/skills/teachme" || install_to "$HOME/.gemini/antigravity/skills/teachme"
    ;;
  gemini)
    [ "$MODE" = "project" ] && install_to ".gemini/skills/teachme" || install_to "$HOME/.gemini/skills/teachme"
    ;;
  windsurf)
    [ "$MODE" = "project" ] && install_to ".windsurf/skills/teachme" || install_to "$HOME/.codeium/windsurf/skills/teachme"
    ;;
  cline)
    [ "$MODE" = "project" ] && install_to ".cline/skills/teachme" || install_to "$HOME/.cline/skills/teachme"
    ;;
  codex|agents)
    [ "$MODE" = "project" ] && install_to ".agents/skills/teachme" || install_to "$HOME/.agents/skills/teachme"
    ;;
  *)
    install_to "$AGENT"
    ;;
esac

echo ""
echo "Central knowledge vault ready at: $HOME/notes/"
echo "Open a new session in your agent and run: /teachme <topic>"
