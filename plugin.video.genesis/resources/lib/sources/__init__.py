# -*- coding: utf-8 -*-

'''
    Genesis Add-on
    Copyright (C) 2015 lambda

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import sys,pkgutil,re,json,urllib,urlparse,random,datetime,time,resolveurl

try: import xbmc
except: pass

try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database

from resources.lib.modules import control
from resources.lib.modules import trakt
from resources.lib.modules import tvmaze
from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import debrid
from resources.lib.modules import workers
from resources.lib.modules import source_utils


class sources:
    def __init__(self):
        self.getConstants()
        self.sources = []


    def play(self, title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, url):
        try:
            if not control.infoLabel('Container.FolderPath').startswith('plugin://'):
                control.playlist.clear()

            control.resolve(int(sys.argv[1]), True, control.item(path=''))
            control.execute('Dialog.Close(okdialog)')
            progress = True

            self.sources = self.getSources(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, progress=progress)
            self.sources = self.sourcesFilter()

            if control.window.getProperty('PseudoTVRunning') == 'True':
                return control.resolve(int(sys.argv[1]), True, control.item(path=str(self.sourcesDirect(progress=progress))))

            if self.sources == []: raise Exception()

            if url == 'direct://':
                url = self.sourcesDirect(progress=progress)
                
            elif url == 'dialog://': 
                url = self.sourcesDialog(progress=progress)
                
            elif not control.infoLabel('Container.FolderPath').startswith('plugin://') and control.setting('autoplay_library') == 'false':
                url = self.sourcesDialog(progress=progress)

            elif control.infoLabel('Container.FolderPath').startswith('plugin://') and control.setting('autoplay') == 'false':
                url = self.sourcesDialog(progress=progress)
                
            else:
                url = self.sourcesDirect(progress=progress)

            if url == None: raise Exception()
            if url == 'close://': return

            control.sleep(200)

            if not tvshowtitle == None: title = tvshowtitle

            from resources.lib.modules.player import player
            player().run(title, year, season, episode, imdb, tvdb, meta, url)

            return url
        except:
            control.infoDialog(control.lang(30501).encode('utf-8'))


    def addItem(self, title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta):
        try:

            self.sources = self.getSources(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered)
            if self.sources == []: raise Exception()
            
            try: self.progressDialog.close()
            except: pass
            
            self.progressDialog = control.progressDialog
            

            self.progressDialog.create(control.addonInfo('name'), '')
            self.progressDialog.update(0, control.lang(30515).encode('utf-8'), str(' '), str(' '))

            self.sources = self.sourcesFilter()

            trailerMenu = control.lang(30516).encode('utf-8') if tvshowtitle == None else control.lang(30517).encode('utf-8')

            infoMenu = control.lang(30502).encode('utf-8') if tvshowtitle == None else control.lang(30503).encode('utf-8')

            downloads = True if control.setting('downloads') == 'true' and not (control.setting('movie.download.path') == '' or control.setting('tv.download.path') == '') else False

            meta = json.loads(meta)

            poster = meta['poster'] if 'poster' in meta else '0'
            banner = meta['banner'] if 'banner' in meta else '0'
            thumb = meta['thumb'] if 'thumb' in meta else poster
            fanart = meta['fanart'] if 'fanart' in meta else '0'

            if poster == '0': poster = control.addonPoster()
            if banner == '0' and poster == '0': banner = control.addonBanner()
            elif banner == '0': banner = poster
            if thumb == '0' and fanart == '0': thumb = control.addonFanart()
            elif thumb == '0': thumb = fanart
            if control.setting('fanart') == 'true' and not fanart == '0': pass
            else: fanart = control.addonFanart()

            systitle = urllib.quote_plus('%s (%s)' % (title, year) if tvshowtitle == None or season == None or episode == None else '%s S%02dE%02d' % (tvshowtitle, int(season), int(episode)))
            sysname = urllib.quote_plus('%s (%s)' % (title, year) if tvshowtitle == None or season == None or episode == None else tvshowtitle)
            sysimage, sysaddon = urllib.quote_plus(poster), sys.argv[0]

            for i in range(len(self.sources)):
                try:
                    if self.progressDialog.iscanceled(): break

                    self.progressDialog.update(int((100 / float(len(self.sources))) * i))

                    label = str(self.sources[i]['label'])

                    syssource = urllib.quote_plus(json.dumps([self.sources[i]]))

                    url = '%s?action=playItem&source=%s' % (sysaddon, syssource)

                    cm = []
                    cm.append((control.lang(30504).encode('utf-8'), 'RunPlugin(%s?action=queueItem)' % sysaddon))

                    if downloads == True:
                        cm.append((control.lang(30505).encode('utf-8'), 'RunPlugin(%s?action=download&name=%s&image=%s&source=%s)' % (sysaddon, systitle, sysimage, syssource)))

                    cm.append((trailerMenu, 'RunPlugin(%s?action=trailer&name=%s)' % (sysaddon, sysname)))
                    cm.append((infoMenu, 'Action(Info)'))
                    cm.append((control.lang(30506).encode('utf-8'), 'RunPlugin(%s?action=refresh)' % sysaddon))
                    cm.append((control.lang(30507).encode('utf-8'), 'RunPlugin(%s?action=openSettings)' % sysaddon))
                    cm.append((control.lang(30508).encode('utf-8'), 'RunPlugin(%s?action=openPlaylist)' % sysaddon))

                    item = control.item(label=label, iconImage='DefaultVideo.png', thumbnailImage=thumb)
                    try: item.setArt({'poster': poster, 'tvshow.poster': poster, 'season.poster': poster, 'banner': banner, 'tvshow.banner': banner, 'season.banner': banner})
                    except: pass
                    item.setInfo(type='Video', infoLabels = meta)
                    if not fanart == None: item.setProperty('Fanart_Image', fanart)
                    item.setProperty('Video', 'true')
                    item.addContextMenuItems(cm, replaceItems=True)
                    control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
                except:
                    pass

            control.directory(int(sys.argv[1]), cacheToDisc=True)
            try: self.progressDialog.close()
            except: pass
        except:
            control.infoDialog(control.lang(30501).encode('utf-8'))
            try: self.progressDialog.close()
            except: pass


    def playItem(self, source):
        try:
            f = dict(urlparse.parse_qsl(control.infoLabel('Container.FolderPath').replace('?','')))

            meta = f['meta'] if 'meta' in f else None
            title = f['title'] if 'title' in f else None
            title = f['tvshowtitle'] if 'tvshowtitle' in f else title
            year = f['year'] if 'year' in f else None
            season = f['season'] if 'season' in f else None
            episode = f['episode'] if 'episode' in f else None
            imdb = f['imdb'] if 'imdb' in f else None
            tvdb = f['tvdb'] if 'tvdb' in f else None

            next = [] ; prev = [] ; total = []

            for i in range(1,1000):
                try:
                    u = control.infoLabel('ListItem(%s).FolderPath' % str(i))
                    if u in total: raise Exception()
                    total.append(u)
                    u = dict(urlparse.parse_qsl(u.replace('?','')))
                    u = json.loads(u['source'])[0]
                    next.append(u)
                except:
                    break
            for i in range(-1000,0)[::-1]:
                try:
                    u = control.infoLabel('ListItem(%s).FolderPath' % str(i))
                    if u in total: raise Exception()
                    total.append(u)
                    u = dict(urlparse.parse_qsl(u.replace('?','')))
                    u = json.loads(u['source'])[0]
                    prev.append(u)
                except:
                    break

            items = json.loads(source)
            items = [i for i in items+next+prev][:20]

            self.progressDialog = control.progressDialog
            self.progressDialog.create(control.addonInfo('name'), '')
            self.progressDialog.update(0)

            block = None

            for i in range(len(items)):
                try:
                    self.progressDialog.update(int((100 / float(len(items))) * i), str(items[i]['label']), str(' '))

                    if items[i]['source'] == block: raise Exception()

                    w = workers.Thread(self.sourcesResolve, items[i])
                    w.start()

                    m = ''

                    for x in range(3600):
                        if self.progressDialog.iscanceled(): return self.progressDialog.close()
                        if xbmc.abortRequested == True: return sys.exit()
                        k = control.condVisibility('Window.IsActive(virtualkeyboard)')
                        if k: m += '1'; m = m[-1]
                        if (w.is_alive() == False or x > 30) and not k: break
                        time.sleep(0.5)

                    for x in range(30):
                        if m == '': break
                        if self.progressDialog.iscanceled(): return self.progressDialog.close()
                        if xbmc.abortRequested == True: return sys.exit()
                        if w.is_alive() == False: break
                        time.sleep(0.5)


                    if w.is_alive() == True: block = items[i]['source']

                    if self.url == None: raise Exception()

                    try: self.progressDialog.close()
                    except: pass

                    control.sleep(200)

                    from resources.lib.modules.player import player
                    player().run(title, year, season, episode, imdb, tvdb, meta, self.url)

                    return self.url
                except:
                    pass

            try: self.progressDialog.close()
            except: pass

            raise Exception()

        except:
            control.infoDialog(control.lang(30501).encode('utf-8'))
            pass


    def getSources(self, title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, quality='HD', timeout=30, progress=True):
        sourceDict = []
        control.makeFile(control.dataPath)
        self.sourceFile = control.sourcescacheFile
        
        sourceDict = self.sourceDict
        
        content = 'movie' if tvshowtitle == None else 'episode'
        if content == 'movie':
            sourceDict = [(i[0], i[1], getattr(i[1], 'movie', None)) for i in sourceDict]
            genres = trakt.getGenre('movie', 'imdb', imdb)
        else:
            sourceDict = [(i[0], i[1], getattr(i[1], 'tvshow', None)) for i in sourceDict]
            genres = trakt.getGenre('show', 'tvdb', tvdb)
        sourceDict = [(i[0], i[1], i[2]) for i in sourceDict if not hasattr(i[1], 'genre_filter') or not i[1].genre_filter or any(x in i[1].genre_filter for x in genres)]
        sourceDict = [(i[0], i[1]) for i in sourceDict if not i[2] == None]

        language = self.getLanguage()
        sourceDict = [(i[0], i[1], i[1].language) for i in sourceDict]
        sourceDict = [(i[0], i[1]) for i in sourceDict if any(x in i[2] for x in language)]
        

        sourceDict = [(i[0], i[1], i[1].priority) for i in sourceDict]

        random.shuffle(sourceDict)
        sourceDict = sorted(sourceDict, key=lambda i: i[2])

        threads = []

        if content == 'movie':
            title = cleantitle.normalize(title)
            localtitle = self.getLocalTitle(title, imdb, tvdb, content)
            aliases = self.getAliasTitles(imdb, localtitle, content)
            for i in sourceDict: threads.append(workers.Thread(self.getMovieSource, title, localtitle, aliases, year, imdb, i[0], i[1]))
        else:
            tvshowtitle = cleantitle.normalize(tvshowtitle)
            localtvshowtitle = self.getLocalTitle(tvshowtitle, imdb, tvdb, content)
            aliases = self.getAliasTitles(imdb, localtvshowtitle, content)
            #Disabled on 11/11/17 due to hang. Should be checked in the future and possible enabled again.
            #season, episode = thexem.get_scene_episode_number(tvdb, season, episode)
            for i in sourceDict: threads.append(workers.Thread(self.getEpisodeSource, title, year, imdb, tvdb, season, episode, tvshowtitle, localtvshowtitle, aliases, premiered, i[0], i[1]))

        s = [i[0] + (i[1],) for i in zip(sourceDict, threads)]
        s = [(i[3].getName(), i[0], i[2]) for i in s]

        mainsourceDict = [i[0] for i in s if i[2] == 0]
        sourcelabelDict = dict([(i[0], i[1].upper()) for i in s])

        [i.start() for i in threads]

        control.idle()
        
        try: timeout = int(control.setting('sources_timeout_40'))
        except: pass
        
        self.progressDialog = control.progressDialog
        self.progressDialog.create(control.addonInfo('name'), '')
        self.progressDialog.update(0)

            

        string1 = control.lang(30512).encode('utf-8')
        string2 = control.lang(30513).encode('utf-8')
        string3 = control.lang(30514).encode('utf-8')
        
        string4 = 'Total'
        string5 = 'Waiting for'
        string6 = 'Paid'
        string7 = 'Free'
        
        quality = control.setting('playback_quality')
        if quality == '': quality = '0'
        
        line1 = line2 = line3 = ""

        source_4k = d_source_4k = 0
        source_1080 = d_source_1080 = 0
        source_720 = d_source_720 = 0
        source_sd = d_source_sd = 0
        total = d_total = 0
        
        debrid_list = debrid.debrid_resolvers
        debrid_status = debrid.status()
        
        total_format = '[COLOR %s][B]%s[/B][/COLOR]'
        pdiag_format = ' 4K: %s | 1080p: %s | 720p: %s | SD: %s | %s: %s'.split('|')
        
        for i in range(0, 4 * timeout):

            try:
                if xbmc.abortRequested == True: return sys.exit()

                try:
                    if self.progressDialog.iscanceled(): break
                except:
                    pass

                if len(self.sources) > 0:
                    if quality in ['0']:
                        source_4k = len([e for e in self.sources if e['quality'] == '4K' and e['debridonly'] == False])
                        source_1080 = len([e for e in self.sources if e['quality'] in ['1440p','1080p'] and e['debridonly'] == False])
                        source_720 = len([e for e in self.sources if e['quality'] in ['720p','HD'] and e['debridonly'] == False])
                        source_sd = len([e for e in self.sources if e['quality'] == 'SD' and e['debridonly'] == False])
                    elif quality in ['1']:
                        source_1080 = len([e for e in self.sources if e['quality'] in ['1440p','1080p'] and e['debridonly'] == False])
                        source_720 = len([e for e in self.sources if e['quality'] in ['720p','HD'] and e['debridonly'] == False])
                        source_sd = len([e for e in self.sources if e['quality'] == 'SD' and e['debridonly'] == False])
                    elif quality in ['2']:
                        source_1080 = len([e for e in self.sources if e['quality'] in ['1080p'] and e['debridonly'] == False])
                        source_720 = len([e for e in self.sources if e['quality'] in ['720p','HD'] and e['debridonly'] == False])
                        source_sd = len([e for e in self.sources if e['quality'] == 'SD' and e['debridonly'] == False])
                    elif quality in ['3']:
                        source_720 = len([e for e in self.sources if e['quality'] in ['720p','HD'] and e['debridonly'] == False])
                        source_sd = len([e for e in self.sources if e['quality'] == 'SD' and e['debridonly'] == False])
                    else:
                        source_sd = len([e for e in self.sources if e['quality'] == 'SD' and e['debridonly'] == False])

                    total = source_4k + source_1080 + source_720 + source_sd

                    if debrid_status:
                        if quality in ['0']:
                            for d in debrid_list:
                                d_source_4k = len([e for e in self.sources if e['quality'] == '4K' and d.valid_url('', e['source'])])
                                d_source_1080 = len([e for e in self.sources if e['quality'] in ['1440p','1080p'] and d.valid_url('', e['source'])])
                                d_source_720 = len([e for e in self.sources if e['quality'] in ['720p','HD'] and d.valid_url('', e['source'])])
                                d_source_sd = len([e for e in self.sources if e['quality'] == 'SD' and d.valid_url('', e['source'])])
                        elif quality in ['1']:
                            for d in debrid_list:
                                d_source_1080 = len([e for e in self.sources if e['quality'] in ['1440p','1080p'] and d.valid_url('', e['source'])])
                                d_source_720 = len([e for e in self.sources if e['quality'] in ['720p','HD'] and d.valid_url('', e['source'])])
                                d_source_sd = len([e for e in self.sources if e['quality'] == 'SD' and d.valid_url('', e['source'])])
                        elif quality in ['2']:
                            for d in debrid_list:
                                d_source_1080 = len([e for e in self.sources if e['quality'] in ['1080p'] and d.valid_url('', e['source'])])
                                d_source_720 = len([e for e in self.sources if e['quality'] in ['720p','HD'] and d.valid_url('', e['source'])])
                                d_source_sd = len([e for e in self.sources if e['quality'] == 'SD' and d.valid_url('', e['source'])])
                        elif quality in ['3']:
                            for d in debrid_list:
                                d_source_720 = len([e for e in self.sources if e['quality'] in ['720p','HD'] and d.valid_url('', e['source'])])
                                d_source_sd = len([e for e in self.sources if e['quality'] == 'SD' and d.valid_url('', e['source'])])
                        else:
                            for d in debrid_list:
                                d_source_sd = len([e for e in self.sources if e['quality'] == 'SD' and d.valid_url('', e['source'])])
                                 
                        d_total = d_source_4k + d_source_1080 + d_source_720 + d_source_sd

                if debrid_status:
                    d_4k_label = total_format % ('orange', d_source_4k) if d_source_4k == 0 else total_format % ('lime', d_source_4k)
                    d_1080_label = total_format % ('orange', d_source_1080) if d_source_1080 == 0 else total_format % ('lime', d_source_1080)
                    d_720_label = total_format % ('orange', d_source_720) if d_source_720 == 0 else total_format % ('lime', d_source_720)
                    d_sd_label = total_format % ('orange', d_source_sd) if d_source_sd == 0 else total_format % ('lime', d_source_sd)
                    d_total_label = total_format % ('orange', d_total) if d_total == 0 else total_format % ('lime', d_total)

                source_4k_label = total_format % ('orange', source_4k) if source_4k == 0 else total_format % ('lime', source_4k)
                source_1080_label = total_format % ('orange', source_1080) if source_1080 == 0 else total_format % ('lime', source_1080)
                source_720_label = total_format % ('orange', source_720) if source_720 == 0 else total_format % ('lime', source_720)
                source_sd_label = total_format % ('orange', source_sd) if source_sd == 0 else total_format % ('lime', source_sd)
                source_total_label = total_format % ('orange', total) if total == 0 else total_format % ('lime', total)

                if (i / 2) < timeout:
                    try:
                        mainleft = [sourcelabelDict[x.getName()] for x in threads if x.is_alive() == True and x.getName() in mainsourceDict]
                        info = [sourcelabelDict[x.getName()] for x in threads if x.is_alive() == True]
                        if i >= timeout and len(mainleft) == 0 and len(self.sources) >= 100 * len(info): break # improve responsiveness
                        if debrid_status:
                            if quality in ['0']:

                                line1 = ('%s:' + '|'.join(pdiag_format)) % (string6, d_4k_label, d_1080_label, d_720_label, d_sd_label, str(string4), d_total_label)
                                line2 = ('%s:' + '|'.join(pdiag_format)) % (string7, source_4k_label, source_1080_label, source_720_label, source_sd_label, str(string4), source_total_label)
                                print line1, line2
                        
                            elif quality in ['1']:
                                line1 = ('%s:' + '|'.join(pdiag_format[1:])) % (string6, d_1080_label, d_720_label, d_sd_label, str(string4), d_total_label)
                                line2 = ('%s:' + '|'.join(pdiag_format[1:])) % (string7, source_1080_label, source_720_label, source_sd_label, str(string4), source_total_label)
                                
                            elif quality in ['2']:
                                
                                line1 = ('%s:' + '|'.join(pdiag_format[1:])) % (string6, d_1080_label, d_720_label, d_sd_label, str(string4), d_total_label)
                                line2 = ('%s:' + '|'.join(pdiag_format[1:])) % (string7, source_1080_label, source_720_label, source_sd_label, str(string4), source_total_label)
                                
                            elif quality in ['3']:
                                line1 = ('%s:' + '|'.join(pdiag_format[2:])) % (string6, d_720_label, d_sd_label, str(string4), d_total_label)
                                line2 = ('%s:' + '|'.join(pdiag_format[2:])) % (string7, source_720_label, source_sd_label, str(string4), source_total_label)
                               
                            else:
                                line1 = ('%s:' + '|'.join(pdiag_format[3:])) % (string6, d_sd_label, str(string4), d_total_label)
                                line2 = ('%s:' + '|'.join(pdiag_format[3:])) % (string7, source_sd_label, str(string4), source_total_label)
                                
                        else:
                            if quality in ['0']:
                                line1 = '|'.join(pdiag_format) % (source_4k_label, source_1080_label, source_720_label, source_sd_label, str(string4), source_total_label)
                            elif quality in ['1']:
                                line1 = '|'.join(pdiag_format[1:]) % (source_1080_label, source_720_label, source_sd_label, str(string4), source_total_label)
                            elif quality in ['2']:
                                line1 = '|'.join(pdiag_format[1:]) % (source_1080_label, source_720_label, source_sd_label, str(string4), source_total_label)
                            elif quality in ['3']:
                                line1 = '|'.join(pdiag_format[2:]) % (source_720_label, source_sd_label, str(string4), source_total_label)
                            else:
                                line1 = '|'.join(pdiag_format[3:]) % (source_sd_label, str(string4), source_total_label)

                        if debrid_status:
                            if len(info) > 6: line3 = string3 % (str(len(info)))
                            elif len(info) > 0: line3 = string3 % (', '.join(info))
                            else: break
                            percent = int(100 * float(i) / (2 * timeout) + 0.5)
                            self.progressDialog.update(max(1, percent), line1, line2, line3)
                        else:
                            if len(info) > 6: line2 = string3 % (str(len(info)))
                            elif len(info) > 0: line2 = string3 % (', '.join(info))
                            else: break
                            percent = int(100 * float(i) / (2 * timeout) + 0.5)
                            self.progressDialog.update(max(1, percent), line1, line2)
                    except Exception as e:
                        print e
                else:
                    try:
                        mainleft = [sourcelabelDict[x.getName()] for x in threads if x.is_alive() == True and x.getName() in mainsourceDict]
                        info = mainleft
                        if debrid_status:
                            if len(info) > 6: line3 = 'Waiting for: %s' % (str(len(info)))
                            elif len(info) > 0: line3 = 'Waiting for: %s' % (', '.join(info))
                            else: break
                            percent = int(100 * float(i) / (2 * timeout) + 0.5) % 100
                            self.progressDialog.update(max(1, percent), line1, line2, line3)
                        else:
                            if len(info) > 6: line2 = 'Waiting for: %s' % (str(len(info)))
                            elif len(info) > 0: line2 = 'Waiting for: %s' % (', '.join(info))
                            else: break
                            percent = int(100 * float(i) / (2 * timeout) + 0.5) % 100
                            self.progressDialog.update(max(1, percent), line1, line2)
                    except:
                        break
                        
                time.sleep(0.5)
            except:
                pass

        try: self.progressDialog.close()
        except: pass

        return self.sources
        
    def checkSources(self, title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, quality='HD', timeout=30, progress=True):
        sourceDict = []
        control.makeFile(control.dataPath)
        self.sourceFile = control.sourcescacheFile
        sourceDict = self.sourceDict
        
        content = 'movie' if tvshowtitle == None else 'episode'
        if content == 'movie':
            sourceDict = [(i[0], i[1], getattr(i[1], 'movie', None)) for i in sourceDict]
            genres = trakt.getGenre('movie', 'imdb', imdb)
        else:
            sourceDict = [(i[0], i[1], getattr(i[1], 'tvshow', None)) for i in sourceDict]
            genres = trakt.getGenre('show', 'tvdb', tvdb)
        sourceDict = [(i[0], i[1], i[2]) for i in sourceDict if not hasattr(i[1], 'genre_filter') or not i[1].genre_filter or any(x in i[1].genre_filter for x in genres)]
        sourceDict = [(i[0], i[1]) for i in sourceDict if not i[2] == None]

        language = self.getLanguage()
        sourceDict = [(i[0], i[1], i[1].language) for i in sourceDict]
        sourceDict = [(i[0], i[1]) for i in sourceDict if any(x in i[2] for x in language)]
        

        sourceDict = [(i[0], i[1], i[1].priority) for i in sourceDict]

        random.shuffle(sourceDict)
        sourceDict = sorted(sourceDict, key=lambda i: i[2])

        threads = []

        if content == 'movie':
            title = cleantitle.normalize(title)
            localtitle = self.getLocalTitle(title, imdb, tvdb, content)
            aliases = self.getAliasTitles(imdb, localtitle, content)
            for i in sourceDict: threads.append(workers.Thread(self.getMovieSource, title, localtitle, aliases, year, imdb, i[0], i[1]))
        else:
            tvshowtitle = cleantitle.normalize(tvshowtitle)
            localtvshowtitle = self.getLocalTitle(tvshowtitle, imdb, tvdb, content)
            aliases = self.getAliasTitles(imdb, localtvshowtitle, content)
            #Disabled on 11/11/17 due to hang. Should be checked in the future and possible enabled again.
            #season, episode = thexem.get_scene_episode_number(tvdb, season, episode)
            for i in sourceDict: threads.append(workers.Thread(self.getEpisodeSource, title, year, imdb, tvdb, season, episode, tvshowtitle, localtvshowtitle, aliases, premiered, i[0], i[1]))


        [i.start() for i in threads]
        
        try: timeout = int(control.setting('sources_timeout_40'))
        except: pass

        for i in range(0, timeout * 2):
            try:
                if xbmc.abortRequested == True: return sys.exit()

                if len(self.sources) >= 5: break

                is_alive = [x.is_alive() for x in threads]
                if all(x == False for x in is_alive): break
                time.sleep(0.5)
            except:
                pass

        if len(self.sources) >= 5: return True
        else: return False


    def getMovieSource(self, title, localtitle, aliases, year, imdb, source, call):
        try:
            dbcon = database.connect(self.sourceFile)
            dbcur = dbcon.cursor()
            dbcur.execute("CREATE TABLE IF NOT EXISTS rel_url (""source TEXT, ""imdb_id TEXT, ""season TEXT, ""episode TEXT, ""rel_url TEXT, ""UNIQUE(source, imdb_id, season, episode)"");")
            dbcur.execute("CREATE TABLE IF NOT EXISTS rel_src (""source TEXT, ""imdb_id TEXT, ""season TEXT, ""episode TEXT, ""hosts TEXT, ""added TEXT, ""UNIQUE(source, imdb_id, season, episode)"");")
        except:
            pass

        try:
            sources = []
            dbcur.execute("SELECT * FROM rel_src WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            match = dbcur.fetchone()
            t1 = int(re.sub('[^0-9]', '', str(match[5])))
            t2 = int(datetime.datetime.now().strftime("%Y%m%d%H%M"))
            update = abs(t2 - t1) > 60
            if update == False:
                sources = eval(match[4].encode('utf-8'))
                return self.sources.extend(sources)
        except:
            pass

        try:
            url = None
            dbcur.execute("SELECT * FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            url = dbcur.fetchone()
            url = eval(url[4].encode('utf-8'))
        except:
            pass

        try:
            if url == None: url = call.movie(imdb, title, localtitle, aliases, year)
            if url == None: raise Exception()
            dbcur.execute("DELETE FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            dbcur.execute("INSERT INTO rel_url Values (?, ?, ?, ?, ?)", (source, imdb, '', '', repr(url)))
            dbcon.commit()
        except:
            pass

        try:
            sources = []
            sources = call.sources(url, self.hostDict, self.hostprDict)
            if sources == None: sources = []
            sources = [json.loads(t) for t in set(json.dumps(d, sort_keys=True) for d in sources)]
            for i in sources: i.update({'provider': source})
            self.sources.extend(sources)
            dbcur.execute("DELETE FROM rel_src WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            dbcur.execute("INSERT INTO rel_src Values (?, ?, ?, ?, ?, ?)", (source, imdb, '', '', repr(sources), datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
            dbcon.commit()
        except:
            pass


    def getEpisodeSource(self, title, year, imdb, tvdb, season, episode, tvshowtitle, localtvshowtitle, aliases, premiered, source, call):
        try:
            dbcon = database.connect(self.sourceFile)
            dbcur = dbcon.cursor()
            dbcur.execute("CREATE TABLE IF NOT EXISTS rel_url (""source TEXT, ""imdb_id TEXT, ""season TEXT, ""episode TEXT, ""rel_url TEXT, ""UNIQUE(source, imdb_id, season, episode)"");")
            dbcur.execute("CREATE TABLE IF NOT EXISTS rel_src (""source TEXT, ""imdb_id TEXT, ""season TEXT, ""episode TEXT, ""hosts TEXT, ""added TEXT, ""UNIQUE(source, imdb_id, season, episode)"");")
        except:
            pass

        try:
            sources = []
            dbcur.execute("SELECT * FROM rel_src WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, season, episode))
            match = dbcur.fetchone()
            t1 = int(re.sub('[^0-9]', '', str(match[5])))
            t2 = int(datetime.datetime.now().strftime("%Y%m%d%H%M"))
            update = abs(t2 - t1) > 60
            if update == False:
                sources = eval(match[4].encode('utf-8'))
                return self.sources.extend(sources)
        except:
            pass

        try:
            url = None
            dbcur.execute("SELECT * FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            url = dbcur.fetchone()
            url = eval(url[4].encode('utf-8'))
        except:
            pass

        try:
            if url == None: url = call.tvshow(imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year)
            if url == None: raise Exception()
            dbcur.execute("DELETE FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            dbcur.execute("INSERT INTO rel_url Values (?, ?, ?, ?, ?)", (source, imdb, '', '', repr(url)))
            dbcon.commit()
        except:
            pass

        try:
            ep_url = None
            dbcur.execute("SELECT * FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, season, episode))
            ep_url = dbcur.fetchone()
            ep_url = eval(ep_url[4].encode('utf-8'))
        except:
            pass

        try:
            if url == None: raise Exception()
            if ep_url == None: ep_url = call.episode(url, imdb, tvdb, title, premiered, season, episode)
            if ep_url == None: raise Exception()
            dbcur.execute("DELETE FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, season, episode))
            dbcur.execute("INSERT INTO rel_url Values (?, ?, ?, ?, ?)", (source, imdb, season, episode, repr(ep_url)))
            dbcon.commit()
        except:
            pass

        try:
            sources = []
            sources = call.sources(ep_url, self.hostDict, self.hostprDict)
            if sources == None: sources = []
            sources = [json.loads(t) for t in set(json.dumps(d, sort_keys=True) for d in sources)]
            for i in sources: i.update({'provider': source})
            self.sources.extend(sources)
            dbcur.execute("DELETE FROM rel_src WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, season, episode))
            dbcur.execute("INSERT INTO rel_src Values (?, ?, ?, ?, ?, ?)", (source, imdb, season, episode, repr(sources), datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
            dbcon.commit()
        except:
            pass


    def alterSources(self, url, meta):
        try:
            setting = control.setting('autoplay')
            if setting == 'false': url += '&url=direct://'
            else: url += '&url=dialog://'

            control.execute('RunPlugin(%s)' % url)
        except:
            pass


    def clearSources(self):
        try:
            control.idle()

            yes = control.yesnoDialog(control.lang(30510).encode('utf-8'), '', '')
            if not yes: return

            control.makeFile(control.dataPath)
            dbcon = database.connect(control.providercacheFile)
            dbcur = dbcon.cursor()
            dbcur.execute("DROP TABLE IF EXISTS rel_src")
            dbcur.execute("VACUUM")
            dbcon.commit()

            control.infoDialog(control.lang(30511).encode('utf-8'))
        except:
            pass

   
    def sourcesFilter(self):

        quality = control.setting('playback_quality')
        if quality == '': quality = '0'

        captcha = control.setting('playback_captcha_hosts')
        
        playback_1080p = control.setting('playback_1080p_hosts')

        playback_720p = control.setting('playback_720p_hosts')

        HEVC = control.setting('HEVC')

        random.shuffle(self.sources)

        #if provider == 'true':
        self.sources = sorted(self.sources, key=lambda k: k['provider'])

        for i in self.sources:
            if 'checkquality' in i and i['checkquality'] == True:
                if not i['source'].lower() in self.hosthqDict and i['quality'] not in ['SD', 'SCR', 'CAM']: i.update({'quality': 'SD'})
        
        local = [i for i in self.sources if 'local' in i and i['local'] == True]
        for i in local: i.update({'language': self._getPrimaryLang() or 'en'})
        self.sources = [i for i in self.sources if not i in local]

        filter = []
        filter += [i for i in self.sources if i['direct'] == True]
        filter += [i for i in self.sources if i['direct'] == False]
        self.sources = filter

        filter = []

        for d in debrid.debrid_resolvers:
            valid_hoster = set([i['source'] for i in self.sources])
            valid_hoster = [i for i in valid_hoster if d.valid_url('', i)]
            filter += [dict(i.items() + [('debrid', d.name)]) for i in self.sources if i['source'] in valid_hoster]
  
        filter += [i for i in self.sources if not i['source'].lower() in self.hostprDict and i['debridonly'] == False]

        self.sources = filter
      
        for i in range(len(self.sources)):
            q = self.sources[i]['quality']            
            if q == 'HD': self.sources[i].update({'quality': '720p'})

        filter = []
        filter += local

        if quality in ['0']: filter += [i for i in self.sources if i['quality'] == '4K' and 'debrid' in i]
        if quality in ['0']: filter += [i for i in self.sources if i['quality'] == '4K' and not 'debrid' in i and 'memberonly' in i]
        if quality in ['0']: filter += [i for i in self.sources if i['quality'] == '4K' and not 'debrid' in i and not 'memberonly' in i]

        if quality in ['0', '1']: filter += [i for i in self.sources if i['quality'] == '1440p' and 'debrid' in i]
        if quality in ['0', '1']: filter += [i for i in self.sources if i['quality'] == '1440p' and not 'debrid' in i and 'memberonly' in i]
        if quality in ['0', '1']: filter += [i for i in self.sources if i['quality'] == '1440p' and not 'debrid' in i and not 'memberonly' in i]

        if quality in ['0', '1', '2'] and playback_1080p == 'true': filter += [i for i in self.sources if i['quality'] == '1080p' and 'debrid' in i]
        if quality in ['0', '1', '2'] and playback_1080p == 'true': filter += [i for i in self.sources if i['quality'] == '1080p' and not 'debrid' in i and 'memberonly' in i]
        if quality in ['0', '1', '2'] and playback_1080p == 'true': filter += [i for i in self.sources if i['quality'] == '1080p' and not 'debrid' in i and not 'memberonly' in i]

        if quality in ['0', '1', '2', '3'] and playback_720p == 'true': filter += [i for i in self.sources if i['quality'] == '720p' and 'debrid' in i]
        if quality in ['0', '1', '2', '3'] and playback_720p == 'true': filter += [i for i in self.sources if i['quality'] == '720p' and not 'debrid' in i and 'memberonly' in i]
        if quality in ['0', '1', '2', '3'] and playback_720p == 'true': filter += [i for i in self.sources if i['quality'] == '720p' and not 'debrid' in i and not 'memberonly' in i]

        filter += [i for i in self.sources if i['quality'] in ['SD', 'SCR', 'CAM']]
        self.sources = filter
        
        multi = [i['language'] for i in self.sources]
        multi = [x for y,x in enumerate(multi) if x not in multi[:y]]
        multi = True if len(multi) > 1 else False

        if multi == True:
            self.sources = [i for i in self.sources if not i['language'] == 'en'] + [i for i in self.sources if i['language'] == 'en']
        
        self.sources = self.sources[:2000]

        extra_info = control.setting('sources.extrainfo')
        
        prem_identify = 'blue'
        
        for i in range(len(self.sources)):
            
            u = self.sources[i]['url']

            p = self.sources[i]['provider']

            q = self.sources[i]['quality']

            s = self.sources[i]['source']
            
            s = s.rsplit('.', 1)[0]

            l = self.sources[i]['language']

            try: f = (' | '.join(['[I]%s [/I]' % info.strip() for info in self.sources[i]['info'].split('|')]))
            except: f = ''

            try: d = self.sources[i]['debrid']
            except: d = self.sources[i]['debrid'] = ''

            if d.lower() == 'real-debrid': d = 'realdebrid'

            if not d == '': label = '%02d | [B]%s | %s[/B] | ' % (int(i+1), d, p)
            else: label = '%02d | [B]%s[/B] | ' % (int(i+1), p)

            if multi == True and not l == 'en': label += '[B]%s[/B] | ' % l

            if q in ['4K', '1440p', '1080p', '720p']: label += '%s | [B][I]%s [/I][/B] | %s' % (s, q, f)
            elif q == 'SD': label += '%s | %s' % (s, f)
            else: label += '%s | %s | [I]%s [/I]' % (s, f, q)
            label = label.replace('| 0 |', '|').replace(' | [I]0 [/I]', '')
            label = re.sub('\[I\]\s+\[/I\]', ' ', label)
            label = re.sub('\|\s+\|', '|', label)
            label = re.sub('\|(?:\s+|)$', '', label)
            
            self.sources[i]['label'] = label.upper()
            
        if captcha == 'false':
            filter = [i for i in self.sources if i['source'].lower() in self.hostcapDict and i['debrid'] == '']
            self.sources = [i for i in self.sources if not i in filter]

        filter = [i for i in self.sources if i['source'].lower() in self.hostblockDict and not 'debrid' in i]
        self.sources = [i for i in self.sources if not i in filter]
            
        self.sources = [i for i in self.sources if 'label' in i]
    
        return self.sources


    def sourcesResolve(self, item):
        try:
            self.url = None

            u = url = item['url']

            d = item['debrid'] ; direct = item['direct']
            local = item.get('local', False)

            provider = item['provider']
            call = [i[1] for i in self.sourceDict if i[0] == provider][0]
            u = url = call.resolve(url)

            if url == None or (not '://' in str(url) and not local): raise Exception()

            if not local:
                url = url[8:] if url.startswith('stack:') else url

                urls = []
                for part in url.split(' , '):
                    u = part
                    if not d == '':
                        part = debrid.resolver(part, d)

                    elif not direct == True:
                        hmf = resolveurl.HostedMediaFile(url=u, include_disabled=True, include_universal=False)
                        if hmf.valid_url() == True: part = hmf.resolve()
                    urls.append(part)

                url = 'stack://' + ' , '.join(urls) if len(urls) > 1 else urls[0]

            if url == False or url == None: raise Exception()

            ext = url.split('?')[0].split('&')[0].split('|')[0].rsplit('.')[-1].replace('/', '').lower()
            if ext == 'rar': raise Exception()

            try: headers = url.rsplit('|', 1)[1]
            except: headers = ''
            headers = urllib.quote_plus(headers).replace('%3D', '=') if ' ' in headers else headers
            headers = dict(urlparse.parse_qsl(headers))


            if url.startswith('http') and '.m3u8' in url:
                result = client.request(url.split('|')[0], headers=headers, output='geturl', timeout='20')
                if result == None: raise Exception()

            elif url.startswith('http'):
                result = client.request(url.split('|')[0], headers=headers, output='chunk', timeout='20')
                if result == None: raise Exception()


            self.url = url
            return url
        except:
            return


    def sourcesDialog(self, progress=True):
        try:
            sources = [{'label': '00 | [B]%s[/B]' % control.lang(30509).encode('utf-8').upper()}] + self.sources

            labels = [i['label'] for i in sources]

            select = control.selectDialog(labels)
            if select == 0: return self.sourcesDirect(progress=progress)
            if select == -1: return 'close://'

            items = [self.sources[select-1]]

            next = [y for x,y in enumerate(self.sources) if x >= select]
            prev = [y for x,y in enumerate(self.sources) if x < select][::-1]

            items = [i for i in items+next+prev][:20]

            if progress == True:
                self.progressDialog = control.progressDialog
                self.progressDialog.create(control.addonInfo('name'), '')
                self.progressDialog.update(0)

            block = None

            for i in range(len(items)):
                try:
                    if progress == True:
                        if self.progressDialog.iscanceled(): break
                        self.progressDialog.update(int((100 / float(len(items))) * i), str(items[i]['label']), str(' '))

                    if items[i]['source'] == block: raise Exception()

                    w = workers.Thread(self.sourcesResolve, items[i])
                    w.start()

                    m = ''

                    for x in range(3600):
                        if progress == True:
                            if self.progressDialog.iscanceled(): return self.progressDialog.close()
                        if xbmc.abortRequested == True: return sys.exit()
                        k = control.condVisibility('Window.IsActive(virtualkeyboard)')
                        if k: m += '1'; m = m[-1]
                        if (w.is_alive() == False or x > 30) and not k: break
                        time.sleep(0.5)

                    for x in range(30):
                        if m == '': break
                        if progress == True:
                            if self.progressDialog.iscanceled(): return self.progressDialog.close()
                        if xbmc.abortRequested == True: return sys.exit()
                        if w.is_alive() == False: break
                        time.sleep(0.5)


                    if w.is_alive() == True: block = items[i]['source']

                    if self.url == None: raise Exception()

                    self.selectedSource = items[i]['label']

                    try: self.progressDialog.close()
                    except: pass

                    return self.url
                except:
                    pass

            try: self.progressDialog.close()
            except: pass

        except:
            try: self.progressDialog.close()
            except: pass

    def getLanguage(self):
        langDict = {'English': ['en'], 'German': ['de'], 'German+English': ['de','en'], 'French': ['fr'], 'French+English': ['fr', 'en'], 'Portuguese': ['pt'], 'Portuguese+English': ['pt', 'en'], 'Polish': ['pl'], 'Polish+English': ['pl', 'en'], 'Korean': ['ko'], 'Korean+English': ['ko', 'en'], 'Russian': ['ru'], 'Russian+English': ['ru', 'en'], 'Spanish': ['es'], 'Spanish+English': ['es', 'en'], 'Greek': ['gr'], 'Italian': ['it'], 'Italian+English': ['it', 'en'], 'Greek+English': ['gr', 'en']}
        name = 'English'
        return langDict.get(name, ['en'])

    def _getPrimaryLang(self):
        langDict = {'English': 'en', 'German': 'de', 'German+English': 'de', 'French': 'fr', 'French+English': 'fr', 'Portuguese': 'pt', 'Portuguese+English': 'pt', 'Polish': 'pl', 'Polish+English': 'pl', 'Korean': 'ko', 'Korean+English': 'ko', 'Russian': 'ru', 'Russian+English': 'ru', 'Spanish': 'es', 'Spanish+English': 'es', 'Italian': 'it', 'Italian+English': 'it', 'Greek': 'gr', 'Greek+English': 'gr'} 
        name = 'English'
        lang = langDict.get(name)
        return lang            

    def getLocalTitle(self, title, imdb, tvdb, content):
        lang = 'en'
        if content == 'movie':
            t = trakt.getMovieTranslation(imdb, lang)
        else:
            t = tvmaze.tvMaze().getTVShowTranslation(tvdb, lang)
        return t or title            
            
    def getAliasTitles(self, imdb, localtitle, content):
        lang = 'en'
        try:
            t = trakt.getMovieAliases(imdb) if content == 'movie' else trakt.getTVShowAliases(imdb)
            t = [i for i in t if i.get('country', '').lower() in [lang, '', 'us'] and i.get('title', '').lower() != localtitle.lower()]
            return t
        except:
            return []


    def sourcesDirect(self, progress=True):
        filter = [i for i in self.sources if i['source'].lower() in self.hostcapDict and i['debrid'] == '']
        self.sources = [i for i in self.sources if not i in filter]

        self.sources = [i for i in self.sources if ('autoplay' in i and i['autoplay'] == True) or not 'autoplay' in i]

        if control.setting("playback_auto_sd") == 'true':
            self.sources = [i for i in self.sources if not i['quality'] in ['4K', '1440p', '1080p', '720p']]

        u = None

        if progress == True:
            self.progressDialog = control.progressDialog
            self.progressDialog.create(control.addonInfo('name'), '')
            self.progressDialog.update(0)

        for i in range(len(self.sources)):
            try:
                if progress == True:
                    if self.progressDialog.iscanceled(): break
                    self.progressDialog.update(int((100 / float(len(self.sources))) * i), str(self.sources[i]['label']), str(' '))

                if xbmc.abortRequested == True: return sys.exit()

                url = self.sourcesResolve(self.sources[i])
                if u == None: u = url
                if not url == None: break
            except:
                pass

        try: self.progressDialog.close()
        except: pass

        return u


    def getConstants(self):
        from resources.lib.sources.scrapers import sources
        self.sourceDict = sources()
        
        try:
            self.hostDict = resolveurl.relevant_resolvers(order_matters=True)
            self.hostDict = [i.domains for i in self.hostDict if not '*' in i.domains]
            self.hostDict = [i.lower() for i in reduce(lambda x, y: x+y, self.hostDict)]
            self.hostDict = [x for y,x in enumerate(self.hostDict) if x not in self.hostDict[:y]]
        except:
            self.hostDict = []

        self.hostprDict = ['1fichier.com', 'oboom.com', 'rapidgator.net', 'rg.to', 'uploaded.net', 'uploaded.to', 'ul.to', 'filefactory.com', 'nitroflare.com', 'turbobit.net', 'uploadrocket.net']

        self.hostcapDict = ['hugefiles', 'kingfiles', 'openload', 'openload.co', 'oload', 'thevideo', 'vidup', 'streamin', 'torba', 'vshare', 'flashx']

        self.hosthqDict = ['gvideo', 'google.com', 'openload.io', 'openload.co', 'oload.tv', 'thevideo.me', 'rapidvideo.com', 'raptu.com', 'filez.tv', 'uptobox.com', 'uptobox.com', 'uptostream.com', 'xvidstage.com', 'streamango.com']

        self.hostblockDict = []


        #self.debridDict = debrid.debridDict()


