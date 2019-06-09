# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib
import generator
from BeautifulSoup import BeautifulStoneSoup , BeautifulSoup , BeautifulSOAP
try :
 from xml . sax . saxutils import escape
except : traceback . print_exc ( )
try :
 import json
except :
 import simplejson as json
import SimpleDownloader as downloader
import time
if 64 - 64: i11iIiiIii
OO0o = [ '180upload.com' , 'allmyvideos.net' , 'bestreams.net' , 'clicknupload.com' , 'cloudzilla.to' , 'movshare.net' , 'novamov.com' , 'nowvideo.sx' , 'videoweed.es' , 'daclips.in' , 'datemule.com' , 'fastvideo.in' , 'faststream.in' , 'filehoot.com' , 'filenuke.com' , 'sharesix.com' , 'docs.google.com' , 'plus.google.com' , 'picasaweb.google.com' , 'gorillavid.com' , 'gorillavid.in' , 'grifthost.com' , 'hugefiles.net' , 'ipithos.to' , 'ishared.eu' , 'kingfiles.net' , 'mail.ru' , 'my.mail.ru' , 'videoapi.my.mail.ru' , 'mightyupload.com' , 'mooshare.biz' , 'movdivx.com' , 'movpod.net' , 'movpod.in' , 'movreel.com' , 'mrfile.me' , 'nosvideo.com' , 'openload.io' , 'played.to' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'uploaded.net' , 'primeshare.tv' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'uploaded.net' , 'sharerepo.com' , 'stagevu.com' , 'streamcloud.eu' , 'streamin.to' , 'thefile.me' , 'thevideo.me' , 'tusfiles.net' , 'uploadc.com' , 'zalaa.com' , 'uploadrocket.net' , 'uptobox.com' , 'v-vids.com' , 'veehd.com' , 'vidbull.com' , 'videomega.tv' , 'vidplay.net' , 'vidspot.net' , 'vidto.me' , 'vidzi.tv' , 'vimeo.com' , 'vk.com' , 'vodlocker.com' , 'xfileload.com' , 'xvidstage.com' , 'zettahost.tv' ]
Oo0Ooo = [ 'plugin.video.dramasonline' , 'plugin.video.f4mTester' , 'plugin.video.shahidmbcnet' , 'plugin.video.SportsDevil' , 'plugin.stream.vaughnlive.tv' , 'plugin.video.ZemTV-shani' ]
if 85 - 85: OOO0O0O0ooooo % IIii1I . II1 - O00ooooo00
class I1IiiI ( urllib2 . HTTPErrorProcessor ) :
 def http_response ( self , request , response ) :
  return response
 https_response = http_response
 if 27 - 27: iIiiiI1IiI1I1 * IIiIiII11i * IiIIi1I1Iiii - Ooo00oOo00o
I1IiI = False ;
if I1IiI :
 if 73 - 73: OOooOOo / ii11ii1ii
 if 94 - 94: OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo
 try :
  import pysrc . pydevd as pydevd
  if 97 - 97: oO0o0ooO0 - IIII / O0oO - o0oO0
  pydevd . settrace ( 'localhost' , stdoutToServer = True , stderrToServer = True )
 except ImportError :
  sys . stderr . write ( "Error: " +
 "You must add org.python.pydev.debug.pysrc to your PYTHONPATH." )
  sys . exit ( 1 )
  if 100 - 100: i11Ii11I1Ii1i
  if 67 - 67: IIii1I . OoOO . OoOO0ooOOoo0O / O00ooooo00 % iIiiiI1IiI1I1 - OOooOOo
