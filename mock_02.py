import os

class Remove(object):
    def rmdir_1(self, path=r'C:\www'):
        r = os.rmdir(path)
        if r == None:
            return "success"
        else:
            return "fail"

    def exists_get_rmdir(self):
        return self.rmdir_1()

re = Remove()
re.exists_get_rmdir()
#re.rmdir_1()