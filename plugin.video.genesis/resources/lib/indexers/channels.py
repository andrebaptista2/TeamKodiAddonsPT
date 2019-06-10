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



import sys,re,json,urllib,urllib2,urlparse,datetime
from resources.lib.modules import metacache
from resources.lib.modules import control
from resources.lib.modules import client
from resources.lib.modules import workers
from resources.lib.modules import views

class channels:
    def __init__(self):
        self.list = [] ; self.items = []

        self.uk_datetime = self.uk_datetime()
        self.systime = (self.uk_datetime).strftime('%Y%m%d%H%M%S%f')
        self.imdb_by_query = 'https://www.imdb.com/search/title?title=%s'
        self.lang = control.setting('infoLang') or 'en'


    def get(self): 
        channels = [('01', 'Sky Premiere', '77'), ('02', 'Sky Classics', '69'), ('03', 'Sky Greats', '76'), ('04', 'Sky Family', '72'), ('05', 'Sky Action', '68'), ('06', 'Sky Comedy', '70'), ('07', 'Sky Drama', '71'), ('08', 'Sky Sci Fi', '78'), ('09', 'Sky Indie', '75'), ('10', 'Film4', '43'), ('11', 'TCM', '89')] 
        
        for i in channels:
            dt = datetime.datetime.now()
            if dt.time() < datetime.time(12):
                when = 'am'
            else:
                when = 'pm'
            content = self.getContent('http://tv.fopii.com/tvlisting%s.html' % i[2])
            onnow = re.findall('<span class="txts">%s</span></td><td width="100%s">(.*?)</td>' % (when, '%'), content,re.MULTILINE | re.DOTALL)
            try:
                if '<a' in onnow[-1]:
                    title = onnow[-2].encode('utf-8')
                else:  
                    title = onnow[-1].encode('utf-8')   	
            except:
                title = ' No Data'
            self.list.append({'title': title, 'channel': i[1], 'year': '0', 'genre': '0', 'duration': '0', 'rating': '0', 'votes': '0', 'mpaa': '0', 'director': '0', 'writer': '0', 'cast': '0', 'plot': '0', 'tagline': '0', 'code': title, 'imdb': title, 'tmdb': '0', 'poster': '0'})
            	
        self.meta = []
        total = len(self.list)
        for i in range(0, total): self.list[i].update({'metacache': False})
        self.list = metacache.fetch(self.list, self.lang)

        for r in range(0, total, 40):
            threads = []
            for i in range(r, r+40):
                if i <= total: threads.append(workers.Thread(self.items_list, i))
            [i.start() for i in threads]
            [i.join() for i in threads]

            
            
        self.list = [i for i in self.list if not i['imdb'] == '0']

        if len(self.meta) > 0: metacache.insert(self.meta)

        
        self.channelDirectory(self.list)
        return self.list

    def getContent(self, url):
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            return link
        except:
            return None
            

    def items_list(self, i):
        try:
        
	        url = self.imdb_by_query % (urllib.quote_plus(self.list[i]['title']))
	
	
	        result = client.request(url)
	
	        result = result.replace('\n', ' ')
	
	        items = client.parseDOM(result, 'div', attrs = {'class': 'lister-item .+?'})
	        items += client.parseDOM(result, 'div', attrs = {'class': 'list_item.+?'})
        except:
            return

        try:
            next = client.parseDOM(result, 'a', ret='href', attrs = {'class': '.+?ister-page-nex.+?'})

            if len(next) == 0:
                next = client.parseDOM(result, 'div', attrs = {'class': 'pagination'})[0]
                next = zip(client.parseDOM(next, 'a', ret='href'), client.parseDOM(next, 'a'))
                next = [i[0] for i in next if 'Next' in i[1]]

            next = url.replace(urlparse.urlparse(url).query, urlparse.urlparse(next[0]).query)
            next = client.replaceHTMLCodes(next)
            next = next.encode('utf-8')
        except:
            next = ''

        try:
	        title = client.parseDOM(items[0], 'a')[1]
	        title = client.replaceHTMLCodes(title)
	        title = title.encode('utf-8')
	        self.list[i].update({'title': title})
	
	        year = client.parseDOM(items[0], 'span', attrs = {'class': 'lister-item-year.+?'})[0]
	        try:
	            year = year.encode('utf-8').replace('(','').replace(')','').split(' ')[1]
	        except:
	        	year = year.encode('utf-8').replace('(','').replace(')','')
	        	self.list[i].update({'year': year})
	
	        imdb = client.parseDOM(items[0], 'a', ret='href')[0]
	        imdb = re.findall('(tt\d*)', imdb)[0]
	        imdb = imdb.encode('utf-8')
	        self.list[i].update({'imdb': imdb, 'code': imdb})
	
	        try: poster = client.parseDOM(items[0], 'img', ret='loadlate')[0]
	        except: poster = '0'
	        if '/nopicture/' in poster: poster = '0'
	        poster = re.sub('(?:_SX|_SY|_UX|_UY|_CR|_AL)(?:\d+|_).+?\.', '_SX500.', poster)
	        poster = client.replaceHTMLCodes(poster)
	        poster = poster.encode('utf-8')
	        self.list[i].update({'poster': poster})
	
	        try: genre = client.parseDOM(items[0], 'span', attrs = {'class': 'genre'})[0]
	        except: genre = '0'
	        genre = ' / '.join([i.strip() for i in genre.split(',')])
	        if genre == '': genre = '0'
	        genre = client.replaceHTMLCodes(genre)
	        genre = genre.encode('utf-8')
	
	        self.list[i].update({'genre': genre})
	
	        try: duration = re.findall('(\d+?) min(?:s|)', items[0])[-1]
	        except: duration = '0'
	        duration = duration.encode('utf-8')
	        self.list[i].update({'duration': duration})
	
	        rating = '0'
	        try: rating = client.parseDOM(items[0], 'span', attrs = {'class': 'rating-rating'})[0]
	        except: pass
	        try: rating = client.parseDOM(rating, 'span', attrs = {'class': 'value'})[0]
	        except: rating = '0'
	        try: rating = client.parseDOM(items[0], 'div', ret='data-value', attrs = {'class': '.*?imdb-rating'})[0]
	        except: pass
	        if rating == '' or rating == '-': rating = '0'
	        rating = client.replaceHTMLCodes(rating)
	        rating = rating.encode('utf-8')
	        self.list[i].update({'rating': rating})
	
	        try: votes = client.parseDOM(items[0], 'div', ret='title', attrs = {'class': '.*?rating-list'})[0]
	        except: votes = '0'
	        try: votes = re.findall('\((.+?) vote(?:s|)\)', votes)[0]
	        except: votes = '0'
	        if votes == '': votes = '0'
	        votes = client.replaceHTMLCodes(votes)
	        votes = votes.encode('utf-8')
	        self.list[i].update({'votes': votes})
	
	        try: mpaa = client.parseDOM(items[0], 'span', attrs = {'class': 'certificate'})[0]
	        except: mpaa = '0'
	        if mpaa == '' or mpaa == 'NOT_RATED': mpaa = '0'
	        mpaa = mpaa.replace('_', '-')
	        mpaa = client.replaceHTMLCodes(mpaa)
	        mpaa = mpaa.encode('utf-8')
	        self.list[i].update({'mpaa': mpaa})
	
	        try: director = re.findall('Director(?:s|):(.+?)(?:\||</div>)', items[0])[0]
	        except: director = '0'
	        director = client.parseDOM(director, 'a')
	        director = ' / '.join(director)
	        if director == '': director = '0'
	        director = client.replaceHTMLCodes(director)
	        director = director.encode('utf-8')
	        self.list[i].update({'director': director})
	
	        try: cast = re.findall('Stars(?:s|):(.+?)(?:\||</div>)', items[0])[0]
	        except: cast = '0'
	        cast = client.replaceHTMLCodes(cast)
	        cast = cast.encode('utf-8')
	        cast = client.parseDOM(cast, 'a')
	        if cast == []: cast = '0'
	        self.list[i].update({'cast': cast})
	
	        plot = '0'
	        try: plot = client.parseDOM(items[0], 'p', attrs = {'class': 'text-muted'})[0]
	        except: pass
	        try: plot = client.parseDOM(items[0], 'div', attrs = {'class': 'item_description'})[0]
	        except: pass
	        plot = plot.rsplit('<span>', 1)[0].strip()
	        plot = re.sub('<.+?>|</.+?>', '', plot)
	        if plot == '': plot = '0'
	        plot = client.replaceHTMLCodes(plot)
	        plot = plot.encode('utf-8')                
	        self.list[i].update({'plot': plot})
	        
	        tagline = re.compile('[.!?][\s]{1,2}(?=[A-Z])').split(plot)[0]
	        try: tagline = tagline.encode('utf-8')
	        except: pass
	        
	        self.meta.append({'imdb': imdb, 'tmdb': '0', 'tvdb': '0', 'lang': self.lang, 'item': {'title': title, 'year': year, 'code': imdb, 'imdb': imdb, 'tmdb': '0', 'poster': poster, 'fanart': '0', 'premiered': '0', 'studio': '0', 'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'director': director, 'writer': '0', 'cast': cast, 'plot': plot, 'tagline': tagline}})              
        except:
            pass


    def uk_datetime(self):
        dt = datetime.datetime.utcnow() + datetime.timedelta(hours = 0)
        d = datetime.datetime(dt.year, 4, 1)
        dston = d - datetime.timedelta(days=d.weekday() + 1)
        d = datetime.datetime(dt.year, 11, 1)
        dstoff = d - datetime.timedelta(days=d.weekday() + 1)
        if dston <=  dt < dstoff:
            return dt + datetime.timedelta(hours = 1)
        else:
            return dt


    def channelDirectory(self, items):
        if items == None or len(items) == 0: return

        playbackMenu = control.lang(30292).encode('utf-8') if control.setting('autoplay') == 'true' else control.lang(30291).encode('utf-8')

        addonPoster, addonBanner = control.addonPoster(), control.addonBanner()
        addonFanart = control.addonFanart()
        sysaddon = sys.argv[0]


        for i in items:
            try:
                label = '[B]%s[/B] : %s (%s)' % (i['channel'].upper(), i['title'], i['year'])
                sysname = urllib.quote_plus('%s (%s)' % (i['title'], i['year']))
                systitle = urllib.quote_plus(i['title'])
                imdb, year = i['imdb'], i['year']

                poster, banner = i['poster'], i['poster']
                if poster == '0': poster = addonPoster
                if banner == '0' and poster == '0': banner = addonBanner
                elif banner == '0': banner = poster

                meta = dict((k,v) for k, v in i.iteritems() if not v == '0')
                meta.update({'trailer': '%s?action=trailer&name=%s' % (sysaddon, sysname)})
                if i['duration'] == '0': meta.update({'duration': '120'})
                try: meta.update({'duration': str(int(meta['duration']) * 60)})
                except: pass
                sysmeta = urllib.quote_plus(json.dumps(meta))

                url = '%s?action=play&title=%s&year=%s&imdb=%s&meta=%s&t=%s' % (sysaddon, systitle, year, imdb, sysmeta, self.systime)
                sysurl = urllib.quote_plus(url)

                cm = []
                cm.append((playbackMenu, 'RunPlugin(%s?action=alterSources&url=%s&meta=%s)' % (sysaddon, sysurl, sysmeta)))
                cm.append((control.lang(30297).encode('utf-8'), 'RunPlugin(%s?action=trailer&name=%s)' % (sysaddon, sysname)))
                cm.append((control.lang(30293).encode('utf-8'), 'Action(Info)'))
                cm.append((control.lang(30294).encode('utf-8'), 'RunPlugin(%s?action=refresh)' % (sysaddon)))
                cm.append((control.lang(30295).encode('utf-8'), 'RunPlugin(%s?action=openSettings)' % (sysaddon)))
                cm.append((control.lang(30296).encode('utf-8'), 'RunPlugin(%s?action=openPlaylist)' % (sysaddon)))

                item = control.item(label=label, iconImage=poster, thumbnailImage=poster)

                try: item.setArt({'poster': poster, 'banner': banner})
                except: pass

                if not addonFanart == None:
                    item.setProperty('Fanart_Image', addonFanart)
                if not year == '0':
                    item.setInfo(type='Video', infoLabels = meta)
                    item.setProperty('Video', 'true')
                    #item.setProperty('IsPlayable', 'true')
                    item.addContextMenuItems(cm, replaceItems=True)
                    control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            except:
                pass

        control.content(int(sys.argv[1]), 'movies')
        control.directory(int(sys.argv[1]), cacheToDisc=True)
        views.setView('movies', {'skin.confluence': 500})


