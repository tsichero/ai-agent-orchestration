# Agent Architecture

## Control flow

The orchestrator owns the workflow and delegates bounded responsibilities to components.

## Safety boundary

Tools should expose explicit contracts and validate their inputs. External side effects should require additional authorization controls before production use.

## Demo status

The current implementation is deterministic and does not call an external LLM or execute real side-effecting tools. It exists to demonstrate orchestration structure and testable routing.
