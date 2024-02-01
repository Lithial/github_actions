# Circles Github Actions

This repo contains a couple of reusable actions used in common frontend github workflows.

Currently included are:

## Setup
All actions require a setup step to be run first. This action well allow them to run
``- uses: actions/checkout@v4 # Necessary to access local action``

```yml
    - uses: circles-learning-labs/github_actions/.github/actions/setup
      name: Setup Project
      with:
        node-version: '20'
```

- Build
```yml

      - uses: circles-learning-labs/github_actions/.github/actions/build
        name: Build Project
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} # The github secret token for pushing new build numbers to the branch
          INCREMENT_VERSION_NUMBER: false # Whether or not to increment the version number or not
```

- Write Changelog
```yml
      - uses: circles-learning-labs/github_actions/.github/actions/write-changelog
        name: Write Changelog
        with:
          PR_TITLE: ${{ github.event.pull_request.title }} # The title of the pull request
          PR_BODY: ${{ github.event.pull_request.body }} # The body of the pull request
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} # The github secret token for pushing the changelog to the branch
          CHANGELOG_FILE: "changes/CHANGELOG.md" # The name of the changelog file and where it should exist
```
