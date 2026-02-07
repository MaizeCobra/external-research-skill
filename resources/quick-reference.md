# External Research Quick Reference

A compact cheatsheet for the external research methodology.

---

## Tool Decision Tree

```
Need external information?
│
├─► What do you need?
│   │
│   ├─► Find documentation URLs → search_web
│   │   └─► Then read them → read_url_content
│   │
│   ├─► Version-specific API details → context7 MCP
│   │   └─► First: resolve-library-id
│   │   └─► Then: query-docs
│   │
│   ├─► Breaking changes/changelog → search_web
│   │   └─► Then read them → read_url_content
│   │
│   └─► Security advisories → search_web
│       └─► Then read them → read_url_content
```

---

## Quick Commands

### search_web

```bash
# Find official docs
search_web("[library] official documentation")

# Find specific feature docs  
search_web("[library] [version] [feature] tutorial")

# 🕐 TIME-AWARE SEARCHES (use current year!)
search_web("[library] best practices 2026")
search_web("[library] security vulnerabilities 2026")
search_web("[library] tutorial 2026")

# Find breaking changes
search_web("[library] breaking changes [old-version] to [new-version]")

# Find security issues
search_web("[library] CVE security advisory")

# Prioritize a domain
search_web("[query]", domain: "docs.example.com")
```

> 💡 **Pro Tip**: Run `python scripts/get_current_time.py --year` to get current year

### read_url_content

```
# Read any URL discovered via search
read_url_content("https://docs.example.com/api/feature")
```

### context7 MCP

```
# Step 1: Get library ID
mcp_context7_resolve-library-id("[library-name]", "[what you're trying to do]")
# Returns: /org/project

# Step 2: Query docs
mcp_context7_query-docs("/org/project", "[specific question about feature]")
```

---

## Common Library IDs

| Library | Context7 ID |
|---------|-------------|
| React | `/facebook/react` |
| Next.js | `/vercel/next.js` |
| FastAPI | `/fastapi/fastapi` |
| Express | `/expressjs/express` |
| Vue | `/vuejs/vue` |
| Django | `/django/django` |
| Flask | `/pallets/flask` |
| Prisma | `/prisma/prisma` |
| TypeORM | `/typeorm/typeorm` |

---

## Citation Template

```markdown
### Relevant Documentation

- [Page Title](https://url.com/path#section)
  - Version: X.Y.Z
  - Key Content: What you extracted
  - Why Needed: How it's used in implementation
  - Sourced via: search_web / read_url_content / context7 MCP
```

---

## Validation Checklist

Copy this into your research output:

```markdown
### Research Validation

- [ ] External APIs/libraries discovered via **search_web**
- [ ] Documentation pages read via **read_url_content**
- [ ] Framework behavior validated via **context7 MCP**
- [ ] Version numbers explicitly stated
- [ ] No undocumented or assumed behavior
```

---

## Never Trust Model Memory For

| ❌ Don't Assume | ✅ Always Verify |
|----------------|-----------------|
| API signatures | Exact params, types, returns |
| Default values | Current defaults for version |
| Available methods | What exists in target version |
| Security patterns | Current best practices |
| Config options | Valid keys and values |
| Import paths | Correct module structure |
| Breaking changes | What changed between versions |

---

## Research Workflow Summary

```
1. IDENTIFY
   └─► List all external dependencies and versions

2. RESEARCH  
   ├─► context7: resolve-library-id → query-docs
   ├─► search_web: find official documentation
   └─► read_url_content: extract actual content

3. DOCUMENT
   ├─► API signatures (exact, not paraphrased)
   ├─► Code examples (from official sources)
   ├─► Gotchas and warnings
   └─► Citations with URLs and versions

4. VALIDATE
   └─► Complete the validation checklist
```
