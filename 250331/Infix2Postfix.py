from ArrayStack import ArrayStack
from EvalPostfix import evalPostfix

# 코드 4.6: 연산자의 우선순위 계산 함수
def precedence (op):
    if   (op=='(' or op==')') : return 0;
    elif (op=='+' or op=='-') : return 1;
    elif (op=='*' or op=='/') : return 2;
    else : return -1

# 코드 4.7: 중위 표기 수식의 후위식 변환 (참고 파일: ch04/Infix2Postfix.py)
def Infix2Postfix( expr ):
    s = ArrayStack(100)
    output = []

    for term in expr :
        if term in '(' :
            s.push('(')

        elif term in ')' :
            while not s.isEmpty() :
                op = s.pop()
                if op=='(' :
                    break;
                else :
                    output.append(op)

        elif term in "+-*/" :
            while not s.isEmpty() :
                op = s.peek()
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)

        else :                  # 피연산자
            output.append(term)

    while not s.isEmpty() :
        output.append(s.pop())

    return output


#=========================================================
#   - 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
#   - 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
#=========================================================
# 코드 4.8: 계산기 테스트 프로그램     참고 파일: ch04/Infix2Postfix.py
if __name__ == "__main__":
    print('스택의 응용3: 중위표기식 후위표기 변환\n')

    infix1 = [ '8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    infix2 = [ '1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']

    postfix1 = Infix2Postfix(infix1)
    postfix2 = Infix2Postfix(infix2)

    result1 = evalPostfix(postfix1)
    result2 = evalPostfix(postfix2)

    print('  중위표기: ', infix1)
    print('  후위표기: ', postfix1)
    print('  계산결과: ', result1, end='\n\n')

    print('  중위표기: ', infix2)
    print('  후위표기: ', postfix2)
    print('  계산결과: ', result2)
