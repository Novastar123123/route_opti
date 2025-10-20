# route_opti

A learning playground for building optimal routing tools. The project is primarily Python-based, with supporting experiments in C++ and mathematical explorations written in LaTeX.

## Repository Layout

- `src/route_opti/` – Python package that will eventually hold the production code.
- `tests/` – Automated tests for the Python package.
- `cpp/` – Space to practice and prototype C++ implementations of routing algorithms.
- `latex/` – LaTeX documents for working through the mathematics behind routing and optimization.

## Getting Started (Python)

1. Ensure you have Python 3.11+ available.
2. Create and activate a virtual environment.
3. Install the project in editable mode:
   ```bash
   pip install -e .[dev]
   ```
4. Run the example script to verify the environment:
   ```bash
   python -m route_opti
   ```

## Getting Started (C++)

The `cpp/` directory includes a simple CMake scaffold. Build it with:

```bash
cd cpp
cmake -S . -B build
cmake --build build
./build/route_opti_cpp
```

## Working with LaTeX

The `latex/` directory contains a starter document. Use your preferred TeX toolchain to compile it, for example:

```bash
cd latex
pdflatex notes.tex
```

Feel free to iterate on any or all of these areas as you explore Python, C++, and the mathematics of routing.
