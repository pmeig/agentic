# Ruby / Rails best practices: setup

- Latest Ruby (`.ruby-version`) and Rails 8, Bundler with a committed `Gemfile.lock`, RuboCop (`rubocop-rails`, `rubocop-rspec`) and Brakeman in CI, `bundler-audit` for dependencies.
- Rails 8 defaults where they fit: Solid Queue/Cache/Cable, Propshaft, Kamal for deployment, built-in authentication generator.
