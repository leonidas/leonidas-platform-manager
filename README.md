# Leonidas Platform Manager

Work in progress.

Answers questions such as

* What is server `foobar.qa.leonidasoy.fi` doing? Is it still needed, can I terminate it?
* Where is Foobar XYZ running?
* Who pays the bill for `foobar.qa.leonidasoy.fi`? If we were to bill it, what are the costs?

## Getting started

    docker-compose up

Open http://localhost:8000 in your browser. Username is `admin`, password is `secret`.

Running tests:

    alias dc-test="docker-compose --file=docker-compose.test.yml up --abort-on-container-exit --exit-code-from=test"
    dc-test
