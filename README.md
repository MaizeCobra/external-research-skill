# External Research Skill

A comprehensive methodology for conducting external research during AI-assisted development. Ensures all external knowledge is gathered from authoritative sources, properly validated, version-aware, and correctly cited.

## Why This Skill?

Large Language Models have knowledge cutoffs and can hallucinate API details. This skill enforces **verified external research** using:

- 🔍 **Web Search** - Find official documentation
- 📄 **URL Fetching** - Read actual page content  
- 📚 **Documentation APIs** - Query structured docs (context7, etc.)

## Installation

```bash
# Using Vercel's skills CLI
npx skills add rohancode/external-research

# Or using add-skill
npx add-skill rohancode/external-research
```

## What's Included

```
external-research/
├── SKILL.md              # Main methodology & instructions
├── examples/
│   ├── fastapi-jwt-auth.md    # Real FastAPI research example
│   └── react-data-fetching.md # Real React research example
├── resources/
│   └── quick-reference.md     # Cheatsheet
└── scripts/
    └── get_current_time.py    # Time-aware search helper
```

## Key Features

- ✅ **Tool-agnostic** - Works with Claude Code, Cursor, Aider, Windsurf, etc.
- ✅ **Time-aware searching** - Add current year to queries for fresh results
- ✅ **Real examples** - Based on actual research, not fabricated
- ✅ **Validation checklist** - Ensure research completeness
- ✅ **Citation format** - Proper source attribution

## Quick Start

After installation, the skill teaches your AI agent to:

1. **Never trust model memory** for API signatures, defaults, or security patterns
2. **Search with the current year** (e.g., "FastAPI JWT 2026")
3. **Read official documentation** directly, not just search snippets
4. **Cite all sources** with URLs and versions
5. **Validate findings** with the included checklist

## Compatible Platforms

| Platform | Web Search | URL Fetch | Doc APIs |
|----------|------------|-----------|----------|
| Claude Code | `WebSearch` | `WebFetch` | MCP ✅ |
| Cursor | `@web` | Browser | MCP ✅ |
| Aider | `/web` | Webcrawl | - |
| Windsurf | Cascade | Web Fetch | MCP ✅ |
| GitHub Copilot | `@github #web` | URL Context | - |

## License

MIT License - see [LICENSE](LICENSE)

## Contributing

PRs welcome! Add more examples in `examples/` or improve the methodology.
