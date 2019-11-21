# -*- coding: utf-8 -*-

""" Navi = plugin.video.miror > resources . settings.xml """



import os,base64,sys,urllib2,urlparse,xbmc,xbmcaddon,xbmcgui
from resources.lib.modules import control,cache,trakt

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1]) ; control.moderator()
artPath = control.artPath() ; addonFanart = control.addonFanart()
imdbCredentials = False if control.setting('imdb.user') == '' else True
traktCredentials = trakt.getTraktCredentialsInfo()
traktIndicators = trakt.getTraktIndicatorsInfo()
queueMenu = control.lang(32065).encode('utf-8')

DBIRDSTAT = (xbmcaddon.Addon('script.module.resolveurl').getSetting('RealDebridResolver_enabled'))
isDbird = 'lime' if DBIRDSTAT == 'true' else 'darkorange'

ADBIRDSTAT = (xbmcaddon.Addon('script.module.resolveurl').getSetting('AllDebridResolver_enabled'))
isAdbird = 'lime' if ADBIRDSTAT == 'true' else 'darkorange'

PREMESTAT = (xbmcaddon.Addon('script.module.resolveurl').getSetting('PremiumizeMeResolver_enabled'))
isPreMe = 'lime' if PREMESTAT == 'true' else 'darkorange'

NEWSFILE  = base64.b64decode(b'aHR0cDovL2N5NHJvb3QuMDAwd2ViaG9zdGFwcC5jb20vbG9nc3RhdHVzL2NodWNreWxvZy50eHQ=')
ADDON_ID      = xbmcaddon.Addon().getAddonInfo('id')
HOMEPATH      = xbmc.translatePath('special://home/')
#THISADDONPATH = os.path.join(ADDONSPATH, ADDON_ID)
#LOCALNEWS     = os.path.join(THISADDONPATH, 'whatsnew.txt')

