export interface CategoryModel {
  cate_id?: number,
  cate_name: string,
  cate_icon?: string
}

export interface BookModel {
  book_id: number;
  book_name: string;
  cate_id: number;
  cate_name: string;
  channel_type?: number;
  author_name: string;
  chapter_num?: number;
  is_publish?: number;
  status?: number;
  cover?: string;
  intro: string;
  word_count: number;
  showed?: number;
  channel_name?: string;
  channel_url?: string;
  ranking?: number;
  short_des?: string;

  collect_count?: number;
  heat?: number;
}
