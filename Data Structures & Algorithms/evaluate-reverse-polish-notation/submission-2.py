class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops=[]
        for i in tokens:
            if i not in ["+","-","/","*"]:
                ops.append(int(i))
            else:
                op2=ops.pop()
                op1=ops.pop()
                if i=='+':
                    ops.append(op1+op2)
                elif i=='-':
                    ops.append(op1-op2)
                elif i=='/':
                    ops.append(int(op1/op2))
                elif i=='*':
                    ops.append(op1*op2)
                else:
                    return "invalid operator"
        return ops[0]
                
                




        