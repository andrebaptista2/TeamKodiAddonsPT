# -*- coding: utf-8 -*-

import sys, os
from os.path import join
import urllib, urllib2, re
import webbrowser
import operator

## use std kodi modules 
import xbmc, xbmcaddon, xbmcplugin, xbmcgui
from xbmcplugin import endOfDirectory , addDirectoryItem
import koding
from koding import Add_Dir

#import my stuff
from resources.lib._addon import *
from resources.lib._common import *
from resources.lib import clean_name

import resolveurl as RESOLVE

chkV = (xbmc.getInfoLabel('System.BuildVersion')) 
if chkV.startswith('17'):
    myPath = sys.path[0]
else:
    myPath = os.path.dirname(__file__)

# Get the plugin url in plugin:// notation. 
#    pluginUrl = sys.argv[0] 
# Get the plugin handle as an integer number. 
#    pluginHandle = int(sys.argv[1])

# default artwork setup - un hash to use std addon artwork
#      myIcon= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.jpg')) 
#      myThumb= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.jpg'))
#      myWall = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg')) 

# default artwork setup
#    addonPath = sys.path[0]
#    addonPath1 = join('special://home/addons',addon_id)
#            artPath = join('special://home/addons/' + addon_id,'resources/art')
artPath = join(myPath,'resources/art')
ICON = 'live.png'       # used in menus
ICON2 = 'live.png'     # used in playlinks
ICON3 = 'NFL.png'    
ICON4 = 'NHL.png'
ICON5 = 'NBATV.png'
ICON6 = 'NCAA.png'
ICON7 = 'WWE.png'
ICON8 = 'MMA.png'
ICON9 = 'MLB-Network.png'

WALL = 'wall.jpg'

myIcon= join (artPath,ICON)   
myIcon2= join (artPath,ICON2)   
myIcon3= join (artPath,ICON3)   
myIcon4= join (artPath,ICON4)   
myIcon5= join (artPath,ICON5)   
myIcon6= join (artPath,ICON6)   
myIcon7= join (artPath,ICON7)   
myIcon8= join (artPath,ICON8)   
myIcon9= join (artPath,ICON9)   

myThumb= join (artPath,ICON)   
myWall = join (artPath,WALL)   

# use to create check xml file
#    xmlCheck = 'SportsList.xml'
#    xmlPath = join(addonPath,'resources/xml')
#    f = open(join(xmlPath,xmlCheck),'w').close ()

#    print '\n'+'PJ DEBUG top -- myIcon = '+myIcon
#    print '\n'+'PJ DEBUG top -- myWall= '+myWall
### ^^^^ std file start         ####
### ^^^^ edit icons if reqd ####
#####################

def index():
    print 'Index mode'
    #    openloadMenu()
    title = '[COLOR deepskyblue]NFL Live[COLOR FFff8397b0][I] [/I][/COLOR]'  
    mode = 4
    #            Menu(title,'',mode,myIcon3,myWall,'','','')   
    
    title = '[COLOR deepskyblue]NHL Live [/COLOR][COLOR FFff8397b0][I] [/I][/COLOR]'  
    mode = 5
    #            Menu(title,'',mode,myIcon4,myWall,'','','')   
    
    title = '[COLOR deepskyblue]NBA Live [/COLOR][COLOR FFff8397b0][I] [/I][/COLOR]'  
    mode = 6
    #            Menu(title,'',mode,myIcon5,myWall,'','','')   
    
    title = '[COLOR deepskyblue]NCAA Live [/COLOR][COLOR FFff8397b0][I] [/I][/COLOR]'  
    mode = 7
    #      !     Menu(title,'',mode,myIcon6,myWall,'','','')   

