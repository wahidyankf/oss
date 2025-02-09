module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      [
        'build',
        'chore',
        'ci',
        'docs',
        'feat',
        'fix',
        'perf',
        'refactor',
        'revert',
        'style',
        'test',
      ],
    ],
    'type-case': [2, 'always', 'lowercase'],
    'type-empty': [2, 'never'],
    'scope-case': [2, 'always', 'lowercase'],
    'subject-case': [2, 'always', 'sentence-case'],
    'subject-empty': [2, 'never'],
    'subject-max-length': [2, 'always', 72],
    'header-max-length': [2, 'always', 100],
  },
};