class navigator:
    def getMenuEnabled(self, menu_title):
        is_enabled = control.setting(menu_title).strip()
        if (is_enabled == '' or is_enabled == 'false'):
            return False
        return True


   

    def root(self):
        self.addDirectoryItem(32001, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
       # self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')
        if not control.setting('lists.widget') == '0':
            self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
	    self.addDirectoryItem(32005, 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')
	    self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32006, 'tvWidget', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png') 
	if self.getMenuEnabled('navi.userlists') == True:
            self.addDirectoryItem(42003, 'imdbLists', 'imdb.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.userlists2') == False:
            self.addDirectoryItem(42001, 'JewNavigator', 'tmdb.png', 'DefaultVideoPlaylists.png')
	if self.getMenuEnabled('navi.vipbox') == True:
            self.addDirectoryItem('VipBox', 'vipbox', 'vip.png', 'fanart2.gif')
	if self.getMenuEnabled('navi.iptvChannels') == True:
            self.addDirectoryItem(42023, 'areaZoneNavigator', 'iptvf.jpg', 'fanart.jpg')	        
        #if self.getMenuEnabled('navi.channels') == True:
            #self.addDirectoryItem(32642, 'channels', 'channels.png', 'DefaultTVShows.png')
        
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
	if self.getMenuEnabled('navi.youtube') == False:
	   self.addDirectoryItem('CollectionBox', 'MirrorcollectionBox', 'people-watching.png', 'DefaultMovies.png')
           self.addDirectoryItem('Youtube Channels', 'youtube', 'youtubemenu.png', 'youtubemenu.png') #(root.txt) 
        #if self.getMenuEnabled('navi.mirror') == True:		    
        if downloads == False:
            #self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')
	    self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')        
            self.addDirectoryItem(42006, 'searchNavigator', 'search.png', 'DefaultFolder.png')
	    self.addDirectoryItem('Online Status', 'newsNavigator', 'icon.gif', 'fanart.jpg')
       
        #if self.getMenuEnabled('navi.changeLog') == False:
            #self.addDirectoryItem(42007,  'ShowChangelog',  'icon.png',  'DefaultFolder.png', isFolder=False)
        if self.getMenuEnabled('navi.dev') == True:
            self.addDirectoryItem('Dev Menu', 'devtoolNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.endDirectory()


    def movies(self, lite=False):
        if self.getMenuEnabled('navi.moviegenre') == True:
            self.addDirectoryItem(32011, 'movieGenres', 'genres.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.fiftys') == True:
            self.addDirectoryItem('50s Films 1950 - 1959', 'movies&url=fiftys', '50.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.sixtys') == True:
            self.addDirectoryItem('60s Films 1960 - 1969', 'movies&url=sixtys', '60.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.seventys') == True:
            self.addDirectoryItem('70s Films 1970 - 1979', 'movies&url=seventys', '70.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.eightys') == True:
            self.addDirectoryItem('80s Films 1980 - 1989', 'movies&url=eightys', '80.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.ninetys') == True:
            self.addDirectoryItem('90s Films 1990 - 1999', 'movies&url=ninetys', '90.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.twothousand') == True:
            self.addDirectoryItem('Y2K Films 2000 - 2010', 'movies&url=twothousand', '2000.png', 'DefaultMovies.png')
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
        if self.getMenuEnabled('navi.twothousands') == True:
            self.addDirectoryItem('Y2K TV Shows 2000 - 2010', 'tvshows&url=twothousandt', '2000.png', 'DefaultTVShows.png')
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

    def areazone(self):
        self.addDirectoryItem(42023, 'iptvChannels', 'live.png', 'fanart.jpg')
	self.addDirectoryItem('Swift Streams', 'swiftNavigator', 'live.png', '')
	self.addDirectoryItem('AcronaiTV',  'acronaitv_menu',  'live.png',  'DefaultTVShows.png')
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
        self.addDirectoryItem(32641, 'openSettings&query=7.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32556, 'libraryNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32613, 'clearAllCache', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32050, 'clearSources', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32052, 'clearCache', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32614, 'clearMetaCache', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32604, 'clearCacheSearch', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem('Clear ResolveURL Cache', 'clearResolveURLcache', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32609, 'urlResolver', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem('[COLOR %s][X][/COLOR]-Toggle RealDebrid (ResolveURL)' % isDbird, 'ToggleDbird', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem('[COLOR %s][X][/COLOR]-Toggle AllDebrid (ResolveURL)' % isAdbird, 'ToggleAdbird', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem('[COLOR %s][X][/COLOR]-Toggle PremiumizeMe (ResolveURL)' % isPreMe, 'TogglePreMe', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32073, 'authTrakt', 'trakt.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(42026,  'PairEm',  'tools.png',  'DefaultAddonProgram.png', isFolder=False)
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
        self.addDirectoryItem(32001, 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')
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
            control.infoDialog('', control.lang(32074).encode('utf-8'), time=5000, sound=False)
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

#######################################################################
# News and Update Code
    def news(self):
            message=self.open_news_url(self.NEWSFILE)
            r = open(self.LOCALNEWS)
            compfile = r.read()       
            if len(message)>1:
                    if compfile == message:pass
                    else:
                            text_file = open(self.LOCALNEWS, "w")
                            text_file.write(message)
                            text_file.close()
                            compfile = message
            self.showText('Status & Information', compfile)
        
    def open_news_url(self, url):
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'klopp')
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            print link
            return link

    def showText(self, heading, text):
        id = 10147
        xbmc.executebuiltin('ActivateWindow(%d)' % id)
        xbmc.sleep(500)
        win = xbmcgui.Window(id)
        retry = 50
        while (retry > 0):
            try:
                xbmc.sleep(10)
                retry -= 1
                win.getControl(1).setLabel(heading)
                win.getControl(5).setText(text)
                quit()
                return
            except: pass
#######################################################################



##################################################################################################################################################################### 

    def collectionBoxset(self):
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]48 Hrs.[/COLOR] [COLOR yellow] (1982-1990)[/COLOR]', 'collections&url=fortyeighthours', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Ace Ventura[/COLOR] [COLOR yellow] (1994-1995)[/COLOR]', 'collections&url=aceventura', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Airplane[/COLOR] [COLOR yellow] (1980-1982)[/COLOR]', 'collections&url=airplane', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Airport[/COLOR] [COLOR yellow] (1970-1979)[/COLOR]', 'collections&url=airport', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]American Graffiti[/COLOR] [COLOR yellow] (1973-1979)[/COLOR]', 'collections&url=americangraffiti', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Anaconda[/COLOR] [COLOR yellow] (1997-2004)[/COLOR]', 'collections&url=anaconda', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Analyze This[/COLOR] [COLOR yellow] (1999-2002)[/COLOR]', 'collections&url=analyzethis', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Anchorman[/COLOR] [COLOR yellow] (2004-2013)[/COLOR]', 'collections&url=anchorman', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Austin Powers[/COLOR] [COLOR yellow] (1997-2002)[/COLOR]', 'collections&url=austinpowers', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Avengers[/COLOR] [COLOR yellow] (2008-2017)[/COLOR]', 'collections&url=avengers', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Back to the Future[/COLOR] [COLOR yellow] (1985-1990)[/COLOR]', 'collections&url=backtothefuture', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Bad Boys[/COLOR] [COLOR yellow] (1995-2003)[/COLOR]', 'collections&url=badboys', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Bad Santa[/COLOR] [COLOR yellow] (2003-2016)[/COLOR]', 'collections&url=badsanta', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Basic Instinct[/COLOR] [COLOR yellow] (1992-2006)[/COLOR]', 'collections&url=basicinstinct', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Batman[/COLOR] [COLOR yellow] (1989-2016)[/COLOR]', 'collections&url=batman', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Beverly Hills Cop[/COLOR] [COLOR yellow] (1984-1994)[/COLOR]', 'collections&url=beverlyhillscop', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Big Mommas House[/COLOR] [COLOR yellow] (2000-2011)[/COLOR]', 'collections&url=bigmommashouse', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Blues Brothers[/COLOR] [COLOR yellow] (1980-1998)[/COLOR]', 'collections&url=bluesbrothers', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Bourne[/COLOR] [COLOR yellow] (2002-2016)[/COLOR]', 'collections&url=bourne', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Bruce Almighty[/COLOR] [COLOR yellow] (2003-2007)[/COLOR]', 'collections&url=brucealmighty', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Caddyshack[/COLOR] [COLOR yellow] (1980-1988)[/COLOR]', 'collections&url=caddyshack', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Cheaper by the Dozen[/COLOR] [COLOR yellow] (2003-2005)[/COLOR]', 'collections&url=cheaperbythedozen', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Cheech and Chong[/COLOR] [COLOR yellow] (1978-1984)[/COLOR]', 'collections&url=cheechandchong', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Childs Play[/COLOR] [COLOR yellow] (1988-2004)[/COLOR]', 'collections&url=childsplay', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]City Slickers[/COLOR] [COLOR yellow] (1991-1994)[/COLOR]', 'collections&url=cityslickers', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Conan[/COLOR] [COLOR yellow] (1982-2011)[/COLOR]', 'collections&url=conan', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Crank[/COLOR] [COLOR yellow] (2006-2009)[/COLOR]', 'collections&url=crank', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Crocodile Dundee[/COLOR] [COLOR yellow] (1986-2001)[/COLOR]', 'collections&url=crodiledunde', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Da Vinci Code[/COLOR] [COLOR yellow] (2006-2017)[/COLOR]', 'collections&url=davincicode', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Daddy Day Care[/COLOR] [COLOR yellow] (2003-2007)[/COLOR]', 'collections&url=daddydaycare', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Dark Knight Trilogy[/COLOR] [COLOR yellow] (2005-2013)[/COLOR]', 'collections&url=darkknight', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Death Wish[/COLOR] [COLOR yellow] (1974-1994)[/COLOR]', 'collections&url=deathwish', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Delta Force[/COLOR] [COLOR yellow] (1986-1990)[/COLOR]', 'collections&url=deltaforce', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Die Hard[/COLOR] [COLOR yellow] (1988-2013)[/COLOR]', 'collections&url=diehard', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Dirty Dancing[/COLOR] [COLOR yellow] (1987-2004)[/COLOR]', 'collections&url=dirtydancing', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Dirty Harry[/COLOR] [COLOR yellow] (1971-1988)[/COLOR]', 'collections&url=dirtyharry', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Dumb and Dumber[/COLOR] [COLOR yellow] (1994-2014)[/COLOR]', 'collections&url=dumbanddumber', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Escape from New York[/COLOR] [COLOR yellow] (1981-1996)[/COLOR]', 'collections&url=escapefromnewyork', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Every Which Way But Loose[/COLOR] [COLOR yellow] (1978-1980)[/COLOR]', 'collections&url=everywhichwaybutloose', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Exorcist[/COLOR] [COLOR yellow] (1973-2005)[/COLOR]', 'collections&url=exorcist', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Expendables[/COLOR] [COLOR yellow] (2010-2014)[/COLOR]', 'collections&url=theexpendables', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Fantastic Four[/COLOR] [COLOR yellow] (2005-2015)[/COLOR]', 'collections&url=fantasticfour', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Fast and the Furious[/COLOR] [COLOR yellow] (2001-2017)[/COLOR]', 'collections&url=fastandthefurious', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Father of the Bride[/COLOR] [COLOR yellow] (1991-1995)[/COLOR]', 'collections&url=fatherofthebride', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Fletch[/COLOR] [COLOR yellow] (1985-1989)[/COLOR]', 'collections&url=fletch', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Friday[/COLOR] [COLOR yellow] (1995-2002)[/COLOR]', 'collections&url=friday', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Friday the 13th[/COLOR] [COLOR yellow] (1980-2009)[/COLOR]', 'collections&url=fridaythe13th', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Fugitive[/COLOR] [COLOR yellow] (1993-1998)[/COLOR]', 'collections&url=fugitive', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]G.I. Joe[/COLOR] [COLOR yellow] (2009-2013)[/COLOR]', 'collections&url=gijoe', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Get Shorty[/COLOR] [COLOR yellow] (1995-2005)[/COLOR]', 'collections&url=getshorty', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Gettysburg[/COLOR] [COLOR yellow] (1993-2003)[/COLOR]', 'collections&url=gettysburg', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Ghost Rider[/COLOR] [COLOR yellow] (2007-2011)[/COLOR]', 'collections&url=ghostrider', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Ghostbusters[/COLOR] [COLOR yellow] (1984-2016)[/COLOR]', 'collections&url=ghostbusters', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Gods Not Dead[/COLOR] [COLOR yellow] (2014-2016)[/COLOR]', 'collections&url=godsnotdead', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Godfather[/COLOR] [COLOR yellow] (1972-1990)[/COLOR]', 'collections&url=godfather', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Godzilla[/COLOR] [COLOR yellow] (1956-2016)[/COLOR]', 'collections&url=godzilla', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Grown Ups[/COLOR] [COLOR yellow] (2010-2013)[/COLOR]', 'collections&url=grownups', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Grumpy Old Men[/COLOR] [COLOR yellow] (2010-2013)[/COLOR]', 'collections&url=grumpyoldmen', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Guns of Navarone[/COLOR] [COLOR yellow] (1961-1978)[/COLOR]', 'collections&url=gunsofnavarone', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Halloween[/COLOR] [COLOR yellow] (1978-2009)[/COLOR]', 'collections&url=halloween', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hangover[/COLOR] [COLOR yellow] (2009-2013)[/COLOR]', 'collections&url=hangover', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hannibal Lector[/COLOR] [COLOR yellow] (1986-2007)[/COLOR]', 'collections&url=hanniballector', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hellraiser[/COLOR] [COLOR yellow] (1987-1996)[/COLOR]', 'collections&url=hellraiser', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Honey I Shrunk the Kids[/COLOR] [COLOR yellow] (1989-1995)[/COLOR]', 'collections&url=honeyishrunkthekids', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Horrible Bosses[/COLOR] [COLOR yellow] (2011-2014)[/COLOR]', 'collections&url=horriblebosses', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hostel[/COLOR] [COLOR yellow] (2005-2011)[/COLOR]', 'collections&url=hostel', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hot Shots[/COLOR] [COLOR yellow] (1991-1996)[/COLOR]', 'collections&url=hotshots', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Hulk[/COLOR] [COLOR yellow] (2003-2008)[/COLOR]', 'collections&url=hulk', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Independence Day[/COLOR] [COLOR yellow] (1996-2016)[/COLOR]', 'collections&url=independenceday', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Indiana Jones[/COLOR] [COLOR yellow] (1981-2008)[/COLOR]', 'collections&url=indianajones', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Insidious[/COLOR] [COLOR yellow] (2010-2015)[/COLOR]', 'collections&url=insidious', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Iron Eagle[/COLOR] [COLOR yellow] (1986-1992)[/COLOR]', 'collections&url=ironeagle', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Iron Man[/COLOR] [COLOR yellow] (2008-2013)[/COLOR]', 'collections&url=ironman', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jack Reacher[/COLOR] [COLOR yellow] (2012-2016)[/COLOR]', 'collections&url=jackreacher', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jack Ryan[/COLOR] [COLOR yellow] (1990-2014)[/COLOR]', 'collections&url=jackryan', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jackass[/COLOR] [COLOR yellow] (2002-2013)[/COLOR]', 'collections&url=jackass', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]James Bond[/COLOR] [COLOR yellow] (1963-2015)[/COLOR]', 'collections&url=jamesbond', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jaws[/COLOR] [COLOR yellow] (1975-1987)[/COLOR]', 'collections&url=jaws', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jeepers Creepers[/COLOR] [COLOR yellow] (2001-2017)[/COLOR]', 'collections&url=jeeperscreepers', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]John Wick[/COLOR] [COLOR yellow] (2014-2017)[/COLOR]', 'collections&url=johnwick', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jumanji[/COLOR] [COLOR yellow] (1995-2005)[/COLOR]', 'collections&url=jumanji', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Jurassic Park[/COLOR] [COLOR yellow] (1993-2015)[/COLOR]', 'collections&url=jurassicpark', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Kick-Ass[/COLOR] [COLOR yellow] (2010-2013)[/COLOR]', 'collections&url=kickass', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Kill Bill[/COLOR] [COLOR yellow] (2003-2004)[/COLOR]', 'collections&url=killbill', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]King Kong[/COLOR] [COLOR yellow] (1933-2016)[/COLOR]', 'collections&url=kingkong', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Lara Croft[/COLOR] [COLOR yellow] (2001-2003)[/COLOR]', 'collections&url=laracroft', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Legally Blonde[/COLOR] [COLOR yellow] (2001-2003)[/COLOR]', 'collections&url=legallyblonde', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Lethal Weapon[/COLOR] [COLOR yellow] (1987-1998)[/COLOR]', 'collections&url=leathalweapon', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Look Whos Talking[/COLOR] [COLOR yellow] (1989-1993)[/COLOR]', 'collections&url=lookwhostalking', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Machete[/COLOR] [COLOR yellow] (2010-2013)[/COLOR]', 'collections&url=machete', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Magic Mike[/COLOR] [COLOR yellow] (2012-2015)[/COLOR]', 'collections&url=magicmike', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Major League[/COLOR] [COLOR yellow] (1989-1998)[/COLOR]', 'collections&url=majorleague', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Man from Snowy River[/COLOR] [COLOR yellow] (1982-1988)[/COLOR]', 'collections&url=manfromsnowyriver', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Mask[/COLOR] [COLOR yellow] (1994-2005)[/COLOR]', 'collections&url=mask', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Matrix[/COLOR] [COLOR yellow] (1999-2003)[/COLOR]', 'collections&url=matrix', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Mechanic[/COLOR] [COLOR yellow] (2011-2016)[/COLOR]', 'collections&url=themechanic', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Meet the Parents[/COLOR] [COLOR yellow] (2000-2010)[/COLOR]', 'collections&url=meettheparents', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Men in Black[/COLOR] [COLOR yellow] (1997-2012)[/COLOR]', 'collections&url=meninblack', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Mighty Ducks[/COLOR] [COLOR yellow] (1995-1996)[/COLOR]', 'collections&url=mightyducks', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Miss Congeniality[/COLOR] [COLOR yellow] (2000-2005)[/COLOR]', 'collections&url=misscongeniality', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Missing in Action[/COLOR] [COLOR yellow] (1984-1988)[/COLOR]', 'collections&url=missinginaction', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Mission Impossible[/COLOR] [COLOR yellow] (1996-2015)[/COLOR]', 'collections&url=missionimpossible', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Naked Gun[/COLOR] [COLOR yellow] (1988-1994)[/COLOR]', 'collections&url=nakedgun', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]National Lampoon[/COLOR] [COLOR yellow] (1978-2006)[/COLOR]', 'collections&url=nationallampoon', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]National Lampoons Vacation[/COLOR] [COLOR yellow] (1983-2015)[/COLOR]', 'collections&url=nationallampoonsvacation', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]National Treasure[/COLOR] [COLOR yellow] (2004-2007)[/COLOR]', 'collections&url=nationaltreasure', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Neighbors[/COLOR] [COLOR yellow] (2014-2016)[/COLOR]', 'collections&url=neighbors', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Night at the Museum[/COLOR] [COLOR yellow] (2006-2014)[/COLOR]', 'collections&url=nightatthemuseum', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Nightmare on Elm Street[/COLOR] [COLOR yellow] (1984-2010)[/COLOR]', 'collections&url=nightmareonelmstreet', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Now You See Me[/COLOR] [COLOR yellow] (2013-2016)[/COLOR]', 'collections&url=nowyouseeme', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Nutty Professor[/COLOR] [COLOR yellow] (1996-2000)[/COLOR]', 'collections&url=nuttyprofessor', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Oceans Eleven[/COLOR] [COLOR yellow] (2001-2007)[/COLOR]', 'collections&url=oceanseleven', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Odd Couple[/COLOR] [COLOR yellow] (1968-1998)[/COLOR]', 'collections&url=oddcouple', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Oh, God[/COLOR] [COLOR yellow] (1977-1984)[/COLOR]', 'collections&url=ohgod', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Olympus Has Fallen[/COLOR] [COLOR yellow] (2013-2016)[/COLOR]', 'collections&url=olympushasfallen', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Omen[/COLOR] [COLOR yellow] (1976-1981)[/COLOR]', 'collections&url=omen', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Paul Blart Mall Cop[/COLOR] [COLOR yellow] (2009-2015)[/COLOR]', 'collections&url=paulblart', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Pirates of the Caribbean[/COLOR] [COLOR yellow] (2003-2017)[/COLOR]', 'collections&url=piratesofthecaribbean', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Planet of the Apes[/COLOR] [COLOR yellow] (1968-2014)[/COLOR]', 'collections&url=planetoftheapes', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Police Academy[/COLOR] [COLOR yellow] (1984-1994)[/COLOR]', 'collections&url=policeacademy', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Poltergeist[/COLOR] [COLOR yellow] (1982-1988)[/COLOR]', 'collections&url=postergeist', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Porkys[/COLOR] [COLOR yellow] (1981-1985)[/COLOR]', 'collections&url=porkys', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Predator[/COLOR] [COLOR yellow] (1987-2010)[/COLOR]', 'collections&url=predator', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Purge[/COLOR] [COLOR yellow] (2013-2016)[/COLOR]', 'collections&url=thepurge', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Rambo[/COLOR] [COLOR yellow] (1982-2008)[/COLOR]', 'collections&url=rambo', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]RED[/COLOR] [COLOR yellow] (2010-2013)[/COLOR]', 'collections&url=red', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Revenge of the Nerds[/COLOR] [COLOR yellow] (1984-1987)[/COLOR]', 'collections&url=revengeofthenerds', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Riddick[/COLOR] [COLOR yellow] (2000-2013)[/COLOR]', 'collections&url=riddick', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Ride Along[/COLOR] [COLOR yellow] (2014-2016)[/COLOR]', 'collections&url=ridealong', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Ring[/COLOR] [COLOR yellow] (2002-2017)[/COLOR]', 'collections&url=thering', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]RoboCop[/COLOR] [COLOR yellow] (1987-1993)[/COLOR]', 'collections&url=robocop', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Rocky[/COLOR] [COLOR yellow] (1976-2015)[/COLOR]', 'collections&url=rocky', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Romancing the Stone[/COLOR] [COLOR yellow] (1984-1985)[/COLOR]', 'collections&url=romancingthestone', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Rush Hour[/COLOR] [COLOR yellow] (1998-2007)[/COLOR]', 'collections&url=rushhour', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Santa Clause[/COLOR] [COLOR yellow] (1994-2006)[/COLOR]', 'collections&url=santaclause', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Saw[/COLOR] [COLOR yellow] (2004-2010)[/COLOR]', 'collections&url=saw', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Sex and the City[/COLOR] [COLOR yellow] (2008-2010)[/COLOR]', 'collections&url=sexandthecity', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Shaft[/COLOR] [COLOR yellow] (1971-2000)[/COLOR]', 'collections&url=shaft', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Shanghai Noon[/COLOR] [COLOR yellow] (2000-2003)[/COLOR]', 'collections&url=shanghainoon', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Sin City[/COLOR] [COLOR yellow] (2005-2014)[/COLOR]', 'collections&url=sincity', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Sinister[/COLOR] [COLOR yellow] (2012-2015)[/COLOR]', 'collections&url=sinister', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Sister Act[/COLOR] [COLOR yellow] (1995-1993)[/COLOR]', 'collections&url=sisteract', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Smokey and the Bandit[/COLOR] [COLOR yellow] (1977-1986)[/COLOR]', 'collections&url=smokeyandthebandit', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Speed[/COLOR] [COLOR yellow] (1994-1997)[/COLOR]', 'collections&url=speed', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Spider-Man[/COLOR] [COLOR yellow] (2002-2017)[/COLOR]', 'collections&url=spiderman', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Stakeout[/COLOR] [COLOR yellow] (1987-1993)[/COLOR]', 'collections&url=stakeout', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Star Trek[/COLOR] [COLOR yellow] (1979-2016)[/COLOR]', 'collections&url=startrek', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Star Wars[/COLOR] [COLOR yellow] (1977-2015)[/COLOR]', 'collections&url=starwars', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Superman[/COLOR] [COLOR yellow] (1978-2016)[/COLOR]', 'collections&url=superman', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Sting[/COLOR] [COLOR yellow] (1973-1983)[/COLOR]', 'collections&url=thesting', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Taken[/COLOR] [COLOR yellow] (2008-2014)[/COLOR]', 'collections&url=taken', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Taxi[/COLOR] [COLOR yellow] (1998-2007)[/COLOR]', 'collections&url=taxi', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Ted[/COLOR] [COLOR yellow] (2012-2015)[/COLOR]', 'collections&url=ted', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Teen Wolf[/COLOR] [COLOR yellow] (1985-1987)[/COLOR]', 'collections&url=teenwolf', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Terminator[/COLOR] [COLOR yellow] (1984-2015)[/COLOR]', 'collections&url=terminator', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Terms of Endearment[/COLOR] [COLOR yellow] (1983-1996)[/COLOR]', 'collections&url=termsofendearment', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Texas Chainsaw Massacre[/COLOR] [COLOR yellow] (1974-2013)[/COLOR]', 'collections&url=texaschainsawmassacre', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]The Thing[/COLOR] [COLOR yellow] (1982-2011)[/COLOR]', 'collections&url=thething', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Thomas Crown Affair[/COLOR] [COLOR yellow] (1968-1999)[/COLOR]', 'collections&url=thomascrownaffair', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Transporter[/COLOR] [COLOR yellow] (2002-2015)[/COLOR]', 'collections&url=transporter', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Under Siege[/COLOR] [COLOR yellow] (1992-1995)[/COLOR]', 'collections&url=undersiege', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Universal Soldier[/COLOR] [COLOR yellow] (1992-2012)[/COLOR]', 'collections&url=universalsoldier', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Wall Street[/COLOR] [COLOR yellow] (1987-2010)[/COLOR]', 'collections&url=wallstreet', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Waynes World[/COLOR] [COLOR yellow] (1992-1993)[/COLOR]', 'collections&url=waynesworld', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Weekend at Bernies[/COLOR] [COLOR yellow] (1989-1993)[/COLOR]', 'collections&url=weekendatbernies', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Whole Nine Yards[/COLOR] [COLOR yellow] (2000-2004)[/COLOR]', 'collections&url=wholenineyards', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]X-Files[/COLOR] [COLOR yellow] (1998-2008)[/COLOR]', 'collections&url=xfiles', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]X-Men[/COLOR] [COLOR yellow] (2000-2016)[/COLOR]', 'collections&url=xmen', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]xXx[/COLOR] [COLOR yellow] (2002-2005)[/COLOR]', 'collections&url=xxx', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Young Guns[/COLOR] [COLOR yellow] (1988-1990)[/COLOR]', 'collections&url=youngguns', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Zoolander[/COLOR] [COLOR yellow] (2001-2016)[/COLOR]', 'collections&url=zoolander', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR yellow]• [/COLOR][/B][COLOR ghostwhite]Zorro[/COLOR] [COLOR yellow] (1998-2005)[/COLOR]', 'collections&url=zorro', 'boxsets14.png', 'DefaultRecentlyAddedMovies.png')

        self.endDirectory()

    def MirrorcollectionBox(self):
	self.addDirectoryItem('TMDB Mirror Collection', 'collections&url=moviemirror', 'mymovies.png', 'DefaultVideoPlaylists.png')
	self.addDirectoryItem('MovieCollectionBox', 'collectionBoxset', 'people-watching.png', 'DefaultMovies.png')	
	#self.addDirectoryItem('Christmas movies', 'collections&url=xmasmovies', 'mymovies.png', 'DefaultVideoPlaylists.png')
	self.addDirectoryItem('Disney', 'collections&url=disneymovies', 'mymovies.png', 'DefaultVideoPlaylists.png')
	self.addDirectoryItem('Kids', 'collections&url=kidsmovies', 'mymovies.png', 'DefaultVideoPlaylists.png')
	self.addDirectoryItem('Kids BoxSets', 'collectionBoxsetKids', 'kidsboxsets.png', 'DefaultVideoPlaylists.png')
	self.addDirectoryItem('Kids BoxSets TMDB', 'collections&url=kidsboxcollection2', 'kidsboxsets.png', 'DefaultVideoPlaylists.png')


	
	self.endDirectory()



    def vipbox(self):
        if self.getMenuEnabled('navi.customList') == True:
            self.addDirectoryItem('Custom List', 'navCustom', 'highly-rated.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.dbMC') == True:
            self.addDirectoryItem(42024, 'dbMC', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.radio') == True:
            self.addDirectoryItem('Radio Zenders', 'radioNavigator', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.tvReviews') == True:
            self.addDirectoryItem(326232, 'tvReviews', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.movieReviews') == True:
            self.addDirectoryItem(32623, 'movieReviews', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.docuHeaven') == True:
            self.addDirectoryItem(32631, 'docuHeaven', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.kidscorner') == True:
            self.addDirectoryItem(32610, 'kidscorner', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.fitness') == True:
            self.addDirectoryItem(32611, 'fitness', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.legends') == True:
            self.addDirectoryItem(32612, 'legends', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.podcast') == True:
            self.addDirectoryItem(32620, 'podcastNavigator', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.xxx') == True:
            self.addDirectoryItem('[COLOR black]xxx[/COLOR]', 'navXXX', 'highly-rated.png', 'DefaultTVShows.png')
        self.endDirectory()
	

    def endDirectory(self):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)