##### nhl720List - mode10 = streamNHL720()
##### nfl720List  - mode11 - TO DO = streamNFL720()
##### mlb720List  - mode12 = streamMLB720()
##### nba720List  - mode13 - TO DO = streamNBA720()
##### mma720List  - mode14 = streamMMA720()
    title = '[COLOR deepskyblue]NHL Live [/COLOR][COLOR FFff8397b0][I] (720streams)[/I][/COLOR]'  
    mode = 10
    Menu(title,'',mode,myIcon4,myWall,'','','')
    
    title = '[COLOR lightskyblue]NFL Live [/COLOR][COLOR FFff8397b0][I] (720streams)[/I][/COLOR]'  
    mode = 11
    #            Menu(title,'',mode,myIcon3,myWall,'','','')
    
    title = '[COLOR deepskyblue]MLB Live [/COLOR][COLOR FFff8397b0][I] (720streams)[/I][/COLOR]'  
    mode = 12
    Menu(title,'',mode,myIcon9,myWall,'','','')
    
    title = '[COLOR lightskyblue]NBA Live [/COLOR][COLOR FFff8397b0][I] (720streams)[/I][/COLOR]'  
    mode = 13
    #            Menu(title,'',mode,myIcon5,myWall,'','','')
    
    title = '[COLOR deepskyblue]MMA Live [/COLOR][COLOR FFff8397b0][I] (720streams)[/I][/COLOR]'  
    mode = 14
    Menu(title,'',mode,myIcon8,myWall,'','','')   
 
###################### 
def main():
    return                      
######################
def nflLive(): 
	#    openloadMenu()      #openload pair option if reqd 
    #    mode = 0
    #    from resources.lib import free
    from resources.lib import sssfree
    print ('Getting freeList')
    #    freeList = free.startScript()
    freeList = sssfree.startScript()
    print 'PJ DEBUG - free list in default is ' + str (freeList)
    icon = join (artPath,ICON3)
    #    return
    
    if not freeList:
        koding.OK_Dialog(title='No Game Available',message='Links are normally active 45 minutes before event time. Click OK to quit.')    
    else:
        #    print 'Games Available'
        #    passThro = 0
        for items in freeList:  
            #    passThro = passThro + 1
            game =items.get('game','Game Missing')
            stream =items.get('stream','Stream Missing')
            print 'Game = '+ str (game)
            print 'Stream = '+ str (stream)
            
            cLink = str (stream)
            cName1 = str (game)
            cName = '[COLOR deepskyblue]'+str (game) + '[/COLOR]'
            icon = myIcon3
            if 'NFL NETWORK' in str (game): icon = join (artPath,'NFL-Network.png')   
            Play(cName,cLink,3,icon,myWall,'','','')    
            
            #        code = urllib.urlopen(stream).getcode() 
            #        print 'PJ DEBUG - NFL code returned ='+str (code)          
            #        if str(code).startswith('2') or str(code).startswith('3'): 
                #        Play(cName,cLink,3,icon,myWall,'','','')            
            #        else:
                #        cName = '[COLOR red][I](offline)  [/I]' + cName
                #        Play(cName,cLink,3,icon,myWall,'','','')    
                                                               
    return  
                  
######################                   
def nhlList (): 
	#    openloadMenu()      #openload pair option if reqd 
    #    mode = 0
    from resources.lib import streamgate
    sgateList = streamgate.startScript()
    print 'PJ DEBUG - default sgate list is ' + str (sgateList)
    icon = join (artPath,ICON4)
    #   mode = 3   #  play
    if not sgateList:
        print 'No NHL Games Available' 
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n'+'[COLOR FFff8397b0]'+'                                   '+'Click OK to quit[/I][/COLOR]' 
        koding.OK_Dialog(title='NHL Games not available....',message=thisMess)  
        index()
    else:
        print 'NHL Games Available'
        for items in sgateList:  
            game = items.get('game','Game Missing')
            stream = items.get('stream','Stream Missing')
            venue = items.get('venue','Venue Missing')
            bitrate = items.get('bitrate','Bitrate Missing')
            icon = myIcon4
            
            cName1 = str (game) +' ('+venue+')'
            cLink = str (stream)
            if 'home' in venue.lower():
                vCol = 'khaki'
                gCol = 'deepskyblue'
            elif 'away' in venue.lower():
                vCol = 'lightgrey'
                gCol = 'cadetblue'
            else:
                vCol = 'darkgrey'
                gCol = 'lightgrey'
                        
            cName = '[COLOR '+gCol+']'+str (game) +'[COLOR ' + vCol + '][I] ('+venue+') [COLOR FFff8397b0]('+bitrate+')[/I][/COLOR]'
                    
            print 'Game = '+ str (game) +' ('+venue+')'+' ('+bitrate+')'
            print 'Stream = '+ str (stream)
            Play(cName,cLink,3,icon,myWall,'','','')    
            
            #    code = urllib.urlopen(stream).getcode() 
            #    print 'PJ DEBUG - NHL code returned ='+str (code)     
            #    if str(code).startswith('2') or str(code).startswith('3'): 
                #    Play(cName,cLink,3,icon,myWall,'','','')             
            #    else:
                #    cName = '[COLOR red][I](offline)  [/I]' + cName
                #    Play(cName,cLink,3,icon,myWall,'','','')       
              
    return
           
