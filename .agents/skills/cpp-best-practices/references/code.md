# C / C++ best practices: code

- **RAII for every resource**; no raw owning pointers or `new`/`delete`: `std::unique_ptr` (default), `std::shared_ptr` only for real shared ownership, references or `std::span`/`std::string_view` for non-owning access.
- Value semantics and `const` by default (`const` locals, `const&` parameters for big types, `constexpr`/`consteval` where possible), rule of zero; `[[nodiscard]]` on functions whose result matters.
- Errors: exceptions for exceptional failures, `std::expected<T, Error>` for expected ones (parsing, I/O, validation); never error codes ignored; `noexcept` on moves and destructors.
- Types: `enum class`, strong types for ids/units, `std::optional` for absence, `std::variant` + `std::visit` for closed sets, concepts to constrain templates, ranges/views for transformations, `std::format`/`std::print` instead of iostream formatting.
- Concurrency: `std::jthread` + `std::stop_token`, `std::mutex` with `std::scoped_lock`, atomics only with a clear memory-order reason; no data shared without synchronization.
- C: `const` correctness, sized types (`<stdint.h>`), bounds-checked APIs, every allocation paired with its free in the same module.
