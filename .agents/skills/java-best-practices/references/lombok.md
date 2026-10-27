# Java best practices: Lombok (never write boilerplate by hand)

| Need | Annotation |
|---|---|
| Spring bean / service with dependencies | `@RequiredArgsConstructor` + `private final` fields (constructor injection, no `@Autowired`) |
| Logger | `@Slf4j` (`log.info("Found {} classes", count)` with placeholders, never string concatenation) |
| Immutable value class | `@Value` (all fields `private final`, getters, equals/hashCode/toString) + `@Builder` when > 3 fields or optional ones; `@With` for copies |
| Mutable class (JPA entity, `@ConfigurationProperties`) | `@Getter` `@Setter` `@NoArgsConstructor`; never `@Data` on a JPA entity (equals/hashCode on lazy relations, `toString` loops): write equals/hashCode on the id, `@ToString(onlyExplicitlyIncluded = true)` |
| Utility holder | `@UtilityClass` (or prefer instance beans) |
| Builder for a record or a class with many args | `@Builder(toBuilder = true)` |
| Checked exception rethrow | avoid `@SneakyThrows`: wrap in a domain exception with the cause |

- `@EqualsAndHashCode(callSuper = ...)` explicit on subclasses. `@NonNull` only where JSpecify/`Objects.requireNonNull` is not enough.
- Records are fine for small immutable DTOs (API payloads, events, query results); add `@Builder` on the record when it has many fields. Use a Lombok `@Value` class when you need inheritance-free immutability with custom methods, builders and validation together.

Lombok build setup (dependency, annotation processor, `lombok.config`): `references/setup.md`.