######################
def nba4List(): 
	#    openloadMenu()      #openload pair option if reqd 
    #    mode = 0
    from resources.lib import nba4live
    nba4List = nba4live.startScript()
    print 'PJ DEBUG - default nba4List list is ' + str (nba4List)
    icon = join (artPath,ICON4)
    #   mode = 3   #  play
    if not nba4List:
        print 'No NBA Games Available' 
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n'+'[COLOR FFff8397b0]'+'                                   '+'Click OK to quit[/I][/COLOR]' 
        koding.OK_Dialog(title='NHL Games not available....',message=thisMess)  
        index()
    else:
        print 'NBS Games Available'
        for items in nba4List:  
            awayName =items.get('awayName','awayName Missing')
            homeName =items.get('homeName','homeName Missing')
            stream =items.get('stream','Stream Missing')
            awayImage =items.get('awayImage','awayImage Missing')
            homeImage =items.get('homeImage','homeImage Missing')
                  
            print 'Title = '+ str (awayName) + ' @ '+ str (homeName) 
            print 'Stream = '+ str (stream)
           
            cName = '[COLOR deepskyblue]'+ str (awayName) + ' @ '+ str (homeName) +'[/COLOR]'
            cLink = stream
            icon = myIcon5
                     
            Play(cName,cLink,3,icon,myWall,'','','')    
              
    return
           
######################  
def ncaaList(): 
	#    openloadMenu()      #openload pair option if reqd 
    #    mode = 0
    from resources.lib import ncaa
    ncaaList = ncaa.startScript()
    print 'PJ DEBUG - default ncaa list is ' + str (ncaaList)
    icon = join (artPath,ICON6)
    #   mode = 3   #  play
    if not ncaaList:
        print 'No NBA Games Available' 
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n'+'[COLOR FFff8397b0]'+'                                   '+'Click OK to quit[/I][/COLOR]' 
        koding.OK_Dialog(title='NCAA Games not available....',message=thisMess)  
        index()
    else:
        print 'NCAA Games Available'
            
        for items in ncaaList:  
            game =items.get('game','Game Missing')
            stream =items.get('stream','Stream Missing')
                     
            print 'Title = '+ str (game)
            print 'Stream = '+ str (stream)
        
            cName = '[COLOR deepskyblue]'+str (game) + '[/COLOR]'
            cLink = stream
            icon = myIcon6
            
            Play(cName,cLink,3,icon,myWall,'','','')            
       
    return
######################
##### 720scraper
##### nhl720List - mode10 = streamNHL720()
##### nfl720List  - mode11 - TO DO = streamNFL720()
##### mlb720List  - mode12 = streamMLB720()
##### nba720List  - mode13 - TO DO = streamNBA720()
##### mma720List  - mode14 = streamMMA720()

def streamNHL720():
    from resources.lib import stream720
    nhl720List = stream720.getNHL()
    if not nhl720List:
        print 'No NHL Games Available' 
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n'+'[COLOR FFff8397b0]'+'                                   '+'Click OK to quit[/I][/COLOR]' 
        koding.OK_Dialog(title='NHL Games not available....',message=thisMess)  
        index()
    for items in nhl720List:
        game =items.get('game','Game Missing')
        stream =items.get('stream','Stream Missing')
        quality =items.get('quality','Quality Missing')
        
        cName = '[COLOR deepskyblue]'+str (game) +' [COLOR FFff8397b0][I](' + str (quality) +'k)' + '[/I][/COLOR]'
        cLink = stream
        icon = myIcon4
               
        Play(cName,cLink,3,icon,myWall,'','','')    
        
    return
    
def streamNFL720():
    thisMess = '[COLOR red][I]We will let you know when completed.'+'\n'+'\n'+'[COLOR FFff8397b0]'+'                                   '+'Click OK to quit[/I][/COLOR]' 
    koding.OK_Dialog(title='Section Under Construction....',message=thisMess)  
    index()
    
