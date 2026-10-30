# PHP best practices: code (types, DTOs, errors)

- `final readonly class` for services and value objects, backed `enum` for fixed sets, typed properties, union/intersection types, `never`, first-class callables; the pipe operator `|>` (8.5) for linear transformations; `#[\NoDiscard]` on functions whose result must be used; property hooks/asymmetric visibility (8.4) instead of getters/setters boilerplate.
- DTOs for input/output mapped and validated at the edge (Symfony Validator / Form Requests), never raw arrays across layers.
- Errors: domain exceptions extending a project base exception, one handler mapping them to RFC 9457 problem responses; never `@` error suppression.
