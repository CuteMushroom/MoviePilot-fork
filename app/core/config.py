import secrets
import sys
import threading
from pathlib import Path
from typing import Optional, List

from pydantic import BaseSettings, validator

from app.utils.system import SystemUtils


class Settings(BaseSettings):
    """
    系统配置类
    """
    # 项目名称
    PROJECT_NAME = "MoviePilot"
    # 域名 格式；https://movie-pilot.org
    APP_DOMAIN: str = ""
    # API路径
    API_V1_STR: str = "/api/v1"
    # 前端资源路径
    FRONTEND_PATH: str = "/public"
    # 密钥
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 允许的域名
    ALLOWED_HOSTS: list = ["*"]
    # TOKEN过期时间
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # 时区
    TZ: str = "Asia/Shanghai"
    # API监听地址
    HOST: str = "0.0.0.0"
    # API监听端口
    PORT: int = 3001
    # 前端监听端口
    NGINX_PORT: int = 3000
    # 是否调试模式
    DEBUG: bool = False
    # 是否开发模式
    DEV: bool = False
    # 是否开启插件热加载
    PLUGIN_AUTO_RELOAD: bool = False
    # 配置文件目录
    CONFIG_DIR: Optional[str] = None
    # 超级管理员
    SUPERUSER: str = "admin"
    # API密钥，需要更换
    API_TOKEN: str = "moviepilot"
    # 登录页面电影海报,tmdb/bing
    WALLPAPER: str = "tmdb"
    # 网络代理 IP:PORT
    PROXY_HOST: Optional[str] = None
    # 媒体搜索来源 themoviedb/douban/bangumi，多个用,分隔
    SEARCH_SOURCE: str = "themoviedb,douban,bangumi"
    # 媒体识别来源 themoviedb/douban
    RECOGNIZE_SOURCE: str = "themoviedb"
    # 刮削来源 themoviedb/douban
    SCRAP_SOURCE: str = "themoviedb"
    # 新增已入库媒体是否跟随TMDB信息变化
    SCRAP_FOLLOW_TMDB: bool = True
    # TMDB图片地址
    TMDB_IMAGE_DOMAIN: str = "image.tmdb.org"
    # TMDB API地址
    TMDB_API_DOMAIN: str = "api.themoviedb.org"
    # TMDB API Key
    TMDB_API_KEY: str = "db55323b8d3e4154498498a75642b381"
    # TVDB API Key
    TVDB_API_KEY: str = "6b481081-10aa-440c-99f2-21d17717ee02"
    # Fanart开关
    FANART_ENABLE: bool = True
    # Fanart API Key
    FANART_API_KEY: str = "d2d31f9ecabea050fc7d68aa3146015f"
    # 支持的后缀格式
    RMT_MEDIAEXT: list = ['.mp4', '.mkv', '.ts', '.iso',
                          '.rmvb', '.avi', '.mov', '.mpeg',
                          '.mpg', '.wmv', '.3gp', '.asf',
                          '.m4v', '.flv', '.m2ts', '.strm',
                          '.tp', '.f4v']
    # 支持的字幕文件后缀格式
    RMT_SUBEXT: list = ['.srt', '.ass', '.ssa', '.sup']
    # 下载器临时文件后缀
    DOWNLOAD_TMPEXT: list = ['.!qB', '.part']
    # 支持的音轨文件后缀格式
    RMT_AUDIO_TRACK_EXT: list = ['.mka']
    # 索引器
    INDEXER: str = "builtin"
    # 订阅模式
    SUBSCRIBE_MODE: str = "spider"
    # RSS订阅模式刷新时间间隔（分钟）
    SUBSCRIBE_RSS_INTERVAL: int = 30
    # 订阅搜索开关
    SUBSCRIBE_SEARCH: bool = False
    # 用户认证站点
    AUTH_SITE: str = ""
    # 交互搜索自动下载用户ID，使用,分割
    AUTO_DOWNLOAD_USER: Optional[str] = None
    # 种子标签
    TORRENT_TAG: str = "MOVIEPILOT"
    # 下载站点字幕
    DOWNLOAD_SUBTITLE: bool = True
    # CookieCloud是否启动本地服务
    COOKIECLOUD_ENABLE_LOCAL: Optional[bool] = False
    # CookieCloud服务器地址
    COOKIECLOUD_HOST: str = "https://movie-pilot.org/cookiecloud"
    # CookieCloud用户KEY
    COOKIECLOUD_KEY: Optional[str] = None
    # CookieCloud端对端加密密码
    COOKIECLOUD_PASSWORD: Optional[str] = None
    # CookieCloud同步间隔（分钟）
    COOKIECLOUD_INTERVAL: Optional[int] = 60 * 24
    # CookieCloud同步黑名单，多个域名,分割
    COOKIECLOUD_BLACKLIST: Optional[str] = None
    # OCR服务器地址
    OCR_HOST: str = "https://movie-pilot.org"
    # CookieCloud对应的浏览器UA
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
    # 电视剧动漫的分类genre_ids
    ANIME_GENREIDS = [16]
    # 电影重命名格式
    MOVIE_RENAME_FORMAT: str = "{{title}}{% if year %} ({{year}}){% endif %}" \
                               "/{{title}}{% if year %} ({{year}}){% endif %}{% if part %}-{{part}}{% endif %}{% if videoFormat %} - {{videoFormat}}{% endif %}" \
                               "{{fileExt}}"
    # 电视剧重命名格式
    TV_RENAME_FORMAT: str = "{{title}}{% if year %} ({{year}}){% endif %}" \
                            "/Season {{season}}" \
                            "/{{title}} - {{season_episode}}{% if part %}-{{part}}{% endif %}{% if episode %} - 第 {{episode}} 集{% endif %}" \
                            "{{fileExt}}"
    # 转移时覆盖模式
    OVERWRITE_MODE: str = "size"
    # 大内存模式
    BIG_MEMORY_MODE: bool = False
    # 插件市场仓库地址，多个地址使用,分隔，地址以/结尾
    PLUGIN_MARKET: str = "https://github.com/jxxghp/MoviePilot-Plugins,https://github.com/thsrite/MoviePilot-Plugins,https://github.com/honue/MoviePilot-Plugins,https://github.com/InfinityPacer/MoviePilot-Plugins"
    # Github token，提高请求api限流阈值 ghp_****
    GITHUB_TOKEN: Optional[str] = None
    # Github代理服务器，格式：https://mirror.ghproxy.com/
    GITHUB_PROXY: Optional[str] = ''
    # 自动检查和更新站点资源包（站点索引、认证等）
    AUTO_UPDATE_RESOURCE: bool = True
    # 元数据识别缓存过期时间（小时）
    META_CACHE_EXPIRE: int = 0
    # 是否启用DOH解析域名
    DOH_ENABLE: bool = True
    # 搜索多个名称
    SEARCH_MULTIPLE_NAME: bool = False
    # 订阅数据共享
    SUBSCRIBE_STATISTIC_SHARE: bool = True
    # 插件安装数据共享
    PLUGIN_STATISTIC_SHARE: bool = True
    # 服务器地址，对应 https://github.com/jxxghp/MoviePilot-Server 项目
    MP_SERVER_HOST: str = "https://movie-pilot.org"

    @validator("SUBSCRIBE_RSS_INTERVAL",
               "COOKIECLOUD_INTERVAL",
               "META_CACHE_EXPIRE",
               pre=True, always=True)
    def convert_int(cls, value):
        if not value:
            return 0
        try:
            return int(value)
        except (ValueError, TypeError):
            raise ValueError(f"{value} 格式错误，不是有效数字！")

    @property
    def INNER_CONFIG_PATH(self):
        return self.ROOT_PATH / "config"

    @property
    def CONFIG_PATH(self):
        if self.CONFIG_DIR:
            return Path(self.CONFIG_DIR)
        elif SystemUtils.is_docker():
            return Path("/config")
        elif SystemUtils.is_frozen():
            return Path(sys.executable).parent / "config"
        return self.ROOT_PATH / "config"

    @property
    def TEMP_PATH(self):
        return self.CONFIG_PATH / "temp"

    @property
    def ROOT_PATH(self):
        return Path(__file__).parents[2]

    @property
    def PLUGIN_DATA_PATH(self):
        return self.CONFIG_PATH / "plugins"

    @property
    def LOG_PATH(self):
        return self.CONFIG_PATH / "logs"

    @property
    def COOKIE_PATH(self):
        return self.CONFIG_PATH / "cookies"

    @property
    def CACHE_CONF(self):
        if self.BIG_MEMORY_MODE:
            return {
                "tmdb": 1024,
                "refresh": 50,
                "torrents": 100,
                "douban": 512,
                "fanart": 512,
                "meta": (self.META_CACHE_EXPIRE or 168) * 3600
            }
        return {
            "tmdb": 256,
            "refresh": 30,
            "torrents": 50,
            "douban": 256,
            "fanart": 128,
            "meta": (self.META_CACHE_EXPIRE or 72) * 3600
        }

    @property
    def PROXY(self):
        if self.PROXY_HOST:
            return {
                "http": self.PROXY_HOST,
                "https": self.PROXY_HOST,
            }
        return None

    @property
    def PROXY_SERVER(self):
        if self.PROXY_HOST:
            return {
                "server": self.PROXY_HOST
            }

    @property
    def GITHUB_HEADERS(self):
        """
        Github请求头
        """
        if self.GITHUB_TOKEN:
            return {
                "Authorization": f"Bearer {self.GITHUB_TOKEN}"
            }
        return {}

    @property
    def VAPID(self):
        return {
            "subject": f"mailto:{self.SUPERUSER}@movie-pilot.org",
            "publicKey": "BH3w49sZA6jXUnE-yt4jO6VKh73lsdsvwoJ6Hx7fmPIDKoqGiUl2GEoZzy-iJfn4SfQQcx7yQdHf9RknwrL_lSM",
            "privateKey": "JTixnYY0vEw97t9uukfO3UWKfHKJdT5kCQDiv3gu894"
        }

    def MP_DOMAIN(self, url: str = None):
        if not self.APP_DOMAIN:
            return None
        domain = self.APP_DOMAIN.rstrip("/")
        if not domain.startswith("http"):
            domain = "http://" + domain
        if not url:
            return domain
        return domain + "/" + url.lstrip("/")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.CONFIG_PATH as p:
            if not p.exists():
                p.mkdir(parents=True, exist_ok=True)
            if SystemUtils.is_frozen():
                if not (p / "app.env").exists():
                    SystemUtils.copy(self.INNER_CONFIG_PATH / "app.env", p / "app.env")
        with self.TEMP_PATH as p:
            if not p.exists():
                p.mkdir(parents=True, exist_ok=True)
        with self.LOG_PATH as p:
            if not p.exists():
                p.mkdir(parents=True, exist_ok=True)
        with self.COOKIE_PATH as p:
            if not p.exists():
                p.mkdir(parents=True, exist_ok=True)

    class Config:
        case_sensitive = True


class GlobalVar(object):
    """
    全局标识
    """
    # 系统停止事件
    STOP_EVENT: threading.Event = threading.Event()
    # webpush订阅
    SUBSCRIPTIONS: List[dict] = []

    def stop_system(self):
        """
        停止系统
        """
        self.STOP_EVENT.set()

    def is_system_stopped(self):
        """
        是否停止
        """
        return self.STOP_EVENT.is_set()

    def get_subscriptions(self):
        """
        获取webpush订阅
        """
        return self.SUBSCRIPTIONS

    def push_subscription(self, subscription: dict):
        """
        添加webpush订阅
        """
        self.SUBSCRIPTIONS.append(subscription)


# 实例化配置
settings = Settings(
    _env_file=Settings().CONFIG_PATH / "app.env",
    _env_file_encoding="utf-8"
)

# 全局标识
global_vars = GlobalVar()
