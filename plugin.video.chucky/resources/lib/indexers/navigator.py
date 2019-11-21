# -*- coding: utf-8 -*-




import os,base64,sys,urllib2,urlparse,xbmc,xbmcaddon,xbmcgui
from resources.lib.modules import control,cache,trakt

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1]) ; control.moderator()
artPath = control.artPath() ; addonFanart = control.addonFanart()
imdbCredentials = False if control.setting('imdb.user') == '' else True
traktCredentials = trakt.getTraktCredentialsInfo()
traktIndicators = trakt.getTraktIndicatorsInfo()
queueMenu = control.lang(32065).encode('utf-8')

DBIRDSTAT = (xbmcaddon.Addon('script.module.resolveurl').getSetting('RealDebridResolver_enabled'))
isDbird = 'blue' if DBIRDSTAT == 'true' else 'gold'

ADBIRDSTAT = (xbmcaddon.Addon('script.module.resolveurl').getSetting('AllDebridResolver_enabled'))
isAdbird = 'blue' if ADBIRDSTAT == 'true' else 'gold'

PREMESTAT = (xbmcaddon.Addon('script.module.resolveurl').getSetting('PremiumizeMeResolver_enabled'))
isPreMe = 'blue' if PREMESTAT == 'true' else 'gold'



class navigator:
    def getMenuEnabled(self, menu_title):
        is_enabled = control.setting(menu_title).strip()
        if (is_enabled == '' or is_enabled == 'false'):
            return False
        return True


   

    def root(self):
        self.addDirectoryItem(32001, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')
        if not control.setting('lists.widget') == '0':
            self.addDirectoryItem(30715, 'mytraktNavigator', 'trakt.png', 'fanart.jpg') 
	    self.addDirectoryItem(42016, 'movies2&url=theaters', 'movies.png', 'fanart.jpg')
	    self.addDirectoryItem('Moviezone', 'moviezoneNavigator', 'people-watching.png', 'DefaultMovies.png') 
	    self.addDirectoryItem('Kidszone', 'kidszoneNavigator', 'kids.png', 'fanart.jpg')

        if self.getMenuEnabled('navi.docu') == False:
            self.addDirectoryItem('Documentary', 'docuNavigator', 'channels.png', 'DefaultMovies.png')
        if self.getMenuEnabled('mytube') == False:   
            self.addDirectoryItem('Channels YT', 'youtubeNavigator', 'userlists.png', 'youtubemenu.png') #(root.txt) 
        if self.getMenuEnabled('areaZoneNavigator') == False:
	    self.addDirectoryItem('Iptv', 'areaZoneNavigator', 'iptv.png', 'fanart.jpg')
        if self.getMenuEnabled('navi.radio') is True:
   	    self.addDirectoryItem('Radio', 'radioNavigator', 'airing-today.png', 'DefaultVideoPlaylists.png')
	    #self.addDirectoryItem('CollectionBox', 'ChuckycollectionBox', 'people-watching.png', 'DefaultMovies.png')                 
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
	if downloads == False:
            #self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')
	    self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')  
            self.addDirectoryItem(42006, 'searchNavigator', 'search.png', 'DefaultFolder.png') 
	    self.addDirectoryItem(30716, 'ShowNews', 'icon.gif', 'fanart.jpg')     
        if  self.getMenuEnabled('navi.dev') == True:
            self.addDirectoryItem('Dev Menu', 'devtoolNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.endDirectory()


    def movies(self, lite=False):
        if self.getMenuEnabled('navi.fiftys') == True:
            self.addDirectoryItem('50s Movies 1950 - 1959', 'movies&url=fiftys', '50.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.sixtys') == True:
            self.addDirectoryItem('60s Movies 1960 - 1969', 'movies&url=sixtys', '60.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.seventys') == True:
            self.addDirectoryItem('70s Movies 1970 - 1979', 'movies&url=seventys', '70.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.eightys') == True:
            self.addDirectoryItem('80s Movies 1980 - 1989', 'movies&url=eightys', '80.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.ninetys') == True:
            self.addDirectoryItem('90s Movies 1990 - 1999', 'movies&url=ninetys', '90.png', 'DefaultMovies.png')
 	if self.getMenuEnabled('navi.moviegenre') == True:
            self.addDirectoryItem(32011, 'movieGenres', 'genres.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movieyears') == True:
            self.addDirectoryItem(32012, 'movieYears', 'years.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.moviepersons') == True:
            self.addDirectoryItem(32013, 'moviePersons', 'people.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movielanguages') == True:
            self.addDirectoryItem(32014, 'movieLanguages', 'languages.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.moviecerts') == True:
            self.addDirectoryItem(32015, 'movieCertificates', 'certificates.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movieboxes') == True:
            self.addDirectoryItem('TMDB Box', 'boxesNavigator', 'tmdb.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.movieMosts') == True:
            self.addDirectoryItem(42009, 'movieMosts', 'people-watching.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.moviefeat') == True:
            self.addDirectoryItem(32035, 'movies&url=featured', 'imdb.png', 'imdb.png')
            self.addDirectoryItem(42010, 'movies2&url=featured', 'featured.png', 'DefaultMovies.png')
            self.addDirectoryItem(42011, 'movies&url=traktfeatured', 'trakt.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movietrending') == True:
            self.addDirectoryItem(32017, 'movies&url=trending', 'trakt.png', 'DefaultRecentlyAddedMovies.png')
        if self.getMenuEnabled('navi.moviepopular') == True:
            self.addDirectoryItem(32018, 'movies&url=popular', 'most-popular.png', 'DefaultMovies.png')
            self.addDirectoryItem('Popular', 'movies&url=traktpopular', 'trakt.png', 'DefaultRecentlyAddedMovies.png')
            self.addDirectoryItem(42012, 'movies2&url=popular', 'most-popular.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movieviews') == True:
            self.addDirectoryItem(32019, 'movies&url=views', 'most-voted.png', 'DefaultMovies.png')
            self.addDirectoryItem(42013, 'movies2&url=toprated', 'movies.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.moviepremiere') == True:
            self.addDirectoryItem(42014, 'movies2&url=premiere', 'movies.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movietheaters') == True:
            #self.addDirectoryItem(32022, 'movies&url=theaters', 'in-theaters.png', 'DefaultRecentlyAddedMovies.png')
            self.addDirectoryItem(42015, 'movies&url=theatersOld', 'in-theaters.png', 'DefaultRecentlyAddedMovies.png')
            self.addDirectoryItem(42016, 'movies2&url=theaters', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        if self.getMenuEnabled('navi.movieoscars') == True:
            self.addDirectoryItem(32021, 'movies&url=oscars', 'oscar-winners.png', 'DefaultMovies.png')
        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(42006, 'searchNavigator', 'search.png', 'DefaultFolder.png')
        self.endDirectory()


    def mytrakt(self, lite=False):
	self.accountCheck()
	self.addDirectoryItem('My Movies', 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
	self.addDirectoryItem('My TV Shows', 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
        self.addDirectoryItem('My Movie Watchlist', 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
	self.addDirectoryItem('My TV Show watchlist', 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
	self.addDirectoryItem('My History Movies', 'movies&url=trakthistory', 'trakt.png', 'DefaultMovies.png', queue=True)
	self.addDirectoryItem('My History tvshow', 'calendar&url=trakthistory', 'trakt.png', 'DefaultTVShows.png', queue=True)
	self.addDirectoryItem('Featured Movies', 'movies&url=traktfeatured', 'trakt.png', 'DefaultMovies.png')
	self.addDirectoryItem('Featured Tvshow', 'tvshows&url=traktfeatured', 'trakt.png', 'DefaultTVShows.png')
	self.addDirectoryItem(32073, 'authTrakt', 'trakt.png', 'DefaultAddonProgram.png', isFolder=False)
	self.endDirectory()

    def kidszone(self):
	self.addDirectoryItem('Disney', 'collections&url=disneymovies', 'kids.png', 'DefaultVideoPlaylists.png')
	self.addDirectoryItem('Kids', 'collections&url=kidsmovies', 'kids.png', 'DefaultVideoPlaylists.png')
	self.addDirectoryItem('Kids BoxSets', 'collectionBoxsetKids', 'kids.png', 'DefaultVideoPlaylists.png')
	self.addDirectoryItem('Kids BoxSets TMDB', 'collections&url=kidsboxcollection2', 'kids.png', 'DefaultVideoPlaylists.png')
	self.endDirectory()

    def areazone(self):
        self.addDirectoryItem(42023, 'iptvChannels', 'iptv.png', 'fanart.jpg')
	self.addDirectoryItem('Swift Streams', 'swiftNavigator', 'swift.png', '')
	self.addDirectoryItem('AcronaiTV',  'acronaitv_menu',  'iptv.png',  'DefaultTVShows.png')
	self.endDirectory()

    def youtubezone(self):
        self.addDirectoryItem(32610, 'kidscorner', 'kids.png', 'DefaultMovies.png')
        self.addDirectoryItem(32611, 'fitness', 'fitness.png', 'DefaultMovies.png')
        self.addDirectoryItem(32612, 'legends', 'legends.png', 'DefaultMovies.png')	
 	self.addDirectoryItem('Chucky Choice', 'mytube', 'icon.png', 'youtubemenu.png')
  
	self.endDirectory()

    def moviezone(self):
	self.addDirectoryItem('TMDB Chucky choice', 'collections&url=moviemirror', 'mymovies.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem('Explore UserLists(Movies)', 'movieimdbUserLists', 'imdb.png', 'DefaultMovies.png')
	self.addDirectoryItem('MovieCollectionBox', 'collectionBoxset', 'people-watching.png', 'DefaultMovies.png')
        self.addDirectoryItem(32013, 'moviePersons', 'people.png', 'DefaultMovies.png')
	self.addDirectoryItem('Mosts Played', 'movieMosts', 'people-watching.png', 'DefaultMovies.png')
        self.addDirectoryItem('Trakt', 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
	self.addDirectoryItem(42006, 'searchNavigator', 'search.png', 'DefaultFolder.png')
	#self.addDirectoryItem('Christmas movies', 'collections&url=xmasmovies', 'mymovies.png', 'DefaultVideoPlaylists.png')
	self.endDirectory()

    def mymovies(self, lite=False):
        self.accountCheck()
        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32032, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32033, 'movies&url=imdbwatchlist2', 'imdb.png', 'DefaultMovies.png', queue=True)
        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32033, 'movies&url=imdbwatchlist2', 'imdb.png', 'DefaultMovies.png', queue=True)
        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem('Trakt OnDeck', 'movies&url=onDeckMovies', 'trakt.png', 'DefaultMovies.png', queue=True)
        self.addDirectoryItem(32039, 'movieUserlists', 'userlists.png', 'DefaultMovies.png')
        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.png', 'DefaultMovies.png')
            self.addDirectoryItem(42006, 'searchNavigator', 'search.png', 'DefaultFolder.png')
        self.endDirectory()


    def movieMosts(self):
		self.addDirectoryItem('Most Played This Week', 'movies&url=played1', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Played This Month', 'movies&url=played2', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Played This Year', 'movies&url=played3', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Played All Time', 'movies&url=played4', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Collected This Week', 'movies&url=collected1', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Collected This Month', 'movies&url=collected2', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Collected This Year', 'movies&url=collected3', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Collected All Time', 'movies&url=collected4', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Watched This Week', 'movies&url=watched1', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Watched This Month', 'movies&url=watched2', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Watched This Year', 'movies&url=watched3', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Watched All Time', 'movies&url=watched4', 'most-popular.png', 'DefaultMovies.png')
		self.endDirectory()	


    def tvshows(self, lite=False):
	if self.getMenuEnabled('navi.fiftyss') == True:
            self.addDirectoryItem('50s TV Shows 1950 - 1959', 'tvshows&url=fiftyst', '50.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.sixtyss') == True:
            self.addDirectoryItem('60s TV Shows 1960 - 1969', 'tvshows&url=sixtyst', '60.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.seventyss') == True:
            self.addDirectoryItem('70s TV Shows 1970 - 1979', 'tvshows&url=seventyst', '70.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.eightyss') == True:
            self.addDirectoryItem('80s TV Shows 1980 - 1989', 'tvshows&url=eightyst', '80.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.ninetyss') == True:
            self.addDirectoryItem('90s TV Shows 1990 - 1999', 'tvshows&url=ninetyst', '90.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvGenres') == True:
            self.addDirectoryItem(32011, 'tvGenres', 'genres.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvNetworks') == True:
            self.addDirectoryItem(32016, 'tvNetworksNavigator', 'networks.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvLanguages') == True:
            self.addDirectoryItem(32014, 'tvLanguages', 'languages.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvCertificates') == True:
            self.addDirectoryItem(32015, 'tvCertificates', 'certificates.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvfeat') == True:
            self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'trakt.png', 'DefaultTVShows.png')
            self.addDirectoryItem(42010, 'tvshows2&url=featured', 'featured.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvTrending') == True:
            self.addDirectoryItem(32017, 'tvshows&url=trending', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png')
        if self.getMenuEnabled('navi.tvPopular') == True:
            self.addDirectoryItem(42012, 'tvshows2&url=popular', 'most-popular.png', 'DefaultTVShows.png')
            self.addDirectoryItem('Popular', 'tvshows&url=traktpopular', 'trakt.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32018, 'tvshows&url=popular', 'most-popular.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvRating') == True:
            self.addDirectoryItem(42017, 'tvshows2&url=rating', 'highly-rated.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32023, 'tvshows&url=rating', 'highly-rated.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvViews') == True:
            self.addDirectoryItem(42018, 'tvshows2&url=views', 'movies.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32019, 'tvshows&url=views', 'most-voted.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvshowMosts') == True:
            self.addDirectoryItem(42019, 'showMosts', 'people-watching.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvAiring') == True:
            self.addDirectoryItem(42020, 'tvshows2&url=airing', 'airing-today.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32024, 'tvshows&url=airing', 'airing-today.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvActive') == True:
            self.addDirectoryItem(42021, 'tvshows2&url=active', 'returning-tvshows.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32025, 'tvshows&url=active', 'returning-tvshows.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvAnticipated') == True:
            self.addDirectoryItem('Anticipated', 'tvshows&url=traktanticipated', 'trakt.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvPremier') == True:
            self.addDirectoryItem(42022, 'tvshows2&url=premiere', 'movies.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32026, 'tvshows&url=premiere', 'new-tvshows.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvAdded') == True:
            self.addDirectoryItem(32006, 'calendar&url=added', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        if self.getMenuEnabled('navi.tvCalendar') == True:
            self.addDirectoryItem(32027, 'calendars', 'calendar.png', 'DefaultRecentlyAddedEpisodes.png')
        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(42006, 'searchNavigator', 'search.png', 'DefaultFolder.png')
        self.endDirectory()


    def mytvshows(self, lite=False):
        self.accountCheck()
        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', 'imdb.png', 'DefaultTVShows.png')
        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', 'imdb.png', 'DefaultTVShows.png')
        if traktIndicators == True:
            self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'DefaultTVShows.png', queue=True)
            self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
            self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
            self.addDirectoryItem('Trakt OnDeck', 'tvshows&url=onDeckTV', 'trakt.png', 'DefaultTVShows.png', queue=True)
        if traktCredentials == True:
            self.addDirectoryItem(32041, 'episodeUserlists', 'userlists.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32040, 'tvUserlists', 'userlists.png', 'DefaultTVShows.png')
        if lite == False:
            self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.png', 'DefaultTVShows.png')
            self.addDirectoryItem(42006, 'searchNavigator', 'search.png', 'DefaultFolder.png')
        self.endDirectory()


    def showMosts(self):
		self.addDirectoryItem('Most Played This Week', 'tvshows&url=played1', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Played This Month', 'tvshows&url=played2', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Played This Year', 'tvshows&url=played3', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Played All Time', 'tvshows&url=played4', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Collected This Week', 'tvshows&url=collected1', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Collected This Month', 'tvshows&url=collected2', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Collected This Year', 'tvshows&url=collected3', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Collected All Time', 'tvshows&url=collected4', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Watched This Week', 'tvshows&url=watched1', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Watched This Month', 'tvshows&url=watched2', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Watched This Year', 'tvshows&url=watched3', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Watched All Time', 'tvshows&url=watched4', 'most-popular.png', 'DefaultTVShows.png')
		self.endDirectory()


    def tvNetworksNavigator(self):
        self.addDirectoryItem('WebChannels', 'tvWebChannels', 'networks.png', 'DefaultTVShows.png')
        self.addDirectoryItem('United States', 'tvNetworks', 'networks.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Canada', 'tvCanadanetworks', 'networks.png', 'DefaultTVShows.png')
        self.addDirectoryItem('United Kingdom', 'tvUnitedKingdomnetworks', 'networks.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Australia', 'tvAustralianetworks', 'networks.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Other Countries 1', 'tvOthers1networks', 'networks.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Other Countries 2', 'tvOthers2networks', 'networks.png', 'DefaultTVShows.png')
        self.endDirectory()


    def imdbLists(self):
        self.addDirectoryItem('Explore Keywords(Movies)', 'movieExploreKeywords', 'imdb.png', 'DefaultMovies.png')
        self.addDirectoryItem('Explore Keywords(TV Shows)', 'tvshowExploreKeywords', 'imdb.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Explore UserLists(Movies)', 'movieimdbUserLists', 'imdb.png', 'DefaultMovies.png')
        self.addDirectoryItem('Explore UserLists(TV Shows)', 'tvshowimdbUserLists', 'imdb.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Hella LifeTime & HallMark Movies', 'hellaLifeTimeHallMark', 'userlists.png', 'DefaultVideoPlaylists.png')
        self.endDirectory()


    def tools(self):
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32047, 'openSettings&query=3.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
	self.addDirectoryItem('SETTINGS: Resloverurl', 'urlResolver', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32556, 'libraryNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32613, 'clearAllCache', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32050, 'clearSources', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32052, 'clearCache', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32614, 'clearMetaCache', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32604, 'clearCacheSearch', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem('CHUCKY: Clear ResolveURL Cache', 'clearResolveURLcache', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32073, 'authTrakt', 'trakt.png', 'DefaultAddonProgram.png', isFolder=False)
        self.endDirectory()


    def devtools(self):
        self.addDirectoryItem('ToonNavigator', 'toonNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('Test Movies(TMDB)', 'movies2&url=tmdbjewtestmovies', 'movies.png', 'DefaultMovies.png')
        self.addDirectoryItem('Test Shows(TMDB)', 'tvshows2&url=tmdbjewtestshows', 'tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32047, 'openSettings&query=3.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32641, 'openSettings&query=7.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32050, 'clearSources', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32613, 'clearAllCache', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem('Clear ResolveURL Cache', 'clearResolveURLcache', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32609, 'urlResolver', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem('[COLOR %s][X][/COLOR]-Toggle RealDebrid (ResolveURL)' % isDbird, 'ToggleDbird', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem('[COLOR %s][X][/COLOR]-Toggle AllDebrid (ResolveURL)' % isAdbird, 'ToggleAdbird', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem('[COLOR %s][X][/COLOR]-Toggle PremiumizeMe (ResolveURL)' % isPreMe, 'TogglePreMe', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.endDirectory()


    def search(self):
        self.addDirectoryItem('MovieSearch', 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem('TvSearch', 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')
	self.addDirectoryItem('Movie Genres', 'movieGenres', 'genres.png', 'DefaultMovies.png')
	self.addDirectoryItem('Tv Genres', 'tvGenres', 'genres.png', 'DefaultTVShows.png')
        self.endDirectory()


    def library(self):
        self.addDirectoryItem(32557, 'openSettings&query=9.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.png', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.png', 'DefaultTVShows.png', isAction=False)
        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png')
        self.endDirectory()


    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')
        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.png', 'DefaultTVShows.png', isAction=False)
        self.endDirectory()


    def views(self):
        try:
            control.idle()
            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]
            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))
            if select == -1:
                return
            content = items[select][1]
            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)
            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()
            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})
            item.setProperty('Fanart_Image', fanart)
            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)
            from resources.lib.modules import views
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False and imdbCredentials == False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()


    def infoCheck(self, version):
        try:
            control.notification(title='default', message=32074, icon='WARNING',  time=5000, sound=True)
            return '1'
        except:
            return '1'


    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes:
            return
        from resources.lib.modules import cache
        cache.cache_clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def clearCacheMeta(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes:
            return
        from resources.lib.modules import cache
        cache.cache_clear_meta()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def clearCacheProviders(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes:
            return
        from resources.lib.modules import cache
        cache.cache_clear_providers()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def clearCacheSearch(self):
        control.idle()
        if control.yesnoDialog(control.lang(32056).encode('utf-8'), '', ''):
            control.setSetting('tvsearch', '')
            control.setSetting('moviesearch', '')
            control.refresh()


    def clearCacheAll(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes:
            return
        from resources.lib.modules import cache
        cache.cache_clear_all()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def Toggle_Dbird(self):
        HMMMPATH = xbmc.translatePath(os.path.join('special://home/addons/', 'script.module.resolveurl'))
        ummmDialog = xbmcgui.Dialog()
        if not os.path.exists(HMMMPATH):
            ummmDialog("ummmm", "There was a error loading script.module.resolveurl.")
            sys.exit()
        try:
            if xbmcaddon.Addon('script.module.resolveurl').getSetting('RealDebridResolver_enabled') != 'true':
                try:
                    xbmcaddon.Addon('script.module.resolveurl') .setSetting(id='RealDebridResolver_enabled', value='true')
                    control.refresh()
                    ummmDialog.notification('[B]Turn On[/B] RealDebridResolver', 'Done, Setting [B]Enabled[/B].', xbmcgui.NOTIFICATION_INFO, 5000)
                except: pass
            elif xbmcaddon.Addon('script.module.resolveurl').getSetting('RealDebridResolver_enabled') != 'false':
                try:
                    xbmcaddon.Addon('script.module.resolveurl') .setSetting(id='RealDebridResolver_enabled', value='false')
                    control.refresh()
                    ummmDialog.notification('[B]Turn Off[/B] RealDebridResolver', 'Done, Setting [B]Disabled[/B].', xbmcgui.NOTIFICATION_INFO, 5000)
                except: pass
        except:
            pass


    def Toggle_Adbird(self):
        HMMMPATH = xbmc.translatePath(os.path.join('special://home/addons/', 'script.module.resolveurl'))
        ummmDialog = xbmcgui.Dialog()
        if not os.path.exists(HMMMPATH):
            ummmDialog("ummmm", "There was a error loading script.module.resolveurl.")
            sys.exit()
        try:
            if xbmcaddon.Addon('script.module.resolveurl').getSetting('AllDebridResolver_enabled') != 'true':
                try:
                    xbmcaddon.Addon('script.module.resolveurl') .setSetting(id='AllDebridResolver_enabled', value='true')
                    control.refresh()
                    ummmDialog.notification('[B]Turn On[/B] AllDebridResolver', 'Done, Setting [B]Enabled[/B].', xbmcgui.NOTIFICATION_INFO, 5000)
                except: pass
            elif xbmcaddon.Addon('script.module.resolveurl').getSetting('AllDebridResolver_enabled') != 'false':
                try:
                    xbmcaddon.Addon('script.module.resolveurl') .setSetting(id='AllDebridResolver_enabled', value='false')
                    control.refresh()
                    ummmDialog.notification('[B]Turn Off[/B] AllDebridResolver', 'Done, Setting [B]Disabled[/B].', xbmcgui.NOTIFICATION_INFO, 5000)
                except: pass
        except:
            pass


    def Toggle_PreMe(self):
        HMMMPATH = xbmc.translatePath(os.path.join('special://home/addons/', 'script.module.resolveurl'))
        ummmDialog = xbmcgui.Dialog()
        if not os.path.exists(HMMMPATH):
            ummmDialog("ummmm", "There was a error loading script.module.resolveurl.")
            sys.exit()
        try:
            if xbmcaddon.Addon('script.module.resolveurl').getSetting('PremiumizeMeResolver_enabled') != 'true':
                try:
                    xbmcaddon.Addon('script.module.resolveurl').setSetting(id='PremiumizeMeResolver_enabled', value='true')
                    control.refresh()
                    ummmDialog.notification('[B]Turn On[/B] PremiumizeMeResolver', 'Done, Setting [B]Enabled[/B].', xbmcgui.NOTIFICATION_INFO, 5000)
                except:
                    pass
            elif xbmcaddon.Addon('script.module.resolveurl').getSetting('PremiumizeMeResolver_enabled') != 'false':
                try:
                    xbmcaddon.Addon('script.module.resolveurl').setSetting(id='PremiumizeMeResolver_enabled', value='false')
                    control.refresh()
                    ummmDialog.notification('[B]Turn Off[/B] PremiumizeMeResolver', 'Done, Setting [B]Disabled[/B].', xbmcgui.NOTIFICATION_INFO, 5000)
                except:
                    pass
        except:
            pass


    def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
        try:
            name = control.lang(name).encode('utf-8')
        except:
            pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue == True:
            cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        if not context == None:
            cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None:
            item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


    def collectionBoxset(self):
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]48 Hrs.[/COLOR] [COLOR yellow] (1982-1990)[/COLOR]', 'collections&url=fortyeighthours', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Ace Ventura[/COLOR] [COLOR yellow] (1994-1995)[/COLOR]', 'collections&url=aceventura', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Airplane[/COLOR] [COLOR yellow] (1980-1982)[/COLOR]', 'collections&url=airplane', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Airport[/COLOR] [COLOR yellow] (1970-1979)[/COLOR]', 'collections&url=airport', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]American Graffiti[/COLOR] [COLOR yellow] (1973-1979)[/COLOR]', 'collections&url=americangraffiti', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Anaconda[/COLOR] [COLOR yellow] (1997-2004)[/COLOR]', 'collections&url=anaconda', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Analyze This[/COLOR] [COLOR yellow] (1999-2002)[/COLOR]', 'collections&url=analyzethis', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Anchorman[/COLOR] [COLOR yellow] (2004-2013)[/COLOR]', 'collections&url=anchorman', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Austin Powers[/COLOR] [COLOR yellow] (1997-2002)[/COLOR]', 'collections&url=austinpowers', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Avengers[/COLOR] [COLOR yellow] (2008-2017)[/COLOR]', 'collections&url=avengers', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Back to the Future[/COLOR] [COLOR yellow] (1985-1990)[/COLOR]', 'collections&url=backtothefuture', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Bad Boys[/COLOR] [COLOR yellow] (1995-2003)[/COLOR]', 'collections&url=badboys', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Bad Santa[/COLOR] [COLOR yellow] (2003-2016)[/COLOR]', 'collections&url=badsanta', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Basic Instinct[/COLOR] [COLOR yellow] (1992-2006)[/COLOR]', 'collections&url=basicinstinct', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Batman[/COLOR] [COLOR yellow] (1989-2016)[/COLOR]', 'collections&url=batman', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Beverly Hills Cop[/COLOR] [COLOR yellow] (1984-1994)[/COLOR]', 'collections&url=beverlyhillscop', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Big Mommas House[/COLOR] [COLOR yellow] (2000-2011)[/COLOR]', 'collections&url=bigmommashouse', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Blues Brothers[/COLOR] [COLOR yellow] (1980-1998)[/COLOR]', 'collections&url=bluesbrothers', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Bourne[/COLOR] [COLOR yellow] (2002-2016)[/COLOR]', 'collections&url=bourne', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Bruce Almighty[/COLOR] [COLOR yellow] (2003-2007)[/COLOR]', 'collections&url=brucealmighty', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Caddyshack[/COLOR] [COLOR yellow] (1980-1988)[/COLOR]', 'collections&url=caddyshack', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Cheaper by the Dozen[/COLOR] [COLOR yellow] (2003-2005)[/COLOR]', 'collections&url=cheaperbythedozen', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Cheech and Chong[/COLOR] [COLOR yellow] (1978-1984)[/COLOR]', 'collections&url=cheechandchong', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Childs Play[/COLOR] [COLOR yellow] (1988-2004)[/COLOR]', 'collections&url=childsplay', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]City Slickers[/COLOR] [COLOR yellow] (1991-1994)[/COLOR]', 'collections&url=cityslickers', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Conan[/COLOR] [COLOR yellow] (1982-2011)[/COLOR]', 'collections&url=conan', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Crank[/COLOR] [COLOR yellow] (2006-2009)[/COLOR]', 'collections&url=crank', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Crocodile Dundee[/COLOR] [COLOR yellow] (1986-2001)[/COLOR]', 'collections&url=crodiledunde', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Da Vinci Code[/COLOR] [COLOR yellow] (2006-2017)[/COLOR]', 'collections&url=davincicode', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Daddy Day Care[/COLOR] [COLOR yellow] (2003-2007)[/COLOR]', 'collections&url=daddydaycare', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Dark Knight Trilogy[/COLOR] [COLOR yellow] (2005-2013)[/COLOR]', 'collections&url=darkknight', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Death Wish[/COLOR] [COLOR yellow] (1974-1994)[/COLOR]', 'collections&url=deathwish', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Delta Force[/COLOR] [COLOR yellow] (1986-1990)[/COLOR]', 'collections&url=deltaforce', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Die Hard[/COLOR] [COLOR yellow] (1988-2013)[/COLOR]', 'collections&url=diehard', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Dirty Dancing[/COLOR] [COLOR yellow] (1987-2004)[/COLOR]', 'collections&url=dirtydancing', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Dirty Harry[/COLOR] [COLOR yellow] (1971-1988)[/COLOR]', 'collections&url=dirtyharry', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Dumb and Dumber[/COLOR] [COLOR yellow] (1994-2014)[/COLOR]', 'collections&url=dumbanddumber', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Escape from New York[/COLOR] [COLOR yellow] (1981-1996)[/COLOR]', 'collections&url=escapefromnewyork', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Every Which Way But Loose[/COLOR] [COLOR yellow] (1978-1980)[/COLOR]', 'collections&url=everywhichwaybutloose', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Exorcist[/COLOR] [COLOR yellow] (1973-2005)[/COLOR]', 'collections&url=exorcist', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Expendables[/COLOR] [COLOR yellow] (2010-2014)[/COLOR]', 'collections&url=theexpendables', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Fantastic Four[/COLOR] [COLOR yellow] (2005-2015)[/COLOR]', 'collections&url=fantasticfour', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Fast and the Furious[/COLOR] [COLOR yellow] (2001-2017)[/COLOR]', 'collections&url=fastandthefurious', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Father of the Bride[/COLOR] [COLOR yellow] (1991-1995)[/COLOR]', 'collections&url=fatherofthebride', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Fletch[/COLOR] [COLOR yellow] (1985-1989)[/COLOR]', 'collections&url=fletch', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Friday[/COLOR] [COLOR yellow] (1995-2002)[/COLOR]', 'collections&url=friday', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Friday the 13th[/COLOR] [COLOR yellow] (1980-2009)[/COLOR]', 'collections&url=fridaythe13th', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Fugitive[/COLOR] [COLOR yellow] (1993-1998)[/COLOR]', 'collections&url=fugitive', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]G.I. Joe[/COLOR] [COLOR yellow] (2009-2013)[/COLOR]', 'collections&url=gijoe', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Get Shorty[/COLOR] [COLOR yellow] (1995-2005)[/COLOR]', 'collections&url=getshorty', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Gettysburg[/COLOR] [COLOR yellow] (1993-2003)[/COLOR]', 'collections&url=gettysburg', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Ghost Rider[/COLOR] [COLOR yellow] (2007-2011)[/COLOR]', 'collections&url=ghostrider', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Ghostbusters[/COLOR] [COLOR yellow] (1984-2016)[/COLOR]', 'collections&url=ghostbusters', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Gods Not Dead[/COLOR] [COLOR yellow] (2014-2016)[/COLOR]', 'collections&url=godsnotdead', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Godfather[/COLOR] [COLOR yellow] (1972-1990)[/COLOR]', 'collections&url=godfather', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Godzilla[/COLOR] [COLOR yellow] (1956-2016)[/COLOR]', 'collections&url=godzilla', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Grown Ups[/COLOR] [COLOR yellow] (2010-2013)[/COLOR]', 'collections&url=grownups', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Grumpy Old Men[/COLOR] [COLOR yellow] (2010-2013)[/COLOR]', 'collections&url=grumpyoldmen', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Guns of Navarone[/COLOR] [COLOR yellow] (1961-1978)[/COLOR]', 'collections&url=gunsofnavarone', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Halloween[/COLOR] [COLOR yellow] (1978-2009)[/COLOR]', 'collections&url=halloween', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hangover[/COLOR] [COLOR yellow] (2009-2013)[/COLOR]', 'collections&url=hangover', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hannibal Lector[/COLOR] [COLOR yellow] (1986-2007)[/COLOR]', 'collections&url=hanniballector', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hellraiser[/COLOR] [COLOR yellow] (1987-1996)[/COLOR]', 'collections&url=hellraiser', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Honey I Shrunk the Kids[/COLOR] [COLOR yellow] (1989-1995)[/COLOR]', 'collections&url=honeyishrunkthekids', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Horrible Bosses[/COLOR] [COLOR yellow] (2011-2014)[/COLOR]', 'collections&url=horriblebosses', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hostel[/COLOR] [COLOR yellow] (2005-2011)[/COLOR]', 'collections&url=hostel', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hot Shots[/COLOR] [COLOR yellow] (1991-1996)[/COLOR]', 'collections&url=hotshots', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hulk[/COLOR] [COLOR yellow] (2003-2008)[/COLOR]', 'collections&url=hulk', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Independence Day[/COLOR] [COLOR yellow] (1996-2016)[/COLOR]', 'collections&url=independenceday', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Indiana Jones[/COLOR] [COLOR yellow] (1981-2008)[/COLOR]', 'collections&url=indianajones', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Insidious[/COLOR] [COLOR yellow] (2010-2015)[/COLOR]', 'collections&url=insidious', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Iron Eagle[/COLOR] [COLOR yellow] (1986-1992)[/COLOR]', 'collections&url=ironeagle', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Iron Man[/COLOR] [COLOR yellow] (2008-2013)[/COLOR]', 'collections&url=ironman', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jack Reacher[/COLOR] [COLOR yellow] (2012-2016)[/COLOR]', 'collections&url=jackreacher', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jack Ryan[/COLOR] [COLOR yellow] (1990-2014)[/COLOR]', 'collections&url=jackryan', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jackass[/COLOR] [COLOR yellow] (2002-2013)[/COLOR]', 'collections&url=jackass', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]James Bond[/COLOR] [COLOR yellow] (1963-2015)[/COLOR]', 'collections&url=jamesbond', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jaws[/COLOR] [COLOR yellow] (1975-1987)[/COLOR]', 'collections&url=jaws', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jeepers Creepers[/COLOR] [COLOR yellow] (2001-2017)[/COLOR]', 'collections&url=jeeperscreepers', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]John Wick[/COLOR] [COLOR yellow] (2014-2017)[/COLOR]', 'collections&url=johnwick', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jumanji[/COLOR] [COLOR yellow] (1995-2005)[/COLOR]', 'collections&url=jumanji', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jurassic Park[/COLOR] [COLOR yellow] (1993-2015)[/COLOR]', 'collections&url=jurassicpark', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Kick-Ass[/COLOR] [COLOR yellow] (2010-2013)[/COLOR]', 'collections&url=kickass', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Kill Bill[/COLOR] [COLOR yellow] (2003-2004)[/COLOR]', 'collections&url=killbill', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]King Kong[/COLOR] [COLOR yellow] (1933-2016)[/COLOR]', 'collections&url=kingkong', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Lara Croft[/COLOR] [COLOR yellow] (2001-2003)[/COLOR]', 'collections&url=laracroft', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Legally Blonde[/COLOR] [COLOR yellow] (2001-2003)[/COLOR]', 'collections&url=legallyblonde', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Lethal Weapon[/COLOR] [COLOR yellow] (1987-1998)[/COLOR]', 'collections&url=leathalweapon', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Look Whos Talking[/COLOR] [COLOR yellow] (1989-1993)[/COLOR]', 'collections&url=lookwhostalking', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Machete[/COLOR] [COLOR yellow] (2010-2013)[/COLOR]', 'collections&url=machete', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Magic Mike[/COLOR] [COLOR yellow] (2012-2015)[/COLOR]', 'collections&url=magicmike', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Major League[/COLOR] [COLOR yellow] (1989-1998)[/COLOR]', 'collections&url=majorleague', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Man from Snowy River[/COLOR] [COLOR yellow] (1982-1988)[/COLOR]', 'collections&url=manfromsnowyriver', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Mask[/COLOR] [COLOR yellow] (1994-2005)[/COLOR]', 'collections&url=mask', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Matrix[/COLOR] [COLOR yellow] (1999-2003)[/COLOR]', 'collections&url=matrix', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Mechanic[/COLOR] [COLOR yellow] (2011-2016)[/COLOR]', 'collections&url=themechanic', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Meet the Parents[/COLOR] [COLOR yellow] (2000-2010)[/COLOR]', 'collections&url=meettheparents', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Men in Black[/COLOR] [COLOR yellow] (1997-2012)[/COLOR]', 'collections&url=meninblack', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Mighty Ducks[/COLOR] [COLOR yellow] (1995-1996)[/COLOR]', 'collections&url=mightyducks', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Miss Congeniality[/COLOR] [COLOR yellow] (2000-2005)[/COLOR]', 'collections&url=misscongeniality', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Missing in Action[/COLOR] [COLOR yellow] (1984-1988)[/COLOR]', 'collections&url=missinginaction', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Mission Impossible[/COLOR] [COLOR yellow] (1996-2015)[/COLOR]', 'collections&url=missionimpossible', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Naked Gun[/COLOR] [COLOR yellow] (1988-1994)[/COLOR]', 'collections&url=nakedgun', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]National Lampoon[/COLOR] [COLOR yellow] (1978-2006)[/COLOR]', 'collections&url=nationallampoon', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]National Lampoons Vacation[/COLOR] [COLOR yellow] (1983-2015)[/COLOR]', 'collections&url=nationallampoonsvacation', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]National Treasure[/COLOR] [COLOR yellow] (2004-2007)[/COLOR]', 'collections&url=nationaltreasure', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Neighbors[/COLOR] [COLOR yellow] (2014-2016)[/COLOR]', 'collections&url=neighbors', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Night at the Museum[/COLOR] [COLOR yellow] (2006-2014)[/COLOR]', 'collections&url=nightatthemuseum', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Nightmare on Elm Street[/COLOR] [COLOR yellow] (1984-2010)[/COLOR]', 'collections&url=nightmareonelmstreet', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Now You See Me[/COLOR] [COLOR yellow] (2013-2016)[/COLOR]', 'collections&url=nowyouseeme', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Nutty Professor[/COLOR] [COLOR yellow] (1996-2000)[/COLOR]', 'collections&url=nuttyprofessor', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Oceans Eleven[/COLOR] [COLOR yellow] (2001-2007)[/COLOR]', 'collections&url=oceanseleven', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Odd Couple[/COLOR] [COLOR yellow] (1968-1998)[/COLOR]', 'collections&url=oddcouple', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Oh, God[/COLOR] [COLOR yellow] (1977-1984)[/COLOR]', 'collections&url=ohgod', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Olympus Has Fallen[/COLOR] [COLOR yellow] (2013-2016)[/COLOR]', 'collections&url=olympushasfallen', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Omen[/COLOR] [COLOR yellow] (1976-1981)[/COLOR]', 'collections&url=omen', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Paul Blart Mall Cop[/COLOR] [COLOR yellow] (2009-2015)[/COLOR]', 'collections&url=paulblart', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Pirates of the Caribbean[/COLOR] [COLOR yellow] (2003-2017)[/COLOR]', 'collections&url=piratesofthecaribbean', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Planet of the Apes[/COLOR] [COLOR yellow] (1968-2014)[/COLOR]', 'collections&url=planetoftheapes', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Police Academy[/COLOR] [COLOR yellow] (1984-1994)[/COLOR]', 'collections&url=policeacademy', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Poltergeist[/COLOR] [COLOR yellow] (1982-1988)[/COLOR]', 'collections&url=postergeist', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Porkys[/COLOR] [COLOR yellow] (1981-1985)[/COLOR]', 'collections&url=porkys', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Predator[/COLOR] [COLOR yellow] (1987-2010)[/COLOR]', 'collections&url=predator', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Purge[/COLOR] [COLOR yellow] (2013-2016)[/COLOR]', 'collections&url=thepurge', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Rambo[/COLOR] [COLOR yellow] (1982-2008)[/COLOR]', 'collections&url=rambo', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]RED[/COLOR] [COLOR yellow] (2010-2013)[/COLOR]', 'collections&url=red', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Revenge of the Nerds[/COLOR] [COLOR yellow] (1984-1987)[/COLOR]', 'collections&url=revengeofthenerds', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Riddick[/COLOR] [COLOR yellow] (2000-2013)[/COLOR]', 'collections&url=riddick', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Ride Along[/COLOR] [COLOR yellow] (2014-2016)[/COLOR]', 'collections&url=ridealong', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Ring[/COLOR] [COLOR yellow] (2002-2017)[/COLOR]', 'collections&url=thering', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]RoboCop[/COLOR] [COLOR yellow] (1987-1993)[/COLOR]', 'collections&url=robocop', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Rocky[/COLOR] [COLOR yellow] (1976-2015)[/COLOR]', 'collections&url=rocky', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Romancing the Stone[/COLOR] [COLOR yellow] (1984-1985)[/COLOR]', 'collections&url=romancingthestone', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Rush Hour[/COLOR] [COLOR yellow] (1998-2007)[/COLOR]', 'collections&url=rushhour', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Santa Clause[/COLOR] [COLOR yellow] (1994-2006)[/COLOR]', 'collections&url=santaclause', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Saw[/COLOR] [COLOR yellow] (2004-2010)[/COLOR]', 'collections&url=saw', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Sex and the City[/COLOR] [COLOR yellow] (2008-2010)[/COLOR]', 'collections&url=sexandthecity', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Shaft[/COLOR] [COLOR yellow] (1971-2000)[/COLOR]', 'collections&url=shaft', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Shanghai Noon[/COLOR] [COLOR yellow] (2000-2003)[/COLOR]', 'collections&url=shanghainoon', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Sin City[/COLOR] [COLOR yellow] (2005-2014)[/COLOR]', 'collections&url=sincity', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Sinister[/COLOR] [COLOR yellow] (2012-2015)[/COLOR]', 'collections&url=sinister', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Sister Act[/COLOR] [COLOR yellow] (1995-1993)[/COLOR]', 'collections&url=sisteract', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Smokey and the Bandit[/COLOR] [COLOR yellow] (1977-1986)[/COLOR]', 'collections&url=smokeyandthebandit', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Speed[/COLOR] [COLOR yellow] (1994-1997)[/COLOR]', 'collections&url=speed', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Spider-Man[/COLOR] [COLOR yellow] (2002-2017)[/COLOR]', 'collections&url=spiderman', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Stakeout[/COLOR] [COLOR yellow] (1987-1993)[/COLOR]', 'collections&url=stakeout', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Star Trek[/COLOR] [COLOR yellow] (1979-2016)[/COLOR]', 'collections&url=startrek', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Star Wars[/COLOR] [COLOR yellow] (1977-2015)[/COLOR]', 'collections&url=starwars', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Superman[/COLOR] [COLOR yellow] (1978-2016)[/COLOR]', 'collections&url=superman', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Sting[/COLOR] [COLOR yellow] (1973-1983)[/COLOR]', 'collections&url=thesting', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Taken[/COLOR] [COLOR yellow] (2008-2014)[/COLOR]', 'collections&url=taken', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Taxi[/COLOR] [COLOR yellow] (1998-2007)[/COLOR]', 'collections&url=taxi', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Ted[/COLOR] [COLOR yellow] (2012-2015)[/COLOR]', 'collections&url=ted', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Teen Wolf[/COLOR] [COLOR yellow] (1985-1987)[/COLOR]', 'collections&url=teenwolf', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Terminator[/COLOR] [COLOR yellow] (1984-2015)[/COLOR]', 'collections&url=terminator', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Terms of Endearment[/COLOR] [COLOR yellow] (1983-1996)[/COLOR]', 'collections&url=termsofendearment', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Texas Chainsaw Massacre[/COLOR] [COLOR yellow] (1974-2013)[/COLOR]', 'collections&url=texaschainsawmassacre', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Thing[/COLOR] [COLOR yellow] (1982-2011)[/COLOR]', 'collections&url=thething', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Thomas Crown Affair[/COLOR] [COLOR yellow] (1968-1999)[/COLOR]', 'collections&url=thomascrownaffair', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Transporter[/COLOR] [COLOR yellow] (2002-2015)[/COLOR]', 'collections&url=transporter', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Under Siege[/COLOR] [COLOR yellow] (1992-1995)[/COLOR]', 'collections&url=undersiege', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Universal Soldier[/COLOR] [COLOR yellow] (1992-2012)[/COLOR]', 'collections&url=universalsoldier', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Wall Street[/COLOR] [COLOR yellow] (1987-2010)[/COLOR]', 'collections&url=wallstreet', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Waynes World[/COLOR] [COLOR yellow] (1992-1993)[/COLOR]', 'collections&url=waynesworld', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Weekend at Bernies[/COLOR] [COLOR yellow] (1989-1993)[/COLOR]', 'collections&url=weekendatbernies', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Whole Nine Yards[/COLOR] [COLOR yellow] (2000-2004)[/COLOR]', 'collections&url=wholenineyards', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]X-Files[/COLOR] [COLOR yellow] (1998-2008)[/COLOR]', 'collections&url=xfiles', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]X-Men[/COLOR] [COLOR yellow] (2000-2016)[/COLOR]', 'collections&url=xmen', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]xXx[/COLOR] [COLOR yellow] (2002-2005)[/COLOR]', 'collections&url=xxx', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Young Guns[/COLOR] [COLOR yellow] (1988-1990)[/COLOR]', 'collections&url=youngguns', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Zoolander[/COLOR] [COLOR yellow] (2001-2016)[/COLOR]', 'collections&url=zoolander', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Zorro[/COLOR] [COLOR yellow] (1998-2005)[/COLOR]', 'collections&url=zorro', 'movies.png', 'DefaultRecentlyAddedMovies.png')

        self.endDirectory()

  
	

    def endDirectory(self):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)


