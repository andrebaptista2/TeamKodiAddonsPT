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



import json

from resources.lib.modules import control
from resources.lib.modules import trakt


def getMovieIndicators(refresh=False):
    try:
        if trakt.getTraktIndicatorsInfo() == True: raise Exception()
        from metahandler import metahandlers
        indicators = metahandlers.MetaData(preparezip=False)
        return indicators
    except:
        pass
    try:
        if trakt.getTraktIndicatorsInfo() == False: raise Exception()
        if refresh == False: timeout = 720
        elif trakt.getWatchedActivity() < trakt.timeoutsyncMovies(): timeout = 720
        else: timeout = 0
        indicators = trakt.cachesyncMovies(timeout=timeout)
        return indicators
    except:
        pass


def getTVShowIndicators(refresh=False):
    try:
        if trakt.getTraktIndicatorsInfo() == True: raise Exception()
        from metahandler import metahandlers
        indicators = metahandlers.MetaData(preparezip=False)
        return indicators
    except:
        pass
    try:
        if trakt.getTraktIndicatorsInfo() == False: raise Exception()
        if refresh == False: timeout = 720
        elif trakt.getWatchedActivity() < trakt.timeoutsyncTVShows(): timeout = 720
        else: timeout = 0
        indicators = trakt.cachesyncTVShows(timeout=timeout)
        return indicators
    except:
        pass


def getSeasonIndicators(imdb):
    try:
        if trakt.getTraktIndicatorsInfo() == False: raise Exception()
        indicators = trakt.syncSeason(imdb)
        return indicators
    except:
        pass


def getMovieOverlay(indicators, imdb):
    try:
        try:
            playcount = indicators._get_watched('movie', imdb, '', '')
            return str(playcount)
        except:
            playcount = [i for i in indicators if i == imdb]
            playcount = 7 if len(playcount) > 0 else 6
            return str(playcount)
    except:
        return '6'


def getTVShowOverlay(indicators, tvdb):
    try:
        playcount = [i[0] for i in indicators if i[0] == tvdb and len(i[2]) >= int(i[1])]
        playcount = 7 if len(playcount) > 0 else 6
        return str(playcount)
    except:
        return '6'


def getEpisodeOverlay(indicators, imdb, tvdb, season, episode):
    try:
        try:
            playcount = indicators._get_watched_episode({'imdb_id' : imdb, 'season' : season, 'episode': episode, 'premiered' : ''})
            return str(playcount)
        except:
            playcount = [i[2] for i in indicators if i[0] == tvdb]
            playcount = playcount[0] if len(playcount) > 0 else []
            playcount = [i for i in playcount if int(season) == int(i[0]) and int(episode) == int(i[1])]
            playcount = 7 if len(playcount) > 0 else 6
            return str(playcount)
    except:
        return '6'


def markMovieDuringPlayback(imdb, watched):
    try:
        if trakt.getTraktIndicatorsInfo() == False: raise Exception()

        if int(watched) == 7: trakt.markMovieAsWatched(imdb)
        else: trakt.markMovieAsNotWatched(imdb)
        trakt.cachesyncMovies()

        if trakt.getTraktAddonMovieInfo() == True:
            trakt.markMovieAsNotWatched(imdb)
    except:
        pass

    try:
        from metahandler import metahandlers
        metaget = metahandlers.MetaData(preparezip=False)
        metaget.get_meta('movie', name='', imdb_id=imdb)
        metaget.change_watched('movie', name='', imdb_id=imdb, watched=int(watched))
    except:
        pass


