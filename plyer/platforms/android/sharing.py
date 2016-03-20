'''
Android Sharing
-----------
'''

from jnius import autoclass, cast
from plyer.facades import Sharing
from plyer.platforms.android import activity

Intent = autoclass('android.content.Intent')
uri = autoclass('android.net.Uri')
PythonActivity = autoclass('org.renpy.android.PythonActivity')


class AndroidSharing(Sharing):

    def _share_text(self, **kwargs):

        String = autoclass('java.lang.String')
        extra_text = kwargs.get('extra_text')
        extra_subject = kwargs.get('extra_subject')

        intent = Intent()
        intent.setAction(Intent.ACTION_SEND)
        intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence',
                        String(extra_subject)))
        intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence',
                        String(extra_text)))
        intent.setType('text/plain')

        _Activity = cast('android.app.Activity', PythonActivity.mActivity)
        _Activity.startActivity(intent)


def instance():
    return AndroidSharing()