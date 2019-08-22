def multiply_by_two(x):
    return x * 2

def test_multiply_by_two():
    assert multiply_by_two(4) == 8

# pytest library는 이름이 test_ 로 시작하는 파일이나 함수를 실행한다
# referred: "깔끔한 파이썬 탄탄한 백엔드" written by 송은우