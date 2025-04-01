# 코드 4.5: 후위수식 계산 알고리즘 (참고 파일: ch04/EvalPostfix.py)
from ArrayStack import ArrayStack


def evalPostfix( expr ):
    s = ArrayStack(100)
    for token in expr :
        if token in "+-*/" :
            val2 = s.pop()
            val1 = s.pop()
            if   (token == '+'): s.push(val1 + val2)
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else :
            s.push( float(token) )

    return s.pop()

#=========================================================
# 코드 1.3: 문자열 역순 출력 프로그램
#   - 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
#   - 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
#=========================================================
if __name__ == "__main__":
    print('스택의 응용2: 후위표기식 계산\n')

    str1 =' 8 +2 / 3 - 3 2 * +'
    expr1 = str1.split()

    #expr1 = [ '8', '2', '/', '3', '-', '3', '2', '*', '+']
    expr2 = [ '1', '2', '/', '4', '*', '1', '4', '/', '*']

    print(expr1, ' --> ', evalPostfix(expr1))
    print(expr2, ' --> ', evalPostfix(expr2))

