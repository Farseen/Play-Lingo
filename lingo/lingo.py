def is_member(f, l):
    if f in l:
        return 'found'
    else:
        return 'notFound'


correct = "Farseen"
correct = correct.lower()
correct = list(correct)
answer = list('adfrews')
tentativeAnswer = list('abcdefq')
guess = ''
z = 0
while answer != correct:
    print("Enter The Guess = ", end='')
    myguess = input()
    if len(myguess) > 7 or len(myguess) < 7:
        print("Please Guess A 7 Letter Word")
        break
    myguess = myguess.lower()
    h = 0
    for x in myguess:
        if x == correct[h]:
            answer[h] = x
            t = ('[', x, ']')
            te = ''.join(t)
            myguess = ''.join(myguess)
            if z is 0:
                guess = myguess.replace(x, te)
                z = 1
            else:
                guess = guess.replace(x, te)

        else:
            d = is_member(x, correct)
            if d == 'found':
                print("Found")
                answer[h] = d
                t = ('(', x, ')')
                te = ''.join(t)
                print("te = ", end='')
                print(te)
                myguess = ''.join(myguess)
                if z is 0:
                    guess = myguess.replace(x, te)
                    z = 1
                else:
                    guess = guess.replace(x, te)
        h = h + 1
    myguess = list(myguess)
    if myguess == correct:
        print("The Guess Is Correct ")
    else:
        print("Clue =", end='')
        print(guess)

