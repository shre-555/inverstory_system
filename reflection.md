#### 1. Which issues were the easiest to fix, and which were the hardest? Why?

* **Easiest fixes:**

  * Replacing general `except:` blocks with specific exceptions like `KeyError` or `FileNotFoundError` was straightforward because the context made it clear which errors were likely to occur.
  * Using **f-strings** instead of string concatenation or `%` formatting improved readability and was a simple mechanical change.
  * Fixing **line length (E501)** issues only required minor formatting adjustments.

* **Hardest fixes:**

  * Refactoring to avoid using `global` variables was trickier since it required rethinking how data was shared between functions.
  * Adding **input validation** for multiple parameter types needed careful handling to avoid breaking existing functionality.



#### 2. Did the static analysis tools report any false positives? If so, describe one example.

* One potential **false positive** was the warning about the use of `global stock_data`. While it’s usually discouraged, in this small standalone script, it was necessary for maintaining state without using classes or dependency injection. The warning was valid in general but not practically harmful in this limited context.


#### 3. How would you integrate static analysis tools into your actual software development workflow?

* I would integrate **Pylint**, **Flake8**, and **Bandit** into a **CI pipeline** (e.g., GitHub Actions) to automatically check for issues on every commit or pull request.
* During local development, I would set up **pre-commit hooks** so that code is linted and security-checked before being committed.
* Developers could also use IDE integrations for real-time feedback, reducing the number of issues that reach CI.


#### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

* **Code readability:** Improved through consistent formatting, f-strings, and clear exception handling.
* **Robustness:** Better error handling and input validation made the program less likely to crash due to bad input or missing files.
* **Maintainability:** The structured logging and reduced use of globals made the script easier to extend and debug in the future.
* **Security:** Removing dangerous functions like `eval()` and catching specific exceptions reduced security risks.

