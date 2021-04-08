export const menuList = [{
  title: '首页',
  name: 'Home',
  path: '/home'
}, {
  name: 'Category',
  title: '分类',
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
},{
  name: 'Book',
  title: '书籍',
  path: '/book',
  child: [{
    name: 'BookList',
    title: '书籍列表',
    path: '/book/list'
  }, {
    name: 'BookAdd',
    title: '添加书籍',
    path: '/book/add'
  }]
}]

