# Continuous Integration (CI) Best Practices

This document outlines the best practices implemented in our GitHub Actions CI workflow to ensure efficient, reliable, and maintainable automation.

## 1. **Trigger Workflows Only When Necessary**
- The workflow is triggered only on changes to the `lab3` branch.
- It runs **only when files inside `app_python/` are modified**.
- This prevents unnecessary workflow executions and saves CI resources.

## 2. **Use Fail-Fast Strategy**
- The `fail-fast: true` setting ensures that if one job in a matrix fails, all remaining jobs stop immediately.
- This saves execution time and provides quicker feedback to developers.

<!-- ## 3. **Define a Python Version Matrix**
- The workflow originally had a mistake where it referenced an undefined `matrix.python-version`.
- Instead, a **fixed Python version (3.11) was set** to avoid errors.
- If multiple versions need testing, a matrix strategy can be implemented:
  ```yaml
  strategy:
    matrix:
      python-version: [3.9, 3.10, 3.11] -->
  <!-- ``` -->
  <!-- This ensures compatibility across different Python environments. -->

## 4. **Use Dependency Caching for Faster Builds**
- **Pip dependencies are cached** to avoid redundant installations across workflow runs.
- Implemented caching with:
  ```yaml
  - name: Cache Python dependencies
    uses: actions/cache@v3
    with:
      path: ~/.cache/pip
      key: ${{ runner.os }}-pip-3.11-${{ hashFiles('**/requirements.txt') }}
      restore-keys: |
        ${{ runner.os }}-pip-3.11-
  ```
- This speeds up dependency installation significantly.

## 5. **Ensure Code Checkout Before Any Steps**
- The `checkout` step is **required before accessing the repository**.
- Initially, the `build-and-push-docker` job was missing the `Checkout Code` step.
- Added:
  ```yaml
  - name: Checkout Code
    uses: actions/checkout@v3
  ```
  Without this, subsequent steps would fail due to missing code files.

<!-- ## 6. **Use Relative Paths Instead of Absolute Paths**
- The original workflow used absolute paths like:
  ```yaml
  cd /home/runner/work/devops/devops/app_python
  ```
- This was replaced with relative paths:
  ```yaml
  cd app_python
  ```
- This improves portability and avoids hardcoded directory issues. -->

By following these best practices, the CI workflow is now **faster, more efficient, and easier to maintain**.

