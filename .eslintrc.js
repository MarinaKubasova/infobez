module.exports = {
  env: {
    node: true,
    commonjs: true,
    es2021: true,
  },
  extends: 'eslint:recommended',
  parserOptions: {
    ecmaVersion: 12,
  },
  rules: {
    'no-console': 'off', // Разрешить использование console.log
    'semi': ['error', 'always'], // Требовать точку с запятой в конце выражений
    // Другие правила могут быть добавлены по необходимости
  },
};
