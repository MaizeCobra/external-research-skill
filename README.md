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

- ✅ **Universal compatibility** - Works in any modern agentic environment or CLI
- ✅ **Tool-agnostic** - Adapts to your platform's web search, URL fetch, and doc API tools
- ✅ **Time-aware searching** - Add current year to queries for fresh results
- ✅ **Real examples** - Based on actual research, not fabricated
- ✅ **Validation checklist** - Ensure research completeness
- ✅ **Citation format** - Proper source attribution

## Compatibility

This skill works with **any modern AI coding assistant** that supports:

- Web search capability (however named in your environment)
- URL/content fetching
- Optional: Documentation APIs like context7 MCP

Tested with: Claude Code, Cursor, Aider, Windsurf, GitHub Copilot, and more.

## License

MIT License - see [LICENSE](LICENSE)

## Contributing

PRs welcome! Add more examples in `examples/` or improve the methodology.
