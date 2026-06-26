## 1. Environment

- Ruby 4.0.5
- Gemfile 4.0.12
- Bundler 4.0.12

## 2. Install Gems via Gemfile and Bundler

```command
$ bundle install
$ bundle lock --add-checksums
```

## 3. Execution

```command
$ rake run_to_be_determined
```

## 4. Unit Test

```command
$ rake
```

## 5. Static Code Analysis

```command
$ rubocop
```

## 6. Type Checks

```command
$ rbs-inline --output sig/generated/ .
$ steep check
```
