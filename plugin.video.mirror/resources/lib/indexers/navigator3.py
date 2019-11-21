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

class navigator:
    ADDON_ID      = xbmcaddon.Addon().getAddonInfo('id')
    HOMEPATH      = xbmc.translatePath('special://home/')
    ADDONSPATH    = os.path.join(HOMEPATH, 'addons')
    THISADDONPATH = os.path.join(ADDONSPATH, ADDON_ID)
    NEWSFILE      = base64.b64decode(b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2N0dzRzNmt1')
    LOCALNEWS     = os.path.join(THISADDONPATH, 'whatsnew.txt')


   

    def root(self):           
        if self.getMenuEnabled('navi.monthlyspotlight') == True:
           #self.addDirectoryItem('Monthly Spotlight', 'movies&url=spotlight', 'spotlight.png', 'DefaultRecentlyAddedMovies.png')
           self.addDirectoryItem(32001, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
           self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')
           self.addDirectoryItem(32631, 'docuNavigator', 'documentaries.png', 'DefaultMovies.png')
           self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
           self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')
           self.addDirectoryItem(32005, 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')
           self.addDirectoryItem('Kids Collectie', 'collectionKids', 'DefaultMovies.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.yt') == True:
           self.addDirectoryItem('Youtube Channels', 'youtube', 'youtube.png', 'youtube.png')
        #if (traktIndicators == True and not control.setting('tv.widget.alt') == '0') or (traktIndicators == False and not control.setting('tv.widget') == '0'):
           self.addDirectoryItem(32006, 'tvWidget', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png')

        if not control.setting('furk.api') == '':
            self.addDirectoryItem('Furk.net', 'furkNavigator', 'movies.png', 'movies.png')
        
        self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('Online Status', 'newsNavigator', 'help.png', 'DefaultAddonProgram.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        if downloads == True:
            self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultAddonProgram.png')

      
    def infoCheck(self, version):
        try:
            control.infoDialog('', control.lang(32074).encode('utf-8'), time=5000, sound=False)
            return '1'
        except:
            return '1'


  

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




    def endDirectory(self):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)


