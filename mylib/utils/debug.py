import os
import traceback
from contextlib import contextmanager


class DebugMixin(object):
    def _dump_log(self, text):
        if not os.path.exists('/home/cpi/tmp'):
            os.makedirs('/home/cpi/tmp')
        with open('/home/cpi/tmp/test.log', 'a') as fp:
            fp.write('\n%s\n' % text)

    def _dump_error(self):
        self._dump_log(traceback.format_exc())

    @contextmanager
    def _try_debug(self, with_raise=False):
        err = None
        try:
            yield
        except Exception as exp:
            self._dump_error()
            err = exp
        finally:
            if with_raise and err:
                raise err


# EOF
