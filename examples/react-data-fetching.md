# Example: React Data Fetching Research

**This is a REAL research example** conducted using the external-research skill methodology with all three tools.

---

## Research Goal

Implement proper data fetching in React 18+ with loading states, error handling, and cleanup to prevent race conditions.

---

## Research Journey

### Step 1: Context7 MCP - Resolve Library ID

**Tool Used**: `mcp_context7_resolve-library-id`

```
mcp_context7_resolve-library-id("react", "useEffect data fetching async cleanup abort controller")
```

**Libraries Found**:

| Library | ID | Snippets | Reputation | Score |
|---------|-----|----------|------------|-------|
| React (react.dev) | `/websites/react_dev` | 5,574 | High | 89.2 |
| React 18 | `/websites/18_react_dev` | 3,921 | High | 82.6 |
| React Reference | `/websites/react_dev_reference` | 2,330 | High | 77.8 |
| React.dev (repo) | `/reactjs/react.dev` | 3,742 | High | 70.5 |

**Selected**: `/websites/react_dev` (highest score, most snippets)

---

### Step 2: Context7 MCP - Query Documentation

**Tool Used**: `mcp_context7_query-docs`

```
mcp_context7_query-docs("/websites/react_dev", "useEffect data fetching async cleanup AbortController race condition memory leak")
```

**Code Snippets Returned**:

1. **Data Fetching with Race Condition Cleanup** (from `react.dev/learn/you-might-not-need-an-effect`)

```javascript
function SearchResults({ query }) {
  const [results, setResults] = useState([]);
  const [page, setPage] = useState(1);
  useEffect(() => {
    let ignore = false;
    fetchResults(query, page).then(json => {
      if (!ignore) {
        setResults(json);
      }
    });
    return () => {
      ignore = true;
    };
  }, [query, page]);
  // ...
}
```

1. **Fixed Async Data Fetching with Cleanup** (from `react.dev/learn/synchronizing-with-effects`)

```javascript
useEffect(() => {
  let ignore = false;
  setBio(null);
  fetchBio(person).then(result => {
    if (!ignore) {
      setBio(result);
    }
  });
  return () => {
    ignore = true;
  }
}, [person]);
```

1. **Async/Await Pattern with Cleanup** (from `react.dev/reference/react/useEffect`)

```javascript
useEffect(() => {
  async function startFetching() {
    setBio(null);
    const result = await fetchBio(person);
    if (!ignore) {
      setBio(result);
    }
  }

  let ignore = false;
  startFetching();
  return () => {
    ignore = true;
  }
}, [person]);
```

1. **Dependent Data Fetching Pattern** (from `react.dev/learn/lifecycle-of-reactive-effects`)

```javascript
// Multiple useEffects for dependent data
useEffect(() => {
  let ignore = false;
  fetchData('/planets').then(result => {
    if (!ignore) {
      setPlanetList(result);
      setPlanetId(result[0].id);
    }
  });
  return () => { ignore = true; }
}, []);

useEffect(() => {
  if (planetId === '') return;
  
  let ignore = false;
  fetchData('/planets/' + planetId + '/places').then(result => {
    if (!ignore) {
      setPlaceList(result);
    }
  });
  return () => { ignore = true; }
}, [planetId]);
```

---

### Step 3: Web Search for Additional Context

**Tool Used**: `search_web`

```
search_web("React 18 useEffect data fetching async cleanup abort controller", domain: "react.dev")
```

**Key Findings**:

- AbortController is essential for cleanup in React
- React Strict Mode runs Effects twice in development to detect cleanup issues
- The `ignore` flag pattern is the official React recommendation
- Race conditions occur when network responses arrive in different order than requests

---

### Step 4: Reading Official React Documentation

**Tool Used**: `read_url_content`

```
read_url_content("https://react.dev/reference/react/useEffect")
```

**Chunks Read**:

- Position 21: Fetching data with Effects - main pattern
- Position 22: Downsides of fetching in Effects, alternatives

**Official React Guidance Extracted**:

> "This ensures your code doesn't suffer from 'race conditions': network responses may arrive in a different order than you sent them."

**Recommended Alternatives to Manual useEffect Fetching**:

- Framework data fetching (Next.js, Remix)
- TanStack Query (React Query)
- useSWR (Vercel)
- React Router 6.4+

**Downsides of Manual useEffect Fetching (from docs)**:

