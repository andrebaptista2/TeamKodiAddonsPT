# -*- coding: utf-8 -*-

"""
ego
"""


import threading
from resources.lib.modules import control,log_utils,trakt


control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))
traktCredentials = trakt.getTraktCredentialsInfo()

try:
    AddonVersion = control.addon('plugin.video.ego').getAddonInfo('version')
    RepoVersion = control.addon('repository.ego').getAddonInfo('version')
    log_utils.log('################### ego ######################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT ego VERSIONS REPORT ##########', log_utils.LOGNOTICE)
    log_utils.log('######### ego PLUGIN VERSION: %s #########' % str(AddonVersion), log_utils.LOGNOTICE)
    log_utils.log('####### ego REPOSITORY VERSION: %s #######' % str(RepoVersion), log_utils.LOGNOTICE)
    log_utils.log('################################################', log_utils.LOGNOTICE)

except:
    log_utils.log('############################# ego ############################', log_utils.LOGNOTICE)
    log_utils.log('################# CURRENT ego VERSIONS REPORT ################', log_utils.LOGNOTICE)
    log_utils.log('# ERROR GETTING ego VERSION - Missing Repo of failed Install #', log_utils.LOGNOTICE)
    log_utils.log('################################################################', log_utils.LOGNOTICE)


def syncTraktLibrary():
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.ego/?action=tvshowsToLibrarySilent&url=traktcollection')
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.ego/?action=moviesToLibrarySilent&url=traktcollection')


def syncTraktWatched():
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.ego/?action=cachesyncTVShows')
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.ego/?action=cachesyncMovies')
    # if control.setting('trakt.notifications') == 'true':
        # control.notification(title = 'default', message = 'Trakt Watched Status Sync Complete', icon='default', time=1, sound=False)


if traktCredentials is True:
    syncTraktWatched()


if control.setting('autoTraktOnStart') == 'true':
    syncTraktLibrary()


if int(control.setting('schedTraktTime')) > 0:
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
    log_utils.log('#################### STARTING TRAKT SCHEDULING ################', log_utils.LOGNOTICE)
    log_utils.log('#################### SCHEDULED TIME FRAME '+ control.setting('schedTraktTime')  + ' HOURS ###############', log_utils.LOGNOTICE)
    timeout = 3600 * int(control.setting('schedTraktTime'))
    schedTrakt = threading.Timer(timeout, syncTraktLibrary)
    schedTrakt.start()



