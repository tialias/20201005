### 接口自动化
#### 测试框架选用

-  选用httprunner框架，项目地址:https://github.com/httprunner/httprunner
-  基于Python，Pytest集成的接口测试框架，可使用yaml数据驱动，结合allure生成测试报告

#### 项目启动，在本地运行脚本  

-  拉取项目到本地  
    
        git clone git@github.com:tialias/20201005.git  
    
- 项目所需环境 
 
        python3
        jdk1.8+
        
- 安装项目依赖  

        pip3 install -r requirements.txt
            
- 进入项目根目录，运行测试

        hrun testcases --alluredir=report

- 生成测试报告  

        allure serve report

    