def streamMLB720():
    from resources.lib import stream720
    mlb720List = stream720.getMLB()
    gameCount = 0
    gameCheck ='start'
    if not mlb720List:
        print 'No MLB Games Available' 
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n'+'[COLOR FFff8397b0]'+'                                   '+'Click OK to quit[/I][/COLOR]' 
        koding.OK_Dialog(title='MLB Games not available....',message=thisMess)  
        index()
    for items in mlb720List:
        
        game =items.get('game','Game Missing')
        stream =items.get('stream','Stream Missing')
        quality =items.get('quality','Quality Missing')
        
        if not gameCheck == game : gameCount = gameCount +1
        
        if gameCount % 2 == 0: 
            gCol = 'deepskyblue'
        else: 
            gCol = 'khaki' # checks if even or odd number  
        
        gameCheck = game
        
        cName = '[COLOR ' + gCol + ']'+str (game) +' [COLOR FFff8397b0][I](' + str (quality) +'k)' + '[/I][/COLOR]'
        cLink = stream
        icon = myIcon9
               
        Play(cName,cLink,3,icon,myWall,'','','')    
        
    return
	
def streamNBA720():
    thisMess = '[COLOR red][I]We will let you know when completed.'+'\n'+'\n'+'[COLOR FFff8397b0]'+'                                   '+'Click OK to quit[/I][/COLOR]' 
    koding.OK_Dialog(title='Section Under Construction....',message=thisMess)  
    index()
    
def streamMMA720():
    from resources.lib import stream720
    mma720List = stream720.getMMA()
    if not mma720List:
        print 'No MMA Streams  Available' 
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n'+'[COLOR FFff8397b0]'+'                                   '+'Click OK to quit[/I][/COLOR]' 
        koding.OK_Dialog(title='MMA Streams not available....',message=thisMess)  
        index()
    for items in mma720List:
        game =items.get('game','Game Missing')
        stream =items.get('stream','Stream Missing')
        quality =items.get('quality','Quality Missing')
        
        cName = '[COLOR deepskyblue]'+str (game) +' [COLOR FFff8397b0][I](' + str (quality) +'k)' + '[/I][/COLOR]'
        cLink = stream
        if 'wwe' in stream:
            icon = myIcon7
        else:
            icon = myIcon8
               
        Play(cName,cLink,3,icon,myWall,'','','')    
        
    return
        
######################
######################
######################


######################
## For Reference - SEE VOD3
##   def Menu(name,url,mode,iconimage,fanart,description,trailer,choice,showcontext=True,allinfo={})
##   Menu(txt,url3,1,ICON,FANART,'','','')
##   Menu('[COLOR red]Favourite Movies[/COLOR]','',4,ICON,FANART,'','',1)
##   
##   def Play(name,url,mode,iconimage,fanart,description,trailer,choice,showcontext=True,allinfo={})   
##   Play(txt,url3,100,ICON,FANART,'','','')
######################
#
#
####################
## KEEP EVERYTHING BELOW
## used everytime
####################   

def chkStream(url):
    playChk = ''
    xbmc.Player().play(url)
    isplaying = koding.Check_Playback()
    if isplaying:
        playChk = 'yes'
        #        dialog.ok('PLAYBACK SUCCESSFUL','Congratulations, playback was successful')
        xbmc.Player().stop()
    else:
        playChk = 'no'
        #        dialog.ok('PLAYBACK FAILED','Sorry, playback failed :(')
    return playChk
####################
def openloadMenu():
    print 'Index mode'
    title = '[COLOR goldenrod]Pair with OpenLoad[/COLOR]'
    link = 'openloadPair()'
    mode = 99
    Menu2(title,link,mode,myIcon3,myWall,'','','')
####################
def openloadPair():
    myplatform =''
    if xbmc.getCondVisibility('system.platform.android'):
        myplatform = 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        myplatform = 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        myplatform = 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        myplatform = 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        myplatform = 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        myplatform = 'ios'
	
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://olpair.com/' ) )
    else:
        opensite = webbrowser . open('https://olpair.com/')
####################  
def urlsolver(url):
    host = RESOLVE.HostedMediaFile(url)
    ValidUrl = host.valid_url()
    if ValidUrl == True :
        resolver = RESOLVE.resolve(url)
    elif ValidUrl == False:
        from resources.lib import genesisresolvers
        resolved=genesisresolvers.get(url).result
        if resolved :
            if isinstance(resolved,list):
                for k in resolved:
                    quality = setting('quality')
                    if k['quality'] == 'HD'  :
                        resolver = k['url']
                        break
                    elif k['quality'] == 'SD' :
                        resolver = k['url']
                    elif k['quality'] == '10080p' and setting('10080pquality') == 'true' :
                        resolver = k['url']
                        break
            else:
                resolver = resolved
    return resolver
