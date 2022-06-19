# Aegon Pension Scraper

## What?
A web scraper that extracts current pension valuations for an [Aegon GPP](https://extranet.secure.aegon.co.uk/login/showLoginPgAction.do?method=showLoginPage&loginStyle=PH).

This is a hobby project. Use at your own risk.

## Why?
Because the website is horrible. Run this on a schedule to build a pension value history.

## How?
This Python app uses Selenium to automate a headless web browser, log in and extract relevant data from the Aegon website. Current pension valuation and fund details are printed to STDOUT.

Runs in docker. Does not work on ARM architectures.

# To run

1. [Install docker](https://docs.docker.com/get-docker/)
2. Create credentials file (env)
3. Run `run.sh`

On success, writes output to STDOUT. On error, dumps current page HTML in `error/` directory to assist debugging.

## Credentials

Account username and password are passed to the container as environment variables:

```
PENSION_USERNAME=<my_email>
PENSION_PASSWORD=<my_password>
```

By default, `run.sh` loads these from a file named `env` in the project root directory.
