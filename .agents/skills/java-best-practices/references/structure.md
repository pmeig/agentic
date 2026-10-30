# Java best practices: naming and layering

- Naming: classes by role (`AnnotationScanner`, `MojoService`, `OrderController`), verb-first methods, `UPPER_SNAKE` `private static final` constants, enum constants UPPER_SNAKE (PascalCase only when mirroring external names), no placeholder names (`MyMojo`, `toto`).
- Layering for applications: controller → service → repository: no repository in a controller, no web objects in a service.

Spring specifics: `spring-boot-best-practices`.
