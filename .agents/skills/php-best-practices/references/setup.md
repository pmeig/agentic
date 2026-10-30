# PHP best practices: setup (PHP version, Composer, tooling, framework)

- Latest PHP (8.5) declared in `composer.json` (`"php": ">=8.5"`), Composer with a committed `composer.lock`, PSR-4 autoload (`App\\` → `src/`).
- `declare(strict_types=1);` at the top of every file; PER Coding Style (PSR-12 successor) with PHP-CS-Fixer or ECS; PHPStan (level max) or Psalm in CI; Rector for upgrades.
- Framework: Symfony (preferred for typed, explicit DI) or Laravel when the project uses it; follow the framework's directory conventions.