OOo = xbmcaddon . Addon ( 'plugin.video.Martunis' )
Ii1IIii11 = OOo . getAddonInfo ( 'version' )
Oooo0000 = xbmc . translatePath ( OOo . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
i11 = xbmc . translatePath ( OOo . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
I11 = os . path . join ( Oooo0000 , 'favorites' )
Oo0o0000o0o0 = os . path . join ( Oooo0000 , 'history' )
oOo0oooo00o = os . path . join ( Oooo0000 , 'list_revision' )
oO0o0o0ooO0oO = os . path . join ( i11 , 'icon.png' )
oo0o0O00 = os . path . join ( i11 , 'fanart.jpg' )
oO = os . path . join ( i11 , 'source_file' )
i1iiIIiiI111 = Oooo0000
oooOOOOO = os . path . join ( Oooo0000 , 'LivewebTV' )
downloader = downloader . SimpleDownloader ( )
i1iiIII111ii = OOo . getSetting ( 'debug' )
if os . path . exists ( I11 ) == True :
 i1iIIi1 = open ( I11 ) . read ( )
else : i1iIIi1 = [ ]
if os . path . exists ( oO ) == True :
 ii11iIi1I = open ( oO ) . read ( )
else : ii11iIi1I = [ ]
if 6 - 6: OOooOOo * IIII
if 67 - 67: i11Ii11I1Ii1i - OoOO0ooOOoo0O * ii11ii1ii % ii11ii1ii % o00O0oo * OOooOOo
def i1IIiiiii ( string ) :
 if i1iiIII111ii == 'true' :
  xbmc . log ( "[addon.Martunis-%s]: %s" % ( Ii1IIii11 , string ) )
  if 55 - 55: O00ooooo00
  if 70 - 70: Ooo00oOo00o . Ooo00oOo00o - Ooo00oOo00o / OoOO * o0000oOoOoO0o
def OoO000 ( url , headers = None ) :
 try :
  if headers is None :
   headers = { 'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0' }
  IIiiIiI1 = urllib2 . Request ( url , None , headers )
  iiIiIIi = urllib2 . urlopen ( IIiiIiI1 )
  ooOoo0O = iiIiIIi . read ( )
  iiIiIIi . close ( )
  return ooOoo0O
 except urllib2 . URLError , OooO0 :
  i1IIiiiii ( 'URL: ' + url )
  if hasattr ( OooO0 , 'code' ) :
   i1IIiiiii ( 'We failed with error code - %s.' % OooO0 . code )
   xbmc . executebuiltin ( "XBMC.Notification(TV Direto,We failed with error code - " + str ( OooO0 . code ) + ",10000," + oO0o0o0ooO0oO + ")" )
  elif hasattr ( OooO0 , 'reason' ) :
   i1IIiiiii ( 'We failed to reach a server.' )
   i1IIiiiii ( 'Reason: %s' % OooO0 . reason )
   xbmc . executebuiltin ( "XBMC.Notification(TV Direto,We failed to reach a server. - " + str ( OooO0 . reason ) + ",10000," + oO0o0o0ooO0oO + ")" )
   if 35 - 35: o0000oOoOoO0o % o0oO0 % i11iIiiIii / II1
def Ii11iI1i ( ) :
 try :
  if os . path . exists ( I11 ) == True :
   Ooo ( 'Favorites' , 'url' , 4 , os . path . join ( i11 , 'resources' , 'favorite.png' ) , oo0o0O00 , '' , '' , '' , '' )
  if OOo . getSetting ( "browse_xml_database" ) == "true" :
   Ooo ( 'XML Database' , 'http://xbmcplus.xb.funpic.de/www-data/filesystem/' , 15 , oO0o0o0ooO0oO , oo0o0O00 , '' , '' , '' , '' )
  if OOo . getSetting ( "browse_community" ) == "true" :
   Ooo ( 'Community Files' , 'community_files' , 16 , oO0o0o0ooO0oO , oo0o0O00 , '' , '' , '' , '' )
  if OOo . getSetting ( "searchotherplugins" ) == "true" :
   Ooo ( 'Search Other Plugins' , 'Search Plugins' , 25 , oO0o0o0ooO0oO , oo0o0O00 , '' , '' , '' , '' )
  if os . path . exists ( oO ) == True :
   O0o0Oo = json . loads ( open ( oO , "r" ) . read ( ) )
   if 78 - 78: IIii1I - oO0o0ooO0 * Ooo00oOo00o + ii11ii1ii + IIII + IIII
   if len ( O0o0Oo ) > 1 :
    for I11I11i1I in O0o0Oo :
     try :
      if 49 - 49: iIiiiI1IiI1I1 % IIII * OOO0O0O0ooooo
      if isinstance ( I11I11i1I , list ) :
       Ooo ( I11I11i1I [ 0 ] . encode ( 'utf-8' ) , I11I11i1I [ 1 ] . encode ( 'utf-8' ) , 1 , oO0o0o0ooO0oO , oo0o0O00 , '' , '' , '' , '' , 'source' )
      else :
       oOOo0oo = oO0o0o0ooO0oO
       o0oo0o0O00OO = oo0o0O00
       o0oO = ''
       I1i1iii = ''
       credits = ''
       i1iiI11I = ''
       if I11I11i1I . has_key ( 'thumbnail' ) :
        oOOo0oo = I11I11i1I [ 'thumbnail' ]
       if I11I11i1I . has_key ( 'fanart' ) :
        o0oo0o0O00OO = I11I11i1I [ 'fanart' ]
       if I11I11i1I . has_key ( 'description' ) :
        o0oO = I11I11i1I [ 'description' ]
       if I11I11i1I . has_key ( 'date' ) :
        I1i1iii = I11I11i1I [ 'date' ]
       if I11I11i1I . has_key ( 'genre' ) :
        i1iiI11I = I11I11i1I [ 'genre' ]
       if I11I11i1I . has_key ( 'credits' ) :
        credits = I11I11i1I [ 'credits' ]
       Ooo ( I11I11i1I [ 'title' ] . encode ( 'utf-8' ) , I11I11i1I [ 'url' ] . encode ( 'utf-8' ) , 1 , oOOo0oo , o0oo0o0O00OO , o0oO , i1iiI11I , I1i1iii , credits , 'source' )
     except : traceback . print_exc ( )
   else :
    if len ( O0o0Oo ) == 1 :
     if isinstance ( O0o0Oo [ 0 ] , list ) :
      iiii ( O0o0Oo [ 0 ] [ 1 ] . encode ( 'utf-8' ) , oo0o0O00 )
     else :
      iiii ( O0o0Oo [ 0 ] [ 'url' ] , O0o0Oo [ 0 ] [ 'fanart' ] )
 except : traceback . print_exc ( )
 if 54 - 54: OoOO * o0000oOoOoO0o
def I1IIIii ( url = None ) :
 if url is None :
  if not OOo . getSetting ( "new_file_source" ) == "" :
   oOoOooOo0o0 = OOo . getSetting ( 'new_file_source' ) . decode ( 'utf-8' )
  elif not OOo . getSetting ( "new_url_source" ) == "" :
   oOoOooOo0o0 = OOo . getSetting ( 'new_url_source' ) . decode ( 'utf-8' )
 else :
  oOoOooOo0o0 = url
 if oOoOooOo0o0 == '' or oOoOooOo0o0 is None :
  return
 i1IIiiiii ( 'Adding New Source: ' + oOoOooOo0o0 . encode ( 'utf-8' ) )
 if 61 - 61: ii11ii1ii / Ooo00oOo00o + i11Ii11I1Ii1i * OoOO0ooOOoo0O / OoOO0ooOOoo0O
 OoOo = None
 if 18 - 18: i11iIiiIii
 ooOoo0O = Ii11I ( oOoOooOo0o0 )
 print 'source_url' , oOoOooOo0o0
 if isinstance ( ooOoo0O , BeautifulSOAP ) :
  if ooOoo0O . find ( 'channels_info' ) :
   OoOo = ooOoo0O . channels_info
  elif ooOoo0O . find ( 'items_info' ) :
   OoOo = ooOoo0O . items_info
 if OoOo :
  OOO0OOO00oo = { }
  OOO0OOO00oo [ 'url' ] = oOoOooOo0o0
  try : OOO0OOO00oo [ 'title' ] = OoOo . title . string
  except : pass
  try : OOO0OOO00oo [ 'thumbnail' ] = OoOo . thumbnail . string
  except : pass
  try : OOO0OOO00oo [ 'fanart' ] = OoOo . fanart . string
  except : pass
  try : OOO0OOO00oo [ 'genre' ] = OoOo . genre . string
  except : pass
  try : OOO0OOO00oo [ 'description' ] = OoOo . description . string
  except : pass
  try : OOO0OOO00oo [ 'date' ] = OoOo . date . string
  except : pass
  try : OOO0OOO00oo [ 'credits' ] = OoOo . credits . string
  except : pass
 else :
  if '/' in oOoOooOo0o0 :
   Iii111II = oOoOooOo0o0 . split ( '/' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '\\' in oOoOooOo0o0 :
   Iii111II = oOoOooOo0o0 . split ( '\\' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '%' in Iii111II :
   Iii111II = urllib . unquote_plus ( Iii111II )
  iiii11I = xbmc . Keyboard ( Iii111II , 'Displayed Name, Rename?' )
  iiii11I . doModal ( )
  if ( iiii11I . isConfirmed ( ) == False ) :
   return
  Ooo0OO0oOO = iiii11I . getText ( )
  if len ( Ooo0OO0oOO ) == 0 :
   return
  OOO0OOO00oo = { }
  OOO0OOO00oo [ 'title' ] = Ooo0OO0oOO
  OOO0OOO00oo [ 'url' ] = oOoOooOo0o0
  OOO0OOO00oo [ 'fanart' ] = o0oo0o0O00OO
  if 50 - 50: IIiIiII11i
 if os . path . exists ( oO ) == False :
  Ii1i11IIii1I = [ ]
  Ii1i11IIii1I . append ( OOO0OOO00oo )
  OOOoO0O0o = open ( oO , "w" )
  OOOoO0O0o . write ( json . dumps ( Ii1i11IIii1I ) )
  OOOoO0O0o . close ( )
 else :
  O0o0Oo = json . loads ( open ( oO , "r" ) . read ( ) )
  O0o0Oo . append ( OOO0OOO00oo )
  OOOoO0O0o = open ( oO , "w" )
  OOOoO0O0o . write ( json . dumps ( O0o0Oo ) )
  OOOoO0O0o . close ( )
 OOo . setSetting ( 'new_url_source' , "" )
 OOo . setSetting ( 'new_file_source' , "" )
 xbmc . executebuiltin ( "XBMC.Notification(Martunis,New source added.,5000," + oO0o0o0ooO0oO + ")" )
 if not url is None :
  if 'xbmcplus.xb.funpic.de' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=14,replace)" % sys . argv [ 0 ] )
  elif 'community-links' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=10,replace)" % sys . argv [ 0 ] )
 else : OOo . openSettings ( )
 if 55 - 55: o0000oOoOoO0o + i11Ii11I1Ii1i . O00ooooo00 - OoOO . OOO0O0O0ooooo - i11Ii11I1Ii1i
def o0O ( name ) :
 O0o0Oo = json . loads ( open ( oO , "r" ) . read ( ) )
 for O00oO in range ( len ( O0o0Oo ) ) :
  if isinstance ( O0o0Oo [ O00oO ] , list ) :
   if O0o0Oo [ O00oO ] [ 0 ] == name :
    del O0o0Oo [ O00oO ]
    OOOoO0O0o = open ( oO , "w" )
    OOOoO0O0o . write ( json . dumps ( O0o0Oo ) )
    OOOoO0O0o . close ( )
    break
  else :
   if O0o0Oo [ O00oO ] [ 'title' ] == name :
    del O0o0Oo [ O00oO ]
    OOOoO0O0o = open ( oO , "w" )
    OOOoO0O0o . write ( json . dumps ( O0o0Oo ) )
    OOOoO0O0o . close ( )
    break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 39 - 39: O0oO - iIiiiI1IiI1I1 * Ooo00oOo00o % ii11ii1ii * iIiiiI1IiI1I1 % iIiiiI1IiI1I1
def OoOOOOO ( url , browse = False ) :
 if url is None :
  url = 'http://xbmcplus.xb.funpic.de/www-data/filesystem/'
 iIi1i111II = BeautifulSoup ( OoO000 ( url ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 for I11I11i1I in iIi1i111II ( 'a' ) :
  OoOO00O = I11I11i1I [ 'href' ]
  if not OoOO00O . startswith ( '?' ) :
   oOOoO0O0O0 = I11I11i1I . string
   if oOOoO0O0O0 not in [ 'Parent Directory' , 'recycle_bin/' ] :
    if OoOO00O . endswith ( '/' ) :
     if browse :
      Ooo ( oOOoO0O0O0 , url + OoOO00O , 15 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' )
     else :
      Ooo ( oOOoO0O0O0 , url + OoOO00O , 14 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' )
    elif OoOO00O . endswith ( '.xml' ) :
     if browse :
      Ooo ( oOOoO0O0O0 , url + OoOO00O , 1 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
     else :
      if os . path . exists ( oO ) == True :
       if oOOoO0O0O0 in ii11iIi1I :
        Ooo ( oOOoO0O0O0 + ' (in use)' , url + OoOO00O , 11 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
       else :
        Ooo ( oOOoO0O0O0 , url + OoOO00O , 11 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
      else :
       Ooo ( oOOoO0O0O0 , url + OoOO00O , 11 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
       if 86 - 86: IIiIiII11i + oO0o0ooO0 % i11iIiiIii * OoOO0ooOOoo0O . i11Ii11I1Ii1i * o00O0oo
       if 44 - 44: OoOO0ooOOoo0O
def o0o0oOoOO0 ( browse = False ) :
 iIi1iIiii111 = 'http://community-links.googlecode.com/svn/trunk/'
 iIi1i111II = BeautifulSoup ( OoO000 ( iIi1iIiii111 ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 iIIIi1 = iIi1i111II ( 'ul' ) [ 0 ] ( 'li' ) [ 1 : ]
 for I11I11i1I in iIIIi1 :
  oOOoO0O0O0 = I11I11i1I ( 'a' ) [ 0 ] [ 'href' ]
  if browse :
   Ooo ( oOOoO0O0O0 , iIi1iIiii111 + oOOoO0O0O0 , 1 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
  else :
   Ooo ( oOOoO0O0O0 , iIi1iIiii111 + oOOoO0O0O0 , 11 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
   if 20 - 20: O00ooooo00 + OoOO - i11Ii11I1Ii1i
def Ii11I ( url , data = None ) :
 if url . startswith ( 'http://' ) or url . startswith ( 'https://' ) :
  data = OoO000 ( url )
  if re . search ( "#EXTM3U" , data ) or 'm3u' in url :
   print 'found m3u data'
   return data
 elif data == None :
  if not '/' in url or not '\\' in url :
   print 'No directory found. Lets make the url to cache dir'
   url = os . path . join ( oooOOOOO , url )
  if xbmcvfs . exists ( url ) :
   if url . startswith ( "smb://" ) or url . startswith ( "nfs://" ) :
    IiI11iII1 = xbmcvfs . copy ( url , os . path . join ( Oooo0000 , 'temp' , 'sorce_temp.txt' ) )
    if IiI11iII1 :
     data = open ( os . path . join ( Oooo0000 , 'temp' , 'sorce_temp.txt' ) , "r" ) . read ( )
     xbmcvfs . delete ( os . path . join ( Oooo0000 , 'temp' , 'sorce_temp.txt' ) )
    else :
     i1IIiiiii ( "failed to copy from smb:" )
   else :
    data = open ( url , 'r' ) . read ( )
    if re . match ( "#EXTM3U" , data ) or 'm3u' in url :
     print 'found m3u data'
     return data
  else :
   i1IIiiiii ( "Soup Data not found!" )
   return
 return BeautifulSOAP ( data , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 29 - 29: IiIIi1I1Iiii - OoOO0ooOOoo0O - o00O0oo % IIII - OoOO0ooOOoo0O
 if 91 - 91: Ooo00oOo00o / o00O0oo - iIiiiI1IiI1I1 . o00O0oo
def iiii ( url , fanart , data = None ) :
 iIi1i111II = Ii11I ( url , data )
 if 18 - 18: ii11ii1ii
 if isinstance ( iIi1i111II , BeautifulSOAP ) :
  if 98 - 98: IIII * IIII / IIII + o00O0oo
  if len ( iIi1i111II ( 'channels' ) ) > 0 and OOo . getSetting ( 'donotshowbychannels' ) == 'false' :
   ii111111I1iII = iIi1i111II ( 'channel' )
   for O00ooo0O0 in ii111111I1iII :
    if 23 - 23: IIII
    if 91 - 91: IIii1I + o0oO0
    i1i = ''
    I1I1iIiII1 = 0
    try :
     i1i = O00ooo0O0 ( 'externallink' ) [ 0 ] . string
     I1I1iIiII1 = len ( O00ooo0O0 ( 'externallink' ) )
    except : pass
    if 4 - 4: i11Ii11I1Ii1i + OOO0O0O0ooooo * o0000oOoOoO0o
    if I1I1iIiII1 > 1 : i1i = ''
    if 55 - 55: IiIIi1I1Iiii + IIii1I / OOooOOo * OoOO0ooOOoo0O - i11iIiiIii - oO0o0ooO0
    oOOoO0O0O0 = O00ooo0O0 ( 'name' ) [ 0 ] . string
    ii1ii1ii = O00ooo0O0 ( 'thumbnail' ) [ 0 ] . string
    if ii1ii1ii == None :
     ii1ii1ii = ''
     if 91 - 91: O0oO
    try :
     if not O00ooo0O0 ( 'fanart' ) :
      if OOo . getSetting ( 'use_thumb' ) == "true" :
       iiIii = ii1ii1ii
      else :
       iiIii = fanart
     else :
      iiIii = O00ooo0O0 ( 'fanart' ) [ 0 ] . string
     if iiIii == None :
      raise
    except :
     iiIii = fanart
     if 79 - 79: II1 / OOO0O0O0ooooo
    try :
     o0oO = O00ooo0O0 ( 'info' ) [ 0 ] . string
     if o0oO == None :
      raise
    except :
     o0oO = ''
     if 75 - 75: OOooOOo % ii11ii1ii % ii11ii1ii . o0oO0
    try :
     i1iiI11I = O00ooo0O0 ( 'genre' ) [ 0 ] . string
     if i1iiI11I == None :
      raise
    except :
     i1iiI11I = ''
     if 5 - 5: ii11ii1ii * i11Ii11I1Ii1i + OOooOOo . o0000oOoOoO0o + OOooOOo
    try :
     I1i1iii = O00ooo0O0 ( 'date' ) [ 0 ] . string
     if I1i1iii == None :
      raise
    except :
     I1i1iii = ''
     if 91 - 91: OOO0O0O0ooooo
    try :
     credits = O00ooo0O0 ( 'credits' ) [ 0 ] . string
     if credits == None :
      raise
    except :
     credits = ''
     if 61 - 61: iIiiiI1IiI1I1
    try :
     if i1i == '' :
      Ooo ( oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , ii1ii1ii , iiIii , o0oO , i1iiI11I , I1i1iii , credits , True )
     else :
      if 64 - 64: i11Ii11I1Ii1i / OOooOOo - OOO0O0O0ooooo - o00O0oo
      Ooo ( oOOoO0O0O0 . encode ( 'utf-8' ) , i1i . encode ( 'utf-8' ) , 1 , ii1ii1ii , iiIii , o0oO , i1iiI11I , I1i1iii , None , 'source' )
    except :
     i1IIiiiii ( 'There was a problem adding directory from getData(): ' + oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) )
  else :
   i1IIiiiii ( 'No Channels: getItems' )
   O0oOoOOOoOO ( iIi1i111II ( 'item' ) , fanart )
 else :
  ii1ii11IIIiiI ( iIi1i111II )
  if 67 - 67: o00O0oo * OoOO0ooOOoo0O * OoOO + o0000oOoOoO0o / O00ooooo00
  if 11 - 11: oO0o0ooO0 + IIII - i11Ii11I1Ii1i * OoOO0ooOOoo0O % i11iIiiIii - o0oO0
def ii1ii11IIIiiI ( data ) :
 o0oOIIiIi1iI = data . rstrip ( )
 i1IiiiI1iI = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\r\n]+)' ) . findall ( o0oOIIiIi1iI )
 i1iIi = len ( i1IiiiI1iI )
 print 'total m3u links' , i1iIi
 for ooOOoooooo , II1I , O0 in i1IiiiI1iI :
  if 'tvg-logo' in ooOOoooooo :
   ii1ii1ii = i1II1Iiii1I11 ( ooOOoooooo , 'tvg-logo=[\'"](.*?)[\'"]' )
   if ii1ii1ii :
    if ii1ii1ii . startswith ( 'http' ) :
     ii1ii1ii = ii1ii1ii
     if 9 - 9: OoOO / IiIIi1I1Iiii - IIiIiII11i / II1 / IIii1I - ii11ii1ii
    elif not OOo . getSetting ( 'logo-folderPath' ) == "" :
     o00oooO0Oo = OOo . getSetting ( 'logo-folderPath' )
     ii1ii1ii = o00oooO0Oo + ii1ii1ii
     if 78 - 78: oO0o0ooO0 % o0oO0 + OoOO
    else :
     ii1ii1ii = ii1ii1ii
     if 64 - 64: OoOO0ooOOoo0O * OOO0O0O0ooooo . IIiIiII11i + iIiiiI1IiI1I1
     if 6 - 6: OOooOOo / IIII . O0oO . O0oO
  else :
   ii1ii1ii = ''
  if 'type' in ooOOoooooo :
   OO00O0O = i1II1Iiii1I11 ( ooOOoooooo , 'type=[\'"](.*?)[\'"]' )
   if OO00O0O == 'yt-dl' :
    O0 = O0 + "&mode=18"
   elif OO00O0O == 'regex' :
    iIi1iIiii111 = O0 . split ( '&regexs=' )
    if 33 - 33: OOO0O0O0ooooo . O0oO . IIiIiII11i
    OoOOooOOO0 = o0o ( Ii11I ( '' , data = iIi1iIiii111 [ 1 ] ) )
    if 73 - 73: O0oO * OoOO + IIiIiII11i . i11Ii11I1Ii1i
    o0oO00000 ( iIi1iIiii111 [ 0 ] , II1I , ii1ii1ii , '' , '' , '' , '' , '' , None , OoOOooOOO0 , i1iIi )
    continue
   elif OO00O0O == 'ftv' :
    O0 = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( II1I ) + '&url=' + O0 + '&mode=125&ch_fanart=na'
  o0oO00000 ( O0 , II1I , ii1ii1ii , '' , '' , '' , '' , '' , None , '' , i1iIi )
def OOOOoo0Oo ( name , url , fanart ) :
 iIi1i111II = Ii11I ( url )
 ii111iI1iIi1 = iIi1i111II . find ( 'channel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 OOO = ii111iI1iIi1 ( 'item' )
 try :
  iiIii = ii111iI1iIi1 ( 'fanart' ) [ 0 ] . string
  if iiIii == None :
   raise
 except :
  iiIii = fanart
 for O00ooo0O0 in ii111iI1iIi1 ( 'subchannel' ) :
  name = O00ooo0O0 ( 'name' ) [ 0 ] . string
  try :
   ii1ii1ii = O00ooo0O0 ( 'thumbnail' ) [ 0 ] . string
   if ii1ii1ii == None :
    raise
  except :
   ii1ii1ii = ''
  try :
   if not O00ooo0O0 ( 'fanart' ) :
    if OOo . getSetting ( 'use_thumb' ) == "true" :
     iiIii = ii1ii1ii
   else :
    iiIii = O00ooo0O0 ( 'fanart' ) [ 0 ] . string
   if iiIii == None :
    raise
  except :
   pass
  try :
   o0oO = O00ooo0O0 ( 'info' ) [ 0 ] . string
   if o0oO == None :
    raise
  except :
   o0oO = ''
   if 68 - 68: iIiiiI1IiI1I1 + o00O0oo
  try :
   i1iiI11I = O00ooo0O0 ( 'genre' ) [ 0 ] . string
   if i1iiI11I == None :
    raise
  except :
   i1iiI11I = ''
   if 45 - 45: IIII / IIII + o0oO0 + i11Ii11I1Ii1i
  try :
   I1i1iii = O00ooo0O0 ( 'date' ) [ 0 ] . string
   if I1i1iii == None :
    raise
  except :
   I1i1iii = ''
   if 47 - 47: ii11ii1ii + i11Ii11I1Ii1i
  try :
   credits = O00ooo0O0 ( 'credits' ) [ 0 ] . string
   if credits == None :
    raise
  except :
   credits = ''
   if 82 - 82: iIiiiI1IiI1I1 . O0oO - IIii1I - O0oO * iIiiiI1IiI1I1
  try :
   Ooo ( name . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 3 , ii1ii1ii , iiIii , o0oO , i1iiI11I , credits , I1i1iii )
  except :
   i1IIiiiii ( 'There was a problem adding directory - ' + name . encode ( 'utf-8' , 'ignore' ) )
 O0oOoOOOoOO ( OOO , iiIii )
 if 77 - 77: IIii1I * Ooo00oOo00o
 if 95 - 95: IIiIiII11i + i11iIiiIii
def I1Ii ( name , url , fanart ) :
 iIi1i111II = Ii11I ( url )
 ii111iI1iIi1 = iIi1i111II . find ( 'subchannel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 OOO = ii111iI1iIi1 ( 'subitem' )
 O0oOoOOOoOO ( OOO , fanart )
 if 94 - 94: oO0o0ooO0 - iIiiiI1IiI1I1 . o0000oOoOoO0o % o00O0oo . i11iIiiIii + OOO0O0O0ooooo
def O0oOoOOOoOO ( items , fanart ) :
 i1iIi = len ( items )
 i1IIiiiii ( 'Total Items: %s' % i1iIi )
 I1IiiiiI = OOo . getSetting ( 'add_playlist' )
 o0OIiII = OOo . getSetting ( 'ask_playlist_items' )
 ii1iII1II = OOo . getSetting ( 'use_thumb' )
 Iii1I1I11iiI1 = OOo . getSetting ( 'parentalblocked' )
 Iii1I1I11iiI1 = Iii1I1I11iiI1 == "true"
 I1I1i1I = OOo . getSetting ( 'premiumpin' )
 I1I1i1I = I1I1i1I == "NatalManiac"
 for ii1I in items :
  O0oO0 = False
  oO0 = False
  if 75 - 75: i11Ii11I1Ii1i + OOooOOo + ii11ii1ii * o00O0oo % OoOO0ooOOoo0O . IIII
  oOI1Ii1I1 = 'false'
  try :
   oOI1Ii1I1 = ii1I ( 'premium' ) [ 0 ] . string
  except :
   i1IIiiiii ( oOI1Ii1I1 )
   oOI1Ii1I1 = ''
  if oOI1Ii1I1 == 'true' :
   if not I1I1i1I : continue
   if 28 - 28: OOO0O0O0ooooo * IiIIi1I1Iiii - o0000oOoOoO0o % IIii1I * oO0o0ooO0 - i11iIiiIii
   if 7 - 7: IiIIi1I1Iiii + OoOO0ooOOoo0O - o0oO0 % oO0o0ooO0 + OoOO
  ooo0OOOoo = 'false'
  try :
   ooo0OOOoo = ii1I ( 'parentalblock' ) [ 0 ] . string
  except :
   i1IIiiiii ( 'parentalblock Error' )
   ooo0OOOoo = ''
  if ooo0OOOoo == 'true' and Iii1I1I11iiI1 : continue
  if 45 - 45: o0oO0 / IIii1I + OOooOOo * Ooo00oOo00o * o0000oOoOoO0o . IIII
  if 32 - 32: ii11ii1ii . O0oO * o00O0oo
  if 93 - 93: ii11ii1ii % O00ooooo00 . oO0o0ooO0 . i11iIiiIii
  if 56 - 56: OoOO % OOO0O0O0ooooo - IIiIiII11i
  if 100 - 100: oO0o0ooO0 - OOO0O0O0ooooo % OoOO0ooOOoo0O * o0000oOoOoO0o + IIiIiII11i
  if 88 - 88: II1 - Ooo00oOo00o * OOO0O0O0ooooo * II1 . II1
  if 33 - 33: o0oO0 + IIII * OoOO0ooOOoo0O / IIii1I - IIiIiII11i
  try :
   oOOoO0O0O0 = ii1I ( 'title' ) [ 0 ] . string
   if oOOoO0O0O0 is None :
    oOOoO0O0O0 = 'unknown?'
  except :
   i1IIiiiii ( 'Name Error' )
   oOOoO0O0O0 = ''
   if 54 - 54: o0oO0 / o0000oOoOoO0o . OoOO0ooOOoo0O % IIII
   if 57 - 57: i11iIiiIii . OoOO - oO0o0ooO0 - OoOO0ooOOoo0O + OOooOOo
   if 63 - 63: OOooOOo * IIII
  try :
   if ii1I ( 'epg' ) :
    if ii1I . epg_url :
     i1IIiiiii ( 'Get EPG Regex' )
     oo = ii1I . epg_url . string
     iIi1 = ii1I . epg_regex . string
     OoOOoOooooOOo = oOo0O ( oo , iIi1 )
     if OoOOoOooooOOo :
      oOOoO0O0O0 += ' - ' + OoOOoOooooOOo
    elif ii1I ( 'epg' ) [ 0 ] . string > 1 :
     oOOoO0O0O0 += oo0O0 ( ii1I ( 'epg' ) [ 0 ] . string )
   else :
    pass
  except :
   i1IIiiiii ( 'EPG Error' )
  try :
   iIi1iIiii111 = [ ]
   if len ( ii1I ( 'link' ) ) > 0 :
    if 22 - 22: OOooOOo . o0000oOoOoO0o * OOooOOo
    if 54 - 54: O0oO + oO0o0ooO0 % Ooo00oOo00o + II1 - OOO0O0O0ooooo - ii11ii1ii
    for I11I11i1I in ii1I ( 'link' ) :
     if not I11I11i1I . string == None :
      iIi1iIiii111 . append ( I11I11i1I . string )
   elif len ( ii1I ( 'lonk' ) ) > 0 :
    if 77 - 77: o0000oOoOoO0o * IIii1I
    if 98 - 98: IIiIiII11i % oO0o0ooO0 * II1
    for I11I11i1I in ii1I ( 'lonk' ) :
     if not I11I11i1I . string == None :
      iIi1iIiii111 . append ( I11I11i1I . string )
      if 51 - 51: IIii1I . OOooOOo / OoOO0ooOOoo0O + ii11ii1ii
   elif len ( ii1I ( 'sportsdevil' ) ) > 0 :
    for I11I11i1I in ii1I ( 'sportsdevil' ) :
     if not I11I11i1I . string == None :
      I11iI1i1I11I11 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + I11I11i1I . string
      o000O0O = ii1I ( 'referer' ) [ 0 ] . string
      if o000O0O :
       if 18 - 18: IIII - o0000oOoOoO0o . o0oO0 . IIii1I
       I11iI1i1I11I11 = I11iI1i1I11I11 + '%26referer=' + o000O0O
      iIi1iIiii111 . append ( I11iI1i1I11I11 )
   elif len ( ii1I ( 'p2p' ) ) > 0 :
    for I11I11i1I in ii1I ( 'p2p' ) :
     if not I11I11i1I . string == None :
      if 'sop://' in I11I11i1I . string :
       i1I = 'plugin://plugin.video.p2p-streams/?mode=2url=' + I11I11i1I . string + '&' + 'name=' + oOOoO0O0O0
       iIi1iIiii111 . append ( i1I )
      else :
       O0ooooOOoo0O = 'plugin://plugin.video.p2p-streams/?mode=1&url=' + I11I11i1I . string + '&' + 'name=' + oOOoO0O0O0
       iIi1iIiii111 . append ( O0ooooOOoo0O )
   elif len ( ii1I ( 'vaughn' ) ) > 0 :
    for I11I11i1I in ii1I ( 'vaughn' ) :
     if not I11I11i1I . string == None :
      II1IiiIi1i = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel=' + I11I11i1I . string
      iIi1iIiii111 . append ( II1IiiIi1i )
   elif len ( ii1I ( 'ilive' ) ) > 0 :
    for I11I11i1I in ii1I ( 'ilive' ) :
     if not I11I11i1I . string == None :
      if not 'http' in I11I11i1I . string :
       iiI11ii1I1 = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/' + I11I11i1I . string + '&amp;link=99&amp;mode=iLivePlay'
      else :
       iiI11ii1I1 = 'plugin://plugin.video.tbh.ilive/?url=' + I11I11i1I . string + '&amp;link=99&amp;mode=iLivePlay'
   elif len ( ii1I ( 'yt-dl' ) ) > 0 :
    for I11I11i1I in ii1I ( 'yt-dl' ) :
     if not I11I11i1I . string == None :
      Ooo0OOoOoO0 = I11I11i1I . string + '&mode=18'
      iIi1iIiii111 . append ( Ooo0OOoOoO0 )
   elif len ( ii1I ( 'dm' ) ) > 0 :
    for I11I11i1I in ii1I ( 'dm' ) :
     if not I11I11i1I . string == None :
      oOo0OOoO0 = "plugin://plugin.video.dailymotion_com/?mode=playVideo&url=" + I11I11i1I . string
      iIi1iIiii111 . append ( oOo0OOoO0 )
   elif len ( ii1I ( 'dmlive' ) ) > 0 :
    for I11I11i1I in ii1I ( 'dmlive' ) :
     if not I11I11i1I . string == None :
      oOo0OOoO0 = "plugin://plugin.video.dailymotion_com/?mode=playLiveVideo&url=" + I11I11i1I . string
      iIi1iIiii111 . append ( oOo0OOoO0 )
   elif len ( ii1I ( 'utube' ) ) > 0 :
    for I11I11i1I in ii1I ( 'utube' ) :
     if not I11I11i1I . string == None :
      if ' ' in I11I11i1I . string :
       II = 'plugin://plugin.video.youtube/search/?q=' + urllib . quote_plus ( I11I11i1I . string )
       oO0 = II
      elif len ( I11I11i1I . string ) == 11 :
       II = 'plugin://plugin.video.youtube/play/?video_id=' + I11I11i1I . string
      elif ( I11I11i1I . string . startswith ( 'PL' ) and not '&order=' in I11I11i1I . string ) or I11I11i1I . string . startswith ( 'UU' ) :
       II = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + I11I11i1I . string
      elif I11I11i1I . string . startswith ( 'PL' ) or I11I11i1I . string . startswith ( 'UU' ) :
       II = 'plugin://plugin.video.youtube/play/?playlist_id=' + I11I11i1I . string
      elif I11I11i1I . string . startswith ( 'UC' ) and len ( I11I11i1I . string ) > 12 :
       II = 'plugin://plugin.video.youtube/channel/' + I11I11i1I . string + '/'
       oO0 = II
      elif not I11I11i1I . string . startswith ( 'UC' ) and not ( I11I11i1I . string . startswith ( 'PL' ) ) :
       II = 'plugin://plugin.video.youtube/user/' + I11I11i1I . string + '/'
       oO0 = II
     iIi1iIiii111 . append ( II )
   elif len ( ii1I ( 'imdb' ) ) > 0 :
    for I11I11i1I in ii1I ( 'imdb' ) :
     if not I11I11i1I . string == None :
      if OOo . getSetting ( 'genesisorpulsar' ) == '0' :
       o0Oo0oO0oOO00 = 'plugin://plugin.video.genesis/?action=play&imdb=' + I11I11i1I . string
      else :
       o0Oo0oO0oOO00 = 'plugin://plugin.video.pulsar/movie/tt' + I11I11i1I . string + '/play'
      iIi1iIiii111 . append ( o0Oo0oO0oOO00 )
   elif len ( ii1I ( 'f4m' ) ) > 0 :
    for I11I11i1I in ii1I ( 'f4m' ) :
     if not I11I11i1I . string == None :
      if '.f4m' in I11I11i1I . string :
       oo00OO0000oO = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( I11I11i1I . string )
      elif '.m3u8' in I11I11i1I . string :
       oo00OO0000oO = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( I11I11i1I . string ) + '&amp;streamtype=HLS'
       if 11 - 11: i11Ii11I1Ii1i / OOooOOo - O0oO * II1 + II1 . OOooOOo
      else :
       oo00OO0000oO = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( I11I11i1I . string ) + '&amp;streamtype=SIMPLE'
     iIi1iIiii111 . append ( oo00OO0000oO )
   elif len ( ii1I ( 'ftv' ) ) > 0 :
    for I11I11i1I in ii1I ( 'ftv' ) :
     if not I11I11i1I . string == None :
      i1I1i111Ii = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( oOOoO0O0O0 ) + '&url=' + I11I11i1I . string + '&mode=125&ch_fanart=na'
     iIi1iIiii111 . append ( i1I1i111Ii )
   elif len ( ii1I ( 'urlsolve' ) ) > 0 :
    for I11I11i1I in ii1I ( 'urlsolve' ) :
     if not I11I11i1I . string == None :
      ooo = I11I11i1I . string + '&mode=19'
      iIi1iIiii111 . append ( ooo )
   if len ( iIi1iIiii111 ) < 1 :
    raise
  except :
   i1IIiiiii ( 'Error <link> element, Passing:' + oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) )
   continue
  try :
   O0oO0 = ii1I ( 'externallink' ) [ 0 ] . string
  except : pass
  if 27 - 27: i11Ii11I1Ii1i % IIiIiII11i
  if O0oO0 :
   o0oooOO00 = [ O0oO0 ]
   O0oO0 = True
  else :
   O0oO0 = False
  try :
   oO0 = ii1I ( 'jsonrpc' ) [ 0 ] . string
  except : pass
  if oO0 :
   if 32 - 32: o0oO0
   o0oooOO00 = [ oO0 ]
   if 30 - 30: IIii1I / o00O0oo . Ooo00oOo00o - ii11ii1ii
   oO0 = True
  else :
   oO0 = False
  try :
   ii1ii1ii = ii1I ( 'thumbnail' ) [ 0 ] . string
   if ii1ii1ii == None :
    raise
  except :
   ii1ii1ii = ''
  try :
   if not ii1I ( 'fanart' ) :
    if OOo . getSetting ( 'use_thumb' ) == "true" :
     iiIii = ii1ii1ii
    else :
     iiIii = fanart
   else :
    iiIii = ii1I ( 'fanart' ) [ 0 ] . string
   if iiIii == None :
    raise
  except :
   iiIii = fanart
  try :
   o0oO = ii1I ( 'info' ) [ 0 ] . string
   if o0oO == None :
    raise
  except :
   o0oO = ''
   if 48 - 48: O00ooooo00 - oO0o0ooO0 / OOO0O0O0ooooo * Ooo00oOo00o
  try :
   i1iiI11I = ii1I ( 'genre' ) [ 0 ] . string
   if i1iiI11I == None :
    raise
  except :
   i1iiI11I = ''
   if 71 - 71: OoOO
  try :
   I1i1iii = ii1I ( 'date' ) [ 0 ] . string
   if I1i1iii == None :
    raise
  except :
   I1i1iii = ''
   if 7 - 7: OoOO - IIiIiII11i . IIii1I - O00ooooo00
  OoOOooOOO0 = None
  if ii1I ( 'regex' ) :
   try :
    o0OOOoO0 = ii1I ( 'regex' )
    OoOOooOOO0 = o0o ( o0OOOoO0 )
   except :
    pass
  try :
   if len ( iIi1iIiii111 ) > 1 :
    o0OoOo00o0o = 0
    I1II1I11I1I = [ ]
    for I11I11i1I in iIi1iIiii111 :
     if I1IiiiiI == "false" :
      o0OoOo00o0o += 1
      o0oO00000 ( I11I11i1I , '%s) %s' % ( o0OoOo00o0o , oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) ) , ii1ii1ii , iiIii , o0oO , i1iiI11I , I1i1iii , True , I1II1I11I1I , OoOOooOOO0 , i1iIi )
     elif I1IiiiiI == "true" and o0OIiII == 'true' :
      if OoOOooOOO0 :
       I1II1I11I1I . append ( I11I11i1I + '&regexs=' + OoOOooOOO0 )
      elif any ( x in I11I11i1I for x in OO0o ) and I11I11i1I . startswith ( 'http' ) :
       I1II1I11I1I . append ( I11I11i1I + '&mode=19' )
      else :
       I1II1I11I1I . append ( I11I11i1I )
     else :
      I1II1I11I1I . append ( I11I11i1I )
    if len ( I1II1I11I1I ) > 1 :
     o0oO00000 ( '' , oOOoO0O0O0 , ii1ii1ii , iiIii , o0oO , i1iiI11I , I1i1iii , True , I1II1I11I1I , OoOOooOOO0 , i1iIi )
   else :
    if O0oO0 :
     if not OoOOooOOO0 == None :
      Ooo ( oOOoO0O0O0 . encode ( 'utf-8' ) , o0oooOO00 [ 0 ] . encode ( 'utf-8' ) , 1 , ii1ii1ii , fanart , o0oO , i1iiI11I , I1i1iii , None , '!!update' , OoOOooOOO0 , iIi1iIiii111 [ 0 ] . encode ( 'utf-8' ) )
      if 54 - 54: II1 + ii11ii1ii - O00ooooo00 % i11iIiiIii
     else :
      Ooo ( oOOoO0O0O0 . encode ( 'utf-8' ) , o0oooOO00 [ 0 ] . encode ( 'utf-8' ) , 1 , ii1ii1ii , fanart , o0oO , i1iiI11I , I1i1iii , None , 'source' , None , None )
      if 3 - 3: ii11ii1ii % ii11ii1ii
    elif oO0 :
     Ooo ( oOOoO0O0O0 . encode ( 'utf-8' ) , o0oooOO00 [ 0 ] , 53 , ii1ii1ii , fanart , o0oO , i1iiI11I , I1i1iii , None , 'source' )
     if 83 - 83: iIiiiI1IiI1I1 + o0oO0
    else :
     o0oO00000 ( iIi1iIiii111 [ 0 ] , oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) , ii1ii1ii , iiIii , o0oO , i1iiI11I , I1i1iii , True , None , OoOOooOOO0 , i1iIi )
     if 73 - 73: IIII
  except :
   i1IIiiiii ( 'There was a problem adding item - ' + oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) )
   if 42 - 42: i11iIiiIii * IIii1I / OoOO . i11iIiiIii % o00O0oo
def o0o ( reg_item ) :
 try :
  OoOOooOOO0 = { }
  for I11I11i1I in reg_item :
   OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] = { }
   OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'name' ] = I11I11i1I ( 'name' ) [ 0 ] . string
   if 41 - 41: O0oO / OOO0O0O0ooooo
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'expres' ] = I11I11i1I ( 'expres' ) [ 0 ] . string
    if not OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'expres' ] :
     OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'expres' ] = ''
   except :
    i1IIiiiii ( "Regex: -- No Referer --" )
   OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'page' ] = I11I11i1I ( 'page' ) [ 0 ] . string
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'referer' ] = I11I11i1I ( 'referer' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No Referer --" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'connection' ] = I11I11i1I ( 'connection' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No connection --" )
    if 51 - 51: o00O0oo % IIiIiII11i
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'notplayable' ] = I11I11i1I ( 'notplayable' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No notplayable --" )
    if 60 - 60: IIiIiII11i / o0000oOoOoO0o . IIiIiII11i / o0oO0 . O0oO
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'noredirect' ] = I11I11i1I ( 'noredirect' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No noredirect --" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'origin' ] = I11I11i1I ( 'origin' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No origin --" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'accept' ] = I11I11i1I ( 'accept' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No accept --" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'includeheaders' ] = I11I11i1I ( 'includeheaders' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No includeheaders --" )
    if 92 - 92: OOooOOo + o0oO0 * oO0o0ooO0 % IIiIiII11i
    if 42 - 42: IiIIi1I1Iiii
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'listrepeat' ] = I11I11i1I ( 'listrepeat' ) [ 0 ] . string
    print 'listrepeat' , OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'listrepeat' ] , I11I11i1I ( 'listrepeat' ) [ 0 ] . string , I11I11i1I
   except :
    i1IIiiiii ( "Regex: -- No listrepeat --" )
    if 76 - 76: IIiIiII11i * IIII % o0oO0
    if 57 - 57: IIii1I - O00ooooo00 / o0oO0 - OOO0O0O0ooooo * II1 % iIiiiI1IiI1I1
    if 68 - 68: II1 * o00O0oo % OOooOOo - O0oO
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'proxy' ] = I11I11i1I ( 'proxy' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No proxy --" )
    if 34 - 34: o0oO0 . IIii1I * OOooOOo * OoOO0ooOOoo0O / o0oO0 / OoOO
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'x-req' ] = I11I11i1I ( 'x-req' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No x-req --" )
    if 78 - 78: IiIIi1I1Iiii - ii11ii1ii / OOooOOo
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'x-addr' ] = I11I11i1I ( 'x-addr' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No x-addr --" )
    if 10 - 10: IIII + IiIIi1I1Iiii * OoOO + IIii1I / o0oO0 / OoOO
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'x-forward' ] = I11I11i1I ( 'x-forward' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No x-forward --" )
    if 42 - 42: IIiIiII11i
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'agent' ] = I11I11i1I ( 'agent' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No User Agent --" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'post' ] = I11I11i1I ( 'post' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a post" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'rawpost' ] = I11I11i1I ( 'rawpost' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a rawpost" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'htmlunescape' ] = I11I11i1I ( 'htmlunescape' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a htmlunescape" )
    if 38 - 38: o0000oOoOoO0o + iIiiiI1IiI1I1 % i11Ii11I1Ii1i % OOooOOo - oO0o0ooO0 / II1
    if 73 - 73: ii11ii1ii * OOO0O0O0ooooo - i11iIiiIii
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'readcookieonly' ] = I11I11i1I ( 'readcookieonly' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a readCookieOnly" )
    if 85 - 85: oO0o0ooO0 % IIII + o00O0oo / ii11ii1ii . OoOO0ooOOoo0O + o0000oOoOoO0o
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = I11I11i1I ( 'cookiejar' ) [ 0 ] . string
    if not OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] :
     OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = ''
   except :
    i1IIiiiii ( "Regex: -- Not a cookieJar" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'setcookie' ] = I11I11i1I ( 'setcookie' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a setcookie" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'appendcookie' ] = I11I11i1I ( 'appendcookie' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a appendcookie" )
    if 62 - 62: i11iIiiIii + i11iIiiIii - ii11ii1ii
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'ignorecache' ] = I11I11i1I ( 'ignorecache' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- no ignorecache" )
    if 28 - 28: IIII . IIII % IIii1I * IIii1I . ii11ii1ii / IIII
    if 27 - 27: Ooo00oOo00o + i11Ii11I1Ii1i - O00ooooo00
    if 69 - 69: O0oO - OOO0O0O0ooooo % OoOO + i11iIiiIii . OOooOOo / Ooo00oOo00o
    if 79 - 79: OOO0O0O0ooooo * i11iIiiIii - O0oO / O0oO
    if 48 - 48: OOO0O0O0ooooo
  OoOOooOOO0 = urllib . quote ( repr ( OoOOooOOO0 ) )
  return OoOOooOOO0
  if 93 - 93: i11iIiiIii - IIiIiII11i * OoOO * o00O0oo % OOO0O0O0ooooo + II1
 except :
  OoOOooOOO0 = None
  i1IIiiiii ( 'regex Error: ' + oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) )
  if 25 - 25: O0oO + oO0o0ooO0 / i11Ii11I1Ii1i . ii11ii1ii % OOO0O0O0ooooo * Ooo00oOo00o
