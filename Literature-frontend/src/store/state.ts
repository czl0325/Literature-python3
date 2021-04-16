export interface GlobalDataProps {
  userInfo: UserInfo
}

export interface UserInfo {
  id?: number;
  openId?: string;
  userName?: string;
  gender?: number;
  city?: string;
  province?: string;
  country?: string;
  avatarUrl?: string;
  token?: string;
}

export default {
  userInfo: {}
}
