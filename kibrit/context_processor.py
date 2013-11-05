from settings import KIBRIT_PATH
from kibrit.base import GitRevision


def revision(request):
    '''
    A context processor to add the "current site" to the current Context
    '''
    try:
        revision = GitRevision(KIBRIT_PATH).revision,
    except:
        revision = ''# an empty string
    return {
            'REVISION': str('?%s'%revision),
            'TAG': revision,
        }