1. Effects don't run on server (SSR issues)
2. Creates "network waterfalls" (sequential fetching)
3. No preloading or caching built-in
4. Lots of boilerplate for race condition handling

---

## Verified Findings

### The `ignore` Flag Pattern (Official React Pattern)

This is the **official React-recommended pattern** for preventing race conditions:

```javascript
import { useState, useEffect } from 'react';

function MyComponent({ userId }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let ignore = false;  // ← Race condition prevention
    
    setLoading(true);
    setError(null);
    
    fetchUserData(userId)
      .then(result => {
        if (!ignore) {  // ← Only update if not stale
          setData(result);
          setLoading(false);
        }
      })
      .catch(err => {
        if (!ignore) {
          setError(err);
          setLoading(false);
        }
      });

    return () => {
      ignore = true;  // ← Cleanup marks request as stale
    };
  }, [userId]);

  // ...
}
```

### Why `ignore` Flag vs AbortController?

| Approach | Pros | Cons |
|----------|------|------|
| **`ignore` flag** | Simple, works with any async operation | Doesn't cancel network request |
| **AbortController** | Actually cancels fetch request | More complex, only works with fetch |

**From official docs**: The `ignore` flag pattern is the recommended default approach. AbortController is optional for optimization.

### API Signature (from official docs)

```typescript
useEffect(setup: () => (() => void) | void, dependencies?: any[]): void

// setup: Function that:
//   - Runs after render
//   - Optionally returns a cleanup function
// dependencies:
//   - [] = run once on mount only
//   - [dep1, dep2] = run when deps change
//   - omitted = run on every render (usually wrong!)
```

### Critical Gotchas Discovered

| Gotcha | Details | Source |
|--------|---------|--------|
| ⚠️ NO async effect directly | `useEffect(async () => {})` is NOT allowed | Context7, react.dev |
| ⚠️ Strict Mode runs twice | Effects mount/unmount/mount in development | react.dev |
| ⚠️ Must return cleanup sync | Cleanup function cannot be async | react.dev |
| ⚠️ Race conditions are real | Fast navigation can cause stale data | Context7 snippets |
| ⚠️ Dependencies matter | Missing deps = stale closures, wrong deps = infinite loops | react.dev |

### Common Anti-Patterns (validated via research)

```javascript
// ❌ WRONG: async effect directly (React will warn)
useEffect(async () => {
  const data = await fetch(url);
}, [url]);

// ❌ WRONG: no cleanup (race conditions possible)
useEffect(() => {
  fetch(url).then(r => r.json()).then(setData);
}, [url]);

// ❌ WRONG: no dependencies (runs on every render)
useEffect(() => {
  fetch(url).then(r => setData(r));
});
```

---

## Citations

| Source | Content | Tool Used |
|--------|---------|-----------|
| [useEffect Reference](https://react.dev/reference/react/useEffect) | Official API docs, data fetching section | read_url_content |
| [Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects) | Cleanup function pattern | context7 MCP |
| [You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect) | Race condition fix pattern | context7 MCP |
| [Lifecycle of Reactive Effects](https://react.dev/learn/lifecycle-of-reactive-effects) | Dependent data fetching | context7 MCP |

---

## Research Validation Checklist

- [x] External APIs/libraries discovered via **search_web**
- [x] Documentation pages read via **read_url_content**
- [x] Framework behavior validated via **context7 MCP** ✅
- [x] Version numbers explicitly stated (React 18+)
- [x] No undocumented or assumed behavior
- [x] All citations include source URLs
- [x] Code examples from official sources
- [x] Anti-patterns documented

---

## Key Takeaways from Real Research

1. **Context7 is extremely valuable**: Returned 4 different code snippets from multiple React docs pages, each showing the same `ignore` flag pattern - proving this IS the official recommendation.

2. **`ignore` flag > AbortController for simplicity**: The official React docs use the `ignore` flag pattern, not AbortController. AbortController is only mentioned as an optional optimization.

3. **React recommends NOT using useEffect for data fetching** when possible: The docs explicitly recommend TanStack Query, useSWR, or framework-level solutions instead.

4. **Strict Mode behavior is intentional**: The double-mount in development is designed to catch cleanup issues - not a bug!

5. **Multiple sources confirm the pattern**: Context7 returned the same `ignore` flag pattern from 4 different doc pages, strongly validating this is the correct approach.
