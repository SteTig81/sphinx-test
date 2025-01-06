Custom project for https://sphinx-performance.readthedocs.io/en/latest/.

# Installation

The following commands are valid for Ubuntu Linux based systems with bash:

## System tools setup

    xargs sudo apt-get -y install < apt-requirements-dev.txt

## Python setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements-dev.txt

## IDE setup

    https://code.visualstudio.com/docs/setup/linux
    Install python extension

# Execution

## sphinx-performance

    sphinx-performance --sphinx 8.1.3 --sphinx_needs 4.1.0 --project ./projects/needs --parallel 1 --parallel 4 --folders 2 --pages 5 --depth 2 --builder html --temp ./temp --keep

## profiling

    cd temp/tmpk4cke7ji  # example
    rm -rf _build && python3 -m cProfile -o profile.out ../../venv/bin/sphinx-build -b html -j 4 ./ ./_build --fail-on-warning
    snakeviz profile.out

## tracing

    cd temp/tmpk4cke7ji  # example
    rm -rf _build && python3 -m viztracer --tracer_entries 500000 ../../venv/bin/sphinx-build -b html -j 4 ./ ./_build --fail-on-warning
    viztracer result.json  # note: use chrome browser as firefox crashes for high tracer_entries values
