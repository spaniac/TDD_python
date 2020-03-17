"""
테스트 메서드 호출하기
먼저 setUp 호출하기
나중에 tearDown 호출하기
TODO: 테스트 메서드가 실패하더라도 tearDown 호출하기
여러 개의 테스트 실행하기
수집된 결과를 출력하기
WasRun에 로그 문자열 남기기
실패한 테스트 보고하기
TODO: setUp 에러를 잡아서 보고하기
TODO: TestCase 클래스에서 TestSuite 생성하기
"""
from was_run import WasRun

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