def markEpisodeDuringPlayback(imdb, tvdb, season, episode, watched):
    try:
        if trakt.getTraktIndicatorsInfo() == False: raise Exception()

        if int(watched) == 7: trakt.markEpisodeAsWatched(tvdb, season, episode)
        else: trakt.markEpisodeAsNotWatched(tvdb, season, episode)
        trakt.cachesyncTVShows()

        if trakt.getTraktAddonEpisodeInfo() == True:
            trakt.markEpisodeAsNotWatched(tvdb, season, episode)
    except:
        pass

    try:
        from metahandler import metahandlers
        metaget = metahandlers.MetaData(preparezip=False)
        metaget.get_meta('tvshow', name='', imdb_id=imdb)
        metaget.get_episode_meta('', imdb_id=imdb, season=season, episode=episode)
        metaget.change_watched('episode', '', imdb_id=imdb, season=season, episode=episode, watched=int(watched))
    except:
        pass


def movies(title, year, imdb, watched):
    try:
        if trakt.getTraktIndicatorsInfo() == False: raise Exception()
        if int(watched) == 7: trakt.markMovieAsWatched(imdb)
        else: trakt.markMovieAsNotWatched(imdb)
        trakt.cachesyncMovies()
        control.refresh()
    except:
        pass

    try:
        from metahandler import metahandlers
        metaget = metahandlers.MetaData(preparezip=False)
        metaget.get_meta('movie', title ,year=year)
        metaget.change_watched('movie', '', imdb, season='', episode='', year='', watched=watched)
        if trakt.getTraktIndicatorsInfo() == False: control.refresh()
    except:
        pass


def episodes(imdb, tvdb, season, episode, watched):
    try:
        if trakt.getTraktIndicatorsInfo() == False: raise Exception()
        if int(watched) == 7: trakt.markEpisodeAsWatched(tvdb, season, episode)
        else: trakt.markEpisodeAsNotWatched(tvdb, season, episode)
        trakt.cachesyncTVShows()
        control.refresh()
    except:
        pass

    try:
        from metahandler import metahandlers
        metaget = metahandlers.MetaData(preparezip=False)
        metaget.get_meta('tvshow', '', imdb_id=imdb)
        metaget.get_episode_meta('', imdb, season, episode)
        metaget.change_watched('episode', '', imdb, season=season, episode=episode, year='', watched=watched)
        if trakt.getTraktIndicatorsInfo() == False: control.refresh()
    except:
        pass


def tvshows(tvshowtitle, year, imdb, tvdb, season, watched):
    try:
        import sys,xbmc

        if not trakt.getTraktIndicatorsInfo() == False: raise Exception()

        from metahandler import metahandlers
        from resources.lib.indexers import episodes

        metaget = metahandlers.MetaData(preparezip=False)

        dialog = control.progressDialog
        dialog.create(control.addonInfo('name'), str(tvshowtitle))
        dialog.update(0, str(tvshowtitle), control.lang(30451).encode('utf-8') + '...')

        metaget.get_meta('tvshow', '', imdb_id=imdb)

        items = episodes.episodes().get(tvshowtitle, year, imdb, '0', tvdb, '0', idx=False)
        try: items = [i for i in items if int('%01d' % int(season)) == int('%01d' % int(i['season']))]
        except: pass
        items = [{'name': i['name'], 'season': int('%01d' % int(i['season'])), 'episode': int('%01d' % int(i['episode']))} for i in items]

        for i in range(len(items)):
            if xbmc.abortRequested == True: return sys.exit()
            if dialog.iscanceled(): return dialog.close()

            dialog.update(int((100 / float(len(items))) * i), str(tvshowtitle), str(items[i]['name']))

            season, episode = items[i]['season'], items[i]['episode']
            metaget.get_episode_meta('', imdb, season, episode)
            metaget.change_watched('episode', '', imdb, season=season, episode=episode, year='', watched=watched)
            
        try: dialog.close()
        except: pass
    except:
        try: dialog.close()
        except: pass


    try:
        if trakt.getTraktIndicatorsInfo() == False: raise Exception()
        if int(watched) == 7: trakt.markTVShowAsWatched(tvdb)
        else: trakt.markTVShowAsNotWatched(tvdb)
        trakt.cachesyncTVShows()
    except:
        pass

    control.refresh()


