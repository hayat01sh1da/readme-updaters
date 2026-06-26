## 1. Environment

- Python 3.14.6
- pip 26.1.2

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

```command
$ invoke run_to_be_determined
```

## 4. Unit Test

```command
$ invoke
```

## 5. Static Code Analysis

```command
$ flake8 .
$ autoflake8 --in-place --remove-duplicate-keys --remove-unused-variables --recursive .
$ autopep8 --in-place --aggressive --aggressive --recursive .
```

## 6. Type Checks

```command
$ mypy .
```
