import configparser
import os
import yaml
class DataRead:
    def get_project_path(self):

        current_file_path=os.path.realpath(__file__)
        print(current_file_path)
        dir_name=os.path.dirname(current_file_path)
        dir_name=os.path.dirname(dir_name)
        return dir_name+"\\"
    def read_ini(self,file_path,key):
        '''
        读取ini文件，返回key对应的value
        file_path:文件路径
        key:key
        :return: key对应的value
        '''
        print(self.get_project_path)
        real_file_path=self.get_project_path()+file_path
        print(real_file_path)
        config=configparser.ConfigParser()
        config.read(real_file_path)#读取ini配置文件
        value=config.get("env",key)#读取[env]里面的key
        return value
    def read_yaml(self,file_path):
        '''
        '''
        real_file_path=self.get_project_path()+file_path
        with open(real_file_path,"r",encoding="utf-8") as f:
            file_content=f.read()
        #用yaml的load转成字典的list
        content=yaml.load(file_content,Loader=yaml.FullLoader)
        print(content)
        return content




if __name__ == "__main__":
    #
    value=DataRead().read_ini(r"data_env\env.ini","url")
    print(value)
    DataRead().read_yaml(r"data_case\register_fail.yaml")
    DataRead().read_yaml(r"data_case\a.yaml")