def o0O0oo0OO0O ( url ) :
 try :
  for I11I11i1I in range ( 1 , 51 ) :
   OO0 = o0Oooo ( url )
   if "EXT-X-STREAM-INF" in OO0 : return url
   if not "EXTM3U" in OO0 : return
   xbmc . sleep ( 2000 )
  return
 except :
  return
  if 36 - 36: II1 . Ooo00oOo00o
def oOIIiIi ( regexs , url , cookieJar = None , forCookieJarOnly = False , recursiveCall = False , cachedPages = { } , rawPost = False , cookie_jar_file = None ) :
 if not recursiveCall :
  regexs = eval ( urllib . unquote ( regexs ) )
  if 91 - 91: OoOO * IiIIi1I1Iiii / IIiIiII11i . OOO0O0O0ooooo + Ooo00oOo00o + OOooOOo
  if 8 - 8: OoOO0ooOOoo0O / OoOO
 i1iI1 = re . compile ( '\$doregex\[([^\]]*)\]' ) . findall ( url )
 if 33 - 33: O0oO % IIii1I * IIiIiII11i
 o00o0 = True
 for II1III1I1I1Ii in i1iI1 :
  if II1III1I1I1Ii in regexs :
   if 70 - 70: Ooo00oOo00o % OoOO0ooOOoo0O + o0000oOoOoO0o / oO0o0ooO0 % OOO0O0O0ooooo
   oO00O0 = regexs [ II1III1I1I1Ii ]
   if 36 - 36: OoOO0ooOOoo0O - oO0o0ooO0 . IiIIi1I1Iiii - i11iIiiIii - o0000oOoOoO0o * IiIIi1I1Iiii
   OooOOOO = False
   if 'cookiejar' in oO00O0 :
    if 45 - 45: OoOO % IIiIiII11i - i11iIiiIii
    OooOOOO = oO00O0 [ 'cookiejar' ]
    if '$doregex' in OooOOOO :
     cookieJar = oOIIiIi ( regexs , oO00O0 [ 'cookiejar' ] , cookieJar , True , True , cachedPages )
     OooOOOO = True
    else :
     OooOOOO = True
     if 11 - 11: IIii1I * IIii1I * IIiIiII11i
   if OooOOOO :
    if cookieJar == None :
     if 46 - 46: OOooOOo + Ooo00oOo00o
     cookie_jar_file = None
     if 'open[' in oO00O0 [ 'cookiejar' ] :
      cookie_jar_file = oO00O0 [ 'cookiejar' ] . split ( 'open[' ) [ 1 ] . split ( ']' ) [ 0 ]
      if 70 - 70: IIII / IIii1I
     cookieJar = Oo0oooO0oO ( cookie_jar_file )
     if cookie_jar_file :
      IiIiII1 ( cookieJar , cookie_jar_file )
      if 21 - 21: OOO0O0O0ooooo % O0oO . IIiIiII11i / iIiiiI1IiI1I1 + O0oO
      if 53 - 53: OoOO0ooOOoo0O - IIiIiII11i - OoOO0ooOOoo0O * IIII
      if 71 - 71: OOO0O0O0ooooo - IIii1I
    elif 'save[' in oO00O0 [ 'cookiejar' ] :
     cookie_jar_file = oO00O0 [ 'cookiejar' ] . split ( 'save[' ) [ 1 ] . split ( ']' ) [ 0 ]
     i1II = os . path . join ( Oooo0000 , cookie_jar_file )
     print 'complete_path' , i1II
     IiIiII1 ( cookieJar , cookie_jar_file )
   if oO00O0 [ 'page' ] and '$doregex' in oO00O0 [ 'page' ] :
    oO00O0 [ 'page' ] = oOIIiIi ( regexs , oO00O0 [ 'page' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 14 - 14: OoOO0ooOOoo0O / OoOO0ooOOoo0O % i11Ii11I1Ii1i
   if 'setcookie' in oO00O0 and oO00O0 [ 'setcookie' ] and '$doregex' in oO00O0 [ 'setcookie' ] :
    oO00O0 [ 'setcookie' ] = oOIIiIi ( regexs , oO00O0 [ 'setcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if 'appendcookie' in oO00O0 and oO00O0 [ 'appendcookie' ] and '$doregex' in oO00O0 [ 'appendcookie' ] :
    oO00O0 [ 'appendcookie' ] = oOIIiIi ( regexs , oO00O0 [ 'appendcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 56 - 56: IIiIiII11i . OOO0O0O0ooooo + IiIIi1I1Iiii
    if 1 - 1: IIII
   if 'post' in oO00O0 and '$doregex' in oO00O0 [ 'post' ] :
    oO00O0 [ 'post' ] = oOIIiIi ( regexs , oO00O0 [ 'post' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    print 'post is now' , oO00O0 [ 'post' ]
    if 97 - 97: o0000oOoOoO0o + IIII + OOO0O0O0ooooo + i11iIiiIii
   if 'rawpost' in oO00O0 and '$doregex' in oO00O0 [ 'rawpost' ] :
    oO00O0 [ 'rawpost' ] = oOIIiIi ( regexs , oO00O0 [ 'rawpost' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages , rawPost = True )
    if 77 - 77: ii11ii1ii / II1
    if 46 - 46: ii11ii1ii % IIii1I . IIII % IIII + i11iIiiIii
   if 'rawpost' in oO00O0 and '$epoctime$' in oO00O0 [ 'rawpost' ] :
    oO00O0 [ 'rawpost' ] = oO00O0 [ 'rawpost' ] . replace ( '$epoctime$' , Oo00o0OO0O00o ( ) )
    if 82 - 82: o00O0oo + II1 - O00ooooo00 . O00ooooo00
   if 'rawpost' in oO00O0 and '$epoctime2$' in oO00O0 [ 'rawpost' ] :
    oO00O0 [ 'rawpost' ] = oO00O0 [ 'rawpost' ] . replace ( '$epoctime2$' , iIi1i ( ) )
    if 27 - 27: o0000oOoOoO0o * i11Ii11I1Ii1i . o0oO0 % O0oO * O0oO . O00ooooo00
    if 72 - 72: o0000oOoOoO0o % OoOO + Ooo00oOo00o / OoOO0ooOOoo0O + O0oO
   I1I1i = ''
   if oO00O0 [ 'page' ] and oO00O0 [ 'page' ] in cachedPages and not 'ignorecache' in oO00O0 and forCookieJarOnly == False :
    I1I1i = cachedPages [ oO00O0 [ 'page' ] ]
   else :
    if oO00O0 [ 'page' ] and not oO00O0 [ 'page' ] == '' and oO00O0 [ 'page' ] . startswith ( 'http' ) :
     if '$epoctime$' in oO00O0 [ 'page' ] :
      oO00O0 [ 'page' ] = oO00O0 [ 'page' ] . replace ( '$epoctime$' , Oo00o0OO0O00o ( ) )
     if '$epoctime2$' in oO00O0 [ 'page' ] :
      oO00O0 [ 'page' ] = oO00O0 [ 'page' ] . replace ( '$epoctime2$' , iIi1i ( ) )
      if 1 - 1: o00O0oo % o0000oOoOoO0o + OOO0O0O0ooooo + O00ooooo00 - Ooo00oOo00o
      if 22 - 22: IIiIiII11i % OoOO
     o0oo0O = oO00O0 [ 'page' ] . split ( '|' )
     Ii1i1iI = o0oo0O [ 0 ]
     IIiI1 = None
     if len ( o0oo0O ) > 1 :
      IIiI1 = o0oo0O [ 1 ]
      if 17 - 17: o0000oOoOoO0o / o0000oOoOoO0o / o00O0oo
      if 1 - 1: O00ooooo00 . i11iIiiIii % o0000oOoOoO0o
      if 82 - 82: IIii1I + IiIIi1I1Iiii . IIii1I % O0oO / oO0o0ooO0 . oO0o0ooO0
      if 14 - 14: ii11ii1ii . o0000oOoOoO0o . o00O0oo + II1 - o0000oOoOoO0o + O0oO
      if 9 - 9: oO0o0ooO0
      if 59 - 59: IIiIiII11i * iIiiiI1IiI1I1 . OOO0O0O0ooooo
      if 56 - 56: oO0o0ooO0 - IIII % IIiIiII11i - ii11ii1ii
      if 51 - 51: OOO0O0O0ooooo / i11Ii11I1Ii1i * IIii1I + OoOO + ii11ii1ii
      if 98 - 98: IIii1I * OoOO * o0000oOoOoO0o + i11Ii11I1Ii1i % i11iIiiIii % OOO0O0O0ooooo
      if 27 - 27: OOO0O0O0ooooo
     OOO0oOOoo = urllib2 . ProxyHandler ( urllib2 . getproxies ( ) )
     if 52 - 52: ii11ii1ii % IiIIi1I1Iiii
     if 64 - 64: OOO0O0O0ooooo % o00O0oo % OOO0O0O0ooooo * Ooo00oOo00o . OoOO0ooOOoo0O + IIiIiII11i
     if 75 - 75: o00O0oo . II1 % ii11ii1ii * o00O0oo % II1
     IIiiIiI1 = urllib2 . Request ( Ii1i1iI )
     if 'proxy' in oO00O0 :
      I11i1 = oO00O0 [ 'proxy' ]
      print 'proxytouse' , I11i1
      if 28 - 28: o00O0oo
      if Ii1i1iI [ : 5 ] == "https" :
       oOOOOoo = urllib2 . ProxyHandler ( { 'https' : I11i1 } )
       if 58 - 58: ii11ii1ii / O0oO . OOooOOo / II1 + o0oO0
      else :
       oOOOOoo = urllib2 . ProxyHandler ( { 'http' : I11i1 } )
       if 86 - 86: o00O0oo * IIiIiII11i + o00O0oo + iIiiiI1IiI1I1
      i1i111iI = urllib2 . build_opener ( oOOOOoo )
      urllib2 . install_opener ( i1i111iI )
      if 29 - 29: OoOO / O00ooooo00 . IIiIiII11i - OOooOOo - OOooOOo - oO0o0ooO0
      if 20 - 20: O00ooooo00 % Ooo00oOo00o . IIiIiII11i / O0oO * i11iIiiIii * o0000oOoOoO0o
     IIiiIiI1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
     I11i1 = None
     if 85 - 85: ii11ii1ii . OOooOOo / i11Ii11I1Ii1i . OOO0O0O0ooooo % o0oO0
     if 'referer' in oO00O0 :
      IIiiIiI1 . add_header ( 'Referer' , oO00O0 [ 'referer' ] )
     if 'accept' in oO00O0 :
      IIiiIiI1 . add_header ( 'Accept' , oO00O0 [ 'accept' ] )
     if 'agent' in oO00O0 :
      IIiiIiI1 . add_header ( 'User-agent' , oO00O0 [ 'agent' ] )
     if 'x-req' in oO00O0 :
      IIiiIiI1 . add_header ( 'X-Requested-With' , oO00O0 [ 'x-req' ] )
     if 'x-addr' in oO00O0 :
      IIiiIiI1 . add_header ( 'x-addr' , oO00O0 [ 'x-addr' ] )
     if 'x-forward' in oO00O0 :
      IIiiIiI1 . add_header ( 'X-Forwarded-For' , oO00O0 [ 'x-forward' ] )
     if 'setcookie' in oO00O0 :
      print 'adding cookie' , oO00O0 [ 'setcookie' ]
      IIiiIiI1 . add_header ( 'Cookie' , oO00O0 [ 'setcookie' ] )
     if 'appendcookie' in oO00O0 :
      print 'appending cookie to cookiejar' , oO00O0 [ 'appendcookie' ]
      OO0ooo0oOO = oO00O0 [ 'appendcookie' ]
      OO0ooo0oOO = OO0ooo0oOO . split ( ';' )
      for oo000 in OO0ooo0oOO :
       ii , OoO = oo000 . split ( '=' )
       Iiiiii111i1ii , ii = ii . split ( ':' )
       i1i1iII1 = cookielib . Cookie ( version = 0 , name = ii , value = OoO , port = None , port_specified = False , domain = Iiiiii111i1ii , domain_specified = False , domain_initial_dot = False , path = '/' , path_specified = True , secure = False , expires = None , discard = True , comment = None , comment_url = None , rest = { 'HttpOnly' : None } , rfc2109 = False )
       cookieJar . set_cookie ( i1i1iII1 )
     if 'origin' in oO00O0 :
      IIiiIiI1 . add_header ( 'Origin' , oO00O0 [ 'origin' ] )
     if IIiI1 :
      IIiI1 = IIiI1 . split ( '&' )
      for oo000 in IIiI1 :
       ii , OoO = oo000 . split ( '=' )
       IIiiIiI1 . add_header ( ii , OoO )
     if not cookieJar == None :
      if 25 - 25: IIii1I % IIII . i11Ii11I1Ii1i
      IIIIi1 = urllib2 . HTTPCookieProcessor ( cookieJar )
      i1i111iI = urllib2 . build_opener ( IIIIi1 , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      i1i111iI = urllib2 . install_opener ( i1i111iI )
      print 'noredirect' , 'noredirect' in oO00O0
      if 3 - 3: o0oO0
      if 'noredirect' in oO00O0 :
       i1iiIiI1Ii1i = urllib2 . build_opener ( I1IiiI )
       i1i111iI = urllib2 . install_opener ( i1iiIiI1Ii1i )
       if 22 - 22: O0oO / i11iIiiIii
     if 'connection' in oO00O0 :
      print '..........................connection//////.' , oO00O0 [ 'connection' ]
      from keepalive import HTTPHandler
      oOOoo = HTTPHandler ( )
      i1i111iI = urllib2 . build_opener ( oOOoo )
      urllib2 . install_opener ( i1i111iI )
      if 14 - 14: ii11ii1ii * OoOO0ooOOoo0O
      if 81 - 81: oO0o0ooO0 * ii11ii1ii + o0oO0 + IiIIi1I1Iiii - II1
      if 32 - 32: oO0o0ooO0 * OOO0O0O0ooooo
     O00oOo00o0o = None
     if 85 - 85: IIII + II1 * IIII - o0oO0 % i11iIiiIii
     if 'post' in oO00O0 :
      OOo00OoO = oO00O0 [ 'post' ]
      if '$LiveStreamRecaptcha' in OOo00OoO :
       ( iIi1i11iiI1111 , oOoooo000Oo00 ) = OOoo ( oO00O0 [ 'page' ] )
       if iIi1i11iiI1111 :
        OOo00OoO += 'recaptcha_challenge_field:' + iIi1i11iiI1111 + ',recaptcha_response_field:' + oOoooo000Oo00
      o00O00oO00 = OOo00OoO . split ( ',' ) ;
      O00oOo00o0o = { }
      for Ii1i1i1i1I1Ii in o00O00oO00 :
       ii = Ii1i1i1i1I1Ii . split ( ':' ) [ 0 ] ;
       OoO = Ii1i1i1i1I1Ii . split ( ':' ) [ 1 ] ;
       O00oOo00o0o [ ii ] = OoO
      O00oOo00o0o = urllib . urlencode ( O00oOo00o0o )
      if 25 - 25: iIiiiI1IiI1I1
     if 'rawpost' in oO00O0 :
      O00oOo00o0o = oO00O0 [ 'rawpost' ]
      if '$LiveStreamRecaptcha' in O00oOo00o0o :
       ( iIi1i11iiI1111 , oOoooo000Oo00 ) = OOoo ( oO00O0 [ 'page' ] )
       if iIi1i11iiI1111 :
        O00oOo00o0o += '&recaptcha_challenge_field=' + iIi1i11iiI1111 + '&recaptcha_response_field=' + oOoooo000Oo00
     if O00oOo00o0o :
      iiIiIIi = urllib2 . urlopen ( IIiiIiI1 , O00oOo00o0o )
     else :
      iiIiIIi = urllib2 . urlopen ( IIiiIiI1 )
      if 11 - 11: IiIIi1I1Iiii
     I1I1i = iiIiIIi . read ( )
     if 74 - 74: OOooOOo * ii11ii1ii + OOooOOo . o0000oOoOoO0o * II1 % OOO0O0O0ooooo
     if 'proxy' in oO00O0 and not OOO0oOOoo is None :
      urllib2 . install_opener ( urllib2 . build_opener ( OOO0oOOoo ) )
      if 85 - 85: i11Ii11I1Ii1i / OOO0O0O0ooooo
     I1I1i = iI1iIIIi1i ( I1I1i )
     if 89 - 89: IIii1I
     if 'includeheaders' in oO00O0 :
      if 21 - 21: o00O0oo % o00O0oo
      I1I1i += '$$HEADERS_START$$:'
      for OOOoO0O0o in iiIiIIi . headers :
       I1I1i += OOOoO0O0o + ':' + iiIiIIi . headers . get ( OOOoO0O0o ) + '\n'
      I1I1i += '$$HEADERS_END$$:'
      if 27 - 27: i11iIiiIii / OoOO
     i1IIiiiii ( I1I1i )
     i1IIiiiii ( cookieJar )
     if 84 - 84: IiIIi1I1Iiii
     iiIiIIi . close ( )
     cachedPages [ oO00O0 [ 'page' ] ] = I1I1i
     if 43 - 43: OoOO0ooOOoo0O - II1
     if 3 - 3: OOO0O0O0ooooo / IIII
     if 31 - 31: o0000oOoOoO0o + ii11ii1ii . II1
     if forCookieJarOnly :
      return cookieJar
    elif oO00O0 [ 'page' ] and not oO00O0 [ 'page' ] . startswith ( 'http' ) :
     if oO00O0 [ 'page' ] . startswith ( '$pyFunction:' ) :
      ooOooo0 = oO0OO0 ( oO00O0 [ 'page' ] . split ( '$pyFunction:' ) [ 1 ] , '' , cookieJar , oO00O0 )
      if forCookieJarOnly :
       return cookieJar
      I1I1i = ooOooo0
     else :
      I1I1i = oO00O0 [ 'page' ]
   if '$pyFunction:playmedia(' in oO00O0 [ 'expres' ] or 'ActivateWindow' in oO00O0 [ 'expres' ] or '$PLAYERPROXY$=' in url or any ( x in url for x in Oo0Ooo ) :
    o00o0 = False
   if '$doregex' in oO00O0 [ 'expres' ] :
    oO00O0 [ 'expres' ] = oOIIiIi ( regexs , oO00O0 [ 'expres' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if not oO00O0 [ 'expres' ] == '' :
    print 'doing it ' , oO00O0 [ 'expres' ]
    if '$LiveStreamCaptcha' in oO00O0 [ 'expres' ] :
     ooOooo0 = o0O0Oo00 ( oO00O0 , I1I1i , cookieJar )
     if 51 - 51: o0000oOoOoO0o % IIii1I - II1 % i11Ii11I1Ii1i * IIii1I % Ooo00oOo00o
     url = url . replace ( "$doregex[" + II1III1I1I1Ii + "]" , ooOooo0 )
    elif oO00O0 [ 'expres' ] . startswith ( '$pyFunction:' ) or '#$pyFunction' in oO00O0 [ 'expres' ] :
     if 99 - 99: OoOO0ooOOoo0O * iIiiiI1IiI1I1 * o0oO0
     if oO00O0 [ 'expres' ] . startswith ( '$pyFunction:' ) :
      ooOooo0 = oO0OO0 ( oO00O0 [ 'expres' ] . split ( '$pyFunction:' ) [ 1 ] , I1I1i , cookieJar , oO00O0 )
     else :
      ooOooo0 = oOooO0 ( oO00O0 [ 'expres' ] , I1I1i , cookieJar , oO00O0 )
     if 'ActivateWindow' in oO00O0 [ 'expres' ] : return
     print 'url k val' , url , II1III1I1I1Ii , ooOooo0
     if 79 - 79: Ooo00oOo00o - IIii1I + oO0o0ooO0 - o0oO0
     url = url . replace ( "$doregex[" + II1III1I1I1Ii + "]" , ooOooo0 )
    else :
     if 'listrepeat' in oO00O0 :
      OoOiIIiii = oO00O0 [ 'listrepeat' ]
      O0i11i1iiI1i = re . findall ( oO00O0 [ 'expres' ] , I1I1i )
      return OoOiIIiii , O0i11i1iiI1i , oO00O0 , regexs
      if 87 - 87: i11Ii11I1Ii1i
     if not I1I1i == '' :
      if 45 - 45: Ooo00oOo00o / II1 - IIII / oO0o0ooO0 % O0oO
      OoOIii11iI11i1I = re . compile ( oO00O0 [ 'expres' ] ) . search ( I1I1i )
      ooOooo0 = ''
      try :
       ooOooo0 = OoOIii11iI11i1I . group ( 1 ) . strip ( )
      except : traceback . print_exc ( )
     else :
      ooOooo0 = oO00O0 [ 'expres' ]
      if 64 - 64: i11iIiiIii
     if rawPost :
      print 'rawpost'
      ooOooo0 = urllib . quote_plus ( ooOooo0 )
     if 'htmlunescape' in oO00O0 :
      if 38 - 38: O0oO / IIiIiII11i - O0oO . o00O0oo
      import HTMLParser
      ooOooo0 = HTMLParser . HTMLParser ( ) . unescape ( ooOooo0 )
     url = url . replace ( "$doregex[" + II1III1I1I1Ii + "]" , ooOooo0 )
     if 69 - 69: II1 + OoOO
   else :
    url = url . replace ( "$doregex[" + II1III1I1I1Ii + "]" , '' )
 if '$epoctime$' in url :
  url = url . replace ( '$epoctime$' , Oo00o0OO0O00o ( ) )
 if '$epoctime2$' in url :
  url = url . replace ( '$epoctime2$' , iIi1i ( ) )
  if 97 - 97: o0000oOoOoO0o - Ooo00oOo00o / oO0o0ooO0 . i11iIiiIii % OoOO0ooOOoo0O * OoOO0ooOOoo0O
 if '$GUID$' in url :
  import uuid
  url = url . replace ( '$GUID$' , str ( uuid . uuid1 ( ) ) . upper ( ) )
 if '$get_cookies$' in url :
  url = url . replace ( '$get_cookies$' , ii1IIIIiI11 ( cookieJar ) )
  if 40 - 40: ii11ii1ii
 if recursiveCall : return url
 print 'final url' , url
 if url == "" :
  return
 else :
  return url , o00o0
  if 67 - 67: OoOO0ooOOoo0O + iIiiiI1IiI1I1 - OOO0O0O0ooooo . OoOO0ooOOoo0O * iIiiiI1IiI1I1 * o00O0oo
def o00 ( ) :
 import binascii
 i1IIiiiii ( "Request" )
 iiii ( generator . url + generator . base , '' )
 if 81 - 81: o0000oOoOoO0o - o00O0oo % i11Ii11I1Ii1i - Ooo00oOo00o / IiIIi1I1Iiii
def Ii1iI111 ( t ) :
 import hashlib
 oo000 = hashlib . md5 ( )
 oo000 . update ( t )
 return oo000 . hexdigest ( )
 if 51 - 51: O0oO * OOO0O0O0ooooo / iIiiiI1IiI1I1 . oO0o0ooO0 % o0000oOoOoO0o / IIiIiII11i
def ii1iii1I1I ( encrypted ) :
 oO0Ooo0ooOO0 = ""
 print 'enc' , encrypted
 if 46 - 46: oO0o0ooO0 % OOooOOo
 if 64 - 64: i11iIiiIii - iIiiiI1IiI1I1
 if 77 - 77: OOooOOo % oO0o0ooO0
 if 9 - 9: Ooo00oOo00o - IiIIi1I1Iiii * II1 . IiIIi1I1Iiii
def ii1Ii1IiIIi ( media_url ) :
 try :
  import CustomPlayer
  o0OO0 = CustomPlayer . MyXBMCPlayer ( )
  oOo00Oo0o0Oo = xbmcgui . ListItem ( label = str ( oOOoO0O0O0 ) , iconImage = "DefaultVideo.png" , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  o0OO0 . play ( media_url , oOo00Oo0o0Oo )
  xbmc . sleep ( 1000 )
  while o0OO0 . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 return ''
 if 37 - 37: O0oO . ii11ii1ii / i11Ii11I1Ii1i . o0000oOoOoO0o
def oOOOOo0OoO ( params ) :
 ooOoo0O = json . dumps ( params )
 oo0o0oooo = xbmc . executeJSONRPC ( ooOoo0O )
 if 20 - 20: O00ooooo00 - o00O0oo
 try :
  iiIiIIi = json . loads ( oo0o0oooo )
 except UnicodeDecodeError :
  iiIiIIi = json . loads ( oo0o0oooo . decode ( 'utf-8' , 'ignore' ) )
  if 30 - 30: OOooOOo
 try :
  if 'result' in iiIiIIi :
   return iiIiIIi [ 'result' ]
  return None
 except KeyError :
  logger . warn ( "[%s] %s" % ( params [ 'method' ] , iiIiIIi [ 'error' ] [ 'message' ] ) )
  return None
  if 21 - 21: i11iIiiIii / o0oO0 % o0000oOoOoO0o * OOO0O0O0ooooo . o00O0oo - IIii1I
  if 26 - 26: iIiiiI1IiI1I1 * OOooOOo
def iioo0o0OoOOO ( proxysettings = None ) :
 if 88 - 88: IIII
 if proxysettings == None :
  print 'proxy set to nothing'
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":false}, "id":1}' )
 else :
  if 19 - 19: iIiiiI1IiI1I1 * O0oO + oO0o0ooO0
  O0o = proxysettings . split ( ':' )
  oO00oO = O0o [ 0 ]
  i11i1iIiii = O0o [ 1 ]
  OOO00OO0oOo = O0o [ 2 ]
  I1I1iI = None
  I1iIi1iiIIiI = None
  if 81 - 81: Ooo00oOo00o * OOooOOo . o0000oOoOoO0o
  if len ( O0o ) > 3 and '@' in proxysettings :
   I1I1iI = O0o [ 3 ]
   I1iIi1iiIIiI = proxysettings . split ( '@' ) [ - 1 ]
   if 11 - 11: i11iIiiIii - OoOO0ooOOoo0O . OoOO0ooOOoo0O
  print 'proxy set to' , OOO00OO0oOo , oO00oO , i11i1iIiii
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":true}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxytype", "value":' + str ( OOO00OO0oOo ) + '}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyserver", "value":"' + str ( oO00oO ) + '"}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyport", "value":' + str ( i11i1iIiii ) + '}, "id":1}' )
  if 31 - 31: o0000oOoOoO0o / IiIIi1I1Iiii * O00ooooo00 . OOooOOo
  if 57 - 57: o0000oOoOoO0o + IIii1I % O00ooooo00 % IIiIiII11i
  if not I1I1iI == None :
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyusername", "value":"' + str ( I1I1iI ) + '"}, "id":1}' )
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxypassword", "value":"' + str ( I1iIi1iiIIiI ) + '"}, "id":1}' )
   if 83 - 83: ii11ii1ii / i11iIiiIii % IIii1I . o00O0oo % OoOO0ooOOoo0O . II1
   if 94 - 94: oO0o0ooO0 + IIii1I % Ooo00oOo00o
def O0OO0oOOo ( ) :
 OO0oO0o = oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.usehttpproxy" } , 'id' : 1 } ) [ 'value' ]
 print 'proxyActive' , OO0oO0o
 OOO00OO0oOo = oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxytype" } , 'id' : 1 } ) [ 'value' ]
 if 39 - 39: ii11ii1ii * i11Ii11I1Ii1i + oO0o0ooO0 * iIiiiI1IiI1I1
 if OO0oO0o :
  oO00oO = oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyserver" } , 'id' : 1 } ) [ 'value' ]
  i11i1iIiii = unicode ( oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyport" } , 'id' : 1 } ) [ 'value' ] )
  I1I1iI = oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyusername" } , 'id' : 1 } ) [ 'value' ]
  I1iIi1iiIIiI = oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxypassword" } , 'id' : 1 } ) [ 'value' ]
  if 97 - 97: IIii1I + o00O0oo + iIiiiI1IiI1I1 % O0oO % o0oO0 % OoOO0ooOOoo0O
  if I1I1iI and I1iIi1iiIIiI and oO00oO and i11i1iIiii :
   return oO00oO + ':' + str ( i11i1iIiii ) + ':' + str ( OOO00OO0oOo ) + ':' + I1I1iI + '@' + I1iIi1iiIIiI
  elif oO00oO and i11i1iIiii :
   return oO00oO + ':' + str ( i11i1iIiii ) + ':' + str ( OOO00OO0oOo )
 else :
  return None
  if 21 - 21: IIiIiII11i / i11Ii11I1Ii1i % i11Ii11I1Ii1i - ii11ii1ii
def oOO ( media_url , name , iconImage , proxyip , port ) :
 if 58 - 58: o00O0oo + iIiiiI1IiI1I1 * IIII * i11iIiiIii - IIii1I
 oooo00o0o0o = xbmcgui . DialogProgress ( )
 oooo00o0o0o . create ( 'Progress' , 'Playing with custom proxy' )
 oooo00o0o0o . update ( 10 , "" , "setting proxy.." , "" )
 O0Oo00oO0O00 = False
 Ii = ''
 try :
  if 63 - 63: IIII * o00O0oo * oO0o0ooO0 - OoOO0ooOOoo0O - oO0o0ooO0
  Ii = O0OO0oOOo ( )
  print 'existing_proxy' , Ii
  if 97 - 97: o0000oOoOoO0o / II1
  iioo0o0OoOOO ( proxyip + ':' + port + ':0' )
  if 18 - 18: Ooo00oOo00o + IIii1I - iIiiiI1IiI1I1 - IIiIiII11i
  print 'proxy setting complete' , O0OO0oOOo ( )
  O0Oo00oO0O00 = True
  oooo00o0o0o . update ( 80 , "" , "setting proxy complete, now playing" , "" )
  oooo00o0o0o . close ( )
  oooo00o0o0o = None
  import CustomPlayer
  o0OO0 = CustomPlayer . MyXBMCPlayer ( )
  oOo00Oo0o0Oo = xbmcgui . ListItem ( label = str ( name ) , iconImage = iconImage , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  o0OO0 . play ( media_url , oOo00Oo0o0Oo )
  xbmc . sleep ( 1000 )
  while o0OO0 . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 if oooo00o0o0o :
  oooo00o0o0o . close ( )
 if O0Oo00oO0O00 :
  print 'now resetting the proxy back'
  iioo0o0OoOOO ( Ii )
  print 'reset here'
 return ''
 if 71 - 71: II1
 if 33 - 33: o0oO0
def OOO0ooo ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  IIiiii = page_value
  page_value = o0Oooo ( page_value , headers = referer )
  if 37 - 37: ii11ii1ii % i11Ii11I1Ii1i
 O0II11i11II = "(eval\(function\(p,a,c,k,e,(?:r|d).*)"
 if 29 - 29: IiIIi1I1Iiii % Ooo00oOo00o % O0oO . ii11ii1ii / II1 * i11Ii11I1Ii1i
 o0 = re . compile ( O0II11i11II ) . findall ( page_value )
 OoO000O = ""
 if o0 and len ( o0 ) > 0 :
  for OoO in o0 :
   OOoiIIiiIIIi1I = OO0o0o0oo0O ( OoO )
   IIiI1I1 = i1II1Iiii1I11 ( OOoiIIiiIIIi1I , '\'(.*?)\'' )
   if 'unescape' in OOoiIIiiIIIi1I :
    OOoiIIiiIIIi1I = urllib . unquote ( IIiI1I1 )
   OoO000O += OOoiIIiiIIIi1I + '\n'
  print 'final value is ' , OoO000O
  if 15 - 15: oO0o0ooO0 * IiIIi1I1Iiii % OoOO * IIii1I - i11iIiiIii
  IIiiii = i1II1Iiii1I11 ( OoO000O , 'src="(.*?)"' )
  if 60 - 60: IIiIiII11i * o0oO0 % Ooo00oOo00o + OoOO0ooOOoo0O
  page_value = o0Oooo ( IIiiii , headers = referer )
  if 52 - 52: O00ooooo00
  if 84 - 84: oO0o0ooO0 / O0oO
  if 86 - 86: OOooOOo * iIiiiI1IiI1I1 - OOO0O0O0ooooo . OOooOOo % IIii1I / o0000oOoOoO0o
 IiIIiIIIiIii = i1II1Iiii1I11 ( page_value , 'streamer\'.*?\'(.*?)\'\)' )
 I1i11II = i1II1Iiii1I11 ( page_value , 'file\',\s\'(.*?)\'' )
 if 31 - 31: OoOO0ooOOoo0O / O0oO * ii11ii1ii . iIiiiI1IiI1I1
 if 89 - 89: OOO0O0O0ooooo
 return IiIIiIIIiIii + ' playpath=' + I1i11II + ' pageUrl=' + IIiiii
 if 2 - 2: OoOO . OoOO + OoOO * ii11ii1ii
def oOo00oOOOOO ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  page_value = o0Oooo ( page_value , headers = referer )
 O0II11i11II = "var a = (.*?);\s*var b = (.*?);\s*var c = (.*?);\s*var d = (.*?);\s*var f = (.*?);\s*var v_part = '(.*?)';"
 o0 = re . compile ( O0II11i11II ) . findall ( page_value ) [ 0 ]
 if 85 - 85: II1 - Ooo00oOo00o - o0oO0 / i11Ii11I1Ii1i - o00O0oo
 iIiI , OOOoO0O0o , iIIIi1i1I11i , oOO0OO0OO , oOOoooO , OoO = ( o0 )
 oOOoooO = int ( oOOoooO )
 iIiI = int ( iIiI ) / oOOoooO
 OOOoO0O0o = int ( OOOoO0O0o ) / oOOoooO
 iIIIi1i1I11i = int ( iIIIi1i1I11i ) / oOOoooO
 oOO0OO0OO = int ( oOO0OO0OO ) / oOOoooO
 if 22 - 22: o00O0oo + IIii1I
 O0i11i1iiI1i = 'rtmp://' + str ( iIiI ) + '.' + str ( OOOoO0O0o ) + '.' + str ( iIIIi1i1I11i ) + '.' + str ( oOO0OO0OO ) + OoO ;
 return O0i11i1iiI1i
 if 24 - 24: OOooOOo % O00ooooo00 + IIII . i11iIiiIii . OoOO
def IIi1II ( url , useragent = None ) :
 str = '#EXTM3U'
 str += '\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=361816'
 str += '\n' + url + '&bytes=0-200000'
 oO = os . path . join ( Oooo0000 , 'testfile.m3u' )
 str += '\n'
 IiiI11i1I ( oO , str )
 if 80 - 80: o0000oOoOoO0o / o00O0oo / OOooOOo + O00ooooo00 - IiIIi1I1Iiii
 return oO
 if 11 - 11: ii11ii1ii * Ooo00oOo00o
def IiiI11i1I ( file_name , page_data , append = False ) :
 if append :
  oOOoooO = open ( file_name , 'a' )
  oOOoooO . write ( page_data )
  oOOoooO . close ( )
 else :
  oOOoooO = open ( file_name , 'wb' )
  oOOoooO . write ( page_data )
  oOOoooO . close ( )
  return ''
  if 15 - 15: OOooOOo
def oOoOoO000OO ( file_name ) :
 oOOoooO = open ( file_name , 'rb' )
 oOO0OO0OO = oOOoooO . read ( )
 oOOoooO . close ( )
 return oOO0OO0OO
 if 38 - 38: ii11ii1ii
def III111iiIi1 ( page_data ) :
 import re , base64 , urllib ;
 Ii11Ii = page_data
 while 'geh(' in Ii11Ii :
  if Ii11Ii . startswith ( 'lol(' ) : Ii11Ii = Ii11Ii [ 5 : - 1 ]
  if 1 - 1: IIiIiII11i % II1 + iIiiiI1IiI1I1 - O0oO
  Ii11Ii = re . compile ( '"(.*?)"' ) . findall ( Ii11Ii ) [ 0 ] ;
  Ii11Ii = base64 . b64decode ( Ii11Ii ) ;
  Ii11Ii = urllib . unquote ( Ii11Ii ) ;
 print Ii11Ii
 return Ii11Ii
 if 43 - 43: o0000oOoOoO0o / Ooo00oOo00o % oO0o0ooO0
def iiiI111I ( page_data ) :
 print 'get_dag_url2' , page_data
 oooOOO00o0 = o0Oooo ( page_data ) ;
 i1Iii = '(http.*)'
 import uuid
 II1I11IIi = str ( uuid . uuid1 ( ) ) . upper ( )
 OoOOo = re . compile ( i1Iii ) . findall ( oooOOO00o0 )
 iii1 = [ ( 'X-Playback-Session-Id' , II1I11IIi ) ]
 for oOO0oo in OoOOo :
  try :
   II1iIi1IiIii = o0Oooo ( oOO0oo , headers = iii1 ) ;
   if 30 - 30: i11Ii11I1Ii1i % IIII * o0000oOoOoO0o - OoOO * oO0o0ooO0 % i11Ii11I1Ii1i
  except : pass
  if 46 - 46: i11iIiiIii - OOO0O0O0ooooo . OoOO0ooOOoo0O
 return page_data + '|&X-Playback-Session-Id=' + II1I11IIi
 if 100 - 100: IIiIiII11i / ii11ii1ii * IIII . OOO0O0O0ooooo / o0000oOoOoO0o
 if 83 - 83: o0oO0
def ii111Ii11iii ( page_data ) :
 print 'get_dag_url' , page_data
 if page_data . startswith ( 'http://dag.total-stream.net' ) :
  iii1 = [ ( 'User-Agent' , 'Verismo-BlackUI_(2.4.7.5.8.0.34)' ) ]
  page_data = o0Oooo ( page_data , headers = iii1 ) ;
  if 62 - 62: IIii1I
 if '127.0.0.1' in page_data :
  return OO0OoOOO0 ( page_data )
 elif i1II1Iiii1I11 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  O00ooOo = i1II1Iiii1I11 ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + i1II1Iiii1I11 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + i1II1Iiii1I11 ( page_data , '\\?y=([^&]+)&' )
 else :
  O00ooOo = i1II1Iiii1I11 ( page_data , 'href="([^"]+)"[^"]+$' )
  if len ( O00ooOo ) == 0 :
   O00ooOo = page_data
 O00ooOo = O00ooOo . replace ( ' ' , '%20' )
 return O00ooOo
 if 80 - 80: ii11ii1ii - o0000oOoOoO0o + II1
def i1II1Iiii1I11 ( data , re_patten ) :
 i1IiiiI1iI = ''
 oO00O0 = re . search ( re_patten , data )
 if oO00O0 != None :
  i1IiiiI1iI = oO00O0 . group ( 1 )
 else :
  i1IiiiI1iI = ''
 return i1IiiiI1iI
 if 98 - 98: o0000oOoOoO0o + O00ooooo00 . IIiIiII11i - iIiiiI1IiI1I1 - ii11ii1ii
def OO0OoOOO0 ( page_data ) :
 O00ooOo = ''
 if '127.0.0.1' in page_data :
  O00ooOo = i1II1Iiii1I11 ( page_data , '&ver_t=([^&]+)&' ) + ' live=true timeout=15 playpath=' + i1II1Iiii1I11 ( page_data , '\\?y=([a-zA-Z0-9-_\\.@]+)' )
  if 24 - 24: IiIIi1I1Iiii - O00ooooo00 + o00O0oo
 if i1II1Iiii1I11 ( page_data , 'token=([^&]+)&' ) != '' :
  O00ooOo = O00ooOo + '?token=' + i1II1Iiii1I11 ( page_data , 'token=([^&]+)&' )
 elif i1II1Iiii1I11 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  O00ooOo = i1II1Iiii1I11 ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + i1II1Iiii1I11 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + i1II1Iiii1I11 ( page_data , '\\?y=([^&]+)&' )
 else :
  O00ooOo = i1II1Iiii1I11 ( page_data , 'HREF="([^"]+)"' )
  if 38 - 38: II1 / OoOO . OOO0O0O0ooooo / O00ooooo00 / IiIIi1I1Iiii + IIii1I
 if 'dag1.asx' in O00ooOo :
  return ii111Ii11iii ( O00ooOo )
  if 96 - 96: IIII
 if 'devinlivefs.fplive.net' not in O00ooOo :
  O00ooOo = O00ooOo . replace ( 'devinlive' , 'flive' )
 if 'permlivefs.fplive.net' not in O00ooOo :
  O00ooOo = O00ooOo . replace ( 'permlive' , 'flive' )
 return O00ooOo
 if 18 - 18: IIII * o00O0oo - oO0o0ooO0
 if 31 - 31: IiIIi1I1Iiii - OOO0O0O0ooooo % OOooOOo % OoOO0ooOOoo0O
def iI1iii ( str_eval ) :
 OOOo = ""
 try :
  oO00OoOoo0 = "w,i,s,e=(" + str_eval + ')'
  exec ( oO00OoOoo0 )
  OOOo = I1iiiiii ( w , I11I11i1I , s , e )
 except : traceback . print_exc ( file = sys . stdout )
 if 65 - 65: O0oO + IiIIi1I1Iiii
 return OOOo
 if 59 - 59: II1 + o00O0oo . o0oO0 - OOO0O0O0ooooo % IIii1I / OOO0O0O0ooooo
def I1iiiiii ( w , i , s , e ) :
 OO = 0 ;
 ooO0o = 0 ;
 ii1iI1iI1 = 0 ;
 o00oOOO = [ ] ;
 OoOO0OOoo = [ ] ;
 while True :
  if ( OO < 5 ) :
   OoOO0OOoo . append ( w [ OO ] )
  elif ( OO < len ( w ) ) :
   o00oOOO . append ( w [ OO ] ) ;
  OO += 1 ;
  if ( ooO0o < 5 ) :
   OoOO0OOoo . append ( i [ ooO0o ] )
  elif ( ooO0o < len ( i ) ) :
   o00oOOO . append ( i [ ooO0o ] )
  ooO0o += 1 ;
  if ( ii1iI1iI1 < 5 ) :
   OoOO0OOoo . append ( s [ ii1iI1iI1 ] )
  elif ( ii1iI1iI1 < len ( s ) ) :
   o00oOOO . append ( s [ ii1iI1iI1 ] ) ;
  ii1iI1iI1 += 1 ;
  if ( len ( w ) + len ( i ) + len ( s ) + len ( e ) == len ( o00oOOO ) + len ( OoOO0OOoo ) + len ( e ) ) :
   break ;
   if 1 - 1: IIiIiII11i * i11iIiiIii + o0oO0 * i11iIiiIii + Ooo00oOo00o
 iI = '' . join ( o00oOOO )
 Ii1IIi = '' . join ( OoOO0OOoo )
 ooO0o = 0 ;
 i111i11I1ii = [ ] ;
 for OO in range ( 0 , len ( o00oOOO ) , 2 ) :
  if 64 - 64: OoOO0ooOOoo0O / i11iIiiIii / ii11ii1ii . II1
  i1iiIIi11I = - 1 ;
  if ( ord ( Ii1IIi [ ooO0o ] ) % 2 ) :
   i1iiIIi11I = 1 ;
   if 80 - 80: i11Ii11I1Ii1i * OOO0O0O0ooooo
  i111i11I1ii . append ( chr ( int ( iI [ OO : OO + 2 ] , 36 ) - i1iiIIi11I ) ) ;
  ooO0o += 1 ;
  if ( ooO0o >= len ( OoOO0OOoo ) ) :
   ooO0o = 0 ;
 O0i11i1iiI1i = '' . join ( i111i11I1ii )
 if 'eval(function(w,i,s,e)' in O0i11i1iiI1i :
  print 'STILL GOing'
  O0i11i1iiI1i = re . compile ( 'eval\(function\(w,i,s,e\).*}\((.*?)\)' ) . findall ( O0i11i1iiI1i ) [ 0 ]
  return iI1iii ( O0i11i1iiI1i )
 else :
  print 'FINISHED'
  return O0i11i1iiI1i
  if 78 - 78: OOooOOo
def OO0o0o0oo0O ( page_value , regex_for_text = '' , iterations = 1 , total_iteration = 1 ) :
 try :
  I1i1i1I1iI1 = None
  if page_value . startswith ( "http" ) :
   page_value = o0Oooo ( page_value )
  print 'page_value' , page_value
  if regex_for_text and len ( regex_for_text ) > 0 :
   page_value = re . compile ( regex_for_text ) . findall ( page_value ) [ 0 ]
   if 53 - 53: o0000oOoOoO0o + IIiIiII11i / i11iIiiIii - ii11ii1ii * OoOO0ooOOoo0O / II1
  page_value = OoOoi1i ( page_value , iterations , total_iteration )
 except : traceback . print_exc ( file = sys . stdout )
 print 'unpacked' , page_value
 if 'sav1live.tv' in page_value :
  page_value = page_value . replace ( 'sav1live.tv' , 'sawlive.tv' )
  print 'sav1 unpacked' , page_value
 return page_value
 if 5 - 5: OoOO + OOO0O0O0ooooo + OOO0O0O0ooooo . o0oO0 - i11Ii11I1Ii1i
def OoOoi1i ( sJavascript , iteration = 1 , totaliterations = 2 ) :
 print 'iteration' , iteration
 if sJavascript . startswith ( 'var _0xcb8a=' ) :
  o00oo0000 = sJavascript . split ( 'var _0xcb8a=' )
  oO00OoOoo0 = "myarray=" + o00oo0000 [ 1 ] . split ( "eval(" ) [ 0 ]
  exec ( oO00OoOoo0 )
  iIi1IIi1ii = 62
  I11Ii = int ( o00oo0000 [ 1 ] . split ( ",62," ) [ 1 ] . split ( ',' ) [ 0 ] )
  iIiII = myarray [ 0 ]
  i1i1IIIIIIIi = myarray [ 3 ]
  with open ( 'temp file' + str ( iteration ) + '.js' , "wb" ) as oo0o0oOo :
   oo0o0oOo . write ( str ( i1i1IIIIIIIi ) )
   if 58 - 58: ii11ii1ii - iIiiiI1IiI1I1 % OoOO0ooOOoo0O + o0oO0 . OOooOOo / O0oO
 else :
  if 8 - 8: OoOO . Ooo00oOo00o * o00O0oo + iIiiiI1IiI1I1 % i11iIiiIii
  if "rn p}('" in sJavascript :
   o00oo0000 = sJavascript . split ( "rn p}('" )
  else :
   o00oo0000 = sJavascript . split ( "rn A}('" )
  print o00oo0000
  if 8 - 8: i11Ii11I1Ii1i * OOO0O0O0ooooo
  iIiII , iIi1IIi1ii , I11Ii , i1i1IIIIIIIi = ( '' , '0' , '0' , '' )
  if 73 - 73: ii11ii1ii / OoOO0ooOOoo0O / o00O0oo / Ooo00oOo00o
  oO00OoOoo0 = "p1,a1,c1,k1=('" + o00oo0000 [ 1 ] . split ( ".spli" ) [ 0 ] + ')'
  exec ( oO00OoOoo0 )
 i1i1IIIIIIIi = i1i1IIIIIIIi . split ( '|' )
 o00oo0000 = o00oo0000 [ 1 ] . split ( "))'" )
 if 11 - 11: OOooOOo + O0oO - II1 / Ooo00oOo00o
 if 34 - 34: i11Ii11I1Ii1i
 if 45 - 45: i11Ii11I1Ii1i / IiIIi1I1Iiii / oO0o0ooO0
 if 44 - 44: OoOO - oO0o0ooO0 / iIiiiI1IiI1I1 * Ooo00oOo00o * IiIIi1I1Iiii
 if 73 - 73: ii11ii1ii - IIiIiII11i * O00ooooo00 / i11iIiiIii * o0000oOoOoO0o % iIiiiI1IiI1I1
 if 56 - 56: II1 * IiIIi1I1Iiii . IiIIi1I1Iiii . OoOO
 if 24 - 24: IiIIi1I1Iiii . o00O0oo * oO0o0ooO0 % IIII / o0000oOoOoO0o
 if 58 - 58: IIiIiII11i - OoOO % OOO0O0O0ooooo . IIiIiII11i % Ooo00oOo00o % O0oO
 if 87 - 87: OoOO0ooOOoo0O - i11iIiiIii
 if 78 - 78: i11iIiiIii / IIii1I - ii11ii1ii
 if 23 - 23: o00O0oo
 if 40 - 40: ii11ii1ii - iIiiiI1IiI1I1 / IiIIi1I1Iiii
 if 14 - 14: OoOO
 if 5 - 5: ii11ii1ii . IIii1I % IIii1I
 if 56 - 56: II1 - o00O0oo - O00ooooo00
 if 8 - 8: o0oO0 / o0000oOoOoO0o . IIiIiII11i + OoOO / i11iIiiIii
 if 31 - 31: i11Ii11I1Ii1i - IIii1I + IIII . IiIIi1I1Iiii / O0oO % IIii1I
 if 6 - 6: O0oO * i11iIiiIii % IIii1I % i11iIiiIii + ii11ii1ii / O00ooooo00
 if 53 - 53: o00O0oo + IIii1I
 if 70 - 70: OoOO
 if 67 - 67: II1
 if 29 - 29: OOO0O0O0ooooo - i11iIiiIii - iIiiiI1IiI1I1 + o0000oOoOoO0o * O0oO
 OooO0 = ''
 oOO0OO0OO = ''
 if 2 - 2: O00ooooo00 - i11Ii11I1Ii1i + IIiIiII11i . ii11ii1ii * ii11ii1ii / OOooOOo
 if 93 - 93: O00ooooo00
 ooOOOo = str ( OO000oOoo0O ( iIiII , iIi1IIi1ii , I11Ii , i1i1IIIIIIIi , OooO0 , oOO0OO0OO , iteration ) )
 if 9 - 9: OoOO0ooOOoo0O * O00ooooo00 - O00ooooo00
 if 16 - 16: IIiIiII11i * O00ooooo00 - ii11ii1ii . O0oO % o00O0oo / ii11ii1ii
 if 14 - 14: IIii1I * o0oO0 * OoOO / IIii1I * O0oO / o00O0oo
 if 77 - 77: Ooo00oOo00o + o0oO0 + o0oO0 * oO0o0ooO0 / II1 . oO0o0ooO0
 if 62 - 62: O00ooooo00 - O00ooooo00
 if iteration >= totaliterations :
  if 69 - 69: OOooOOo % OoOO0ooOOoo0O - o00O0oo
  return ooOOOo
 else :
  if 38 - 38: IIii1I + i11iIiiIii / i11iIiiIii % Ooo00oOo00o / i11Ii11I1Ii1i % oO0o0ooO0
  return OoOoi1i ( ooOOOo , iteration + 1 )
  if 7 - 7: O0oO * IIiIiII11i + O00ooooo00 + i11iIiiIii + IiIIi1I1Iiii % IIiIiII11i
def OO000oOoo0O ( p , a , c , k , e , d , iteration , v = 1 ) :
 if 62 - 62: ii11ii1ii - oO0o0ooO0 * OOooOOo - i11iIiiIii % i11Ii11I1Ii1i
 if 52 - 52: OoOO % OoOO0ooOOoo0O - i11iIiiIii
 if 30 - 30: IIII / Ooo00oOo00o + OoOO0ooOOoo0O
 while ( c >= 1 ) :
  c = c - 1
  if ( k [ c ] ) :
   I1I = str ( o00oOOoO0oO ( c , a ) )
   if v == 1 :
    p = re . sub ( '\\b' + I1I + '\\b' , k [ c ] , p )
   else :
    p = I11iiIIII1I1 ( p , I1I , k [ c ] )
    if 38 - 38: o0oO0 % o0000oOoOoO0o - II1
    if 87 - 87: Ooo00oOo00o % IIiIiII11i
    if 77 - 77: IIii1I - O00ooooo00 . OoOO0ooOOoo0O
    if 26 - 26: ii11ii1ii * O0oO . O00ooooo00
    if 59 - 59: OOO0O0O0ooooo + O00ooooo00 - ii11ii1ii
    if 62 - 62: i11iIiiIii % o0000oOoOoO0o . O0oO . o0000oOoOoO0o
 return p
 if 84 - 84: i11iIiiIii * Ooo00oOo00o
 if 18 - 18: o0000oOoOoO0o - oO0o0ooO0 - OOooOOo / o0oO0 - OOO0O0O0ooooo
 if 30 - 30: OOO0O0O0ooooo + OoOO + iIiiiI1IiI1I1
def I11iiIIII1I1 ( source_str , word_to_find , replace_with ) :
 III1I = None
 III1I = source_str . split ( word_to_find )
 if len ( III1I ) > 1 :
  I1I111iIi = [ ]
  OoOOOO = 0
  for I1iiIi111I in III1I :
   if 34 - 34: i11iIiiIii - iIiiiI1IiI1I1 / IIiIiII11i % ii11ii1ii
   I1I111iIi . append ( I1iiIi111I )
   ooOooo0 = word_to_find
   if 33 - 33: o0000oOoOoO0o
   if 35 - 35: i11iIiiIii - IIiIiII11i / o0000oOoOoO0o + oO0o0ooO0 * OoOO0ooOOoo0O
   if OoOOOO == len ( III1I ) - 1 :
    ooOooo0 = ''
   else :
    if len ( I1iiIi111I ) == 0 :
     if ( len ( III1I [ OoOOOO + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( III1I [ OoOOOO + 1 ] ) > 0 and III1I [ OoOOOO + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) :
      ooOooo0 = replace_with
      if 49 - 49: ii11ii1ii * oO0o0ooO0 + o00O0oo + IIII
    else :
     if ( III1I [ OoOOOO ] [ - 1 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) and ( ( len ( III1I [ OoOOOO + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( III1I [ OoOOOO + 1 ] ) > 0 and III1I [ OoOOOO + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) ) :
      ooOooo0 = replace_with
      if 30 - 30: ii11ii1ii / o0000oOoOoO0o / O0oO % i11Ii11I1Ii1i + iIiiiI1IiI1I1
   I1I111iIi . append ( ooOooo0 )
   OoOOOO += 1
   if 4 - 4: IIII - IiIIi1I1Iiii - O0oO - o00O0oo % i11iIiiIii / Ooo00oOo00o
  source_str = '' . join ( I1I111iIi )
 return source_str
 if 50 - 50: i11Ii11I1Ii1i + O00ooooo00
def i11IiIIi11I ( num , radix ) :
 if 78 - 78: O0oO
 OO0 = ""
 if num == 0 : return '0'
 while num > 0 :
  OO0 = "0123456789abcdefghijklmnopqrstuvwxyz" [ num % radix ] + OO0
  num /= radix
 return OO0
 if 83 - 83: IIii1I % OOooOOo % ii11ii1ii % o0oO0 . OoOO % OOO0O0O0ooooo
def o00oOOoO0oO ( cc , a ) :
 I1I = "" if cc < a else o00oOOoO0oO ( int ( cc / a ) , a )
 cc = ( cc % a )
 iIiIi1ii = chr ( cc + 29 ) if cc > 35 else str ( i11IiIIi11I ( cc , 36 ) )
 return I1I + iIiIi1ii
 if 28 - 28: IIii1I + IIii1I
 if 28 - 28: OoOO0ooOOoo0O
def ii1IIIIiI11 ( cookieJar ) :
 try :
  ooo0oo = ""
  for O00oO , IIiI1i in enumerate ( cookieJar ) :
   ooo0oo += IIiI1i . name + "=" + IIiI1i . value + ";"
 except : pass
 if 6 - 6: OoOO / IIII - o0000oOoOoO0o
 return ooo0oo
 if 62 - 62: o00O0oo % o0000oOoOoO0o
 if 54 - 54: OOooOOo % IIII . OOooOOo * o0000oOoOoO0o + OOooOOo % O00ooooo00
def IiIiII1 ( cookieJar , COOKIEFILE ) :
 try :
  i1II = os . path . join ( Oooo0000 , COOKIEFILE )
  cookieJar . save ( i1II , ignore_discard = True )
 except : pass
 if 23 - 23: o0oO0 - o0000oOoOoO0o + oO0o0ooO0 - OOooOOo * OOooOOo . IiIIi1I1Iiii
def Oo0oooO0oO ( COOKIEFILE ) :
 if 47 - 47: OoOO0ooOOoo0O % IIii1I
 IiI1IIIII1I = None
 if COOKIEFILE :
  try :
   i1II = os . path . join ( Oooo0000 , COOKIEFILE )
   IiI1IIIII1I = cookielib . LWPCookieJar ( )
   IiI1IIIII1I . load ( i1II , ignore_discard = True )
  except :
   IiI1IIIII1I = None
   if 35 - 35: oO0o0ooO0 - oO0o0ooO0 + O00ooooo00 - OOO0O0O0ooooo - o0oO0
 if not IiI1IIIII1I :
  IiI1IIIII1I = cookielib . LWPCookieJar ( )
  if 58 - 58: OOooOOo - IIII - II1
 return IiI1IIIII1I
 if 96 - 96: IIii1I
def oO0OO0 ( fun_call , page_data , Cookie_Jar , m ) :
 OOOo00 = ''
 if i1iiIIiiI111 not in sys . path :
  sys . path . append ( i1iiIIiiI111 )
  if 91 - 91: IIii1I . ii11ii1ii . OoOO + II1
 print fun_call
 try :
  o0o0O0Oo = 'import ' + fun_call . split ( '.' ) [ 0 ]
  print o0o0O0Oo , sys . path
  exec ( o0o0O0Oo )
  print 'done'
 except :
  print 'error in import'
  traceback . print_exc ( file = sys . stdout )
 print 'ret_val=' + fun_call
 exec ( 'ret_val=' + fun_call )
 print OOOo00
 if 1 - 1: IIii1I + IiIIi1I1Iiii / OOO0O0O0ooooo - IIII % O0oO + O0oO
 return str ( OOOo00 )
 if 24 - 24: IIiIiII11i + IiIIi1I1Iiii + o0000oOoOoO0o - II1 + IiIIi1I1Iiii
def oOooO0 ( fun_call , page_data , Cookie_Jar , m ) :
 print 'doEvalFunction'
 OOOo00 = ''
 if i1iiIIiiI111 not in sys . path :
  sys . path . append ( i1iiIIiiI111 )
 oOOoooO = open ( i1iiIIiiI111 + "/LSProdynamicCode.py" , "w" )
 oOOoooO . write ( fun_call ) ;
 oOOoooO . close ( )
 import LSProdynamicCode
 OOOo00 = LSProdynamicCode . GetLSProData ( page_data , Cookie_Jar , m )
 return str ( OOOo00 )
 if 93 - 93: i11Ii11I1Ii1i . IIii1I % i11iIiiIii . OOooOOo % i11Ii11I1Ii1i + OOO0O0O0ooooo
 if 65 - 65: oO0o0ooO0 + Ooo00oOo00o - II1
def OOoo ( url ) :
 OOoOO0o = o0Oooo ( url )
 oO0O0oO0 = ""
 I11Ii1iI11iI1 = ""
 i1III1 = "<script.*?src=\"(.*?recap.*?)\""
 i1IiiiI1iI = re . findall ( i1III1 , OOoOO0o )
 Iii111IiIii = False
 OooO0ooo0 = None
 I11Ii1iI11iI1 = None
 if 2 - 2: II1
 if i1IiiiI1iI and len ( i1IiiiI1iI ) > 0 :
  o0o0O00 = i1IiiiI1iI [ 0 ]
  Iii111IiIii = True
  if 35 - 35: IIii1I
  o00oOOo = 'challenge.*?\'(.*?)\''
  o0ooOo00O = '\'(.*?)\''
  Ii1i1I1 = o0Oooo ( o0o0O00 )
  oO0O0oO0 = re . findall ( o00oOOo , Ii1i1I1 ) [ 0 ]
  O0O00OooO = 'http://www.google.com/recaptcha/api/reload?c=' ;
  I1IiI1iI11 = o0o0O00 . split ( 'k=' ) [ 1 ]
  O0O00OooO += oO0O0oO0 + '&k=' + I1IiI1iI11 + '&captcha_k=1&type=image&lang=en-GB'
  iIi = o0Oooo ( O0O00OooO )
  OooO0ooo0 = re . findall ( o0ooOo00O , iIi ) [ 0 ]
  iiO0O0o0oO0O00 = 'http://www.google.com/recaptcha/api/image?c=' + OooO0ooo0
  if not iiO0O0o0oO0O00 . startswith ( "http" ) :
   iiO0O0o0oO0O00 = 'http://www.google.com/recaptcha/api/' + iiO0O0o0oO0O00
  import random
  ii = random . randrange ( 100 , 1000 , 5 )
  o0O0oO0 = os . path . join ( Oooo0000 , str ( ii ) + "captcha.img" )
  oo0 = open ( o0O0oO0 , "wb" )
  oo0 . write ( o0Oooo ( iiO0O0o0oO0O00 ) )
  oo0 . close ( )
  i1 = i1IiIi1 ( captcha = o0O0oO0 )
  I11Ii1iI11iI1 = i1 . get ( )
  os . remove ( o0O0oO0 )
 return OooO0ooo0 , I11Ii1iI11iI1
 if 22 - 22: o00O0oo * OOO0O0O0ooooo . iIiiiI1IiI1I1 - Ooo00oOo00o
def o0Oooo ( url , cookieJar = None , post = None , timeout = 20 , headers = None ) :
 if 90 - 90: OoOO0ooOOoo0O
 if 94 - 94: o00O0oo / OoOO * o0oO0 - OOooOOo
 IIIIi1 = urllib2 . HTTPCookieProcessor ( cookieJar )
 i1i111iI = urllib2 . build_opener ( IIIIi1 , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
 if 44 - 44: oO0o0ooO0 % i11iIiiIii - IIII * OoOO + IiIIi1I1Iiii * o0000oOoOoO0o
 IIiiIiI1 = urllib2 . Request ( url )
 IIiiIiI1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lMartunis Gecko) Chrome/33.0.1750.154 Safari/537.36' )
 if headers :
  for oo000 , IiI1iI1IiiIi1 in headers :
   IIiiIiI1 . add_header ( oo000 , IiI1iI1IiiIi1 )
   if 90 - 90: OOO0O0O0ooooo + o00O0oo - II1 . o00O0oo
 iiIiIIi = i1i111iI . open ( IIiiIiI1 , post , timeout = timeout )
 I1I1i = iiIiIIi . read ( )
 iiIiIIi . close ( )
 return I1I1i ;
 if 60 - 60: ii11ii1ii . ii11ii1ii / IIII
def Iio00 ( str , reg = None ) :
 if reg :
  str = re . findall ( reg , str ) [ 0 ]
 IiI1iiII1i1i = urllib . unquote ( str [ 0 : len ( str ) - 1 ] ) ;
 i1IiI = '' ;
 for I11I11i1I in range ( len ( IiI1iiII1i1i ) ) :
  i1IiI += chr ( ord ( IiI1iiII1i1i [ I11I11i1I ] ) - IiI1iiII1i1i [ len ( IiI1iiII1i1i ) - 1 ] ) ;
 i1IiI = urllib . unquote ( i1IiI )
 print i1IiI
 return i1IiI
 if 82 - 82: OOooOOo
def iI1iIIIi1i ( str ) :
 oO000o0Oo00 = re . findall ( 'unescape\(\'(.*?)\'' , str )
 print 'js' , oO000o0Oo00
 if ( not oO000o0Oo00 == None ) and len ( oO000o0Oo00 ) > 0 :
  for OooO0O in oO000o0Oo00 :
   if 44 - 44: OOO0O0O0ooooo . OoOO0ooOOoo0O * i11iIiiIii % i11iIiiIii + OOO0O0O0ooooo / o0000oOoOoO0o
   str = str . replace ( OooO0O , urllib . unquote ( OooO0O ) )
 return str
 if 89 - 89: oO0o0ooO0 % O00ooooo00 % OoOO0ooOOoo0O
oOooO0O0OoooO = 0
def o0O0Oo00 ( m , html_page , cookieJar ) :
 global oOooO0O0OoooO
 oOooO0O0OoooO += 1
 iIi1Iii111I = m [ 'expres' ]
 IIiiii = m [ 'page' ]
 IIi11i11 = re . compile ( '\$LiveStreamCaptcha\[([^\]]*)\]' ) . findall ( iIi1Iii111I ) [ 0 ]
 if 18 - 18: IIii1I + o00O0oo * IIiIiII11i - o0000oOoOoO0o / IIiIiII11i
 o0o0O00 = re . compile ( IIi11i11 ) . findall ( html_page ) [ 0 ]
 print iIi1Iii111I , IIi11i11 , o0o0O00
 if not o0o0O00 . startswith ( "http" ) :
  o00iI1i1II = 'http://' + "" . join ( IIiiii . split ( '/' ) [ 2 : 3 ] )
  if o0o0O00 . startswith ( "/" ) :
   o0o0O00 = o00iI1i1II + o0o0O00
  else :
   o0o0O00 = o00iI1i1II + '/' + o0o0O00
   if 14 - 14: i11Ii11I1Ii1i - IIii1I / OOO0O0O0ooooo % O0oO . OOooOOo
 o0O0oO0 = os . path . join ( Oooo0000 , str ( oOooO0O0OoooO ) + "captcha.jpg" )
 oo0 = open ( o0O0oO0 , "wb" )
 print ' c capurl' , o0o0O00
 IIiiIiI1 = urllib2 . Request ( o0o0O00 )
 IIiiIiI1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  IIiiIiI1 . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  IIiiIiI1 . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'setcookie' in m :
  print 'adding cookie' , m [ 'setcookie' ]
  IIiiIiI1 . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 18 - 18: OoOO0ooOOoo0O * OoOO0ooOOoo0O % OoOO0ooOOoo0O
  if 17 - 17: OOO0O0O0ooooo * OOooOOo * OoOO * iIiiiI1IiI1I1 * o00O0oo % O00ooooo00
  if 33 - 33: OoOO * OoOO . i11Ii11I1Ii1i . i11iIiiIii
  if 48 - 48: ii11ii1ii . oO0o0ooO0 + OOooOOo % OoOO / i11iIiiIii
 urllib2 . urlopen ( IIiiIiI1 )
 iiIiIIi = urllib2 . urlopen ( IIiiIiI1 )
 if 74 - 74: iIiiiI1IiI1I1 . OOO0O0O0ooooo - IIiIiII11i + O0oO % i11iIiiIii % OOooOOo
 oo0 . write ( iiIiIIi . read ( ) )
 iiIiIIi . close ( )
 oo0 . close ( )
 i1 = i1IiIi1 ( captcha = o0O0oO0 )
 I11Ii1iI11iI1 = i1 . get ( )
 return I11Ii1iI11iI1
 if 78 - 78: oO0o0ooO0 + OOooOOo + O0oO - O0oO . i11iIiiIii / Ooo00oOo00o
def I11i11i1 ( imageregex , html_page , cookieJar , m ) :
 global oOooO0O0OoooO
 oOooO0O0OoooO += 1
 if 68 - 68: IiIIi1I1Iiii . IiIIi1I1Iiii - OoOO / o00O0oo . i11Ii11I1Ii1i / O00ooooo00
 if 12 - 12: OoOO * O00ooooo00 * o00O0oo
 if not imageregex == '' :
  if html_page . startswith ( "http" ) :
   o00iI1i1II = o0Oooo ( html_page , cookieJar = cookieJar )
  else :
   o00iI1i1II = html_page
  o0o0O00 = re . compile ( imageregex ) . findall ( html_page ) [ 0 ]
 else :
  o0o0O00 = html_page
  if 'oneplay.tv/embed' in html_page :
   import oneplay
   o00iI1i1II = o0Oooo ( html_page , cookieJar = cookieJar )
   o0o0O00 = oneplay . getCaptchaUrl ( o00iI1i1II )
   if 23 - 23: o0000oOoOoO0o / OOO0O0O0ooooo / IIiIiII11i
 o0O0oO0 = os . path . join ( Oooo0000 , str ( oOooO0O0OoooO ) + "captcha.jpg" )
 oo0 = open ( o0O0oO0 , "wb" )
 print ' c capurl' , o0o0O00
 IIiiIiI1 = urllib2 . Request ( o0o0O00 )
 IIiiIiI1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  IIiiIiI1 . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  IIiiIiI1 . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'accept' in m :
  IIiiIiI1 . add_header ( 'Accept' , m [ 'accept' ] )
 if 'setcookie' in m :
  print 'adding cookie' , m [ 'setcookie' ]
  IIiiIiI1 . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 49 - 49: o00O0oo . ii11ii1ii % OoOO0ooOOoo0O / oO0o0ooO0
  if 95 - 95: OOO0O0O0ooooo * OOooOOo * O0oO . i11Ii11I1Ii1i / IIii1I
  if 28 - 28: O0oO + OoOO0ooOOoo0O - i11Ii11I1Ii1i / IIii1I - IIiIiII11i
  if 45 - 45: OOO0O0O0ooooo / O00ooooo00 * OoOO0ooOOoo0O * Ooo00oOo00o
  if 35 - 35: OoOO / IIII % IIiIiII11i + IIii1I
 iiIiIIi = urllib2 . urlopen ( IIiiIiI1 )
 if 79 - 79: OOooOOo / i11Ii11I1Ii1i
 oo0 . write ( iiIiIIi . read ( ) )
 iiIiIIi . close ( )
 oo0 . close ( )
 i1 = i1IiIi1 ( captcha = o0O0oO0 )
 I11Ii1iI11iI1 = i1 . get ( )
 return I11Ii1iI11iI1
 if 77 - 77: IiIIi1I1Iiii
 if 46 - 46: o0oO0
 if 72 - 72: IIII * o0000oOoOoO0o
 if 67 - 67: O00ooooo00
 if 5 - 5: iIiiiI1IiI1I1 . II1
 if 57 - 57: IIiIiII11i
 if 35 - 35: II1 - o0oO0 / Ooo00oOo00o
 if 50 - 50: OOooOOo
 if 33 - 33: o00O0oo
 if 98 - 98: OOooOOo % iIiiiI1IiI1I1
 if 95 - 95: IIii1I - o0oO0 - o0000oOoOoO0o + o0oO0 % OoOO . IIiIiII11i
 if 41 - 41: OOO0O0O0ooooo + OoOO0ooOOoo0O . O00ooooo00 - iIiiiI1IiI1I1 * ii11ii1ii . Ooo00oOo00o
 if 68 - 68: ii11ii1ii
def i11Ii1IIi ( name , headname ) :
 if 36 - 36: OOO0O0O0ooooo * Ooo00oOo00o % IIII * IIII / Ooo00oOo00o * O0oO
 if 14 - 14: O00ooooo00 . O0oO + OOO0O0O0ooooo * i11Ii11I1Ii1i
 o0OO00 = xbmc . Keyboard ( 'default' , 'heading' , True )
 o0OO00 . setDefault ( name )
 o0OO00 . setHeading ( headname )
 o0OO00 . setHiddenInput ( False )
 return o0OO00 . getText ( )
 if 14 - 14: OoOO + i11iIiiIii
 if 83 - 83: OoOO / i11iIiiIii + iIiiiI1IiI1I1 . IIII * o0000oOoOoO0o + O0oO
 if 42 - 42: O00ooooo00 % iIiiiI1IiI1I1 . i11Ii11I1Ii1i
 if 7 - 7: OoOO - OoOO0ooOOoo0O * o0000oOoOoO0o + ii11ii1ii . OoOO
class i1IiIi1 ( xbmcgui . WindowDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . cptloc = kwargs . get ( 'captcha' )
  self . img = xbmcgui . ControlImage ( 335 , 30 , 624 , 60 , self . cptloc )
  self . addControl ( self . img )
  self . kbd = xbmc . Keyboard ( )
  if 85 - 85: OOO0O0O0ooooo
 def get ( self ) :
  self . show ( )
  time . sleep ( 2 )
  self . kbd . doModal ( )
  if ( self . kbd . isConfirmed ( ) ) :
   Iii = self . kbd . getText ( )
   self . close ( )
   return Iii
  self . close ( )
  return False
  if 42 - 42: iIiiiI1IiI1I1 + o0oO0 - oO0o0ooO0 - OOO0O0O0ooooo / ii11ii1ii % O0oO
def Oo00o0OO0O00o ( ) :
 import time
 return str ( int ( time . time ( ) * 1000 ) )
 if 83 - 83: o0000oOoOoO0o / OOO0O0O0ooooo % IIII - ii11ii1ii . IiIIi1I1Iiii
def iIi1i ( ) :
 import time
 return str ( int ( time . time ( ) ) )
 if 49 - 49: IIii1I * O00ooooo00 . II1
def OOOO0oOo00O ( ) :
 i1I1I1i1i1i = [ ]
 ii1 = sys . argv [ 2 ]
 if len ( ii1 ) >= 2 :
  o0oo0Ooooo0 = sys . argv [ 2 ]
  Oo0oOo000OoO0 = o0oo0Ooooo0 . replace ( '?' , '' )
  if ( o0oo0Ooooo0 [ len ( o0oo0Ooooo0 ) - 1 ] == '/' ) :
   o0oo0Ooooo0 = o0oo0Ooooo0 [ 0 : len ( o0oo0Ooooo0 ) - 2 ]
  IIi = Oo0oOo000OoO0 . split ( '&' )
  i1I1I1i1i1i = { }
  for I11I11i1I in range ( len ( IIi ) ) :
   i1I1i = { }
   i1I1i = IIi [ I11I11i1I ] . split ( '=' )
   if ( len ( i1I1i ) ) == 2 :
    i1I1I1i1i1i [ i1I1i [ 0 ] ] = i1I1i [ 1 ]
 return i1I1I1i1i1i
 if 22 - 22: IiIIi1I1Iiii % Ooo00oOo00o - II1 * IiIIi1I1Iiii
 if 38 - 38: IIii1I / i11Ii11I1Ii1i
def i11oooOo ( ) :
 OOO = json . loads ( open ( I11 ) . read ( ) )
 i1iIi = len ( OOO )
 for I11I11i1I in OOO :
  oOOoO0O0O0 = I11I11i1I [ 0 ]
  iIi1iIiii111 = I11I11i1I [ 1 ]
  oo0oo0O0 = I11I11i1I [ 2 ]
  try :
   iiIii = I11I11i1I [ 3 ]
   if iiIii == None :
    raise
  except :
   if OOo . getSetting ( 'use_thumb' ) == "true" :
    iiIii = oo0oo0O0
   else :
    iiIii = o0oo0o0O00OO
  try : I1II1I11I1I = I11I11i1I [ 5 ]
  except : I1II1I11I1I = None
  try : OoOOooOOO0 = I11I11i1I [ 6 ]
  except : OoOOooOOO0 = None
  if 18 - 18: IIii1I + o0000oOoOoO0o + IIii1I . OoOO + o0oO0 . i11Ii11I1Ii1i
  if I11I11i1I [ 4 ] == 0 :
   o0oO00000 ( iIi1iIiii111 , oOOoO0O0O0 , oo0oo0O0 , iiIii , '' , '' , '' , 'fav' , I1II1I11I1I , OoOOooOOO0 , i1iIi )
  else :
   Ooo ( oOOoO0O0O0 , iIi1iIiii111 , I11I11i1I [ 4 ] , oo0oo0O0 , o0oo0o0O00OO , '' , '' , '' , '' , 'fav' )
   if 7 - 7: OoOO + IIii1I * o00O0oo * o00O0oo / iIiiiI1IiI1I1 - oO0o0ooO0
   if 65 - 65: OoOO0ooOOoo0O + OOooOOo + iIiiiI1IiI1I1
def oOOooi1I1iIii11 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 oOoO0O0oO = [ ]
 try :
  if 92 - 92: IiIIi1I1Iiii / i11iIiiIii + OoOO
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11 ) == False :
  i1IIiiiii ( 'Making Favorites File' )
  oOoO0O0oO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iIiI = open ( I11 , "w" )
  iIiI . write ( json . dumps ( oOoO0O0oO ) )
  iIiI . close ( )
 else :
  i1IIiiiii ( 'Appending Favorites' )
  iIiI = open ( I11 ) . read ( )
  ooOoo0O = json . loads ( iIiI )
  ooOoo0O . append ( ( name , url , iconimage , fanart , mode ) )
  OOOoO0O0o = open ( I11 , "w" )
  OOOoO0O0o . write ( json . dumps ( ooOoo0O ) )
  OOOoO0O0o . close ( )
  if 87 - 87: OOooOOo % IIii1I
  if 72 - 72: o0000oOoOoO0o . o0000oOoOoO0o - OoOO
def III1II1i ( name ) :
 ooOoo0O = json . loads ( open ( I11 ) . read ( ) )
 for O00oO in range ( len ( ooOoo0O ) ) :
  if ooOoo0O [ O00oO ] [ 0 ] == name :
   del ooOoo0O [ O00oO ]
   OOOoO0O0o = open ( I11 , "w" )
   OOOoO0O0o . write ( json . dumps ( ooOoo0O ) )
   OOOoO0O0o . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 3 - 3: IIII
def I1 ( url ) :
 import urlresolver
 iIIIiI = urlresolver . HostedMediaFile ( url )
 if iIIIiI :
  ooo = urlresolver . resolve ( url )
  Oo = ooo
  if isinstance ( Oo , list ) :
   for II1III1I1I1Ii in Oo :
    iI1I1 = OOo . getSetting ( 'quality' )
    if II1III1I1I1Ii [ 'quality' ] == 'HD' :
     ooo = II1III1I1I1Ii [ 'url' ]
     break
    elif II1III1I1I1Ii [ 'quality' ] == 'SD' :
     ooo = II1III1I1I1Ii [ 'url' ]
    elif II1III1I1I1Ii [ 'quality' ] == '1080p' and OOo . getSetting ( '1080pquality' ) == 'true' :
     ooo = II1III1I1I1Ii [ 'url' ]
     break
  else :
   ooo = Oo
 else :
  xbmc . executebuiltin ( "XBMC.Notification(Martunis,Urlresolver donot support this domain. - ,5000)" )
 return ooo
def I1III1i1I ( name , mu_playlist , queueVideo = None ) :
 I1II1I11I1I = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 if 51 - 51: OoOO0ooOOoo0O + Ooo00oOo00o + IIII + IIII % ii11ii1ii
 if OOo . getSetting ( 'ask_playlist_items' ) == 'true' and not queueVideo :
  import urlparse
  iIi1i1iIi1Ii1 = [ ]
  for I11I11i1I in mu_playlist :
   oOOoOOO0oo0 = urlparse . urlparse ( I11I11i1I ) . netloc
   if oOOoOOO0oo0 == '' :
    iIi1i1iIi1Ii1 . append ( name )
   else :
    iIi1i1iIi1Ii1 . append ( oOOoOOO0oo0 )
  O00O = xbmcgui . Dialog ( )
  O00oO = O00O . select ( 'Choose a video source' , iIi1i1iIi1Ii1 )
  if O00oO >= 0 :
   if "&mode=19" in mu_playlist [ O00oO ] :
    if 94 - 94: oO0o0ooO0 - OoOO + ii11ii1ii - IiIIi1I1Iiii
    xbmc . Player ( ) . play ( I1 ( mu_playlist [ O00oO ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) ) )
   elif "$doregex" in mu_playlist [ O00oO ] :
    print mu_playlist [ O00oO ]
    iiIi1iiI1I = mu_playlist [ O00oO ] . split ( '&regexs=' )
    print iiIi1iiI1I
    iIi1iIiii111 , o00o0 = oOIIiIi ( iiIi1iiI1I [ 1 ] , iiIi1iiI1I [ 0 ] )
    Iiii1I = iIi1iIiii111 . replace ( ';' , '' )
    xbmc . Player ( ) . play ( Iiii1I )
    if 56 - 56: i11iIiiIii - IIii1I . iIiiiI1IiI1I1
   else :
    iIi1iIiii111 = mu_playlist [ O00oO ]
    xbmc . Player ( ) . play ( iIi1iIiii111 )
 elif not queueVideo :
  if 81 - 81: O0oO / OOooOOo * O0oO . OOO0O0O0ooooo
  I1II1I11I1I . clear ( )
  ii1I = 0
  for I11I11i1I in mu_playlist :
   ii1I += 1
   OOOOo00oo00O = xbmcgui . ListItem ( '%s) %s' % ( str ( ii1I ) , name ) )
   if 83 - 83: iIiiiI1IiI1I1 * O00ooooo00 * IIII . OoOO / o00O0oo + O00ooooo00
   try :
    if "$doregex" in I11I11i1I :
     iiIi1iiI1I = I11I11i1I . split ( '&regexs=' )
     print iiIi1iiI1I
     iIi1iIiii111 , o00o0 = oOIIiIi ( iiIi1iiI1I [ 1 ] , iiIi1iiI1I [ 0 ] )
    elif "&mode=19" in I11I11i1I :
     iIi1iIiii111 = I1 ( I11I11i1I . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    if iIi1iIiii111 :
     I1II1I11I1I . add ( iIi1iIiii111 , OOOOo00oo00O )
    else :
     raise
   except Exception :
    I1II1I11I1I . add ( I11I11i1I , OOOOo00oo00O )
    pass
    if 43 - 43: II1
  xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
 else :
  if 97 - 97: OoOO / IiIIi1I1Iiii + o0oO0
  oOo00Oo0o0Oo = xbmcgui . ListItem ( name )
  I1II1I11I1I . add ( mu_playlist , oOo00Oo0o0Oo )
  if 32 - 32: i11Ii11I1Ii1i % o0oO0 * IiIIi1I1Iiii
  if 72 - 72: i11Ii11I1Ii1i . IIII - o0oO0 - oO0o0ooO0 % O00ooooo00
def oO0o00O0O0oo0 ( name , url ) :
 if OOo . getSetting ( 'save_location' ) == "" :
  xbmc . executebuiltin ( "XBMC.Notification('Martunis','Choose a location to save files.',15000," + oO0o0o0ooO0oO + ")" )
  OOo . openSettings ( )
 o0oo0Ooooo0 = { 'url' : url , 'download_path' : OOo . getSetting ( 'save_location' ) }
 downloader . download ( name , o0oo0Ooooo0 )
 O00O = xbmcgui . Dialog ( )
 O0i11i1iiI1i = O00O . yesno ( 'Martunis' , 'Do you want to add this file as a source?' )
 if O0i11i1iiI1i :
  I1IIIii ( os . path . join ( OOo . getSetting ( 'save_location' ) , name ) )
  if 24 - 24: o0oO0 * OoOO0ooOOoo0O
def Oo000O ( url , name ) :
 if 42 - 42: O0oO % IIII % ii11ii1ii % OoOO0ooOOoo0O + o00O0oo % OOooOOo
 iI1iIIiii = [ 'plugin.video.PsycoTV' , 'plugin://plugin.video.phstreams' , 'plugin://plugin.video.SportsDevil' , 'plugin://plugin.video.CanTVLive' , 'plugin://plugin.video.ccloudtv' , 'plugin://plugin.video.prosport' , 'plugin://plugin.video.p2psport' , ]
 if 52 - 52: oO0o0ooO0 % o0000oOoOoO0o * IIiIiII11i % o00O0oo + o0000oOoOoO0o / IIII
 if 80 - 80: II1 + O0oO
 if 95 - 95: o0oO0 / OoOO0ooOOoo0O * o0oO0 - II1 * II1 % Ooo00oOo00o
 if 43 - 43: IiIIi1I1Iiii . o0oO0
 if 12 - 12: o0oO0 + o0000oOoOoO0o + o00O0oo . O0oO / oO0o0ooO0
 if 29 - 29: O0oO . i11Ii11I1Ii1i - iIiiiI1IiI1I1
 if 68 - 68: IIii1I + iIiiiI1IiI1I1 / OoOO0ooOOoo0O
 iIi1i1iIi1Ii1 = [ 'Psycho TV' , 'Phoenix' , 'SportsDevil' , 'CanTVLive' , 'Ccloudtv' , 'Prosport' , 'P2psport' ]
 if 91 - 91: OOooOOo % IIii1I . IIiIiII11i
 O00O = xbmcgui . Dialog ( )
 O00oO = O00O . select ( 'Choose a video source' , iIi1i1iIi1Ii1 )
 if 70 - 70: o00O0oo % iIiiiI1IiI1I1 % OOO0O0O0ooooo . O00ooooo00 / o0oO0
 if O00oO >= 0 :
  url = iI1iIIiii [ O00oO ]
  print 'url' , url
  OO0ooOoOO0OOo ( url )
  if 51 - 51: IIii1I * ii11ii1ii / IIii1I . IIii1I . IIII * o00O0oo
def Ooo ( name , url , mode , iconimage , fanart , description , genre , date , credits , showcontext = False , regexs = None , reg_url = None , allinfo = { } ) :
 if 93 - 93: OoOO0ooOOoo0O * oO0o0ooO0
 ii11i1I1iiii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 I11iI1I = True
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 Iii1iiIi1II1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if len ( allinfo ) < 1 :
  Iii1iiIi1II1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date , "credits" : credits } )
 else :
  Iii1iiIi1II1 . setInfo ( type = "Video" , infoLabels = allinfo )
 Iii1iiIi1II1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Oo000o = [ ]
  Iii1I1I11iiI1 = OOo . getSetting ( 'parentalblocked' )
  Iii1I1I11iiI1 = Iii1I1I11iiI1 == "true"
  OO00oo = OOo . getSetting ( 'parentalblockedpin' )
  if 84 - 84: i11Ii11I1Ii1i + i11iIiiIii - o0000oOoOoO0o * i11Ii11I1Ii1i
  if len ( OO00oo ) > 0 :
   if Iii1I1I11iiI1 :
    Oo000o . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   else :
    Oo000o . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 33 - 33: i11Ii11I1Ii1i % O00ooooo00 - OoOO0ooOOoo0O . OOO0O0O0ooooo / OOO0O0O0ooooo
  if showcontext == 'source' :
   if 96 - 96: II1 + O0oO * OOO0O0O0ooooo
   if name in str ( ii11iIi1I ) :
    Oo000o . append ( ( 'Remove from Sources' , 'XBMC.RunPlugin(%s?mode=8&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 86 - 86: oO0o0ooO0
    if 29 - 29: IIii1I - Ooo00oOo00o + IIiIiII11i % IIii1I % o0000oOoOoO0o
  elif showcontext == 'download' :
   Oo000o . append ( ( 'Download' , 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'fav' :
   Oo000o . append ( ( 'Remove from Martunis Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if showcontext == '!!update' :
   O0OOO00 = (
 '%s?url=%s&mode=17&regexs=%s'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( reg_url ) , regexs )
 )
   Oo000o . append ( ( '[COLOR yellow]!!update[/COLOR]' , 'XBMC.RunPlugin(%s)' % O0OOO00 ) )
  if not name in i1iIIi1 :
   Oo000o . append ( ( 'Add to Martunis Favorites' , 'XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Iii1iiIi1II1 . addContextMenuItems ( Oo000o )
 I11iI1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii11i1I1iiii , listitem = Iii1iiIi1II1 , isFolder = True )
 return I11iI1I
def ooOOo0o ( url , title , media_type = 'video' ) :
 if 50 - 50: iIiiiI1IiI1I1 - o0oO0 + IIii1I + IIii1I
 if 91 - 91: iIiiiI1IiI1I1 - OOO0O0O0ooooo . IIii1I . OOO0O0O0ooooo + OoOO - iIiiiI1IiI1I1
 import youtubedl
 if not url == '' :
  if media_type == 'audio' :
   youtubedl . single_YD ( url , download = True , audio = True )
  else :
   youtubedl . single_YD ( url , download = True )
 elif xbmc . Player ( ) . isPlaying ( ) == True :
  import YDStreamExtractor
  if YDStreamExtractor . isDownloading ( ) == True :
   if 26 - 26: ii11ii1ii
   YDStreamExtractor . manageDownloads ( )
  else :
   IiIi = xbmc . Player ( ) . getPlayingFile ( )
   if 88 - 88: OOooOOo - o0000oOoOoO0o
   IiIi = IiIi . split ( '|User-Agent=' ) [ 0 ]
   OOOOo00oo00O = { 'url' : IiIi , 'title' : title , 'media_type' : media_type }
   youtubedl . single_YD ( '' , download = True , dl_info = OOOOo00oo00O )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(DOWNLOAD,First Play [COLOR yellow]WHILE playing download[/COLOR] ,10000)" )
  if 63 - 63: O0oO * II1
  if 19 - 19: O0oO - ii11ii1ii . IIii1I . OOooOOo / o0000oOoOoO0o
def OOO0O00Oo ( string ) :
 if isinstance ( string , basestring ) :
  if isinstance ( string , unicode ) :
   string = string . encode ( 'ascii' , 'ignore' )
 return string
def ii1oOOO0ooOO ( string , encoding = 'utf-8' ) :
 if isinstance ( string , basestring ) :
  if not isinstance ( string , unicode ) :
   string = unicode ( string , encoding , 'ignore' )
 return string
def i11IiI1iiI11 ( s ) : return "" . join ( filter ( lambda OOoOOOO00 : ord ( OOoOOOO00 ) < 128 , s ) )
if 49 - 49: Ooo00oOo00o - OOO0O0O0ooooo / Ooo00oOo00o * OOooOOo + o0oO0
def Iiii1IOoo000000 ( command ) :
 ooOoo0O = ''
 try :
  ooOoo0O = xbmc . executeJSONRPC ( ii1oOOO0ooOO ( command ) )
 except UnicodeEncodeError :
  ooOoo0O = xbmc . executeJSONRPC ( OOO0O00Oo ( command ) )
  if 80 - 80: iIiiiI1IiI1I1 - o0000oOoOoO0o % II1 . IIii1I - i11Ii11I1Ii1i + IIiIiII11i
 return ii1oOOO0ooOO ( ooOoo0O )
 if 21 - 21: i11iIiiIii
def OO0ooOoOO0OOo ( url , give_me_result = None , playlist = False ) :
 if 'audio' in url :
  o00iIiiiII = ii1oOOO0ooOO ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params": {"directory":"%s","media":"video", "properties": ["title", "album", "artist", "duration","thumbnail", "year"]}, "id": 1}' ) % url
 else :
  o00iIiiiII = ii1oOOO0ooOO ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":[ "plot","playcount","director", "genre","votes","duration","trailer","premiered","thumbnail","title","year","dateadded","fanart","rating","season","episode","studio","mpaa"]},"id":1}' ) % url
 Ii1I1 = json . loads ( Iiii1IOoo000000 ( o00iIiiiII ) )
 if 71 - 71: OOooOOo + IIii1I * OoOO0ooOOoo0O . o0oO0 % i11iIiiIii % IIii1I
 if give_me_result :
  return Ii1I1
 if Ii1I1 . has_key ( 'error' ) :
  return
 else :
  if 63 - 63: II1 * Ooo00oOo00o / o00O0oo - OoOO0ooOOoo0O . IIii1I + IIII
  for I11I11i1I in Ii1I1 [ 'result' ] [ 'files' ] :
   ii1IIiI1IIi = { }
   url = I11I11i1I [ 'file' ]
   oOOoO0O0O0 = i11IiI1iiI11 ( I11I11i1I [ 'label' ] )
   ii1ii1ii = i11IiI1iiI11 ( I11I11i1I [ 'thumbnail' ] )
   o0oo0o0O00OO = i11IiI1iiI11 ( I11I11i1I [ 'fanart' ] )
   ii1IIiI1IIi = dict ( ( k , v ) for k , v in I11I11i1I . iteritems ( ) if not v == '0' or not v == - 1 or v == '' )
   ii1IIiI1IIi . pop ( "file" , None )
   if I11I11i1I [ 'filetype' ] == 'file' :
    if playlist :
     I1III1i1I ( oOOoO0O0O0 , url , queueVideo = '1' )
     continue
    else :
     o0oO00000 ( url , oOOoO0O0O0 , ii1ii1ii , o0oo0o0O00OO , '' , '' , '' , '' , None , '' , total = len ( Ii1I1 [ 'result' ] [ 'files' ] ) , allinfo = ii1IIiI1IIi )
     if 76 - 76: IIII / Ooo00oOo00o + OOooOOo
     if I11I11i1I [ 'type' ] and I11I11i1I [ 'type' ] == 'tvshow' :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'tvshows' )
     elif I11I11i1I [ 'episode' ] > 0 :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'episodes' )
      if 86 - 86: i11iIiiIii + i11iIiiIii . o0oO0 % IIiIiII11i . i11Ii11I1Ii1i
   else :
    Ooo ( oOOoO0O0O0 , url , 53 , ii1ii1ii , o0oo0o0O00OO , '' , '' , '' , '' , allinfo = ii1IIiI1IIi )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if 17 - 17: oO0o0ooO0
def o0oO00000 ( url , name , iconimage , fanart , description , genre , date , showcontext , playlist , regexs , total , setCookie = "" , allinfo = { } ) :
 if 67 - 67: OOO0O0O0ooooo * o00O0oo - ii11ii1ii - iIiiiI1IiI1I1
 Oo000o = [ ]
 Iii1I1I11iiI1 = OOo . getSetting ( 'parentalblocked' )
 Iii1I1I11iiI1 = Iii1I1I11iiI1 == "true"
 OO00oo = OOo . getSetting ( 'parentalblockedpin' )
 if 41 - 41: IIiIiII11i - o0oO0 % iIiiiI1IiI1I1 . o0oO0 - o00O0oo
 if len ( OO00oo ) > 0 :
  if Iii1I1I11iiI1 :
   Oo000o . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  else :
   Oo000o . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   if 45 - 45: oO0o0ooO0 - o0000oOoOoO0o
 try :
  name = name . encode ( 'utf-8' )
 except : pass
 if 70 - 70: Ooo00oOo00o % IIiIiII11i / IIiIiII11i . o00O0oo % i11Ii11I1Ii1i . iIiiiI1IiI1I1
 if 10 - 10: oO0o0ooO0 - i11iIiiIii . OoOO % O00ooooo00
 if 78 - 78: IIii1I * IiIIi1I1Iiii . IiIIi1I1Iiii - o0000oOoOoO0o . IIii1I
 if 30 - 30: i11Ii11I1Ii1i + i11Ii11I1Ii1i % O0oO - ii11ii1ii - OoOO
 if 36 - 36: o00O0oo % o0000oOoOoO0o
 if 72 - 72: IIiIiII11i / IIII - OOO0O0O0ooooo + o00O0oo
 I11iI1I = True
 o0iIIIIi = False
 if regexs :
  i1I11ii = '17'
  if 'listrepeat' in regexs :
   o0iIIIIi = True
   print 'setting as folder in link'
  Oo000o . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif ( any ( x in url for x in OO0o ) and url . startswith ( 'http' ) ) or url . endswith ( '&mode=19' ) :
  url = url . replace ( '&mode=19' , '' )
  i1I11ii = '19'
  Oo000o . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . endswith ( '&mode=18' ) :
  url = url . replace ( '&mode=18' , '' )
  i1I11ii = '18'
  Oo000o . append ( ( '[COLOR white]!!Download!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  if OOo . getSetting ( 'dlaudioonly' ) == 'true' :
   Oo000o . append ( ( '!!Download [COLOR seablue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . startswith ( 'magnet:?xt=' ) :
  if '&' in url and not '&amp;' in url :
   url = url . replace ( '&' , '&amp;' )
  url = 'plugin://plugin.video.pulsar/play?uri=' + url
  i1I11ii = '12'
 else :
  i1I11ii = '12'
  Oo000o . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 if 'plugin://plugin.video.youtube/play/?video_id=' in url :
  o0ooO00O0O = url . replace ( 'plugin://plugin.video.youtube/play/?video_id=' , 'https://www.youtube.com/watch?v=' )
  Oo000o . append ( ( '!!Download [COLOR blue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( o0ooO00O0O ) , urllib . quote_plus ( name ) ) ) )
 ii11i1I1iiii = sys . argv [ 0 ] + "?"
 iiiI1iI1 = False
 if playlist :
  if OOo . getSetting ( 'add_playlist' ) == "false" :
   ii11i1I1iiii += "url=" + urllib . quote_plus ( url ) + "&mode=" + i1I11ii
  else :
   ii11i1I1iiii += "mode=13&name=%s&playlist=%s" % ( urllib . quote_plus ( name ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) )
   name = name + '[COLOR green][/COLOR]'
   iiiI1iI1 = True
 else :
  ii11i1I1iiii += "url=" + urllib . quote_plus ( url ) + "&mode=" + i1I11ii
 if regexs :
  ii11i1I1iiii += "&regexs=" + regexs
 if not setCookie == '' :
  ii11i1I1iiii += "&setCookie=" + urllib . quote_plus ( setCookie )
  if 15 - 15: O0oO . O00ooooo00 * OOooOOo % IIii1I
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 Iii1iiIi1II1 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 if len ( allinfo ) < 1 :
  Iii1iiIi1II1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date } )
  if 35 - 35: OoOO + o0oO0 - OOooOOo % OoOO0ooOOoo0O % ii11ii1ii % OOooOOo
 else :
  Iii1iiIi1II1 . setInfo ( type = "Video" , infoLabels = allinfo )
 Iii1iiIi1II1 . setProperty ( "Fanart_Image" , fanart )
 if 45 - 45: IIiIiII11i * o0000oOoOoO0o % Ooo00oOo00o
 if ( not iiiI1iI1 ) and not any ( x in url for x in Oo0Ooo ) and not '$PLAYERPROXY$=' in url :
  if regexs :
   if 24 - 24: i11Ii11I1Ii1i - o00O0oo * OoOO0ooOOoo0O
   if '$pyFunction:playmedia(' not in urllib . unquote_plus ( regexs ) and 'notplayable' not in urllib . unquote_plus ( regexs ) and 'listrepeat' not in urllib . unquote_plus ( regexs ) :
    if 87 - 87: oO0o0ooO0 - OoOO % OoOO . OoOO0ooOOoo0O / OoOO
    Iii1iiIi1II1 . setProperty ( 'IsPlayable' , 'true' )
  else :
   Iii1iiIi1II1 . setProperty ( 'IsPlayable' , 'true' )
 else :
  i1IIiiiii ( 'NOT setting isplayable' + url )
 if showcontext :
  if 6 - 6: OOooOOo / IIii1I * II1 * i11iIiiIii
  if showcontext == 'fav' :
   Oo000o . append (
 ( 'Remove from Martunis Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) )
 )
  elif not name in i1iIIi1 :
   o0O0OOo0oO = (
 '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) )
 )
   if playlist :
    o0O0OOo0oO += 'playlist=' + urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) )
   if regexs :
    o0O0OOo0oO += "&regexs=" + regexs
   Oo000o . append ( ( 'Add to Martunis Favorites' , 'XBMC.RunPlugin(%s)' % o0O0OOo0oO ) )
  Iii1iiIi1II1 . addContextMenuItems ( Oo000o )
 if not playlist is None :
  if OOo . getSetting ( 'add_playlist' ) == "false" :
   Iiiii = name . split ( ') ' ) [ 1 ]
   iiI = [
 ( 'Play ' + Iiiii + ' PlayList' , 'XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( Iiiii ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) ) )
 ]
   Iii1iiIi1II1 . addContextMenuItems ( iiI )
   if 17 - 17: i11iIiiIii / IiIIi1I1Iiii . Ooo00oOo00o / IIiIiII11i
 I11iI1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii11i1I1iiii , listitem = Iii1iiIi1II1 , totalItems = total , isFolder = o0iIIIIi )
 if 38 - 38: O00ooooo00 . OoOO % oO0o0ooO0 + IIii1I + OOO0O0O0ooooo
 if 47 - 47: Ooo00oOo00o + O0oO / iIiiiI1IiI1I1
 return I11iI1I
 if 97 - 97: OoOO / IIiIiII11i % OOO0O0O0ooooo + O00ooooo00 - i11Ii11I1Ii1i
 if 38 - 38: ii11ii1ii % o0oO0 + i11iIiiIii + IIII + i11Ii11I1Ii1i / i11iIiiIii
def o0OOOOOo0 ( url , name , iconimage , setresolved = True ) :
 if setresolved :
  Iii1iiIi1II1 = xbmcgui . ListItem ( name , iconImage = iconimage )
  Iii1iiIi1II1 . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
  Iii1iiIi1II1 . setProperty ( "IsPlayable" , "true" )
  Iii1iiIi1II1 . setPath ( url )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Iii1iiIi1II1 )
 else :
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  if 57 - 57: IIii1I + IIii1I
  if 56 - 56: OoOO0ooOOoo0O + i11Ii11I1Ii1i
  if 32 - 32: iIiiiI1IiI1I1 + OOooOOo % i11Ii11I1Ii1i / OOooOOo + OoOO
  if 2 - 2: i11iIiiIii - o0oO0 + Ooo00oOo00o % o00O0oo * oO0o0ooO0
def oo0O0 ( link ) :
 iIi1iIiii111 = urllib . urlopen ( link )
 Ooo000O00 = iIi1iIiii111 . read ( )
 iIi1iIiii111 . close ( )
 i1iI1Iiii1I = Ooo000O00 . split ( "Jetzt" )
 I1iII = i1iI1Iiii1I [ 1 ] . split ( 'programm/detail.php?const_id=' )
 Iii1I1IIII = I1iII [ 1 ] . split ( '<br /><a href="/' )
 OooooOoO = Iii1I1IIII [ 0 ] [ 40 : len ( Iii1I1IIII [ 0 ] ) ]
 o00OoOO0O0 = I1iII [ 2 ] . split ( "</a></p></div>" )
 I1i1II1 = o00OoOO0O0 [ 0 ] [ 17 : len ( o00OoOO0O0 [ 0 ] ) ]
 I1i1II1 = I1i1II1 . encode ( 'utf-8' )
 return "  - " + I1i1II1 + " - " + OooooOoO
 if 89 - 89: Ooo00oOo00o / Ooo00oOo00o
 if 1 - 1: OoOO . i11iIiiIii
def oOo0O ( url , regex ) :
 ooOoo0O = OoO000 ( url )
 try :
  ii1I = re . findall ( regex , ooOoo0O ) [ 0 ]
  return ii1I
 except :
  i1IIiiiii ( 'regex failed' )
  i1IIiiiii ( regex )
  return
  if 74 - 74: OOO0O0O0ooooo + II1 / OoOO0ooOOoo0O / OOooOOo . OoOO % OoOO0ooOOoo0O
  if 34 - 34: O00ooooo00 . IIiIiII11i
  if 6 - 6: o0oO0 % OoOO0ooOOoo0O % oO0o0ooO0
def OooIi ( d , root = "root" , nested = 0 ) :
 if 92 - 92: OoOO0ooOOoo0O / o0000oOoOoO0o . OoOO
 i1iOO = lambda OO00OoooO : '<' + OO00OoooO + '>'
 IIIi = lambda OO00OoooO : '</' + OO00OoooO + '>\n'
 Ii1iiI1 = lambda OoO , o0ooOOoO0oO0 : o0ooOOoO0oO0 + i1iOO ( oo00 ) + str ( OoO ) + IIIi ( oo00 )
 if 35 - 35: i11Ii11I1Ii1i % IIiIiII11i - i11Ii11I1Ii1i - Ooo00oOo00o - II1
 o0ooOOoO0oO0 = i1iOO ( root ) + '\n' if root else ""
 if 46 - 46: O00ooooo00 . O00ooooo00 . OoOO0ooOOoo0O / o00O0oo / i11Ii11I1Ii1i
 for oo00 , Ii1I in d . iteritems ( ) :
  iii = type ( Ii1I )
  if nested == 0 : oo00 = 'regex'
  if iii is list :
   for OoO in Ii1I :
    OoO = escape ( OoO )
    o0ooOOoO0oO0 = Ii1iiI1 ( OoO , o0ooOOoO0oO0 )
    if 59 - 59: i11iIiiIii . II1 / o00O0oo * OoOO + II1
  if iii is dict :
   o0ooOOoO0oO0 = Ii1iiI1 ( '\n' + OooIi ( Ii1I , None , nested + 1 ) , o0ooOOoO0oO0 )
  if iii is not list and iii is not dict :
   if not Ii1I is None : Ii1I = escape ( Ii1I )
   o0ooOOoO0oO0 = Ii1iiI1 ( Ii1I , o0ooOOoO0oO0 )
   if 3 - 3: i11iIiiIii * IiIIi1I1Iiii % IIii1I % IIiIiII11i * IIII / o0000oOoOoO0o
 o0ooOOoO0oO0 += IIIi ( root ) if root else ""
 if 95 - 95: O0oO * OOO0O0O0ooooo * o0oO0 . II1 % IiIIi1I1Iiii + OoOO
 return o0ooOOoO0oO0
xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
if 98 - 98: OoOO0ooOOoo0O . II1
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_UNSORTED )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_DATE )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_GENRE )
except :
 pass
 if 54 - 54: OOO0O0O0ooooo / O0oO % i11Ii11I1Ii1i * O00ooooo00 * OOO0O0O0ooooo
o0oo0Ooooo0 = OOOO0oOo00O ( )
if 48 - 48: ii11ii1ii . OoOO0ooOOoo0O % OOooOOo - OOooOOo
iIi1iIiii111 = None
oOOoO0O0O0 = None
i1I11ii = None
I1II1I11I1I = None
oo0oo0O0 = None
o0oo0o0O00OO = oo0o0O00
I1II1I11I1I = None
i1IiI1Iiii = None
OoOOooOOO0 = None
if 87 - 87: O0oO / o0oO0 - IiIIi1I1Iiii
try :
 iIi1iIiii111 = urllib . unquote_plus ( o0oo0Ooooo0 [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 oOOoO0O0O0 = urllib . unquote_plus ( o0oo0Ooooo0 [ "name" ] )
except :
 pass
try :
 oo0oo0O0 = urllib . unquote_plus ( o0oo0Ooooo0 [ "iconimage" ] )
except :
 pass
try :
 o0oo0o0O00OO = urllib . unquote_plus ( o0oo0Ooooo0 [ "fanart" ] )
except :
 pass
try :
 i1I11ii = int ( o0oo0Ooooo0 [ "mode" ] )
except :
 pass
try :
 I1II1I11I1I = eval ( urllib . unquote_plus ( o0oo0Ooooo0 [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 i1IiI1Iiii = int ( o0oo0Ooooo0 [ "fav_mode" ] )
except :
 pass
try :
 OoOOooOOO0 = o0oo0Ooooo0 [ "regexs" ]
except :
 pass
 if 56 - 56: OOO0O0O0ooooo
i1IIiiiii ( "Mode: " + str ( i1I11ii ) )
if 45 - 45: OOooOOo - Ooo00oOo00o - OOooOOo
if 41 - 41: IiIIi1I1Iiii / O00ooooo00 / IiIIi1I1Iiii - IIII . ii11ii1ii
if not iIi1iIiii111 is None :
 i1IIiiiii ( "URL: " + str ( iIi1iIiii111 . encode ( 'utf-8' ) ) )
i1IIiiiii ( "Name: " + str ( oOOoO0O0O0 ) )
if 65 - 65: OOO0O0O0ooooo * i11iIiiIii . II1 / IIiIiII11i / IIII
if i1I11ii == None :
 o00 ( )
 i1IIiiiii ( "getSources" )
 Ii11iI1i ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 69 - 69: i11Ii11I1Ii1i % i11Ii11I1Ii1i
elif i1I11ii == 1 :
 i1IIiiiii ( "getData" )
 ooOoo0O = None
 if OoOOooOOO0 :
  ooOoo0O = oOIIiIi ( OoOOooOOO0 , iIi1iIiii111 )
  iIi1iIiii111 = ''
  if 76 - 76: i11iIiiIii * IIII / Ooo00oOo00o % OoOO + o0000oOoOoO0o
 iiii ( iIi1iIiii111 , o0oo0o0O00OO , ooOoo0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 48 - 48: IIii1I % O00ooooo00 + OOooOOo % ii11ii1ii
elif i1I11ii == 2 :
 i1IIiiiii ( "getChannelItems" )
 OOOOoo0Oo ( oOOoO0O0O0 , iIi1iIiii111 , o0oo0o0O00OO )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 79 - 79: OOooOOo % IIiIiII11i % oO0o0ooO0 / O00ooooo00 % Ooo00oOo00o
elif i1I11ii == 3 :
 i1IIiiiii ( "getSubChannelItems" )
 I1Ii ( oOOoO0O0O0 , iIi1iIiii111 , o0oo0o0O00OO )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 56 - 56: IIii1I - i11iIiiIii * IIII
elif i1I11ii == 4 :
 i1IIiiiii ( "getFavorites" )
 i11oooOo ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 84 - 84: o0000oOoOoO0o + oO0o0ooO0 + ii11ii1ii
elif i1I11ii == 5 :
 i1IIiiiii ( "addFavorite" )
 try :
  oOOoO0O0O0 = oOOoO0O0O0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOOoO0O0O0 = oOOoO0O0O0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 oOOooi1I1iIii11 ( oOOoO0O0O0 , iIi1iIiii111 , oo0oo0O0 , o0oo0o0O00OO , i1IiI1Iiii )
 if 33 - 33: oO0o0ooO0
elif i1I11ii == 6 :
 i1IIiiiii ( "rmFavorite" )
 try :
  oOOoO0O0O0 = oOOoO0O0O0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOOoO0O0O0 = oOOoO0O0O0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 III1II1i ( oOOoO0O0O0 )
 if 93 - 93: i11Ii11I1Ii1i
elif i1I11ii == 7 :
 i1IIiiiii ( "addSource" )
 I1IIIii ( iIi1iIiii111 )
 if 34 - 34: OoOO0ooOOoo0O - i11Ii11I1Ii1i * IiIIi1I1Iiii / ii11ii1ii
elif i1I11ii == 8 :
 i1IIiiiii ( "rmSource" )
 o0O ( oOOoO0O0O0 )
 if 19 - 19: OoOO
elif i1I11ii == 9 :
 i1IIiiiii ( "download_file" )
 oO0o00O0O0oo0 ( oOOoO0O0O0 , iIi1iIiii111 )
 if 46 - 46: IIii1I . i11iIiiIii - OOooOOo % OOO0O0O0ooooo / iIiiiI1IiI1I1 * O00ooooo00
elif i1I11ii == 10 :
 i1IIiiiii ( "getCommunitySources" )
 o0o0oOoOO0 ( )
 if 66 - 66: OOO0O0O0ooooo
elif i1I11ii == 11 :
 i1IIiiiii ( "addSource" )
 I1IIIii ( iIi1iIiii111 )
 if 52 - 52: Ooo00oOo00o * II1
elif i1I11ii == 12 :
 i1IIiiiii ( "setResolvedUrl" )
 if not iIi1iIiii111 . startswith ( "plugin://plugin" ) or not any ( x in iIi1iIiii111 for x in Oo0Ooo ) :
  ii1I = xbmcgui . ListItem ( path = iIi1iIiii111 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1I )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + iIi1iIiii111 + ')' )
  if 12 - 12: OOO0O0O0ooooo + O0oO * O00ooooo00 . Ooo00oOo00o
  if 71 - 71: o0oO0 - ii11ii1ii - o0000oOoOoO0o
elif i1I11ii == 13 :
 i1IIiiiii ( "play_playlist" )
 I1III1i1I ( oOOoO0O0O0 , I1II1I11I1I )
 if 28 - 28: IIii1I
elif i1I11ii == 14 :
 i1IIiiiii ( "get_xml_database" )
 OoOOOOO ( iIi1iIiii111 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 7 - 7: ii11ii1ii % O0oO * OOooOOo
elif i1I11ii == 15 :
 i1IIiiiii ( "browse_xml_database" )
 OoOOOOO ( iIi1iIiii111 , True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 58 - 58: O0oO / o00O0oo + iIiiiI1IiI1I1 % IIII - II1
elif i1I11ii == 16 :
 i1IIiiiii ( "browse_community" )
 o0o0oOoOO0 ( iIi1iIiii111 , browse = True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 25 - 25: OOooOOo % II1 * IiIIi1I1Iiii - O00ooooo00 * iIiiiI1IiI1I1 * OoOO0ooOOoo0O
elif i1I11ii == 17 :
 i1IIiiiii ( "getRegexParsed" )
 if 30 - 30: o00O0oo % OOooOOo / OoOO * OOO0O0O0ooooo * oO0o0ooO0 . IIiIiII11i
 ooOoo0O = None
 if OoOOooOOO0 and 'listrepeat' in urllib . unquote_plus ( OoOOooOOO0 ) :
  OoOiIIiii , O0i11i1iiI1i , oO00O0 , OoOOooOOO0 = oOIIiIi ( OoOOooOOO0 , iIi1iIiii111 )
  if 46 - 46: OOooOOo - OOO0O0O0ooooo
  oOO0OO0OO = ''
  if 70 - 70: o00O0oo + IiIIi1I1Iiii * IIii1I . IIiIiII11i * o00O0oo
  if 49 - 49: ii11ii1ii
  I11iiI = oO00O0 [ 'name' ]
  i1iIii1i111 = OoOOooOOO0 . pop ( I11iiI )
  if 65 - 65: IiIIi1I1Iiii * OOO0O0O0ooooo / oO0o0ooO0 . o0oO0 % IiIIi1I1Iiii
  iIi1iIiii111 = ''
  import copy
  i1Ii1i1 = ''
  for OoOoIiI1 in O0i11i1iiI1i :
   try :
    iiIiII = copy . deepcopy ( OoOOooOOO0 )
    if 7 - 7: IiIIi1I1Iiii - O00ooooo00 . OoOO / IIii1I * ii11ii1ii
    O0O0 = OoOiIIiii
    I11I11i1I = 0
    for I11I11i1I in range ( len ( OoOoIiI1 ) ) :
     if 70 - 70: o0000oOoOoO0o * OoOO0ooOOoo0O / IIiIiII11i * OOooOOo * IIiIiII11i
     if len ( iiIiII ) > 0 :
      for OOoO0o , O00Oo in iiIiII . iteritems ( ) :
       if O00Oo is not None :
        for iiiO0ooO0O0Ooo0o , IIi11IIiIi1i in O00Oo . iteritems ( ) :
         if IIi11IIiIi1i is not None :
          if 20 - 20: O00ooooo00 . OoOO . o0oO0 % O00ooooo00
          if 8 - 8: o00O0oo / II1 / iIiiiI1IiI1I1 / OoOO0ooOOoo0O + iIiiiI1IiI1I1
          if 79 - 79: i11Ii11I1Ii1i
          if 40 - 40: ii11ii1ii + o00O0oo
          if type ( IIi11IIiIi1i ) is dict :
           for OoO000Oo0oO , iiiIiiiI1 in IIi11IIiIi1i . iteritems ( ) :
            if iiiIiiiI1 is not None :
             IIi11IIiIi1i [ OoO000Oo0oO ] = iiiIiiiI1 . replace ( '[' + I11iiI + '.param' + str ( I11I11i1I + 1 ) + ']' , OoOoIiI1 [ I11I11i1I ] . decode ( 'utf-8' ) )
          else :
           O00Oo [ iiiO0ooO0O0Ooo0o ] = IIi11IIiIi1i . replace ( '[' + I11iiI + '.param' + str ( I11I11i1I + 1 ) + ']' , OoOoIiI1 [ I11I11i1I ] . decode ( 'utf-8' ) )
     O0O0 = O0O0 . replace ( '[' + I11iiI + '.param' + str ( I11I11i1I + 1 ) + ']' , OoOoIiI1 [ I11I11i1I ] . decode ( 'utf-8' ) )
     if 50 - 50: i11Ii11I1Ii1i * OOooOOo + OoOO - i11iIiiIii + IiIIi1I1Iiii * OoOO
     if 20 - 20: o0oO0 / ii11ii1ii % OOooOOo
     if 69 - 69: o0oO0 - O00ooooo00 % IIII . o0000oOoOoO0o - o0000oOoOoO0o
    o0oO00o = ''
    if len ( iiIiII ) > 0 :
     o0oO00o = OooIi ( iiIiII , 'lsproroot' )
     o0oO00o = o0oO00o . split ( '<lsproroot>' ) [ 1 ] . split ( '</lsproroot' ) [ 0 ]
     if 78 - 78: IiIIi1I1Iiii * o0oO0 - II1 - Ooo00oOo00o
    i1Ii1i1 += '\n<item>%s\n%s</item>' % ( O0O0 , o0oO00o )
   except : traceback . print_exc ( file = sys . stdout )
   if 83 - 83: i11Ii11I1Ii1i / o0000oOoOoO0o
   if 39 - 39: O0oO + o00O0oo
   if 9 - 9: IIiIiII11i % o00O0oo . IiIIi1I1Iiii * IIiIiII11i
   if 99 - 99: OOO0O0O0ooooo . ii11ii1ii % o00O0oo - IiIIi1I1Iiii / o00O0oo
   if 20 - 20: OOooOOo * IIII
  iiii ( '' , '' , i1Ii1i1 )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 else :
  iIi1iIiii111 , o00o0 = oOIIiIi ( OoOOooOOO0 , iIi1iIiii111 )
  if iIi1iIiii111 :
   if '$PLAYERPROXY$=' in iIi1iIiii111 :
    iIi1iIiii111 , oOOOOoo = iIi1iIiii111 . split ( '$PLAYERPROXY$=' )
    print 'proxy' , oOOOOoo
    i1i1 , I1iiIiIII = oOOOOoo . split ( ':' )
    oOO ( iIi1iIiii111 , oOOoO0O0O0 , oo0oo0O0 , i1i1 , I1iiIiIII )
   else :
    o0OOOOOo0 ( iIi1iIiii111 , oOOoO0O0O0 , oo0oo0O0 , o00o0 )
  else :
   xbmc . executebuiltin ( "XBMC.Notification(Martunis,Failed to extract regex. - " + "this" + ",4000," + oO0o0o0ooO0oO + ")" )
elif i1I11ii == 18 :
 i1IIiiiii ( "youtubedl" )
 try :
  import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(Martunis,Please [COLOR yellow]install Youtube-dl[/COLOR] module ,10000," ")" )
 O0 = youtubedl . single_YD ( iIi1iIiii111 )
 o0OOOOOo0 ( O0 , oOOoO0O0O0 , oo0oo0O0 )
elif i1I11ii == 19 :
 i1IIiiiii ( "Genesiscommonresolvers" )
 o0OOOOOo0 ( I1 ( iIi1iIiii111 ) , oOOoO0O0O0 , oo0oo0O0 , True )
 if 68 - 68: OOO0O0O0ooooo
elif i1I11ii == 21 :
 i1IIiiiii ( "download current file using youtube-dl service" )
 ooOOo0o ( '' , oOOoO0O0O0 , 'video' )
elif i1I11ii == 23 :
 i1IIiiiii ( "get info then download" )
 ooOOo0o ( iIi1iIiii111 , oOOoO0O0O0 , 'video' )
elif i1I11ii == 24 :
 i1IIiiiii ( "Audio only youtube download" )
 ooOOo0o ( iIi1iIiii111 , oOOoO0O0O0 , 'audio' )
elif i1I11ii == 25 :
 i1IIiiiii ( "Searchin Other plugins" )
 Oo000O ( iIi1iIiii111 , oOOoO0O0O0 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1I11ii == 55 :
 i1IIiiiii ( "enabled lock" )
 OO00oo = OOo . getSetting ( 'parentalblockedpin' )
 iiii11I = xbmc . Keyboard ( '' , 'Enter Pin' )
 iiii11I . doModal ( )
 if not ( iiii11I . isConfirmed ( ) == False ) :
  Ooo0OO0oOO = iiii11I . getText ( )
  if Ooo0OO0oOO == OO00oo :
   OOo . setSetting ( 'parentalblocked' , "false" )
   xbmc . executebuiltin ( "XBMC.Notification(Martunis,Parental Block Disabled,5000," + oO0o0o0ooO0oO + ")" )
  else :
   xbmc . executebuiltin ( "XBMC.Notification(Martunis,Wrong Pin??,5000," + oO0o0o0ooO0oO + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1I11ii == 56 :
 i1IIiiiii ( "disable lock" )
 OOo . setSetting ( 'parentalblocked' , "true" )
 xbmc . executebuiltin ( "XBMC.Notification(Martunis,Parental block enabled,5000," + oO0o0o0ooO0oO + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 76 - 76: OoOO
elif i1I11ii == 53 :
 i1IIiiiii ( "Requesting JSON-RPC Items" )
 OO0ooOoOO0OOo ( iIi1iIiii111 )
 if 99 - 99: ii11ii1ii
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
