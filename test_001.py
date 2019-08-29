
import allure
class Test_001:

    @allure.step("这是001测试方法")
    def test_001(self):
        print("--test_001")
        assert True
    @allure.step("登录操作")
    def test_002(self):
        print("---test_002")
        allure.attach('用户名','lili')
        allure.attach('密码','123456')
        assert True