####################
def saveXML (xmlPath,fName,data):
    outputFile = fName+'.xml'
    f2 = open(join(xmlPath,outputFile),'w')
    f2.write (fName+'\n')
    f2.write (str (data)+'\n')
    f2.write ('\n')
    f2.close()
####################
# for items that need non playable 
# folder menu items 
# ie take you to another menu
####################

def Menu(name,url,mode,iconimage,fanart,description,trailer,choice,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&trailer="+urllib.quote_plus(trailer)+"&choice="+str(choice)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        #        liz.setProperty("IsPlayable","true")
        
        liz.setProperty("IsPlayable","false")
        #        liz.setProperty("isFolder","true")
        
        #    if showcontext:
            #    contextMenu = []
            #    if not name in movie_favourites_read:
                #    contextMenu.append(('Add to Movie Favourites','XBMC.RunPlugin(%s?choice=1&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            #    if not name in tv_favourites_read:
                #    contextMenu.append(('Add to TV Favorites','XBMC.RunPlugin(%s?choice=2&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            #    if not name in music_favourites_read:
                #    contextMenu.append(('Add to Music Favorites','XBMC.RunPlugin(%s?choice=3&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))				
            #    if not name in kids_favourites_read:
                #    contextMenu.append(('Add to Kids Favorites','XBMC.RunPlugin(%s?choice=4&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            #    liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
####################
# for items that need non playable 
# non folder menu item
# ie take you to menu items that
# need to do somethig like 
# olpair or urlresolve etc
####################

def Menu2(name,url,mode,iconimage,fanart,description,trailer,choice,showcontext=True,allinfo={}):      
        if iconimage == 'IMDB':
            search_name = name
            url3 = url
            imdbIcon = Imdb_Thumb(name,search_name)
            if imdbIcon == 'NONE': 
                iconimage = 'https://m.media-amazon.com/images/G/01/imdb/images/mobile/AppUpsell/IMDbLogo-8429101133._CB470041665_.png'
            else:
                iconimage = imdbIcon
                
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&trailer="+urllib.quote_plus(trailer)+"&choice="+str(choice)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        liz.setProperty("IsPlayable","False")
        #
        #       liz.setProperty("isFolder","False")
        #
        #    if showcontext:
            #    contextMenu = []
            #    if not name in movie_favourites_read:
                #    contextMenu.append(('Add to Movie Favourites','XBMC.RunPlugin(%s?choice=1&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            #    if not name in tv_favourites_read:
                #    contextMenu.append(('Add to TV Favorites','XBMC.RunPlugin(%s?choice=2&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #   %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            #    if not name in music_favourites_read:
                #    contextMenu.append(('Add to Music Favorites','XBMC.RunPlugin(%s?choice=3&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))	
            #    if not name in kids_favourites_read:
                #    contextMenu.append(('Add to Kids Favorites','XBMC.RunPlugin(%s?choice=4&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
			
            #    liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
 
####################
# for items that need playable 
# items and dont need url resolver 
####################

def Play(name,url,mode,iconimage,fanart,description,trailer,choice,showcontext=True,allinfo={}):      
        if iconimage == 'IMDB':
            search_name = name
            url3 = url
            imdbIcon = Imdb_Thumb(name,search_name)
            if imdbIcon == 'NONE': 
                iconimage = 'https://m.media-amazon.com/images/G/01/imdb/images/mobile/AppUpsell/IMDbLogo-8429101133._CB470041665_.png'
            else:
                iconimage = imdbIcon
                
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&trailer="+urllib.quote_plus(trailer)+"&choice="+str(choice)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        liz.setProperty("IsPlayable","True")
        #
        liz.setProperty("isFolder","False")
        #    if showcontext:
            #    contextMenu = []
            #    if not name in movie_favourites_read:
                #    contextMenu.append(('Add to Movie Favourites','XBMC.RunPlugin(%s?choice=1&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            #    if not name in tv_favourites_read:
                #    contextMenu.append(('Add to TV Favorites','XBMC.RunPlugin(%s?choice=2&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #   %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            #    if not name in music_favourites_read:
                #    contextMenu.append(('Add to Music Favorites','XBMC.RunPlugin(%s?choice=3&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))	
            #    if not name in kids_favourites_read:
                #    contextMenu.append(('Add to Kids Favorites','XBMC.RunPlugin(%s?choice=4&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
			
            #    liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)        #    ,isFolder=False)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
####################                
#***********************#              
# for creating popup window with play link choices - needs fixing
def PLAYVIDEO(url):
    Dialog = xbmcgui.Dialog()
    sources = []
    link = openURL(url)
    match = re.compile('<source src="(.+?)".+?res="(.+?)"').findall(link)
    for playlink,quality in match:
        sources.insert(0, {'quality': quality, 'playlink': playlink})
        if len(sources) == len(match):
            choice = Dialog.select('Select Playlink',[link["quality"] for link in sources])
            if choice != -1:
                playlink = sources[choice]['playlink']
                isFolder=False
                xbmc.Player().play(playlink)
                mode = 9
    
####################                                

def openURL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    return link
####################                    
        
        
####################       
         
def myPlay(name,url):
		stream_url = url
		liz        = xbmcgui.ListItem(name, path=stream_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
####################          

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                splitparams={}
                splitparams=pairsofparams[i].split('=')
                if (len(splitparams))==2:
                    param[splitparams[0]]=splitparams[1]
        return param
xbmcplugin.setContent(int(sys.argv[1]), 'movies')

params=get_params()
url=None
name=None
mode=None
playlist=None
iconimage=None
fanart=addon_fanart
playlist=None
fav_mode=None
regexs=None
description=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass

##################
# MODES
##################

if mode==None or mode==0:
    print ('Opening Index mode = {}'.format(mode))
    index()

elif mode==1:
    print ('Opening Main mode = {}'.format(mode))
    main()

elif mode==2:
    print ('this is using std XBMC Player - attempting to play url = {} & mode = {}'.format(url,mode))
    myPLAYER = xbmc.Player()
    myPLAYER.play(url)
    #    myPlay (name,url)
    #    pass

elif mode==3:
    print ('USING STD XBMC PLAYER with resolveurl  if reqd - Attempting to play url = {} & mode = {}'.format(url,mode))
    if 'o' in url and 'load' in url:
        url = urlsolver(url)
    
    liz = xbmcgui.ListItem(name, path=url)
    infoLabels={"title": name}
    liz.setInfo(type="video", infoLabels=infoLabels)
    liz.setProperty('IsPlayable', 'true')
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    
    #    myPLAYER = xbmc.Player()
    #    myPLAYER.play(url)
    #    myPlay (name,url)

elif mode==4:
    print ('Getting NFL Network Live')
    nflLive()
    pass

elif mode==5:
    print ('Getting NHL Live Games')
    nhlList ()
    pass

elif mode==6:
    print ('Getting NBA Live Games')
    nba4List()
    pass

elif mode==7:
    print ('Getting NCAA Live Games')
    ncaaList()
    pass

elif mode==8:
    print ('TBA')
    pass
    
elif mode==9:
    print ('TBA')
    pass

##### nhl720List - mode10 = streamNHL720()
##### nfl720List  - mode11 - TO DO = streamNFL720()
##### mlb720List  - mode12 = streamMLB720()
##### nba720List  - mode13 - TO DO = streamNBA720()
##### mma720List  - mode14 = streamMMA720()

elif mode==10:
    print ('Getting NHL720 Live Games')
    streamNHL720()
    pass
    
elif mode==11:
    print ('Getting NFL720 Live Games')
    streamNFL720()
    pass
    
elif mode==12:
    print ('Getting MLB720 Live Games')
    streamMLB720()
    pass
    
elif mode==13:
    print ('Getting NBA720 Live Games')
    streamNBA720()
    pass
    
elif mode==14:
    print ('Getting MMS720 Live Games')
    streamMMA720()
    pass

####################                    
##    Leave these modes in all the time 
####################                    

elif mode== 99:
    print ('Pairing with Openload')
    openloadPair ()
    #    pass
   
elif mode== 100:
    print ('Getting Selected Links')
    #    GetLink ()
    #    PLAYVIDEO(url)   # not working
    #    pass
    
elif mode== 101: # not reqd?
    print ('Play Selected Link - no resolveURL reqd')
    liz = xbmcgui.ListItem(name, path=url)
    infoLabels={"title": name}
    liz.setInfo(type="video", infoLabels=infoLabels)
    liz.setProperty('IsPlayable', 'true')
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
   

xbmcplugin.endOfDirectory(int(sys.argv[1]))