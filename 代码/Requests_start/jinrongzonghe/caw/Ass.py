import pytest_check as check
class Assert:
    def equal(self,expect,response,key_str):
        try:
            keys=key_str.split(",")
            for key in keys:
                r=str(response[key])
                e=str(expect[key])
                check.equal(r,e)
        except Exception as e:
            print(f"shibai{e}")
            # pass