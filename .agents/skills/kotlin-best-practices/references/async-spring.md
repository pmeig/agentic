# Kotlin best practices: coroutines and Spring injection

- Coroutines (apps/Android): `suspend` functions, structured concurrency (`coroutineScope`, viewModelScope), `Dispatchers.IO` injected for testability, `Flow`/`StateFlow` for streams; no `GlobalScope`, no `runBlocking` in production code. Reactive Spring code: Reactor `Mono`/`Flux` or coroutines, not both mixed in one flow.
- Spring injection: primary constructor with `private val` parameters; never `@Autowired lateinit` (only `lateinit` for `*Aware` callbacks).

Spring: `spring-boot-best-practices`.
