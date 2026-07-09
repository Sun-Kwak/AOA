# Graph Routing

## Purpose

Define how AOA dynamically routes tasks between agents based on task state and capability,
rather than following a fixed hierarchical execution order.

---

## Scope

Covers:
- Routing graph structure (nodes = agents, edges = conditions)
- Dynamic next-agent selection based on task output
- Conditional branching rules
- Cycle prevention
- Entry and exit node definitions

---

## Why Graph Routing

Hierarchical delegation works well for predictable tasks.
Graph routing is needed when:
- The next agent depends on the result of the current agent.
- Multiple paths are possible depending on task state.
- Conditional branching is required mid-workflow.
- Loops or retries are part of the workflow design.

---

## TODO

Define routing graph schema.
Define condition evaluation rules.
Define cycle detection and prevention mechanism.
Define how graph state is persisted in Memory.
