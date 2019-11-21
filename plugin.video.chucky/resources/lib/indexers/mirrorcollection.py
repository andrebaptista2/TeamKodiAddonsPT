import os,sys,re,json,urllib,urlparse,datetime,base64

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?',''))) if len(sys.argv) > 1 else dict()

action = params.get('action')


class MirrorcollectionBox:
    def __init__(self):
        self.list = []

        self.tmdb_link = 'https://api.themoviedb.org'
        self.trakt_link = 'https://api.trakt.tv'
        self.imdb_link = 'https://www.imdb.com'
        self.tmdb_key = control.setting('tm.user')
        if self.tmdb_key == '' or self.tmdb_key == None:
            self.tmdb_key = '0049795edb57568b95240bc9e61a9dfc'
        self.datetime = (datetime.datetime.utcnow() - datetime.timedelta(hours = 5))
        self.systime = (self.datetime).strftime('%Y%m%d%H%M%S%f')
        self.trakt_user = control.setting('trakt.user').strip()
        self.lang = control.apiLanguage()['trakt']
        self.imdb_user = control.setting('imdb.user').replace('ur', '')
        self.tmdb_lang = 'en'
        self.today_date = (self.datetime).strftime('%Y-%m-%d')
        self.month_date = (self.datetime - datetime.timedelta(days = 30)).strftime('%Y-%m-%d')
        self.year_date = (self.datetime - datetime.timedelta(days = 365)).strftime('%Y-%m-%d')
        self.tmdb_info_link = 'https://api.themoviedb.org/3/movie/%s?api_key=%s&language=%s&append_to_response=credits,releases,external_ids' % ('%s', self.tmdb_key, self.tmdb_lang)
        self.imdb_by_query = 'https://www.omdbapi.com/?t=%s&y=%s'
        self.imdbinfo = 'https://www.omdbapi.com/?i=%s&plot=short&r=json'
        self.tmdb_image = 'https://image.tmdb.org/t/p/original'
        self.tmdb_poster = 'https://image.tmdb.org/t/p/w500'
        self.tm_user = control.setting('tm.user')
        self.fanart_tv_user = control.setting('fanart.tv.user')
        self.user = str(control.setting('fanart.tv.user')) + str(control.setting('tm.user'))
        self.lang = control.apiLanguage()['trakt']

        self.search_link = 'https://api.trakt.tv/search/movie?limit=20&page=1&query='
        self.fanart_tv_art_link = 'https://webservice.fanart.tv/v3/movies/%s'
        self.fanart_tv_level_link = 'https://webservice.fanart.tv/v3/level'
        self.tm_art_link = 'https://api.themoviedb.org/3/movie/%s/images?api_key=%s&language=en-US&include_image_language=en,%s,null' % ('%s', self.tmdb_key, self.lang)
        self.tm_img_link = 'https://image.tmdb.org/t/p/w%s%s'

        self.traktlists_link = 'https://api.trakt.tv/users/me/lists'
        self.traktlikedlists_link = 'https://api.trakt.tv/users/likes/lists?limit=1000000'
        self.traktlist_link = 'https://api.trakt.tv/users/%s/lists/%s/items'
        self.traktcollection_link = 'https://api.trakt.tv/users/me/collection/movies'
        self.traktwatchlist_link = 'https://api.trakt.tv/users/me/watchlist/movies'
        self.traktfeatured_link = 'https://api.trakt.tv/recommendations/movies?limit=40'
        self.trakthistory_link = 'https://api.trakt.tv/users/me/history/movies?limit=40&page=1'
        self.imdblists_link = 'https://www.imdb.com/user/ur%s/lists?tab=all&sort=modified:desc&filter=titles' % self.imdb_user
        self.imdblist_link = 'https://www.imdb.com/list/%s/?view=detail&sort=title:asc&title_type=feature,short,tv_movie,tv_special,video,documentary,game&start=1'
        self.imdblist2_link = 'https://www.imdb.com/list/%s/?view=detail&sort=created:desc&title_type=feature,short,tv_movie,tv_special,video,documentary,game&start=1'
        self.imdbwatchlist_link = 'https://www.imdb.com/user/ur%s/watchlist?sort=alpha,asc' % self.imdb_user
        self.imdbwatchlist2_link = 'https://www.imdb.com/user/ur%s/watchlist?sort=date_added,desc' % self.imdb_user


	self.addDirectoryItem('Test TMDB Mirror', 'collections&url=moviemirror', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
	self.addDirectoryItem('Christmas movies', 'collections&url=xmasmovies', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
	self.endDirectory()


