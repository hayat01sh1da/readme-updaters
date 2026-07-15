## 1. Environment

- Ruby 4.0.6
- Gemfile 4.0.12
- Bundler 4.0.12

## 2. Install Gems via Gemfile and Bundler

```command
$ bundle install
$ bundle lock --add-checksums
```

## 3. Execution

```command
$ rake update_readme
========== Start Updating README ===========
========== Finish Updating README ===========
```

## 4. Unit Test

```command
$ rake
Run options: --seed 63787

# Running:

.

Finished in 0.001413s, 707.8218 runs/s, 707.8218 assertions/s.

1 runs, 1 assertions, 0 failures, 0 errors, 0 skips
```

## 5. Static Code Analysis

```command
$ rubocop
Inspecting 5 files
.....

5 files inspected, no offenses detected
```

## 6. Type Checks

```command
$ rbs-inline --output sig/generated/ .
🎉 Generated 2 RBS files under sig/generated
$ steep check
# Type checking files:

....

No type error detected. 🫖
```
