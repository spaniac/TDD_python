import logging

"""
로깅 시스템
1. Logger 객체를 가져온다.
2. Logger의 output을 설정한다(지금은 콘솔. StreamHandler)
3. Logger의 level을 설정한다.
"""
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result):
        result.testStarted()

        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            result.testFailed()

        self.tearDown()


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        self.log = None
        super(WasRun, self).__init__(name)
        # TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception


class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "setUp testMethod tearDown " == test.log
        # 실제 테스트 코드가 있을 것이고
        # 마지막으로 assert ~~~ 으로 결과 판독할 것.

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def testFailedResultFormatting(self):
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == self.result.summary()

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))

        suite.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()


class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0

    def summary(self):
        # return "%d run, %d failed" % (self.runCount, self.failureCount)
        return "{} run, {} failed".format(self.runCount, self.failureCount)

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failureCount += 1


class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        """
        TestCase.run()에 매개 변수를 추가하게 되면 TestSuite.run()도 똑같은 매개 변수를 추가해야 한다.
        다음과 같은 세 가지 대안이 있다.

        1. 파이썬의 기본 매개 변수 기능 사용 ???
            : 기본값은 런타임이 아닌 컴파일타임에 평가되므로 하나의 TestResult를 재사용할 수 없게 된다.
            (조사 필요)
        2. 메서드를 두 부분으로 나눈다.
            : 하나는 TestResult를 할당하는 부분, 또 하나는 할당된 TestResult를 가지고 테스트를 수행하는 부분.
            그런데 이 두 부분에 대한 좋은 이름이 떠오르질 않는다. 그것은 이렇게 나누는 것이 그리 좋은 전략이 아니라는 것을 뜻한다.
        V 3. TestSuite.run()을 호출하는 곳에서 TestResult를 할당한다. => 매개 변수 수집 패턴(collecting parameter pattern)
        """

        for test in self.tests:
            test.run(result)


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))

result = TestResult()
suite.run(result)
logger.info(result.summary())