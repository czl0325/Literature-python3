module.exports = {
  root: true,
  parserOptions: {
    sourceType: 'module'
  },
  parser: 'babel-eslint',
  env: {
    browser: true,
    node: true,
    es6: true
  },
  extends: [
    // 'eslint:recommended',
    // 'plugin:vue/recommended',
    // 'plugin:vue/vue3-essential',
    // '@vue/typescript/recommended'
  ],
  // plugins: ["vue"],
  'rules': {
    'vue/no-multiple-template-root': 'off',
    'vue/singleline-html-element-content-newline': 'off',
    'vue/multiline-html-element-content-newline': 'off',
    'vue/max-attributes-per-line': 'off',
    'vue/no-v-model-argument': 'off',
    'no-multi-comp': 'off',
    'arrow-parens': 0,
    'generator-star-spacing': 0,
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    '@typescript-eslint/no-var-requires': 0,
    'no-undef': 0,
    'no-console': 'off',
    'space-before-function-paren': ["off", "never"],
    "strict": 'off',
    "no-implicit-coercion": 'off',
    "no-mixed-requires": [0, false],
    "no-multi-spaces": 0,
    "no-tabs": "off",
    'no-mixed-spaces-and-tabs': 0,
    "no-unused-vars": [
      2,
      {
        // 允许声明未使用变量
        "vars": "local",
        // 参数不检查
        "args": "none"
      }
    ],
    // 关闭语句强制分号结尾
    "semi": [0],
    // key值前面是否要有空格
    "key-spacing": [0, {
      "singleLine": {
        "beforeColon": false,
        "afterColon": true
      },
      "multiLine": {
        "beforeColon": true,
        "afterColon": true,
        "align": "colon"
      },
      // 空行最多不能超过100行
      "no-multiple-empty-lines": [0, {"max": 100}],
      // 数组第一个指定是否启用这个规则，第二个指定几个空格
      "indent":[1,2]
    }]
  }
}

