export const menuList = [{
  title: '首页',
  name: 'Home',
  path: '/home'
}, {
  name: 'Category',
  title: '表格',
  path: '/category',
  child: [{
    name: 'CategoryList',
    title: '分类列表',
    path: '/category/list'
  }, {
    name: 'CategoryAdd',
    title: '添加分类',
    path: '/category/add'
  }]
}]

